# write a function which takes an integer argument and gives the sqaure of that number as return value

# 5
# 25


def int_square(num):
    square = pow(num, 2)
    return square


print(int_square(5))


# write a function which takes an integer as an argument and gives the times table till 12 result as a list

# 2
# [2,4,6,8,10....24]


def times_table(num):
    list1 = []
    for i in range(1, 13):
        list1.append(num*i)
    print(list1)


times_table(2)


# write a function which takes an empty list and integer as arguments and gives back the following

# 4,[]
# [4,16,64,256,1024]

def func_mul(num, list1):
    list1 = [num]
    for i in range(num):
        list1.append(num*list1[-1])
    return list1


print(func_mul(4, []))


# write a function which takes a list with integers as arguement and gives back even numbers from that list

# [1,2,3,4,5,8,12]
# [2,4,8,12]

def list_even(list1):
    even_list = []
    for i in list1:
        if i % 2 == 0:
            even_list.append(i)
    print(even_list)


list_even([1, 2, 3, 4, 5, 8, 12])
