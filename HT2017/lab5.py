#Övningar Labb5
def create_lock(key, msg):
    def my_lock(n):
        if n == key:
            print(msg)
        else:
            print("Fel Kod!")
    return my_lock

