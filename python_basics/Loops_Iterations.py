
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print("Found!")
        break
    print(num)

print("------------")

for num in nums:
    if num == 3:
        print("Found!")
        continue #skip to next iteration
    print(num)

print("------------")

for num in nums:
    for letter in 'abc':
        print(num, letter)

print("------------")

for i in range(10):
    print(i)

print("------------")

for i in range(1, 11):
    print(i)

print("------------")

x = 0

while x < 10:
    print(x)
    x += 1

print("------------")

y = 0

while y < 10:
    if y == 5:
        break
    print(y)
    y += 1






