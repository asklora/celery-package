from os import environ

broker_url = environ["BROKER_URL"]
result_backend = environ["RESULT_BACKEND"]
task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
timezone = "utc"
enable_utc = True
