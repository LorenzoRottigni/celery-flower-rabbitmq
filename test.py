import requests

# Enqueue the task
response = requests.post(
    'http://localhost:5555/api/task/async-apply/celery_worker.add',
    json={"args": [1, 2]},
    auth=('guest', 'guest')
)

print(response.status_code)
print(response.text)
