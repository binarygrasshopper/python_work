my_fav_pizzas = ['Pepperoni','Loaded','Ham & Pineapple']
print("My favorite pizza's are:")
for my_fav_pizza in my_fav_pizzas:
    print(f"\tOne of my favorite pizza is: {my_fav_pizza.title()}")

print(f"\nPizza is one great food\nThease are my favorite types {my_fav_pizzas}\nI really love pizza!")

#number counting
print("\n")
for value in range(1,21):
    print(value) 

print("\n")
for value in range(1,1000001):
    print(value) 

print("\n")
million_numbers = [value for value in range(1,1000001)]
print(f"Min Number: {min(million_numbers)}")
print(f"Max Number: {max(million_numbers)}")
print(f"Sum of Numbers: {sum(million_numbers)}")




