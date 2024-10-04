
import argparse
import sqlite3
import hashlib
from termcolor import colored

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
    hashed = hashlib.sha256(password.encode())
    hashed_final = hashed.hexdigest()
    cur.execute('INSERT INTO users (username,site,password) VALUES (?,?,?)', (username,site,hashed_final))
    conn.commit()
    conn.close()
'''def insert_site(site):
    conn = sqlite3.connect("manager.db")
    cur = conn.cursor()
    cur.execute('INSERT INTO users (site) VALUES (?)', (site,))
    conn.commit()
    conn.close()'''
def show_password(site):
    conn = sqlite3.connect("manager.db")
    cur = conn.cursor()
    cur.execute('SELECT username, password FROM users WHERE site = ?', (site,))

# Fetch the result
    result = cur.fetchone()

    if result:
     username, password = result
     print(f"Username: {username}\nPassword: {password}")
    else:
     print("No matching record found.")


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
     conn = sqlite3.connect("manager.db")
     cur = conn.cursor()
     cur.execute('SELECT username, password FROM users ')

# Fetch the result

     result = cur.fetchall()

     if result:
       for username, password in result:
        print(f"Username: {username}\nPassword: {password}")
     else:
      print("No matching record found.")
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

   print("Welcome to Lock🔒")
   status = True
   while status:
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
      status = False



if __name__ == "__main__":
   main()