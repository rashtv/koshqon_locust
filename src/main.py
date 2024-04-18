from random import randint

from locust import HttpUser, task, between


class KoshQonUser(HttpUser):
    wait_time = between(1, 3)

    @task(10)
    def get_announcements_task(self):
        self.client.get("/api/v1/announcements")

    @task(5)
    def get_announcement_task(self):
        announcement_id = randint(1, 3)
        self.client.get(f"/api/v1/announcements/{announcement_id}")

    @task(2)
    def get_user_profiles_task(self):
        self.client.get("/api/v1/user_profiles")

    @task(5)
    def get_user_profile_task(self):
        user_profile_id = randint(1, 3)
        self.client.get(f"/api/v1/user_profiles/{user_profile_id}")

    @task(1)
    def get_users_task(self):
        self.client.get("/api/v1/users")

    @task(2)
    def get_user_task(self):
        user_id = randint(1, 3)
        self.client.get(f"/api/v1/users/{user_id}")

    @task(2)
    def get_user_connections(self):
        user_profile_id = randint(1, 3)
        self.client.get(f"/api/v1/user_profiles/{user_profile_id}/friends")

    @task(3)
    def get_user_favorites_task(self):
        user_profile_id = randint(1, 3)
        self.client.get(f"/api/v1/user_profiles/{user_profile_id}/favorites")

    @task(3)
    def get_user_announcements_task(self):
        user_profile_id = randint(1, 3)
        self.client.get(f"/api/v1/user_profiles/{user_profile_id}/announcements")

    @task(1)
    def get_cities_task(self):
        self.client.get("/api/v1/workflow/cities")
