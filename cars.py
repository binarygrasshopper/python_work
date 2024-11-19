cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
print("\n\n\n")
#sort reverse order
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

#original / and sorted (temporary) list
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("\n\n\n")
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
cars.reverse()
print(cars)
print(len(cars))
