# Movie Catalogue

A simple app to track movie collections.

---

### Set up

The application is broken up in two pieces, the server-side api written using Flask and a client-side
SPA written using React.

#### API

##### Requirements

- [Python3.7](https://www.python.org/)
- [pipenv](https://docs.pipenv.org/)

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
```

5. Run
```bash
FLASK_ENV=development # Optional
FLASK_APP=api:create_app flask run
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
