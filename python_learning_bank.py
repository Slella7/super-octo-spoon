
"""
        Python Learnings Bank
    
    Please enter account number - 8943  # This account number should be 4 digit

    Please enter valid account number

    Account doesnt exists!! please try again

    Please enter your pin - 45 # pin number should always be 2 digit


        Welcom Mr Mark / Ms Leena
        

        please select from following options
            1. withdrawl
            2. balance display

            if 2 -> Your account has 34$

           if 1->  please enter amount you want to withdraw - 35

            if withdrawl amount is in the range please update the balance in the dictionary 
            else display insufficient funds message

        you want to continue 1 or 2 
        to exit press 3


"""
bank_details = {
    1234:
    {
        "name": "Mark",
        "balance": 45,
        "pin": 12,
        "gender": "Male"
    },
    4567:
    {
        "name": "Leena",
        "balance": 30,
        "pin": 45,
        "gender": "Female"
    }
}
# account number


def get_num():
    account_num = int(input("Please enter account number: "))

    while account_num >= 10000:
        print("Account number invalid")
        account_num = int(input("Please enter valid account number: "))

    keys = bank_details.keys()
    while account_num not in keys:
        print("Account number doesn't exist")
        account_num = int(input("Please enter valid account number: "))


get_num()

#    Please enter your pin - 45 # pin number should always be 2 digit
pin_num = int(input("Please enter pin number: "))
while pin_num >= 100:
    print("pin number invalid")
    pin_num = int(nput("Please enter valid pin number: "))


# welcome page
def welcome():
    if account_num in keys:
        if pin_num == bank_details[account_num]["pin"]:
            if bank_details[account_num]["gender"].lower() == "male":
                print("Welcome Mr." + bank_details[account_num]["name"])
            else:
                print("Welcome Ms." + bank_details[account_num]["name"])


welcome()

# please select from following options:
# 1. withdrawl
# 2. balance display


def options():
    print("Please select from the following options: ")
    option1 = int(input("1. Withdrawal /n2. Display Balance /n3. Exit"))

    if option1 == 1:
        wdwl_amt = int(input("Please enter amount you want to withdraw: "))
        if wdwl_amt > bank_details[account_num]["balance"]:
            print("Insifficient funds")
        else:
            print("Withdrawal amount: " + str(wdwl_amt))
            balance = bank_details[account_num]["balance"] - wdwl_amt
            bank_details[account_num].update({"balance": balance})
    elif option1 == 2:
        balance = bank_details[account_num]["balance"]
        print("Your account balance is " + balance)
    elif option1 == 3:
        print("EXIT")
        get_num()
    else:
        print("Invalid option")
        options()


options()
