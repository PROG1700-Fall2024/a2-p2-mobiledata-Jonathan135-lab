#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    gender = input("Are you 'Male' or 'Female': ")
    age = int(input("Enter your age: "))
    vehicle_price = float(input("Please enter the purchase price of the vehicle: "))

    rate = 0 

    if gender == "male": 
        if 15 <= age < 25: 
            rate = 0.25
        elif 25 <= age < 40: 
            rate = 0.17 
        elif 40 <=age < 70: 
            rate = 0.10
        else: 
            rate = 0.10 
    elif gender == "female":
        if 15 <= age < 25:
            rate = 0.20
        elif 25 <= age< 40: 
            rate = 0.15 
        elif 40 <= age< 70: 
            rate = 0.10 
        else: 
            rate = 0.10 

    annual_insurance = vehicle_price * rate 
    monthly_insurance = annual_insurance / 12 

    print(f"Your monthly insurance will be ${monthly_insurance:.2f}")





    # YOUR CODE ENDS HERE

main()