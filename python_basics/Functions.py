
def hello_func():
    print("Hello Function!")

hello_func()

print("--------")

def hello_func2():
    return "Hello Function!"

print(hello_func2())
print(hello_func2().upper())

print("--------")

def hello_func3(greeting):
    return "{} Function.".format(greeting)

print(hello_func3("Hi"))

print("--------")

def hello_func4(greeting, name = "You"):
    return "{}, {} Function.".format(greeting, name)

print(hello_func4("Hi", name = "Claire"))

print("--------")

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info("Math", "Art", name = "John", age = 22)

print("--------")

courses = ["Math", "Art"]
info = {"name": "John", "age": 22}

student_info(*courses, **info)

print("--------")

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """ Return True for leap years"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """ return number of days in that month in that year"""
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29 
    return month_days[month]

print(is_leap(2017))
print(days_in_month(2017, 2))

print("--------")











