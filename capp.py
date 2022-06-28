from celery import Celery

Capp = Celery("capp")
Capp.config_from_object("config")
Capp.autodiscover_tasks()
