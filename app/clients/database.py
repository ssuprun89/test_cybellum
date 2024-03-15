from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from .base import BaseClient
from app.config import get_settings
from app.db.engine import SQLALCHEMY_DATABASE_URL

settings = get_settings()


class DatabaseClient(BaseClient):
    def __init__(self):
        self._engine = create_engine(
            SQLALCHEMY_DATABASE_URL, max_overflow=10, pool_size=5
        )

    @classmethod
    def get_client(cls):
        return cls()

    def _get_session(self) -> Session:
        return sessionmaker(autocommit=False, autoflush=False, bind=self._engine)()

    @staticmethod
    def _query(db, model, *criterion):
        return db.query(model).filter(*criterion)

    def get(self, model, *criterion):
        with self._get_session() as db:
            obj = self._query(db, model, *criterion).one()
            return obj

    def get_or_none(self, model, *criterion):
        with self._get_session() as db:
            obj = self._query(db, model, *criterion).one_or_none()
            return obj

    def count(self, model, *criterion):
        with self._get_session() as db:
            count = self._query(db, model, *criterion).count()
            return count

    def filter(self, model, *criterion):
        with self._get_session() as db:
            return self._query(db, model, *criterion)

    def all(self, model, *criterion):
        with self._get_session() as db:
            return self._query(db, model, *criterion).all()

    def update(
        self,
        model,
        defaults,
        criterion,
        refresh: bool = False,
    ):
        with self._get_session() as db:
            query = self._query(db, model, *criterion)
            query.update(defaults)
            db.commit()
            if refresh:
                updated_instance = query.first()
                db.refresh(updated_instance)
                return updated_instance

    def create(self, model, **data):
        with self._get_session() as db:
            new_object = model(**data)
            db.add(new_object)
            db.commit()
            db.refresh(new_object)
            return new_object

    def delete(self, model, *criterion):
        with self._get_session() as db:
            instance = self._query(db, model, *criterion).first()
            if instance:
                db.delete(instance)
                db.commit()
