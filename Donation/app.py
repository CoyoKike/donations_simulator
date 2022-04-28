from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register
#variables
database = {"admin": "password123"}
donations = []
authorized_user = ""

while True:
    #Main menu
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate. ")
    else:
        print("Logged in as: ", authorized_user)
    user_input = input("Choose an option: ")
    if user_input == "1":
        username = input("Choose an username: ")
        password = input("Create a password: ")
        authorized_user = login(database, username, password)
    elif user_input == "2":
        username = input("Create an username: ")
        password = input("Create password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password

    elif user_input == "3":
        if authorized_user == "":
            print("You are not logged in")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
        


    elif user_input == "4":
        show_donations(donations)

    elif user_input == "5":
        print("Goodbye!")
        break
    else:
        print("Try again")