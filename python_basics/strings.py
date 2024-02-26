
print("Hello World")

message = "Hello World"
print(message)
print(len(message)) #For printing out the length of the string

print(message[0]) #For printing specific character from string
print(message[0:5]) #First index inclusive second one is exclusive
print(message[5: ])
print(message[ :6])

print(message.lower())
print(message.upper())
print(message.count("Hello"))
print(message.count("l"))
print(message.find("World")) #Returns index of starting chracter
print(message.find("Universe")) #Returns -1 when it is not exist

new_message = message.replace("World", "Universe")
print(new_message)

message_2 = "Bobby's World" #if single quote was used ' for string / should be used for escape e.g. 'Bobby/'s World'
print(message_2)

message_3 = """Bobby's World was a good 
cartoon in the 1990s.""" # Use triple quotation """ for multiple line text
print(message_3)

greeting = "Hello"
name = "Micheal"

message_4 = greeting + " " + name
print(message_4)

message_5 = greeting + ", " + name + ". Welcome!"
print(message_5)

message_6 = "{}, {}. Welcome!".format(greeting, name)
print(message_6)

message_7 = f"{greeting}, {name}. Welcome!"
print(message_7)

#print(dir(name)) #for printing usable methods and functions on the varible name
#print(help(str)) #for printing what are those methods and functions on class string
#print(help(str.lower)) #for printing what is specific method and function does on class string
