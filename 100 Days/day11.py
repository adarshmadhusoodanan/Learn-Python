#******** Day 11 of 100 days of coding ********
# BlackJack Project
logo='''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
      |  \/ K|                            _/ |                
      '------'                           |__/                  
'''
import random

def sum(user):
    sum=0
    for i in user:
        sum += i
    return sum

def check(user,computer):
    if user>21:
        result=0 #user lost
    elif computer>21:
        result = 1 #user win
    elif user==21 and computer==21:
        result = 2 #draw
    elif user>computer and user<=21:
        result = 3 #user win
    elif computer>user and computer<=21:
        result = 4 #user lost

    return result
    


def game():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

    user =[]
    number1=random.choice(cards)
    user.append(number1)
    cards.remove(number1)
    user.append(random.choice(cards))
    

    user_sum = sum(user)
    

            
    print(f"Your card: {user}, current score:{user_sum}")
    

    computer=[]
    num2 =random.choice(cards)
    computer.append(num2)
    print(f"Computer first card:{num2}")
    cards.remove(num2)
    computer.append(random.choice(cards))

    computer_sum = sum(computer)
    #print(computer_sum)

    

    if user_sum<21:
        again = input("Type 'y' to get another card, type 'n' to pass:")
        if again =='y':
            user.append(random.choice(cards))
            user_sum = sum(user)
            print(f"Your card: {user}, final score:{user_sum}")
            print(f"computer card: {computer}, final score:{computer_sum}")
            result=check(user_sum,computer_sum)
        else:
            print(f"Your card: {user}, final score:{user_sum}")
            print(f"computer card: {computer}, final score:{computer_sum}")
            result=check(user_sum,computer_sum)
            return result,user_sum
    else:
        result=check(user_sum,computer_sum)      


    
    return result,user_sum
    

def play():
    result,user_sum=game()
    if result == 0:
        print("You Lost")  
    elif result== 1:
        print("You Win")
    elif result == 2:
        print("Draw")
    elif result == 3:
        print("You Win")
    elif result == 4:
        print("User Lost")


start = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

if start =="y":
    print(logo)
    play()
    


