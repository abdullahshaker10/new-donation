from locust import HttpUser, TaskSet, task

class UserBehavior(TaskSet):
    @task
    def load_cases(self):
        response = self.client.get("/cases/cases/")  

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 2000
    host = "http://127.0.0.1:8002"