#Restaurant game on who will pay the bill based on lists and random module
import random
people=['Tayo', 'Oto', 'Chima','Hassan','Rukky', 'Tim'] #list of people
peeps= random.randint(1,len(people)+1) #initializing the random module
if peeps==1:
    print(f'{people[0]} will pay the bill')
elif peeps==2:
    print(f'{people[1]} will pay the bill')
elif peeps==3:
    print(f'{people[2]} will pay the bill')
elif peeps==4:
    print(f'{people[3]} will pay the bill')
elif peeps==5:
    print(f'{people[4]} will pay the bill')
elif peeps==6:
    print(f'{people[5]} will pay the bill')
else:
    print("Invalid Choice")


    """
    ---------------------Or---------------------    
    """
print(f'second pick: {random.choice(people)} will pay')

"""
    ---------------------Or---------------------    
"""
print(f'Third pick: {people[random.randint(0,len(people))]} will pay')