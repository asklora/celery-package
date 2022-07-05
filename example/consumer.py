"""
to run
celery -A consumer worker --loglevel=INFO

where consumer is consumer.py
"""

# import in here, the command [celery -A consumer worker]  will detect and run the worker
from connection import worker

def do_something_in_task_called():
    print("called")