'''

1. create an empty dictionary 
2. use dictionary methods to update each item one at a time (use different datatypes)


Dictionary Methods: 
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

'''

# created empty dictionary inside a list for family details
family_details = [{}]

# person 1
person_1 = {

    "first_name": "John",
    "middle_name": "",
    "last_name": "Doe",
    "age": 40,
    "occupation": "Engineer",
    "hobbies": ["TV", "music", "gardening"]
}

# added person 1 to first index of family details
family_details[0] = person_1

# copied person 1 into person 2
person_2 = person_1.copy()

# updated the data for person 2 and added to family details
person_2.update({

    "first_name": "Jane",
    "middle_name": "",
    "last_name": "Doe",
    "age": 35,
    "hobbies": ["TV", "cooking", "crafts", "singing"]
})

family_details.append(person_2)

# created person 3 and 4 and added to family details
person_3 = {

    "first_name": "Shane",
    "middle_name": "Watson",
    "last_name": "Doe",
    "age": 12,
    "occupation": "5th Grade",
    "hobbies": ["dance", "TV"]
}


person_4 = {

    "first_name": "Lilly",
    "middle_name": "",
    "last_name": "Doe",
    "age": 5,
    "occupation": None,
    "siblings": 1
}

person_4.pop("siblings")
person_4.update({"hobbies": ["TV"]})

person_2.values()
person_2.setdefault("occupation")

family_details.append(person_3)
family_details.append(person_4)


print(family_details)

# pet details info in dictionary
pet_details = {

    "no_of_pets": 2,
    "pets": [
        {
            "name": "Oliver",
            "gender": "male",
            "age": 5
        },
        {
            "name": "Gus",
            "gender": "male",
            "age": 4
        }
    ]
}

# adding pet details to family details
family_details.append(pet_details)
print(family_details)


'''
3. check for the following conditions from the above data: 
- who has more number of hobbies
- who doesn't have a middle name 
- what is the age of Oliver? 
- are both pets male or female? 
- whose occupation is not given in the above table? 
- whose age is an even number and number of characters in his/her name is 4

'''

# who has a greater number of hobbies
family_details_length = len(family_details)
n = 0
key = "hobbies"
highest_no_hobbies = ""
hobbies_length = 0

while n < family_details_length:
    if (key in family_details[n].keys()):
        hobbies_no = len(family_details[n][key])
        name = family_details[n]["first_name"]
        if hobbies_no > hobbies_length:
            hobbies_length = hobbies_no
            highest_no_hobbies = name
    n = n+1

print("person with the most hobbies is " + highest_no_hobbies)


# who doesn't have a middle name
