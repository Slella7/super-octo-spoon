'''

Exercise : weekend

    Clone your own repository.

    Write a program to pring 

            biodata of a sample person X
            Name,Age,marital,children,

            "I am learning Python"

            use slicing concepts on the above and print the words

            make sure you have in-line


    push your code to the repository

    share your code link in the group

    '''

first_name = "Sai"
last_name = "B"
age = 30
marital_status = True
children = 2


# sample biodata of person as a list
biodata = [first_name, last_name, age, marital_status, children]

print(biodata)

# sample biodata printed seperately
print("First Name: " + first_name)
print("Last Name: " + last_name)
print("Age: " + str(age))
print("Married: " + str(marital_status))
print("Number of Children: " + str(children))


# Slicing concepts
string = "I am learning Python"
print(string[0])
print(string[2:4])
print(string[5:13])
print(string[14:])
print(string[:])
print(string[-1::-1])
