import getpass
loginattempt = 0
username = "Greed"
password = "Secret123"

while True:
    user = input("Enter Your Username: ---> ")
    pas = input("Enter Your Password: ---> ")

    if user == username and pas == password:
        print("Successfull Log In")
        print("Login Attempts: ", loginattempt)
        break
    else:
        print('Failed to log in')
        loginattempt = loginattempt + 1