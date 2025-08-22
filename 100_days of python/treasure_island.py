print('''
      _____
              .-" .-. "-.
            _/ '=(0.0)=' \_
          /`   .='|m|'=.   `\
          \________________ /
      .--.__///`'-,__~\\\\~`
     / /6|__\// a (__)-\\\\
     \ \/--`((   ._\   ,)))
     /  \\  ))\  -==-  (O)(
    /    )\((((\   .  /)))))
   /  _.' /  __(`~~~~`)__
  //"\\,-'-"`   `~~~~\\~~`"-.
 //  /`"              `      `\
//

jgs
      ''')
print("Welcome to treasure Island \nYour mission is to Find the treasure!!")
decision1= input("Would you like to go left or right? ") #First decision to move
if decision1.lower()=="left":
    decision2=input('Would you like to swim or wait? ')#Second decision if first is successful
    if decision2.lower()=="wait":
        decision3= input("Which door would you like to enter: Red, Blue or Yellow: ")#third decision inf first 2 are successful
        if decision3.lower()=="red":  #first door
            print("Burned by fire \nGame Over")
        elif decision3.lower()=="blue":#second door
            print("Eaten by beasts \nGame Over.")
        elif decision3.lower()=="yellow": #door3
            print("You win!!")
        else:
            print("Game over!!")
    else:
        print("Attacked by a trout \n game over")
else:
    print('Fall into a hole \nGame over')    