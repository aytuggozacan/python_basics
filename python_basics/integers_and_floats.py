
num = 3
print(type(num))

num_2 =3.14
print(type(num_2))

#Basic Arithmetic

print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2) #floor division: not include decimals 
print(3 ** 2) #exponent
print(3 % 2)  #modulus: gives remainder. Useful for find odd and even numbers. 

print(3 * (2 + 1)) #Paranthesis could be used as normal arithmetic

num_3 = 1
num_3 += 1 #could be used for other operations. e.g. num_3 *= 10
print(num_3)

print(abs(-3)) #for absolute value
print(round(3.75)) #round number to neares integer
print(round(3.75, 1)) # to round first decimal

num_4 = 3
num_5 = 2

#Comparisions (returns boolean)
print(num_4 == num_5)
print(num_4 != num_5)
print(num_4 > num_5)
print(num_4 < num_5)
print(num_4 >= num_5)
print(num_4 <= num_5)

#Casting
num_6 = "100"
num_7 = "200"

num_6 = int(num_6)
num_7 = int(num_7)

print(num_6 + num_7)



