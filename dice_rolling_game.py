#Loop for repition
import random

attempts = 0
third_dice = False #we dont need this one just yet
while True: #good practise to have a space between 
    my_choice = input('Roll the dice? (Y/N:) ').upper() 
    if my_choice == 'Y':
        attempts += 1 #increments counter as we keep track

        if attempts == 7:
            third_dice = input('Do you want to add a third die? (Y/N)').upper()
            if third_dice == 'Y':
                third_dice = True
            elif third_dice != 'N': #we only have 2 options 
                print('Not Valid!, Looks like you dont need a third one!!')
        dice1 = random.randint(1,6) #generates a random number between 1-6
        dice2 = random.randint(1,6)
        if third_dice:
            dice3 = random.randint(1,6)
            print(f'{dice1}, {dice2}, {dice3}')
        else:
            print(f'{dice1}, {dice2}')
    elif my_choice == "N":
        print('Thanks for playing')
        break
    else:
        print('Invalid choice!')




