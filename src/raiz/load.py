import json

from database import get_engine_from_settings
from sqlalchemy import insert
from sqlalchemy.orm import DeclarativeBase, Session


def load_to_database(json_file: str, Model: DeclarativeBase):

    with open(f'../../data/{json_file}', 'r') as file:
        data = json.load(file)
        schema_list = data[json_file.split('_')[0]]

    engine = get_engine_from_settings()

    with Session(engine) as session:
        session.execute(insert(Model), schema_list)
        session.commit()

    pass
