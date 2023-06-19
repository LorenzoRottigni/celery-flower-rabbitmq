from celery import Celery

app = Celery(
    'celery_worker',
    broker='amqp://guest:guest@rabbitmq:5672/',
    backend='rpc://guest:guest@rabbitmq:5673/'
)


@app.task
def add(x, y):
    return x + y

@app.task
def multiply(x, y):
    return x * y