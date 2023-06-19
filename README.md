CHECK RABBITMQ AUTH => curl -u guest:guest http://localhost:15672/api/whoami
swagger => http://localhost:15672/api/


http://localhost:5555/api/task/send-task/celery_worker.add

raw body - application/json
{
  "args": [1, 2]
}
