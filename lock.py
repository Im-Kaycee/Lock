
from cryptography.fernet import Fernet
import sqlite3
import hashlib
from termcolor import colored
user_status = False
login_attempts = 3
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the previously generated key
def load_key():
    return open("secret.key", "rb").read()
import os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved!")

def check_and_generate_key():
    key_file = "secret.key"
    
    # Check if the file exists
    if not os.path.exists(key_file):
        print("No encryption key found. Generating a new one...")
        generate_key()
    else:
        # Check if the file is empty
        if os.path.getsize(key_file) == 0:
            print("Encryption key file is empty. Generating a new one...")
            generate_key()
        else:
            print("Encryption key file exists and is not empty.")

def create_user(email_address, password):
   conn = sqlite3.connect("manager.db")
   cur = conn.cursor()
   cur.execute( """CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)""")
   hashed = hashlib.sha256(password.encode())
   passhash = hashed.hexdigest()
   hashed_user = hashlib.sha256(email_address.encode())
   userhash = hashed_user.hexdigest()
   cur.execute('INSERT INTO user(username,password) VALUES(?,?)', (userhash, passhash))
   conn.commit()
   conn.close()

def login(email_address,T_password):
  global user_status
  conn = sqlite3.connect("manager.db")
  cur = conn.cursor()
  cur.execute('SELECT username, password FROM user WHERE username = ?', (hashlib.sha256(email_address.encode()).hexdigest(),))
  result = cur.fetchone()
  if result:
        username, password = result
        # Hash the provided password and compare with stored one
        pass_case = hashlib.sha256(T_password.encode()).hexdigest()
        if password == pass_case:
            user_status = True
            print("Login successful!")
        else:
            print("Invalid password. Try again.")
  else:
        print("User not found. Please check the email address.")
  conn.close()
def create_table():
    conn = sqlite3.connect("manager.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, site TEXT, password TEXT)""")
    conn.commit()
    conn.close()


def insert_details(username,site,password):
    print(username)
    conn = sqlite3.connect("manager.db")
    cur = conn.cursor()
    #hashed = hashlib.sha256(password.encode())
    #hashed_final = hashed.hexdigest()
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())  # Encrypt the password
    cur.execute('INSERT INTO users (username,site,password) VALUES (?,?,?)', (username,site,encrypted_password))
    conn.commit()
    conn.close()
'''def insert_site(site):
    conn = sqlite3.connect("manager.db")
    cur = conn.cursor()
    cur.execute('INSERT INTO users (site) VALUES (?)', (site,))
    conn.commit()
    conn.close()'''
def show_password(site):
    key = load_key()
    f = Fernet(key)
    conn = sqlite3.connect("manager.db")
    cur = conn.cursor()
    cur.execute('SELECT username, password FROM users WHERE site = ?', (site,))

# Fetch the result
    result = cur.fetchone()

    if result:
     username, encrypted_password = result
     decrypted_password = f.decrypt(encrypted_password).decode()
     print(f"Username: {username}\nPassword: {decrypted_password}")
    else:
     print("No matching record found.")
    conn.close()


def delete_password(site):
    conn = sqlite3.connect("manager.db")
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE site = ?', (site,))
    conn.commit()
    conn.close()

'''def insert_password(password):
   conn = sqlite3.connect("manager.db")
   cur = conn.cursor()
   hashed = hashlib.sha256(password.encode())
   hashed_final = hashed.hexdigest()
   cur.execute('INSERT INTO users(password) VALUES (?)', (hashed_final,))
   conn.commit()
   conn.close()'''


        
     
  
  


def show_all():
     key = load_key()
     f = Fernet(key)
     conn = sqlite3.connect("manager.db")
     cur = conn.cursor()
     cur.execute('SELECT username, password, site FROM users ')

# Fetch the result

     result = cur.fetchall()

     if result:
       for username, encrypted_password, site in result:
        decrypted_password = f.decrypt(encrypted_password).decode()
        print(f"Username: {username}\nPassword: {decrypted_password}\nSite: {site}")
     else:
      print("No matching record found.")
     conn.close()

def main():


   print(colored("░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░", 'green'))
   print(colored("░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░", 'green'))
   print(colored("░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░", 'green'))
   print(colored("░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░", 'green'))
   print(colored("░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░", 'green'))
   print(colored("░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░", 'green'))
   print(colored("░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░", 'green'))
   print(colored("                                                     ", 'green'))
   print(colored("                                                     ", 'green'))
   check_and_generate_key()
   action = input("Do you want to create a new account or login? (new/login): ").lower()
   create_table()  # Ensure table is created before operations
   if action == "new":
        email_address = input("Enter your email: ")
        password = input("Enter your password: ")
        create_user(email_address, password)
        print('User Created Successfully. Login to continue')
   elif action == "login":
        for attempt in range(login_attempts):
            email_address = input("Enter your email: ")
            password = input("Enter your password: ")
            login(email_address, password)
            if user_status:
                break
            else:
                print(f"Remaining attempts: {login_attempts - attempt - 1}")
        else:
            print("Too many failed login attempts. Exiting...")
            return
   '''while status:
    choice = input("What do you want to do today?").lower()
    create_table()
    if choice == "add new site":
      username = input("username: ").lower()
      site = input("site: ").lower()
      password = input("password: ")
      insert_details(username,site,password)
    elif choice == "view details":
      site = input("site: ").lower()
      show_password(site)
    elif choice == "delete site":
      site = input("site: ").lower()
      delete_password(site)
    elif choice == "view all":
      show_all()
    elif choice == quit:
      status = False'''
   if user_status:
        print("Welcome to Lock🔒")
        status = True
        while status:
            choice = input("What do you want to do today? (add/view/delete/view all/quit): ").lower()
            
            if choice == "add":
                username = input("Username: ").lower()
                site = input("Site: ").lower()
                password = input("Password: ")
                insert_details(username, site, password)
            elif choice == "view":
                site = input("Site: ").lower()
                show_password(site)
            elif choice == "delete":
                site = input("Site: ").lower()
                delete_password(site)
            elif choice == "view all":
                show_all()
            elif choice == "quit":
                status = False
            else:
                print("Invalid option. Please try again.")



if __name__ == "__main__":
   main()
   