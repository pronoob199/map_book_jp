from utils.crud import read
from models.data import users

if __name__ == '_main_':

    print(f"Witaj {users[0]['name']}!")
    while True:
        print("Menu:")
        print("0. Zakończ program:")
        print("1. Pokaż co u znajomych: ")
        menu_option:str=input("Wybierz dostępną funkcje z menu: ")
        if menu_option=="0":
            break
        if menu_option == "1":
            read(users)



