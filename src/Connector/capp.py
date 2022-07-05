from celery import Celery, bootsteps
from . import app_config


class HostNameStep(bootsteps.StartStopStep):
    hostname: str = "celery@%h"

    def __init__(self, worker, **kwargs):
        worker.hostname = "{}@worker".format(self.hostname)


class Worker(Celery):
    app_args: list[str] = []

    @staticmethod
    def init_modules(modules: list[str]) -> None:
        for module in modules:
            __import__(module)

    @classmethod
    def create(
        cls,
        node_name,
        app_name,
        worker_queue_name,
        tasks_modules: list[str],
        broker_url: str = "pyamqp://rabbitmq:rabbitmq@localhost//",
        result_backend: str = "redis://localhost",
    ) -> Celery:
        if node_name.isspace():
            raise ValueError("Node name cannot use whitespace")
        Capp = cls(app_name)
        app_config.broker_url = broker_url
        app_config.result_backend = result_backend
        Capp.config_from_object(app_config)
        Capp.conf.task_default_queue = worker_queue_name
        HostNameStep.hostname = node_name
        Capp.steps["worker"].add(HostNameStep)
        cls.init_modules(tasks_modules)
        Capp.autodiscover_tasks(tasks_modules)
        return Capp
