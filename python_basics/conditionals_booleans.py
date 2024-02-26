
language = "Java"

if language == "Python":
    print("Language is Python")
elif language == "Java":
    print("Language is Java")
elif language == "JavaScript":
    print("Language is JavaScript")
else: 
    print("No match")

user = "Admin"
logged_in = False

if user == "Admin" and logged_in:
    print("Admin Page")
else:
    print("Bad Creeds")

if user == "Admin" or logged_in:
    print("Admin Page")
else:
    print("Bad Creeds")

if not logged_in:
    print("Please Log In")
else:
    print("Welcome")

a = [1, 2, 3]
b = [1, 2, 3]
c = b

print(a == b)

print(id(a))
print(id(b))
print(id(c))
print(a is b) # "is" checks whether id(a) == id(b) not the value
print(b is c)

#False values
#False
#None
#Zero of any numeric type
#Any empty sequence, e.g. "", (), [].
#Any empty mapping, e.g. {}.

















