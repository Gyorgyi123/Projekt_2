"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author = Bc. Gyorgyi Fucsekova Posztosova
email: posztosgyorgyi@seznam.cz 
"""
import random
import time

num_of_hits = [] # number of hits for each game
game_durations = [] # duration of each game in seconds
generated = [] # list of generated number for each game


def generate_unique_number():
    """Generates a unique 4 digit number wich do not 
    start with 0 and each numbers do not repeat.
    """
    first_num = random.sample(range(1, 10), 1)
    remained_nums = random.sample(range(10), 3)
    generated_number = first_num + remained_nums
    if len(generated_number) > len(set(generated_number)):
        generate_unique_number()
    else:
        generated.append(generated_number)
        return generated_number

def evaluate_guess(user_tip, generated_number):
    """Evaluates the guess against the generated number and returns number of Bulls and Cows.
    """
    bulls = 0
    cows = 0
    tip = [int(i) for i in str(user_tip)]

    for i in range(4):
        if tip[i] == generated_number[i]:
            bulls += 1
        elif tip[i] in generated_number:
            cows +=1
    return bulls, cows

def generate_statistics():
    """Generates statistics of all games in this running program.
    """
    print(f"""
Your game statistics are:
You played {len(num_of_hits)} games.
The shortest game you took {min(num_of_hits)} shots, 
the longest {max(num_of_hits)}.
You played {round(sum(game_durations))} seconds.
The shortest game you took {round(min(game_durations))} seconds, 
the longest {round(max(game_durations))}.
              """)

def play_game():
    """Plays the Bulls and Cows game.
    """
    start_time = time.time()
    all_tips = []
    generated_number = generate_unique_number()
    print(f"""
Hi there!
{'-' * 40}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{'-' * 40}
        """)

    while True:
        print("-" * 40)
        user_tip = input("Enter your guess:")     
        if not user_tip.isdigit():
            print("Invalid input. Please enter only numbers.")
            continue
        elif (len(user_tip) != 4) or \
                (len(set(user_tip)) != 4) or \
                (user_tip[0] == "0"):
            print("Invalid input. Please read the rules again and enter a new number.")
        elif user_tip in all_tips:
            print("You already used this number. Please enter a new one.")
            continue
        else:
            all_tips.append(user_tip)
            bulls, cows = evaluate_guess(user_tip, generated_number)
            print(f"""In your tip are {bulls} Bulls and {cows} Cows.""")
            
            if bulls == 4:
                end_time = time.time()
                num_of_hits.append(len(all_tips))
                game_length = end_time - start_time
                game_durations.append(game_length)
                print(f"""
{'-' * 40}
Congratulations!!!!! Your tip is correct. 
It took you {len(all_tips)} shots and 
{round(game_length)} seconds to find the right number!
{'-' * 40}
                        """)
                choice = input(f"""{'-' * 40}                               
Do you want to play again? Press y.
Do you want to see your game statistics? Press s.
Do you want to quit game? Press any other button.
{'-' * 40}""")
                
                if choice == "y" or choice == "Y":
                    play_game()
                elif choice == "s" or choice == "S":
                    generate_statistics()
                    choice_2 = input(f"""{'-' * 40}
Do you wanna play again? Press y.
Do you wanna quit? Press any other button.
{'-' * 40}""")
                    
                    if choice_2 == "y" or choice_2 == "Y":
                        play_game()
                    else:
                        print("Thank you for your game. See you soon.")
                        break
                else:
                    print("Thank you for your game. See you soon.")
                    break

if __name__ == "__main__":
    play_game()