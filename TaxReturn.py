# ***********************
# By: Luciano Zavala   *
# ***********************

# welcome message
print("Welcome to the Tax Return program")
print("----------------------------------------")

# Prompt the user
single = input("Are you single? ")
if (single == 'N') or (single=='n'):
    print("You must be Single")
    
#Yes if you are single
elif (single == 'Y') or (single=='y'):
    under65 = input("Are you under 65 year old? ")
		
#No under 65 years old	
    if (under65 == 'N') or(under65=='n'):
        income9400 = input("Is yous income less than $9400")
        
#No Income under $9400
        if (income9400 == 'N') or (income9400=='n'):
            print("you have to pay taxes")
            
#Income above $9400
        elif (income9400 == 'Y') or(income9400== 'y'):
            print("You do not have to pay taxes")
            
#Invalid Input
        else:
            print("Invalid Input")

#If Yes under 65 years old
    elif (under65 == 'Y') or(under65== 'y'):
        income8540 = input("is your income less than $8540?")

#If income above $8540
        if (income8540 == 'N') or (income8540=='n'):
            print("you have to pay taxes")
            
#If income less than $8540
        elif (income8540 == 'Y') or (income8540=='y'):
            print("You do not have to pay taxes")
            
#Invalid Iuput
        else:
            print("Invalid Input")

#Invalid Input
    else:
        print("Invalid Input")
        
#Invalid input
else:
    print("Invalid Input")







