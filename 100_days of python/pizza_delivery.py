print('Welcome to python pizza deliveries')
price= 0

size= input('What size of pizza do you want:\n small, medium or large: ')
peperoni=input('Would you like pepperoni: Y or N? ')
cheese= input('Would you like extra cheese? Y or N? ')

if size.lower()=="small":
    price+= 15
    if peperoni.upper()=="Y":
        price+=2
    else:
        print('small with no peperoni')
elif size.lower()=="medium":
    price+= 20
    if peperoni.upper()=="Y":
        price+=3
    else:
        print('medium with no peperoni')
elif size.lower()=="large":
    price+=25
    if peperoni.upper()=="Y":
        price+=3
    else:
        print(f'large with no peperoni')
else:
    print('invalid size request')
if cheese.upper()=="Y":
    price+=1
else:
    print('and no cheese')
print(f'Your total bill is ${price} \n Thanks for choosing python kitchen')