required_password = "opensesame"
count = 3

while count > 0:
    pw = input("Enter your Password:")
    count -= 1
    if pw == required_password:
        print("Access enabled!")
        break
    else:
        if count > 0:
            print(f"Wrong Password! Try again! You have {count} attempt(s) left.")
        else:
            print("Access denied.")