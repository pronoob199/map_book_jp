from utils.crud import read, create_user
from models.data import users


if __name__ == '_main_':

    print(f"Witaj {users[0]['name']}!")
    while True:
        print("Menu:")
        print("0. Zakończ program:")
        print("1. Pokaż co u znajomych: ")
        print("2. Dodaj znajomego: ")
        menu_option:str=input("Wybierz dostępną funkcje z menu: ")
        if menu_option=="0":
            break
        if menu_option == "1":
            read(users)
        if menu_option == "2":
            create_user(users)





