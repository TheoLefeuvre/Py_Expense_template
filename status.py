from PyInquirer import prompt
import csv


class Expenditure:
    def __init__(self) -> None:
        self.amount = 0
        self.spender = ""
        self.others = []

    def print(self):
        print(self.amount)
        print(self.spender)
        print(self.others)


def update_user_amount(debts, user, amount):
    i = 0
    while i < len(debts):
        (a, b) = debts[i]
        if user == a:
            debts[i] = (a, b + amount)
            break
        i += 1


def show_status():
    # Load file into a program variable to compute status
    path = "expense_report.csv"
    file = open(path, "r")
    content = file.read()
    expenses = content.split(";")
    expenses.pop()
    sane_expenses = []

    for block in expenses:
        block = block.strip("\n")
        block = block.strip()
        sane_expenses.append(block)

    object_expenses = []

    for exp in sane_expenses:
        count = 0
        obj = Expenditure()
        for line in exp.splitlines():
            if count == 0:
                obj.amount = int(line.split(",")[1])
            elif count == 1:
                count += 1
                continue
            elif count == 2:
                obj.spender = line.split(",")[1]
            elif count == 3:
                for other in line.split(","):
                    obj.others.append(other)
                object_expenses.append(obj)
                # Remove last elt caused by trailing "comma"
                obj.others.pop()
                obj.print()
            else:
                count = 0
            count += 1

    # Store debts
    debts = []

    path = "users.csv"

    users = csv.reader(open(path, "r"), delimiter=",")
    for user in users:
        debts.append((user, 0))

    # Compute debts
    for exp in object_expenses:
        total_others = len(exp.others)
        part = exp.amount / total_others
        update_user_amount(debts, exp.spender, part)
        for other in exp.others:
            update_user_amount(debts, other, -part)

    print(debts)
