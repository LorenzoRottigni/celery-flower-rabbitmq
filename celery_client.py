from celery import Celery

app = Celery(
    'celery_worker',
    # LOCALHOST BECAUSE IT'S RUNNING OUTSIDE OF DOCKER, OTHERWISE USE 'rabbitmq' AS HOSTNAME
    broker='amqp://guest:guest@localhost:5672/',
    # LOCALHOST BECAUSE IT'S RUNNING OUTSIDE OF DOCKER, OTHERWISE USE 'rabbitmq' AS HOSTNAME
    backend='rpc://guest:guest@localhost:5673/'
)

# Send tasks to the Celery worker
result_add = app.send_task('celery_worker.add', args=(4, 5), result='rpc')

# Wait for the result
task_result = result_add.get()
print("Task add result:", task_result)
