#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    data_usage = float(input("Enter Data usage(Mb): "))

    if data_usage <= 200:
        total_charge = 20.0 
    elif 200 < data_usage <= 500:
        rate_per_mb = 0.105
        total_charge = data_usage * rate_per_mb 
    elif 500 < data_usage <= 1000:
        rate_per_mb =  0.11
        total_charge = data_usage * rate_per_mb 
    else :
        total_charge = 118.0
    

    

    print(f"Total charge is ${total_charge:.2f}")

    # YOUR CODE ENDS HERE

main()