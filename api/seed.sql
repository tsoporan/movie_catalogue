-- Initial seed data

-- Movies
INSERT into movies(id, title, created_at) VALUES (1, 'Donnie Darko', 1533516337);
INSERT into movies(id, title, created_at) VALUES (2, 'Eternal Sunshine of the Spotless Mind', 1532516337);
INSERT into movies(id, title, created_at) VALUES (3, 'Memento', 1533556337);
INSERT into movies(id, title, created_at) VALUES (4, 'The Matrix', 1513516337);
INSERT into movies(id, title, created_at) VALUES (5, 'Titanic', 1533512222);
INSERT into movies(id, title, created_at) VALUES (6, 'John Wick', 1532226337);


-- Actors
INSERT INTO actors(id, name) VALUES (1, 'Jim Carrey');
INSERT INTO actors(id, name) VALUES (2, 'Kate Winslet');
INSERT INTO actors(id, name) VALUES (3, 'Jake Gyllenhaal');
INSERT INTO actors(id, name) VALUES (4, 'Guy Pearce');
INSERT INTO actors(id, name) VALUES (5, 'Keanu Reeves');
INSERT INTO actors(id, name) VALUES (6, 'Carrie-Anne Moss');


-- Genres
INSERT INTO genres(id, name) VALUES (1, 'drama');
INSERT INTO genres(id, name) VALUES (2, 'action');
INSERT INTO genres(id, name) VALUES (3, 'romance');
INSERT INTO genres(id, name) VALUES (4, 'thriller');
INSERT INTO genres(id, name) VALUES (5, 'sci-fi');

-- Movies Actors
INSERT INTO movies_actors(movie_id, actor_id) VALUES (1, 3);

INSERT INTO movies_actors(movie_id, actor_id) VALUES (2, 1);
INSERT INTO movies_actors(movie_id, actor_id) VALUES (2, 2);

INSERT INTO movies_actors(movie_id, actor_id) VALUES (3, 5);
INSERT INTO movies_actors(movie_id, actor_id) VALUES (3, 6);

INSERT INTO movies_actors(movie_id, actor_id) VALUES (3, 6);
INSERT INTO movies_actors(movie_id, actor_id) VALUES (3, 4);

INSERT INTO movies_actors(movie_id, actor_id) VALUES (4, 5);
INSERT INTO movies_actors(movie_id, actor_id) VALUES (4, 6);

INSERT INTO movies_actors(movie_id, actor_id) VALUES (5, 2);

INSERT INTO movies_actors(movie_id, actor_id) VALUES (6, 5);

-- Moves Genres
INSERT INTO movies_genres(movie_id, genre_id) VALUES (1, 4);
INSERT INTO movies_genres(movie_id, genre_id) VALUES (1, 5);

INSERT INTO movies_genres(movie_id, genre_id) VALUES (2, 1);
INSERT INTO movies_genres(movie_id, genre_id) VALUES (2, 3);
INSERT INTO movies_genres(movie_id, genre_id) VALUES (2, 5);

INSERT INTO movies_genres(movie_id, genre_id) VALUES (3, 2);
INSERT INTO movies_genres(movie_id, genre_id) VALUES (3, 5);

INSERT INTO movies_genres(movie_id, genre_id) VALUES (4, 5);
INSERT INTO movies_genres(movie_id, genre_id) VALUES (4, 2);

INSERT INTO movies_genres(movie_id, genre_id) VALUES (5, 3);
INSERT INTO movies_genres(movie_id, genre_id) VALUES (5, 1);

INSERT INTO movies_genres(movie_id, genre_id) VALUES (6, 2);
