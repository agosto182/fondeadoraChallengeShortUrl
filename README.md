# fondeadoraChallengeShortUrl

This project is a little url shortener. Maded with python3 and the next libraries:
- Fast api
- Sqlalchemy
- Sqlite

## How to run

### Docker way

With docker-compose you can run the project easy:

```
$ docker-compose up
```

### Manual way
You need to install the dependencies (I recommend create a new environment with pyenv first).

```
$ pip install -r requeriments.txt
```

And run the application with uvicorn:

```
$ uvicorn main:app --app-dir app
```

## Testing

With all the dependencies installed run the follow command:

```
$ pytest
```


## Documentation

Once the app is running, please go to the path `/docs` to see the routes available.
