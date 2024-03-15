import datetime

from sqlalchemy import Column, Integer, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base

from app.db.managers import BaseManager


meta = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

Base = declarative_base(metadata=meta)


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class OrmManager:
    @classmethod
    @property
    def objects(cls) -> BaseManager:
        return BaseManager(cls)
