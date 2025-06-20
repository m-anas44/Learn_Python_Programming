from user import User

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