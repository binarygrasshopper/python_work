magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, eveyone.  That was a great magic show!")

#forgetting to indent
for magician in magicians:
    print(magician)  #indentation error produced: IndentationError: expected an indented block after 'for' statement on line 9

#Forgetting to Indent Additional Lines
print(f"I can't wait to see your next trick, {magician.title()}.\n")


