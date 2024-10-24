#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    house_number = input("Enter House Number: ")
    property_depth = float(input("Enter property depth(feet): "))
    property_width = float(input("Enter property width(feet): "))
    type_of_grass = input("Enter the type of grass(fescue, bentgrass, campus): ").lower()
    number_of_trees = int(input("Enter the number of trees: "))

    area = property_depth * property_width 
    base_labour_cost = 1000.0
    additional_cost = 0.0
    if area > 5000 :
        additional_cost = 500.0
    if type_of_grass == "fescue": 
        cost = 0.05
    elif type_of_grass == "bentgrass":
        cost = 0.02 
    elif type_of_grass == "campus" : 
        cost = 0.01
    
    tree_cost = 100.0 * number_of_trees 

    total_cost = ( area * cost) + tree_cost + base_labour_cost + additional_cost

    print(f"total cost for house {house_number} is: ${total_cost:.2f}")

    # YOUR CODE ENDS HERE

main()