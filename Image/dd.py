class Product:
    def __init__(self, product_id, name, price, manufacturer, weight, expiration_date, year):
        self.supermarket_name = "safi market"
        self.__product_id = product_id
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.weight = weight
        self.expiration_date = expiration_date
        self.year = year

    def product_details(self):
        print(f"\nProduct Details:")
        print(f"Supermarket: {self.supermarket_name}")
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Weight: {self.weight}gm")
        print(f"Expiration Date: {self.expiration_date}")
        print(f"Year: {self.year}")

    def set_product_id(self, new_id):
        self.__product_id = new_id
        print("Product ID updated successfully.")
    def get_product_id(self):
        return self.__product_id

class Healthy(Product):
    def __init__(self, product_id, name, price, manufacturer, weight, expiration_date, year, components):
        super().__init__(product_id, name, price, manufacturer, weight, expiration_date, year)
        self.calories = 0
        self.components = components

    def product_details(self):
        super().product_details()
        print(f"Calories per gram: {self.calories}")
        print(f"Components: {self.components}")

    def update_calories(self, new_calories):
        self.calories = new_calories
        print("Calories updated to", new_calories, "calories/gram")

    def compute_total_calories(self, weight,calories):
        self.calories = calories
        total_calories = calories * weight
        print(f"Total calories for {weight} g: {total_calories}")

weight = 0
new_calories = 0
total_calories = 0
def main():
    products = [Product(5261988, "corona chocolate", 25, "corona", 5, 6/7/2024, 2024)]
    healthy_products = [Healthy(4325671, "v7", 20, "ttt", 4, 44, 2023,"ggg")]

    while True:
        system_choice = input("\nChoose the subsystem (1-Product, 2-Healthy, 3-Exit): ")
        if system_choice == '3':
            print("Exiting Supermarket System.")
            break

        elif system_choice == '1':
            while True:
                print("\n--- Product Sub-System ---")
                choice = input("1-Add Product, 2-Display Products, 3-Change Product ID, 4-Exit Sub-system: ")
                if choice == '4':
                    break
                elif choice == '1':
                    product_id = input("Enter product ID: ")
                    name = input("Enter product name: ")
                    price = float(input("Enter price: "))
                    manufacturer = input("Enter manufacturer: ")
                    weight = input("Enter weight (g): ")
                    expiration_date = input("Enter expiration date: ")
                    year = input("Enter year: ")
                    product = Product(product_id, name, price, manufacturer, weight, expiration_date, year)
                    products.append(product)
                    print("Product added successfully.")
                elif choice == '2':
                    for product in products:
                        product.product_details()
                elif choice == '3':
                    prod_id = input("Enter current product ID to change: ")
                    new_id = input("Enter new product ID: ")
                    print("product ID changed successfully")
                    for product in products:
                        if product.get_product_id() == prod_id:
                            product.set_product_id(new_id)

        elif system_choice == '2':
            while True:
                print("\n--- Healthy Sub-System ---")
                choice = input(
                    "1-Add Healthy Product, 2-Display Healthy Products, 3-Change Calories, 4-Check Details, 5-Compute Total Calories, 6-Exit Sub-system: ")
                if choice == '6':
                    break
                elif choice == '1':
                    product_id = input("Enter product ID: ")
                    name = input("Enter product name: ")
                    price = float(input("Enter price: "))
                    manufacturer = input("Enter manufacturer: ")
                    weight = input("Enter weight (g): ")
                    expiration_date = input("Enter expiration date: ")
                    year = input("Enter year: ")
                    components = input("Enter the components: ")
                    print("product is added successfully")

                elif choice == '2':
                    for product in healthy_products:
                        product.product_details()

                elif choice == '3':
                    product_name = input("Enter product name to update calories: ")
                    new_calories = int(input("Enter new calories per gram: "))


                    found = False
                    for product in healthy_products:
                        if product.name == product_name:
                            product.update_calories(new_calories)
                            found = True

                elif choice == '4':
                    product_name = input("Enter product name to check details: ")
                    found = False
                    for product in healthy_products:
                        if product.name == product_name:
                            product.product_details()
                            found = True
                    if not found:
                        print("Product not found.")
                elif choice == '5':
                    product_name = input("Enter product name for calorie computation: ")
                    x = int(input("Enter weight (g) for calorie computation: "))
                    found = False
                    for product in healthy_products:
                        if product.name == product_name:
                            product.compute_total_calories(weight=x,calories=80)
                            found = True
                            if not found:
                                print("Product not found.")


if __name__ == "__main__":
    main()
