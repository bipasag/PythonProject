correct_username = "bipasa"
correct_password = "python"

attempts = 0

while attempts < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        attempts += 1
        print("Wrong credentials. Try again.")

if attempts == 5:
    print("Access denied.")
