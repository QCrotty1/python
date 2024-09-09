from classes import My_Api_Handler, My_Class

my_api = My_Api_Handler.My_Api_Handler()
my_class = My_Class.My_Class(string="STRING", number=5)
user = my_api.get_user()
cat_fact = my_api.get_cat_fact()

print(f"my_class has string: {my_class.get_string()} and number {my_class.get_number()}")
print(f"random cat fact from my_api is: {cat_fact}")
print (f"Full Name of User: {user['name']['first']} {user['name']['last']}")
print(f"Yes or No: {my_api.get_yes_no()}")