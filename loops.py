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


dict_1 = [{}, {}]
count = 1
for i in range(300):
    if (i % 2 != 0):
        continue
    if (i < 100):
        dict_1[0].update({count: i})
    elif (i > 100 and i < 200):
        if i == 102:
            count = 1
        dict_1[1].update({count: i})
    else:
        if i == 202:
            count = 1
        dict_1.append({count: i})
    count += 1
print(dict_1)



for outer_range in range(1,3):
    for inner_range in range(1,100):
        
        print(outer_range, inner_range)