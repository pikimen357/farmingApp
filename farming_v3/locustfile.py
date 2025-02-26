
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_tanaman(self):
        self.client.get("http://localhost:8000/v3/hama")