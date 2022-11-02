from PyInquirer import prompt
import csv

user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "What's your name ?",
    }
]


def find_user(user, path):
    csv_file = csv.reader(open(path, "r"), delimiter=",")
    for row in csv_file:
        if row[0] == user:
            return True
    return False


def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)

    user = infos.get("name")
    if find_user(user, "users.csv"):
        print("User already exists !")
    else:
        file = open("users.csv", "a")
        file.write(user + "\n")
        file.close()
        print("User added !")

    return
