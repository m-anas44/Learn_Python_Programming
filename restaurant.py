class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

    def describe_restaurant(self):
        print(f"{self.restaurant_name} carries delicious tastes with {self.cuisine_type}")

    def open_restaurant(self):
        print("The Restaurant is now open!")