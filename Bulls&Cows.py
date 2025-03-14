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

def main():
    """Plays the game with choices after each game.
    """    
    run_game = True
    play_game()

    while run_game == True:
        choice = input(f"{'-' * 40}\n"                             
                            "Do you want to play again? Press y.\n"
                            "Do you want to see your game statistics? Press s.\n"
                            "Do you want to quit game? Press any other button.\n"
                            f"{'-' * 40}")
        if choice.upper() == "Y":
            print("OK")
            play_game()
        elif choice.upper() == "S":
            generate_statistics()
        else:
            print("Thank you for your game. See you soon.")
            run_game = False

def generate_unique_number():
    """Generates a unique 4 digit number wich do not 
    start with 0 and each numbers do not repeat.
    """
    unique = False
    while unique == False:
        first_num = random.sample(range(1, 10), 1) # the first digit in range 1 to 9
        remained_nums = random.sample(range(10), 3) # the remaining 3 digits in range 0 to 9
        generated_number = first_num + remained_nums

        if len(generated_number) == len(set(generated_number)):
            generated.append(generated_number)            
            unique = True
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
    print("Your game statistics are:\n"
        f"You played {len(num_of_hits)} games.\n"
        f"The shortest game you took {min(num_of_hits)} shots,\n" 
        f"the longest {max(num_of_hits)}.\n"
        f"You played {round(sum(game_durations))} seconds.\n"
        f"The shortest game you took {round(min(game_durations))} seconds,\n"
        f"the longest {round(max(game_durations))}.")

def play_game():
    """Defines the Bulls and Cows game.
    """
    start_time = time.time()
    all_tips = []
    generated_number = generate_unique_number()
    print("Hi there!\n"
        f"{'-' * 40}\n"
        "I've generated a random 4 digit number for you.\n"
        "Let's play a bulls and cows game.\n"
        f"{'-' * 40}")
    
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
            
            if bulls ==1:
                bull_or_bulls = "Bull"
            else:
                bull_or_bulls = "Bulls"

            if cows == 1:
                cow_or_cows = "Cow"
            else:
                cow_or_cows = "Cows"
            print(f"""In your tip are {bulls} {bull_or_bulls} and {cows} {cow_or_cows}.""")
            
            if bulls == 4:
                end_time = time.time()
                num_of_hits.append(len(all_tips))
                game_length = end_time - start_time
                game_durations.append(game_length)
                print(f"{'-' * 40}\n"
                    "Congratulations!!!!! Your tip is correct.\n"
                    f"It took you {len(all_tips)} shots and\n"
                    f"{round(game_length)} seconds to find the right number!\n"
                    f"{'-' * 40}")
                break

if __name__ == "__main__":
    main()