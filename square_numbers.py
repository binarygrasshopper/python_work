squares = []
for value in range(1,11):
    #square = value ** 2
    squares.append(value ** 2)

print(squares)

#simple statistics with a list of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
print(f"Min digit {min(digits)}")
print(f"Max digit {max(digits)}")
print(f"Sum of digits {sum(digits)}")

#list comprehension examples
squares = [value**2 for value in range(1,11)]
print(squares)


