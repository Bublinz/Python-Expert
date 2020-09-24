
# A python program with the continue statement
while True:
    print("Who are you")
    name = input()
    if name != 'Peter':
        continue
    print("Hello, Peter. What is the password? (It is a Fish)")
    password = input()
    if password == "swordfish":
        break
print("Access Granted")
