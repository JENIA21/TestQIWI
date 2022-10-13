from config import Config
from celery import Celery


class Celeriac:
    def __init__(self, include, backend=Config.CELERY_RESULT_BACKEND, broker=Config.CELERY_BROKER_URL):
        self._celery_app = None
        self.backend = backend
        self.broker = broker
        self.include = include

    @property
    def celery_app(self):
        if self._celery_app is None:
            self._celery_app = Celery(
                backend=self.backend,
                broker=self.broker,
                include=self.include)
        return self._celery_app


celeriac = Celeriac(['celery_app.task'])
celery = celeriac.celery_app
