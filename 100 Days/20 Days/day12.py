#******** Day 12 of 100 days of coding ********
# Number guessing game


logo = """

  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|        

"""


from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5



#check the user guess is correct
#reduce the number of turns
def check(answer, guess,turns):
    if answer>guess:
        print("Too Low")
        return turns-1
    elif answer<guess:
        print("Too high")
        return turns-1
    else:
        print("correct answer")






#check the difficulty level and return the turns
def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if level =='easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL
    




#get the user guess
def play():
    #set a randam number in between 1-100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    turns = difficulty()

    answer = randint(1,100)
    #print(answer)
    
    
    guess=0
    #repeate until the correct ans is guessed or no of turns is  0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns=check(answer,guess,turns)
        if turns ==0:
            print(f"Correct answer is {answer}")
            return
        elif guess != answer:
            print("Guess again")
        

            
        
    

play()



