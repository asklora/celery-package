from connection import worker
from consumer import do_something_in_task_called

@worker.task
def summ(a, b):
    do_something_in_task_called()
    return a + b