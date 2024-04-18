    def read(users:list[dict])->None:
        for user in users[1:]:
            print(f'Twój znajomy {user["name"]} opublikował: {user["posts"]}')
    def create(users:list[dict])->None:
        name:str=input("Podaj imie uzytkownika: ")
        surnmame: str=input("Podaj nazwisko użytkownika: ")
        posts: str=input("Podaj lczbę postów:")
        user:dict={ "name": name, "surname": surname, "posts": posts}
        users.append(user)

     def seeach(user:list[dict])-> None
            user_name: str = input("Kogo szukasz: ")
            for user in users[1:]:
                if user["name"]==user_name:
                    print(f'Twój znajomy {user["name"]} opublikował: {user["posts"]}')


    def remove(users: list[dict]) -> None
        user_name: str = input("Kogo szukasz: ")
        for user in users[1:]:
            if user["name"] == user_name:
                users.remove(user)