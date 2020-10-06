from locust import HttpUser, TaskSet, between, task


class LocustTasks(TaskSet):
    @task(1)
    def token_test(self):
        self.client.post('/login', data={"username": "test", "password": "test"})


class LoadTest(HttpUser):
    tasks = [LocustTasks]
    wait_time = between(0.100, 1.500)
    host = "http://localhost:8000"
