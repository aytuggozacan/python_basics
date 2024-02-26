
#Lists 

courses = ["History", "Math", "Physics", "CompSci"]
courses_2 = ["Art", "Education"]
nums = [1, 5, 2, 4, 3]

print(courses)
print(courses[0])
print(courses[3])
print(courses[-1]) #start counting from the end
print(courses[0:2])
print(courses[:2])
print(courses[2:])
print(len(courses))

courses.append("Art")
print(courses)
courses = ["History", "Math", "Physics", "CompSci"]


courses.insert(0, "Art") #to insert specific location 
print(courses)
courses = ["History", "Math", "Physics", "CompSci"]

courses.extend(courses_2) #To extend the list by elements of second list, not append it with the whole list as a one element
print(courses)
courses = ["History", "Math", "Physics", "CompSci"]

popped = courses.pop() #remove last element
print(popped) #returns popped value
print(courses) #returns the list without the popped element
courses = ["History", "Math", "Physics", "CompSci"]

courses.reverse() #to reverse the list
print(courses) 
courses = ["History", "Math", "Physics", "CompSci"]

courses.sort() #to sort the list
nums.sort()
print(courses) 
print(nums)
courses = ["History", "Math", "Physics", "CompSci"]
nums = [1, 5, 2, 4, 3]

nums.sort(reverse=True) #to sort desc order
print(nums)
nums = [1, 5, 2, 4, 3]

sorted_courses = sorted(courses) #sort the list without altering the original list
print(sorted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index("CompSci")) #gives index of the value
print("Math" in courses) #Turns boolean
print("Art" in courses)

for item in courses:
    print(item)

for index, course in enumerate(courses, start=1):
    print(index, course)

courses_str = ", ".join(courses)
new_list = courses_str.split(", ")
print(courses_str)
print(new_list)

#Tuples

list1 = ["History", "Math", "Physics", "CompSci"]
list2 = list1

print(list1)
print(list2)

list1[0] = "Art"

print(list1)
print(list2)

#tuples are immutable
tuple_1 = ("History", "Math", "Physics", "CompSci")
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#tuple_1[0] = "Art"

#print(tuple_1)
#print(tuple_2)

#Sets
#Sets do not care about order
cs_courses = {"History", "Math", "Physics", "CompSci"}
art_courses = {"History", "Math", "Art", "Design"}

print(cs_courses)
print("Math" in cs_courses)

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

empty_set = set() # empty_set = {} is wrong it is empty dictionary
















