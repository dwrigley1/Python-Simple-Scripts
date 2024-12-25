'''
This script is a good example of combining while True loops with if/else statements, and exceptions.
'''

# pip install IPython
# if using Spyder, this clears the console so you can have a blank canvas
try:
    from IPython import get_ipython
    get_ipython().magic('clear')
    get_ipython().magic('reset -f')
except:
    pass
# ^ this can be deleted if it is not needed ^ #

while True: 
    size = input("Would you like a small, medium, or large coffee? ")
    if size == 'small': 
        cupSize = 2.00
        print("That will be $2.00")
    if size == 'medium':
        cupSize = 3.00
        print("That will be $3.00")
    if size == 'large':
        cupSize = 4.00
        print("That will be $4.00")
    if size.lower() not in ('small', 'medium', 'large'):
        print("That is not a valid size, please try again.")
    else:
        break
       
while True: 
    cream = input("Would you like cream, milk, half and half or none? ") 
    if cream == 'cream': 
        creamAdd = 2.00 
        print("That will be an additional $2.00")
    if cream == 'milk':
        creamAdd = 1.00
        print("That will be an additional $1.00")
    if cream == 'half and half':
        creamAdd = 1.50
        print("That will be an additional $1.50")
    if cream == 'none':
        creamAdd = 0.00
        print("Ok, no additional charge then")
    if cream.lower() not in ('cream', 'milk', 'half and half', 'none'):
        print("That is not a valid option, please try again.")
    else:
        break
    
while True: 
    sugar = input("Would you like to add sugar for $1.00? ") 
    if sugar == 'yes': 
        sugarAdd = 1.00
        print("Ok, great!")
    if sugar == 'no':
        sugarAdd = 0.00
        print("Ok, no problem")
    if sugar.lower() not in ('yes', 'no'):
        print("That is not a valid response, please answer 'yes' or 'no'.")
    else:
        break
    
while True:
    pastry = input("Would you like to add a pastry? ")
    if pastry == 'yes':
        print("Ok, which style?")
    if pastry == 'no':
        pastryCost = 0.00
        print("Ok, just a coffee then!")
    if pastry.lower() not in ('yes', 'no'):
        print("Please say yes or no")
    else: 
        break

while pastry == 'yes': 
    pastryStyle = input("Would you like a danish, bagel, donut, or muffin? ")
    if pastryStyle == 'danish': 
        pastryCost = 2.00
        print("Ok, that will be $2.00")
    if pastryStyle == 'bagel':
        pastryCost = 1.50
        print("Ok, that will be an additional $1.50")
    if pastryStyle == 'donut':
        pastryCost = 1.75
        print("Ok, that will be an additional $1.75")
    if pastryStyle == 'muffin':
        pastryCost = 2.00
        print("Ok, that will be an additional $2.00")
    if pastryStyle.lower() not in ('danish', 'bagel', 'donut', 'muffin'):
        print("Sorry, that is not a valid selection. Try Again")
    else:
        break
    
    
orderTotal = cupSize + creamAdd + sugarAdd + pastryCost
orderTotal = '{:.2f}'.format(orderTotal)

print("Your Total Is $",orderTotal)