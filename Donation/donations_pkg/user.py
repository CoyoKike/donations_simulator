from optparse import Values

database = {}
username = ""
password = ""
def login(database, username, password):
    if username.lower() in database.keys() and password in database.values(): 
        print("Welcome ", username, "!")
        return username
    elif password in database.values() and username not in database.keys():
        print("Username not found, try again")
        return ""
    elif username in database.keys() and database[username] != password:
        print("Wrong password for ", username,  "try again")
        return ""
    else:
        print("Username or password not found, try again")
        return ""

def register(database, username):
    if username in database.keys():
        print("Username already exists")
        return ""
    elif len(username) > 10:
        print("Username cannot be more than 10 characters long, try again")

    else:
        print("Your username is " + username)
        return username

