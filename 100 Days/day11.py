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


def game():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

    user =[]
    number1=random.choice(cards)
    user.append(number1)
    cards.remove(number1)
    user.append(random.choice(cards))
    print(f"Your card: {user}")

    user_sum = sum(user)
    print(user_sum)

    computer=[]
    num2 =random.choice(cards)
    computer.append(num2)
    print(f"Computer first card:{num2}")
    cards.remove(num2)
    computer.append(random.choice(cards))

    computer_sum = sum(computer)
    print(computer_sum)


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

if play =="y":
    print(logo)
    game()


