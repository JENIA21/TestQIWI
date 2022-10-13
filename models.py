from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa

from config import Config

base = declarative_base()
engine = sa.create_engine(Config.SQLALCHEMY_DATABASE_URI)
base.metadata.bind = engine
session = orm.scoped_session(orm.sessionmaker())(bind=engine)


class GameData(base):
    __tablename__ = 'output_data'

    id = sa.Column(sa.Integer, primary_key=True)
    output_data = sa.Column(sa.String(4096))


base.metadata.create_all(engine)
