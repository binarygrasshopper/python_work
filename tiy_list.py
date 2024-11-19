#my initial dinner guest list
guests = ['Dad','Mom','Steven','Chris','Rainie','Bev']
print(f"Hi {guests[0]}, please come to dinner with me.")
print(f"Hi {guests[1]}, please come to dinner with me.")
print(f"Hi {guests[2]}, please come to dinner with me.")
print(f"Hi {guests[3]}, please come to dinner with me.")
print(f"Hi {guests[4]}, please come to dinner with me.")
print(f"Hi {guests[-1]}, please come to dinner with me.")

#print out the guest that can't make it to dinner
guests = ['Dad','Mom','Steven','Chris','Rainie','Bev']
print(f"it turns out that {guests[-1]} can't make it to dinner.")

#replace the person that can't make it to dinner with someone else and resend invitations.
guests[-1] = 'Trudy'
print(f"Hi {guests[0]}, please come to dinner with me.")
print(f"Hi {guests[1]}, please come to dinner with me.")
print(f"Hi {guests[2]}, please come to dinner with me.")
print(f"Hi {guests[3]}, please come to dinner with me.")
print(f"Hi {guests[4]}, please come to dinner with me.")
print(f"Hi {guests[-1]}, please come to dinner with me.")

#execise more guest
guests = ['Dad','Mom','Steven','Chris','Rainie','Bev']
guests[-1] = 'Trudy'
print(f"Hi {guests}, hey we just found a bigger table for dinner")
guests.insert(0,'Nikki')
guests.insert(4,'David')
guests.append('Johnanthan')
print(f"Hi {guests[0]}, please come to dinner with me.")
print(f"Hi {guests[1]}, please come to dinner with me.")
print(f"Hi {guests[2]}, please come to dinner with me.")
print(f"Hi {guests[3]}, please come to dinner with me.")
print(f"Hi {guests[4]}, please come to dinner with me.")
print(f"Hi {guests[5]}, please come to dinner with me.")
print(f"Hi {guests[6]}, please come to dinner with me.")
print(f"Hi {guests[7]}, please come to dinner with me.")
print(f"Hi {guests[-1]}, please come to dinner with me.")

#execise only 2 guest
guests = ['Dad','Mom','Steven','Chris','Rainie','Bev']
guests[-1] = 'Trudy'
guests.insert(0,'Nikki')
guests.insert(4,'David')
guests.append('Johnanthan')
print(f"Hi {guests}, \nThe table we have can only seat 2 people for dinner")
person_to_message = guests.pop()
print(f"Hi {person_to_message}, sorry, we can't invite you for dinner")
person_to_message = guests.pop()
print(f"Hi {person_to_message}, sorry, we can't invite you for dinner")
person_to_message = guests.pop()
print(f"Hi {person_to_message}, sorry, we can't invite you for dinner")
person_to_message = guests.pop()
print(f"Hi {person_to_message}, sorry, we can't invite you for dinner")
person_to_message = guests.pop()
print(f"Hi {person_to_message}, sorry, we can't invite you for dinner")
person_to_message = guests.pop()
print(f"Hi {person_to_message}, sorry, we can't invite you for dinner")
person_to_message = guests.pop()
print(f"Hi {person_to_message}, sorry, we can't invite you for dinner")
print(f"Hi, {guests}, please come to dinner.\n")
del guests[0]
del guests[-1]
print(guests)

#places i would like to visit
places_i_want_to_visit = ['Hawaii','Caribian','England','Scottland','Florida']
print(places_i_want_to_visit)
print(f"{sorted(places_i_want_to_visit)}")
print(places_i_want_to_visit)
places_i_want_to_visit.reverse()
print(places_i_want_to_visit)
places_i_want_to_visit.reverse()
print(places_i_want_to_visit)
places_i_want_to_visit.sort()
print(places_i_want_to_visit)

#testing length of a list.
guests = ['Dad','Mom','Steven','Chris','Rainie','Bev']
guests[-1] = 'Trudy'
print(f"Hi {guests}, hey we just found a bigger table for dinner")
guests.insert(0,'Nikki')
guests.insert(4,'David')
guests.append('Johnanthan')
print(f"{guests}, are coming to dinner, the number of guest is {len(guests)}")

#3-10 - write a program that stores things you care about and then uses each function you learned in this chapter 
#at least once.

#use title()
programming_languages_i_have_learned = ['Cobol','Fortran','Pascal','C','RPG','Visual Basic','C++','C#','Python','JavaScript']
print(f"Here is the first Programming Language i learned in my career, {programming_languages_i_have_learned[0].title()}")

#print the current programming language i am learning.
print(f"The current programming language i am learning is, {programming_languages_i_have_learned[-2].title()}")

#replace something in the list.
programming_languages_i_have_learned[-1] = 'TypeScript'
print(f"Updated list of programming languages i have learned, {programming_languages_i_have_learned}")

#add something to the end of the list.
programming_languages_i_have_learned.append('JavaScript')
print(f"Appended list of programming languages i have learned, {programming_languages_i_have_learned}")

#add something to the list.
programming_languages_i_have_learned.insert(4,'Rust')
print(f"Inserted list of programming languages i have learned, {programming_languages_i_have_learned}")

#delete something from the list.
del programming_languages_i_have_learned[4]
print(f"Deleted from list of programming languages i have learned, {programming_languages_i_have_learned}")

#pop something from the list.
programming_languages_i_have_learned.pop()
print(f"Popped from list of programming languages i have learned, {programming_languages_i_have_learned}")

#popped programming language
popped_programming_language = programming_languages_i_have_learned.pop()
print(f"Popped programming language from list of programming languages i have learned is, {popped_programming_language}")
print(f"Left programming languages i have learned after i popped a language from the list, {programming_languages_i_have_learned}")

#remove an item from the list via value.
programming_languages_i_have_learned.remove('RPG')
print(f"Removed programming language from list of programming languages i have learned is, {programming_languages_i_have_learned}")

#temp sort list and perm sort list
print(f"Temporary sorted programming list i have learned is, {sorted(programming_languages_i_have_learned)}")
print(f"Temporary sorted programming list in decending order i have learned is, {sorted(programming_languages_i_have_learned,reverse=True)}")
print(programming_languages_i_have_learned)
programming_languages_i_have_learned.sort()
print(f"Permanently sorted programming list i have learned is, {programming_languages_i_have_learned}")
programming_languages_i_have_learned.sort(reverse=True)
print(f"Permanently sorted programming list in decending order i have learned is, {programming_languages_i_have_learned}")

#reverse list 
programming_languages_i_have_learned.reverse()
print(programming_languages_i_have_learned)
programming_languages_i_have_learned.reverse()
print(programming_languages_i_have_learned)

#print the length of the list
print(f"The length of the list is, {len(programming_languages_i_have_learned)}")





