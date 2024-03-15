import json
import pandas as pd


def load_password():
    try:
        df = pd.read_excel('Passwörter.xlsx')#I use pandas to read my excel File and load its content into a DataFrame = df            
        return df ['Account'].tolist(), df['Username'].tolist(), df['Password'].tolist()#line returns the data loaded from the Excel file
        #tolist() method is called on each column to convert them into Python lists.
    except FileNotFoundError:
        return [], [], []



def save_passwords(accounts, usernames, passwords):
    df = pd.DataFrame({'Account':accounts, 'Username': usernames, 'Password': passwords})#this will create a dataframe from a dc keys are columns
    df.to_excel('Passwörter.xlsx', index=False) #set the index to false to exclude row numbers


def _question():
    accounts,usernames,passwords = load_password()
    while True:#in a while loop to let the program not directly close after one input. If you want to delete more passwords or add more
        question = input("What would you like to do?\n1. Add a new password\n2. Delete an account\n3. See passwords\n4. Gar nichts\nEnter the number corresponding to your choice: ")
        if question == '1':
            print("Okay lets go it has to have 13 and a special character: ")
            _add_password(accounts,usernames, passwords)

        elif question == '2':
            _delete_password(accounts,usernames,passwords)

        elif question == '3':
            print('Anbieter:')
            print(accounts)
            print("All usernames:")
            print(usernames)
            print("All passwords:")
            print(passwords)
    
        elif question == '4':
            print("Okay hope I see you soon!")
            break
        else:
            print("Please enter a number from 1-4")

def _add_password(accounts,usernames, passwords):
    new_account = input("Enter the Acoount: ")
    new_username = input("Username pls: ")
    new_password = input("Enter your new password: ")
    sonderzeichen = ".,/!?"
    #mit dem char schaut er jeden character in sonderzeichen nach
    if any(char in sonderzeichen for char in new_password):
        if len(new_password) >= 13:
            print("Congrats that is working")
            print(new_username)
            passwords.append(new_password)
            usernames.append(new_username)
            accounts.append(new_account)
            save_passwords(accounts, usernames, passwords)
        else:
            print("Password has to be longer")
    else:
        print("Password must contain at least one special character")

def _delete_password(accounts, usernames, passwords):
    delete_one = input("Enter which Account you want to delete:")
    if delete_one in accounts: #wenn deleteone in accounts ist dann aus der liste löschen
        index = accounts.index(delete_one)
        del accounts[index]
        del usernames[index]
        del passwords[index]
        print("Account deleted successfully.")
        save_passwords(accounts,usernames,passwords)
    else:
        print("This Account does not exist!")  
        

_question()
#Display the usernames and passwords
