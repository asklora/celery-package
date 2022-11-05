from workerconnector import Worker


worker = Worker.create('quant','quant worker','quant', ['registered_tasks'])