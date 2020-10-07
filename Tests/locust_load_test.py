from locust import HttpUser, TaskSet, between, task


class LocustTasks(TaskSet):
    @task(1)
    def token_test(self):
        self.client.post('/login', data={"username": "test", "password": "test"})

    @task(2)
    def category_test(self, categories_array=None):
        if categories_array is None:
            categories_array = ['food', 'learning', 'art', 'sport', 'party', 'friends', 'travel']
        for category in categories_array:
            self.client.get(f'/v1/{category}')


class LoadTest(HttpUser):
    tasks = [LocustTasks]
    wait_time = between(0.100, 1.500)
    host = "http://localhost:8000"
