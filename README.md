# MovieCatalogrrr

**NOTE: This is a quick and dirty example project using a RESTful API and React!**

A simple app to track movie collections.

![Image of MovieCatalogrrr](https://i.imgur.com/ohPLcgs.png)

---

### Set up

The application is broken up in two pieces, the server-side api written using Flask and a client-side
SPA written using React.

#### API

##### Requirements

- [Python3.7](https://www.python.org/)
- [pipenv](https://docs.pipenv.org/)
- [sqlite3](https://www.sqlite.org/index.html)

1. Install
```bash
cd api && pipenv install
```

2. Activate env
```bash
pipenv shell
```

4. Load up the DB
```bash
python db.py

# Optionally load up some seed data
sqlite3 movies.db < seed.sql
```

5. Run
```bash
export FLASK_ENV=development # Optional
FLASK_APP=api:create_app flask run
```

##### Examples

The API can currently only return a JSON response, ex:

```bash
λ ~/projects/movie_catalogue/ master* curl localhost:5000/movies/1
{
  "actors": [
    {
      "id": 3,
      "name": "Jake Gyllenhaal"
    }
  ],
  "created_at": 1533516337,
  "genres": [
    {
      "id": 4,
      "name": "thriller"
    },
    {
      "id": 5,
      "name": "sci-fi"
    }
  ],
  "id": 1,
  "rating": null,
  "seen": 0,
  "title": "Donnie Darko"
}
```


Some examples of querying with [cURL](https://curl.haxx.se/):

```bash
# See all movies
curl "localhost:5000/movies"

# Apply some filters
curl "localhost:5000/movies?title=John"
curl "localhost:5000/movies?limit=2"
curl "localhost:5000/movies?genre=action"
curl "localhost:5000/movies?genre=action&limit=1"

curl localhost:5000/genres
curl localhost:5000/actors

# Adding a movie
curl -X POST -d "title=Sharknado" http://localhost:5000/movies # Try again and notice error response
curl -X POST -d "title=John%20Wick%202&genres=action&actors=Keanu%20Reeves" http://localhost:5000/movies # With genre and actor
curl -X POST -d "title=Speed&genres=action,crime&actors=Keanu%20Reeves,Sandra%20Bullock" http://localhost:5000/movies # Multiple

# Use movie ID to query
curl http://localhost:5000/movies/1 # Your ID

# You can also POST to create genres and actors
```

---

#### SPA

##### Requirements

- [yarn](https://yarnpkg.com/en/)

1. Install
```
cd app
yarn install
```

2. Run
```
yarn start
```
