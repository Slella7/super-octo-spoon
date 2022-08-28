family_details = {

}
family_details.update({
    "husband": {
        "first_name": "John",
        "middle_name": "",
        "last_name": "Doe",
        "age": 40,
        "occupation": "Engineer",
        "hobbies": ["Tv", "Music", "Gardening", "Dance"]
    }
}
)
family_details.update({
    "wife": {
        "first_name": "Jane",
        "middle_name": "",
        "last_name": "Doe",
        "age": 35,
        "occupation": None,
        "hobbies": ["Tv", "Cooking", "Craft"]
    }
})
family_details.update({
    "children": [
        {"first_name": "Shane",
         "middle_name": "Watson",
         "last_name": "Doe",
         "age": 12,
         "occupation": None,
         "hobbies": ["Dance", "Tv"]},
        {"first_name": "Lilly",
         "middle_name": None,
         "last_name": "Doe",
         "age": 5,
         "occupation": None,
         "hobbies": ["Tv"]}
    ]
})
family_details.update({
    "pets": [
        {
            "name": "Oliver",
            "age": 7,
            "gender": "Male"
        },
        {
            "name": "Gus",
            "age": 5,
            "gender": "Male"
        }
    ]
})

'''
3. check for the following conditions from the above data: 
- who has more number of hobbies
- who doesn't have a middle name 
- what is the age of Oliver? 
- are both pets male or female? 
- whose occupation is not given in the above table? 
- whose age is an even number and number of characters in his/her name is 4

'''
wife_hobbies = len(family_details["wife"]["hobbies"])
child_1_hobbies = len(family_details["children"][0]["hobbies"])
child_2_hobbies = len(family_details["children"][1]["hobbies"])
husband_hobbies = len(family_details["husband"]["hobbies"])

larger = 0

child_1_hobbies = 1
wife_hobbies = 7
child_2_hobbies = 11
husband_hobbies = 6

if (wife_hobbies > husband_hobbies and child_1_hobbies and child_2_hobbies):
    person_with_more_hobbies = "wife"
    larger = wife_hobbies
elif (child_1_hobbies > husband_hobbies and child_2_hobbies and wife_hobbies):
    person_with_more_hobbies = "child_1"
    larger = child_1_hobbies
elif (child_2_hobbies > child_1_hobbies and husband_hobbies and wife_hobbies):
    person_with_more_hobbies = "child_2"
    larger = child_2_hobbies
elif (husband_hobbies > child_1_hobbies and child_2_hobbies and wife_hobbies):
    person_with_more_hobbies = "husband"
    larger = husband_hobbies
else:
    pass

print(person_with_more_hobbies)


# who doesn't have a middle name


wife_middle = family_details["wife"]["middle_name"]
husband_middle = family_details["husband"]["middle_name"]
child_1_middle = family_details["children"][0]["middle_name"]
child_2_middle = family_details["children"][1]["middle_name"]


if (husband_middle == "" or husband_middle == None):
    print("Husband doesn't have a middle name")
if (wife_middle == "" or wife_middle == None):
    print("wife doesn't have a middle name")
if (child_1_middle == "" or child_1_middle == None):
    print("child_1 doesn't have a middle name")
if (child_2_middle == "" or child_2_middle == None):
    print("child_2 doesn't have a middle name")

# OR

# middle_names = {"husband": husband_middle, "wife": wife_middle,
#                 "child_1": child_1_middle, "child_2": child_2_middle}
# key = middle_names.keys()
# if (key in middle_names.get(key) == ""):
#     print(key + " doesn't have a middle name")

# which pet is older
if (type(family_details["pets"][0]["age"]) is int and type(family_details["pets"][1]["age"]) is int):

    if (family_details["pets"][0]["age"] == family_details["pets"][1]["age"]):
        print("same")
    elif (family_details["pets"][0]["age"] > family_details["pets"][1]["age"]):
        print("Oliver")
    else:
        print("Gus")
else:
    print("One of the operands is of not integer type")


# gender male or not
# if (type(family_details["pets"][0]["gender"]) is str and type(family_details["pets"][1]["gender"]) is str):

#     if (family_details["pets"][0]["gender"] == "male"):
#         print("same")
#     elif (family_details["pets"][0]["age"] > family_details["pets"][1]["age"]):
#         print("Oliver")
#     else:
#         print("Gus")
# else:
#     print("One of the operands is of not integer type")

gender = family_details["pets"].get(0).get("gender")
