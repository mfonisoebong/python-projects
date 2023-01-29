import random

print(f"""

*********************************
Welcome to my Number Guesser game.
*********************************

""")


accepted_levels= ['easy', 'normal', 'hard']

level_range= {
    'easy': 50,
    'normal': 100,
    'hard': 150
}

def print_results(score:int, correct_number:int, success:bool):
    if(not success):
        print(f"""
----------------------------
Wrong!!!

The correct answer is {correct_number}
Your score is {score}

----------------------------
            """)
    else:
        print(f"""
----------------------------
Correct!!!
Your score is {score}

----------------------------
            """)


def print_goodbye(): 
    print(f"""
*****************************
GOODBYE!!
*****************************
    """)

def guess_game(): 
    game_is_active= True
    level= input('easy, normal or hard: ').strip().lower()
    score= 0
    if(level not in accepted_levels):
        accepted= "".join(accepted_levels)
        print(f"Accepted levels are: {accepted}")
        return

    while game_is_active:
        correct_number= random.randrange(1,level_range[level])
        
        guess_number= input('Enter a guess number or (q to quit): ').strip()

        if(guess_number =='q'):
            print_goodbye()
            game_is_active= False
            return
        

        if(int(guess_number)==correct_number):
            score= score+1
            print_results(score, correct_number, True)            
        
        else:
            print_results(score, correct_number, False)
            

guess_game()     





