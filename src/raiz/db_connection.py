from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from src.raiz.local_settings import postgresql as settings


def get_engine(user, password, host, port, db):
    url = f'postgresql://{user}:{password}@{host}:{port}/{db}?client_encoding=UTF8'

    if not database_exists(url):
        create_database(url)

    engine = create_engine(url, pool_size=50, echo=True)

    print(engine.url)

    return engine


def get_engine_from_settings():

    keys = ['pguser', 'pgpasswd', 'pghost', 'pgport', 'pgdb']

    if not all(key in keys for key in settings.keys()):
        raise Exception('Bad Config file')

    return get_engine(
        user=settings['pguser'],
        password=settings['pgpasswd'],
        host=settings['pghost'],
        port=settings['pgport'],
        db=settings['pgdb'],
    )


def get_session():

    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine)()
    print(session)
    return session
