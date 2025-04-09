class Divar:
    
    usernames = []
    advertise = {}

    @classmethod
    def register(cls, username):
        if username in cls.usernames:
            print("invalid username!")
        else:
            cls.usernames.append(username)
            cls.advertise[username] = []
            print(f"{username} registered successfully")
        print("*" * 30)


    @classmethod
    def add_advertise(cls, username, advertise_title):
        if username not in cls.usernames:
            print(f"{username} is not registered!. Please register first. \n")
            response = input("Do you want to sign up? (yes/no): \n").lower()
            if response == "yes":
                cls.register(username)
                
            else:
                return

        if advertise_title in cls.advertise[username]:
            print("invalid title!")
        else:
            cls.advertise[username].append(advertise_title)
            print(f"{username}, your advertise: { advertise_title}, posted successfully")
        print("*" * 30)

    @classmethod
    def rem_advertise(cls, username, advertise_title):
        if username not in cls.usernames:
            print(f"{username} is not registered!. Please register first.\n")
            response = input("Do you want to sign up? (yes/no): \n").lower()
            if response == "yes":
                cls.register(username)
            else:
                return
            print("*" * 20)

        if advertise_title not in cls.advertise[username]:
            print("access denied!")
        else:
            cls.advertise[username].remove(advertise_title)
            print(f"{advertise_title} removed successfully")
        print("*" * 20)

    @classmethod
    def list_my_advertises(cls, username):
        if username not in cls.usernames:
            print(f"{username} is not registered!.")
            
            return

        titles = cls.advertise.get(username,[])
        if not titles:
            print("no adverts yet")
        else:
            print(" ".join(titles))

def main():
    while True:
        print("    ")
        print("your choices: \n")
        print("1_ sign in")
        print("2_ add advertise")
        print("3_ remove advertise")
        print("4_ my advertises list \n")
        choice=input("enter your choice number: ")
        print("    ")
        if choice =='1':
            username=input("enter your username:")
            Divar.register(username)
        elif choice =='2':
            username=input("enter your username:")
            advertise_title=input("enter your advertise_title :")
            Divar.add_advertise(username,advertise_title)
        elif choice =='3':
            username=input("enter your username:")
            advertise_title=input("enter your advertise_title :")
            Divar.rem_advertise(username,advertise_title)
        elif choice =='4':
            username=input("enter your username:")
            Divar.list_my_advertises(username)
        else:
            print("invalide number!")


main()






         