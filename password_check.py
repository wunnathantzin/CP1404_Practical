Symbol="*"
def main():
    password=input("Enter the password:")
    while not valid_password(password):
        print("Invalid password")
        password=input("Enter the password:")
def valid_password(password):
    if len(password)<=0:
        return False
    password_count=0
    for char in password:
        if char.islower():
            password_count +=1
        if char.isupper():
            password_count += 1
    for i in range(password_count):
        print(Symbol,end='')
    if password_count<0:
        return False
    return True
main()
