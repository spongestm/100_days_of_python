import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

numbers=['1','2','3','4','5','6','7','8','9','0']

symbols=['!','#','@','$','%','&','*']

num_L=int(input('How may letters would you like: '))
num_N= int(input('How may numbers would you like: '))
num_S= int(input('How may symbols would you like: '))

password=[]

for letter in range(num_L):
    password.append(random.choice(letters))

for number in range(num_N):
    password.append(random.choice(numbers))

for symbol in range(num_S):
    password.append(random.choice(symbols))

print(password)
random.shuffle(password)
print(password)