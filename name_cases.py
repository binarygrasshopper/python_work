name = "David"
#print a message to the user
print(f"Hello, {name}, do youu like to learn some Python today!")

#print the name in lower case
print(name.lower())

#print the name in upper case
print(name.upper())

#print the name in title case
print(name.title())

#some famous quotes using f-strings
lincoln_quote = "Sir, my concern is not whether God is on our side; my greatest concern is to be on God's side, for God is always right."
print(f"Abraham Lincoln once said, \"{lincoln_quote}\"")

famous_person = "Abraham Lincoln"
message = f"{famous_person} once said, \"{lincoln_quote}\""

print(message)

#striping white spaces
name2 = "  \nDavid Bendixen\t  "
print(name2)
print(name2.lstrip())
print(name2.rstrip())
print(name2.strip())

#remove a suffix from a string
filename = "python_notes.txt"
print(filename)
print(filename.removesuffix(".txt"))