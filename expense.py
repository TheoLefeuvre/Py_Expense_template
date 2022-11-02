from PyInquirer import prompt
from user import find_user

expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "input",
        "name": "spender",
        "message": "New Expense - Spender: ",
    },
    {
        "type": "input",
        "name": "others",
        "message": "Type the user names of the other people involved in this expenditure\nPlease respect the following format: user1,user2,user3,user4...,userX"
    }

]


def new_expense(*args):
    infos = prompt(expense_questions)

    # Check if amount is a number
    if not infos.get('amount').isnumeric():
        print('Amount entered is not a number !')
        return False

    # Check if spender exists beforehand
    boolean = find_user(infos.get('spender'), "users.csv")
    if not boolean:
        print("User doesn't exist !")
        return False

    # Split others involved people string into a list
    others = infos.get('others')
    list_others = others.split(',')

    # Check if all users exists
    for other in list_others:
        # Check if user exists
        # If user is empty, we skip it
        if other != '' and not find_user(other, "users.csv"):
            print("This user doesn't exists: " + other)
            print("Please try again")
            return False

    # Open expense file
    file = open("expense_report.csv", "a")

    # Write amount, expense label and user name
    file.write("amount," + infos.get("amount") + "\n")
    file.write("label," + infos.get("label") + "\n")
    file.write("spender," + infos.get("spender") + "\n")

    writed = False

    # Write other spenders
    for other in list_others:
        if other == infos.get('spender') or other == '':
            continue
        writed = True
        file.write(other + ',')
    if writed:
        file.write("\n")

    file.close()
    print("Expense Added !")
    return True
