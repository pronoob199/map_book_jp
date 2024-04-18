def read(users:list[dict])->None:
    for user in users[1:]:
        print(f'Twój znajomy {user["name"]} opublikował: {user["posts"]}')
   users: list[dict] = [
        {"name": "Jakub", "surname": "Praski", "posts": 20},
        {"name": "Janek", "surname": "Mielec", "posts": 1},
        {"name": "Maciej", "surname": "Przybytek", "posts": 45},
        {"name": "Bartosz", "surname": "Pietrasik", "posts": 30},
        {"name": "Tymoteusz", "surname": "Miszczak", "posts": 15},
        {"name": "Mateusz", "surname": "Matysiak", "posts": 10},

    name:str=input("Podaj imie uzytkownika: ")
    surnmame: str=input("Podaj nazwisko użytkownika: ")
    posts: str=input("Podaj lczbę postów:")
    user:dict={ "name": name, "surname": surname, "posts": posts}
    users.append(user)

create_users(users)

print(users)