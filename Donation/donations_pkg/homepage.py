def show_homepage():
    print("=== DonateMe Homepage ===\n---------------------\n|1.  Login   |2.  Register        |\n|3.  Donate  |4.  Show Donations  |\n|    5.    Exit                   |\n --------------------- ")

def donate (username):
    donation_atm = float(input("Enter amount to donate "))
    donation_string = username, " donated ", float(donation_atm)
    print("You donated: ", donation_atm, " Thank you!")
    return donation_string
    
    

def show_donations(donations):
    print("\n---All Donations---")
    if not donations:
        print("Currently there are no donations, Don't be cheap!")
    else:
        print(donations)
