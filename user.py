class User:
    def __init__(self, user_email, user_name, user_password, user_job_title):
        self.email = user_email
        self.name = user_name
        self.password = user_password
        self.job_title = user_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_jobtitle(self, new_job_title):
        self.job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as {self.job_title},you can contact them in {self.email}")


