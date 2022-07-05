from Connector import Worker


producer = Worker.create('app-producer','producer')
# queue must specify, which queue to use
# will return an error / nothing happen if queue does not exist
res = producer.send_task('quant.tasks.summ', args=(1,2), queue="quant")
print(res.id)