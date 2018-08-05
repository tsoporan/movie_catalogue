'''
Movie Catalogue Flask API
'''

from sqlite3 import IntegrityError, Row
from flask import Flask, g, request, jsonify

from werkzeug.local import LocalProxy

from db import get_conn
from helpers import get_current_ts, extract_at_idx, row_to_dict

# Manage the DB connection per request
# Ref: http://flask.pocoo.org/docs/1.0/appcontext/#storing-data
def get_db():
    if 'db' not in g:
        g.db = get_conn()
        g.db.row_factory = Row

    return g.db

db = LocalProxy(get_db)

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        return jsonify({"status": "OK"})

    @app.route('/movies', methods=['GET', 'POST'])
    def movies():

        # Filtered movies by params
        if request.method == 'GET':

            title = request.args.get('title')
            genre = request.args.get('genre')
            actor = request.args.get('actor')

            results = get_movies({
                "title": title,
                "genre": genre,
                "actor": actor
            })

            return jsonify({'movies': row_to_dict(results)})

        # Creating a new movie
        if request.method == 'POST':
            title = request.form['title']
            genres = request.form.get('genres')
            actors = request.form.get('actors')
            rating = request.form.get('rating')
            seen = request.form.get('seen', False)

            err, movie_id = create_movie(
                title,
                genres,
                actors,
                rating,
                seen
            )

            if err:
                return jsonify({"error": err}), 400

            _, movie = get_movie(movie_id)

            return jsonify(movie)

    @app.route('/movies/<movie_id>', methods=['GET'])
    def movie_detail(movie_id):
        err, movie = get_movie(movie_id)

        if err:
            return jsonify({"errors": err}), 404

        return jsonify(movie)

    @app.route('/genres', methods=['GET', 'POST'])
    def genres():
        if request.method == 'GET':
            genres = db.execute('''SELECT * from genres;''').fetchall()
            return jsonify({'genres': row_to_dict(genres)})

        # Creating a new genre
        if request.method == 'POST':
            genre_name = request.form['name']

            err, genre_id = create_genre(genre_name)

            if err:
                return jsonify({"error": err}), 400

            _, genre = get_genre(genre_id)

            return jsonify(genre)

    @app.route('/genres/<genre_id>', methods=['GET'])
    def genre_detail(genre_id):
        err, genre = get_genre(genre_id)

        if err:
            return jsonify({"errors": err}), 404

        return jsonify(genre)

    @app.route('/actors', methods=['GET', 'POST'])
    def actors():
        if request.method == 'GET':
            actors = db.execute('''SELECT * from actors;''').fetchall()
            return jsonify({'movies': row_to_dict(actors)})

        # Creating a new actor
        if request.method == 'POST':
            actor_name = request.form['name']

            err, actor_id = create_actor(actor_name)

            if err:
                return jsonify({"errors": err}), 400

            _, actor = get_actor(actor_id)

            return jsonify(actor)

    @app.route('/actors/<actor_id>')
    def actor_detail(actor_id):
        err, actor = get_actor(actor_id)

        if err:
            return jsonify({"errors": err}), 404

        return jsonify(actor)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "{}".format(error)}), 404

    @app.teardown_appcontext
    def teardown_db(e=None):
        db = g.pop('db', None)

        if db is not None:
            db.close()

    return app


def create_movie(title, genres, actors, rating, seen):
    '''
    Create a new movie with title genres and actors.

    Movie titles are required to be unique!
    '''

    try:
        movie_id = db.execute('''
            INSERT INTO movies(
                title,
                created_at,
                rating,
                seen
            ) VALUES (?, ?, ?, ?);
        ''', (
            title,
            get_current_ts(),
            rating,
            seen
        )).lastrowid

        db.commit()
    except IntegrityError as exc:
        return "Failed to insert: {}".format(exc), None

    attach_genres(movie_id, genres)
    attach_actors(movie_id, actors)

    return None, movie_id


def get_movies(filter_opts):
    '''
    Retrieve a set of movies based on filters.
    '''

    title = filter_opts.get('title')
    genre_name = filter_opts.get('genre')
    actor_name = filter_opts.get('actor')

    # In case of title do a wildcard text search.
    if title:
        movies = db.execute('''
            SELECT
                id,
                title
            FROM movies
            WHERE title LIKE ?;
        ''', ('%{}%'.format(title), )).fetchall()

        return movies

    # In case of genre find all matching movies with this genre applied.
    if genre_name:
        genre = db.execute('''
            SELECT id FROM genres WHERE name = ?;
        ''', (genre_name,)).fetchone()

        if not genre:
            return []

        movies = db.execute('''
            SELECT
                m.id,
                m.title
            FROM movies_genres mg
            JOIN movies m on m.id = mg.movie_id
            WHERE mg.genre_id = ?;
        ''', (genre[0], )).fetchall()

        return movies

    # In case of actor find all matching movies with this actor.
    if actor_name:
        actor = db.execute('''
            SELECT id FROM actors WHERE name = ?;
        ''', (actor_name, )).fetchone()

        if not actor:
            return []

        movies = db.execute('''
            SELECT
                m.id,
                m.title
            FROM movies_actors ma
            JOIN movies m on m.id = ma.movie_id
            WHERE ma.actor_id = ?;
        ''', (actor[0], ))

        return movies

    all_movies = db.execute("SELECT * FROM movies;").fetchall()

    return all_movies


def get_movie(movie_id):
    '''
    Retrieve a movie representation
    '''

    result = db.execute('''
        SELECT
            id,
            title,
            seen,
            rating,
            created_at
        FROM movies WHERE id = ?;
    ''', (movie_id,)).fetchone()

    if not result:
        return "No movie found.", None

    genres = db.execute('''
        SELECT id, name
        FROM
            movies_genres mg
        JOIN
            genres g ON g.id = mg.genre_id
        WHERE
            movie_id = ?;
    ''', (movie_id, )).fetchall()

    mapped_genres = list(map(
        lambda item: {"id": item[0], "name": item[1]},
        genres
    ))

    actors = db.execute('''
        SELECT id, name
        FROM
            movies_actors ma
        JOIN
            actors a ON a.id = ma.actor_id
        WHERE
            movie_id = ?;
    ''', (movie_id, )).fetchall()

    mapped_actors = list(map(
        lambda item: {"id": item[0], "name": item[1]},
        actors
    ))

    return None, {
        "id": result["id"],
        "title": result["title"],
        "seen": result["seen"],
        "rating": result["rating"],
        "created_at": result["created_at"],
        "genres": mapped_genres or [],
        "actors": mapped_actors or []
    }


def create_actor(name):
    '''
    Create an actor based on name.
    '''

    normalized_name = name.strip()

    # If the actor already exists we can short circuit
    actor_id = db.execute('''
        SELECT id FROM actors WHERE name = ?;
    ''', (normalized_name, )).fetchone()

    if actor_id:
        return None, actor_id[0]

    try:
        actor_id = db.execute('''
            INSERT INTO actors(name) VALUES (?);
        ''', (normalized_name, )).lastrowid

        db.commit()
    except IntegrityError as exc:
        return "Failed to insert: {}".format(exc), None

    return None, actor_id


def get_actor(actor_id):
    '''
    Retrieve an actor representation
    '''

    result = db.execute('''
        SELECT * FROM actors WHERE id = ?;
    ''', (actor_id,)).fetchone()

    if not result:
        return "No actor found.", None

    return None, {
        "id": result["id"],
        "name": result["name"]
    }


def create_genre(name):
    '''
    Create a new genre based on name.
    '''

    normalized_name = name.lower().strip()

    # If the genre already exists we can short circuit
    genre_id = db.execute('''
        SELECT id FROM genres WHERE name = ?;
    ''', (normalized_name, )).fetchone()

    if genre_id:
        return None, genre_id[0]

    try:
        genre_id = db.execute('''
            INSERT INTO genres(name) VALUES (?);
        ''', (normalized_name, )).lastrowid

        db.commit()
    except IntegrityError as exc:
        return "Failed to insert: {}".format(exc), None

    return None, genre_id


def get_genre(genre_id):
    '''
    Retrieve a genre representation
    '''

    result = db.execute('''
        SELECT * FROM genres WHERE id = ?;
    ''', (genre_id,)).fetchone()

    if not result:
        return "No genre found.", None

    return None, {
        "id": result["id"],
        "name": result["name"]
    }


def attach_genres(movie_id, genres):
    '''
    Given a movie and string of csv genres attach genres to movie.
    '''

    if not genres:
        return

    normalized_genres = [g.lower().strip() for g in genres.split(",")]

    # Unfortunately, with sqlite3, we need to place a
    # param mark for each value -- this does not pose an injection risk
    val_placeholders = '?' * len(normalized_genres)

    query = '''SELECT id FROM genres WHERE name IN ({});'''.format(
        ','.join(val_placeholders)
    )

    # Extract the ID part
    existing_genres = extract_at_idx(
        db.execute(query, normalized_genres).fetchall(),
        idx=0
    )

    if not existing_genres:
        return

    movie_genre_mapping = [
        (movie_id, genre_id) for genre_id in existing_genres
    ]

    db.executemany('''
        INSERT INTO movies_genres(
            movie_id,
            genre_id
        ) VALUES (?, ?);''', movie_genre_mapping)

    db.commit()


def attach_actors(movie_id, actors):
    '''
    Given a movie and string of csv acotrs attach actors to movie.
    '''

    if not actors:
        return

    normalized_actors = [a.strip() for a in actors.split(",")]

    val_placeholders = '?' * len(normalized_actors)

    query = '''SELECT id FROM actors WHERE name IN ({});'''.format(
        ','.join(val_placeholders)
    )

    # Extract the ID part
    existing_actors = extract_at_idx(
        db.execute(query, normalized_actors).fetchall(),
        idx=0
    )

    if not existing_actors:
        return

    movie_actor_mapping = [
        (movie_id, actor_id) for actor_id in existing_actors
    ]

    db.executemany('''
        INSERT INTO movies_actors(
            movie_id,
            actor_id
        ) VALUES (?, ?);''', movie_actor_mapping)

    db.commit()
