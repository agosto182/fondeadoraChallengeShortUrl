from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV = 'dev'
    SERVER_URL = 'http://localhost:8080'
    DB_URL = 'sqlite:///sql_app.db'
    DB_TEST_URL = 'sqlite:///sql_test_app.db'


settings = Settings()
