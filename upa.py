class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}\nAge: {self.age}\nGender: {self.gender}")

    def greet_user(self):
        print(f"Greetings, Welcome {self.first_name}!\n")

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Admin Privileges:")
        for index, privilege in enumerate(self.privileges, 1):
            print(f"{index}: {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, gender, privileges_list):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges(privileges_list)