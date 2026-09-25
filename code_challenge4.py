import getpass
username = "Greed"
password = "mahalkopasya123"



x = input("Input USERNAME -->")
y = getpass.getpass("Input PASSWORD -->")  

if x == username or y == password:
  print("Your password are correct.")
else:
 print("Incorrect password or username.")
 exit()

first_name = input("Enter your first name -->")
age = eval(input("Enter your age -->"))
job_description = input("Enter your Job Description -->")
income = float(input("What is your yearly income? "))
is_employed = input("Are you currently employed (True\\False)-->") == "True"
has_collateral = input("Do you have any collateral (True\\False)-->") == "True"
credit_score = eval(input("Credit scrore history -->"))
annual_income = eval(input("How much is your annual income -->"))

if has_collateral == "True":
    collateral_value = float(input("What is the value of your collateral? "))
    if collateral_value >= 30000:
        print("Collateral value is sufficient for a loan.")
    else:
        collateral_value < 30000
        has_collateral = "False"
        print("Collateral value is too low for a loan.")
if age >= 21 or age <= 65 and is_employed == "True":
        loan_amount = float(input("How much money are you looking to borrow? "))
        if credit_score >= 750:
          if annual_income >= 100000: 
            final_rate = loan_amount // 4.5
            total_value = loan_amount + final_rate
            print("Final rate is 4.5%, total interest amount is: ",final_rate, "Total loan amount with interest is: ",total_value)
          else:
            final_rate = loan_amount // 5.0
            total_value = loan_amount + final_rate
            print("Final rate is 5.0%, total interest amount is: ",final_rate, "Total loan amount with interest is: ",total_value)
        elif credit_score >= 600 and credit_score < 750: 
           if has_collateral == "True":
            final_rate = loan_amount //7.0
            total_value = loan_amount + final_rate
            print("Final rate is 7.0%, total interest amount is: ",final_rate,"Total loan amount with interest is: ",total_value)
           else:
            final_rate = loan_amount // 8.0
            total_value = loan_amount + final_rate
            print("Final rate is 8.0%, total interest amount is: ",final_rate, "Total loan amount with interest is: ",total_value)       
        else:
         print("Credit score too low for a loan.")
else:
 print("You need to be 21 years old and employed to apply for a loan.")