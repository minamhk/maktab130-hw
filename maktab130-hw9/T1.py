class Singleton:
    _instance= None

    def __new__(cls):
        if cls._instance is None:
            print("making new one")
            cls._instance = super().__new__(cls)
        else:
            print("already existed")
        return cls._instance


ob1 = Singleton()
ob2 = Singleton()
ob3 = Singleton()

print(ob1 is ob2)
print(ob1 != ob3)
