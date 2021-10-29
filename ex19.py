#this the main function. It defines the variables for cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
        print(f"You have {cheese_count} cheese!")
        print(f"You have {boxes_of_crackers} boxes of crakcers!")
        print("Man that's enough for a party!")
        print("Get a blanket. \n")


#calls the function cheese_and_crackers and fills in the variable's values
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


#gives the variables values in cheese_and_crackers
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

#calls the function with the defined variable above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#calls the function cheese_and_crackers and fills in the variables as a list after doing some maths
print("We can even do math inside too:")
cheese_and_crackers(10 + 2, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
