from database.db import dbConnection
from updateCheckBot import search
import time

dbc = dbConnection()



while True:
    print("------------------------------------------")
    print("Let's check the update for favorite things")
    print("1. print all info")
    print("2. insert data into table")
    print("3. search updates")
    print("4. create table")
    print("------------------------------------------")
    number = int(input("input number : "))

    if number is 1:
        search(dbc.printAll())
    elif number is 2:
        name = input("name :")
        url = input("url :")
        dbc.insertIntoFavoriteUpdate(name, url)
    elif number is 3:
        while True:
            time.sleep(100000)
    elif number is 4:
        dbc.createTable()

