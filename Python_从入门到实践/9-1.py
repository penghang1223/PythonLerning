class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"嘿嘿嘿,{self.restaurant_name},{self.cuisine_type}")

    def open_restaurant(self):
        print(f"哈哈哈,{self.cuisine_type}")


restaurant = Restaurant("餐馆", "烧烤")
restaurant.describe_restaurant()
restaurant.open_restaurant()


