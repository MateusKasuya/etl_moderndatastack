from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import create_database, database_exists

settings = dotenv_values('.env')


def get_engine(user, password, host, port, db):
    url = f'postgresql://{user}:{password}@{host}:{port}/{db}?client_encoding=UTF8'

    if not database_exists(url):
        create_database(url)

    engine = create_engine(url, pool_size=50, echo=True)

    #print(engine.url)

    return engine


def get_engine_from_settings():
    keys = ['PGUSER', 'PGPASSWORD', 'PGHOST', 'PGPORT', 'PGDB']

    if not all(key in settings for key in keys):
        raise Exception('Bad Config file')

    return get_engine(
        user=settings['PGUSER'],
        password=settings['PGPASSWORD'],
        host=settings['PGHOST'],
        port=settings['PGPORT'],
        db=settings['PGDB'],
    )



engine = get_engine_from_settings()
Session = sessionmaker(bind=engine)
Base = declarative_base()
