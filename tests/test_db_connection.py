from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists

from src.raiz.db_connection import get_engine_from_settings
from src.raiz.local_settings import postgresql as settings


def test_database_exists():

    url = f'postgresql://postgres:user@localhost:5432/mdsraiz'

    assert database_exists(url)


def test_url_settings():

    keys = ['pguser', 'pgpasswd', 'pghost', 'pgport', 'pgdb']

    assert all(key in keys for key in settings.keys())


def test_session():

    engine = get_engine_from_settings()
    assert sessionmaker(bind=engine)()
