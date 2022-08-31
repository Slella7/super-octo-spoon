# continue - skips that instance and skips the rest of that loop
for i in range(0, 10):
    if (i == 4):
        continue
    print("NUMBER - ", i)


for i in range(0, 10):
    if (i == 4):
        break
    print("NUMBER - ", i)

list_1 = []
for i in range(100):
    if (i % 2 != 0):
        continue
    list_1.append(i)
print(list_1)

dict_1 = {}
count = 1
for i in range(100):
    if (i % 2 != 0):
        continue
    dict_1.update({count: i})
    count += 1
print(dict_1)


dict_1 = [{}, {}, {}]
count = 1
for i in range(300):
    if (i % 2 != 0):
        continue
    if (i <= 100):
        dict_1[0].update({count: i})
    elif (i > 100 and i <= 200):
        if i == 102:
            count = 1
        dict_1[1].update({count: i})
    else:
        if i == 202:
            count = 1
        dict_1[2].update({count: i})
    count += 1
print(dict_1)


# factorial of any number

number = 9
x = 1
factorial = 1
while number > x:
    factorial *= number
    number -= 1
print(factorial)

# number = 5
# x = 1
# factorial = 1
# for y in range(number, 1, -1):
#     factorial *= number

# use logical operators and elif

if factorial % 2 == 0 and factorial / 10 == int:
    print("factorial is divisble by 10 and is even")
elif factorial % 2 != 0 and factorial / 3 == int:
    print("factorial is odd and divisible by 3")
else:
    print("none of the above conditions met")
