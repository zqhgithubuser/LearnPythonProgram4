import shelve


class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id


with shelve.open("shelf1.shelve") as db:
    db["obil"] = Person("Obi-Wan", 123)
    db["ani"] = Person("Anakin", 456)
    db["a_list"] = [2, 3, 5]
    db["delete_me"] = "we will have to delete this one..."
    print(list(db.keys()))
    del db["delete_me"]
    print(list(db.keys()))
    print("delete_me" in db)
    print("ani" in db)
    a_list = db["a_list"]
    a_list.append(7)
    db["a_list"] = a_list
    print(db["a_list"])
