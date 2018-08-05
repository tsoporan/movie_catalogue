-- Move Catalogue Sqlite Schema

CREATE TABLE movies (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created_at INTEGER NOT NULL,
  seen BOOLEAN DEFAULT false,
  rating INTEGER,
  title TEXT UNIQUE NOT NULL
);

CREATE TABLE actors (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);

CREATE TABLE genres (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);

--  M2M
CREATE TABLE movies_actors (
  actor_id INTEGER,
  movie_id INTEGER,
  FOREIGN KEY(actor_id) REFERENCES actors(id),
  FOREIGN KEY(movie_id) REFERENCES movies(id)
);

CREATE TABLE movies_genres (
  movie_id INTEGER,
  genre_id INTEGER,
  FOREIGN KEY(movie_id) REFERENCES movies(id),
  FOREIGN KEY(genre_id) REFERENCES genres(id)
);
