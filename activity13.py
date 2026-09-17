
age = eval(input("Enter your age"))
is_employed = input("Are you currently employed -->") == "True"
credit_score = eval(input("Credit scrore history -->"))
annual_income = eval(input("How much is your annual income -->"))
has_collateral = input("Do you have any collateral") == "True"
    

if age >= 21 and is_employed == "True":
    if credit_score >= 750:
        if annual_income >= 100000: 
            print("Final rate is 4.5%")
        else:
            print("Final rate is 5.0%")
    elif credit_score >= 600 and credit_score < 750: #tier 2
        if has_collateral == "True":
            print("Final rate is 7.0%")
        elif  annual_income < 40000:
            print("Final rate is 8.0%")
        
    elif credit_score < 600:
        print("Rejected: Credit score too low")
else:
    print("Rejected: Fails baseline criteria")


            
    
