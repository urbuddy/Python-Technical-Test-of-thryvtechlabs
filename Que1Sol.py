import random

weapons = ["Sword", "Bow", "Magic Staff"]
keys = ["Golden Key", "Silver Key", "Bronze Key"]
riddles = [
    ("What has keys but can't open locks?", "piano"),
    ("What runs but never walks?", "water"),
    ("The more you take, the more you leave behind?", "footsteps"),
    ("I speak without a mouth and hear without ears. What am I?", "echo")
]

def get_valid_input(prompt, options):
    """
    Display a message and get valid user input from a list of choices.
    :param prompt: The message to display.
    :param options: A list of choices for the user to pick from.
    :return: The option chosen by the user.
    """
    while True:
        try:
            print(prompt)
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            choice = int(input("Enter the number corresponding to your choice: ").strip())
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(f"Invalid choice! Please select a number between 1 and {len(options)}.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def ask_riddle(riddle_data):
    """
    Display a riddle and check the user's answer.
    :param riddle_data: A tuple containing the riddle and its correct answer.
    :return: True if the answer is correct, False otherwise.
    """
    riddle, correct_answer = riddle_data
    print(f"Riddle: {riddle}")
    user_answer = input("Answer: ").strip().lower()
    return user_answer == correct_answer.lower()

def select_weapon(weapons):
    """
    Let the user choose a weapon from a list.
    :param weapons: A list of available weapons.
    :return: The chosen weapon.
    """
    return get_valid_input("Choose a weapon from the list:", weapons)

def select_key(keys):
    """
    Let the user choose a key from a shuffled list to add randomness.
    :param keys: A list of available keys.
    :return: The chosen key.
    """
    shuffled_keys = random.sample(keys, len(keys))  # Shuffle keys to add randomness
    return get_valid_input("Choose a key from the list:", shuffled_keys)

def check_key(keys, chosen_key):
    """
    Check if the chosen key is the correct one.
    :param keys: A list of available keys.
    :param chosen_key: The key chosen by the player.
    :return: True if the correct key is chosen, False otherwise.
    """
    if random.choice(keys) == chosen_key:
        return True
    else:
        return False

def check_lives(lives):
    """
    Check if the player still has lives remaining.
    :param lives: The number of lives the player has left.
    :return: True if the player has lives remaining, False otherwise.
    """
    if lives <= 0:
        print("Game Over! You've lost all your lives.")
        return False
    return True

def check_weapon(correct_weapon, chosen_weapon):
    """
    Check if the chosen weapon is the correct one.
    :param correct_weapon: The correct weapon to defeat the villain.
    :param chosen_weapon: The weapon chosen by the player.
    :return: True if the correct weapon is chosen, False otherwise.
    """
    return chosen_weapon == correct_weapon

def select_weapon_n_key(weapons, keys, lives):
    """
    Handle the selection of both weapon and key for progressing through the game.
    :param weapons: A list of available weapons.
    :param keys: A list of available keys.
    :param lives: The number of lives the player has left.
    """
    chosen_weapon = select_weapon(weapons)
    print(f"You chose the {chosen_weapon}.")

    chosen_key = select_key(keys)
    print(f"You chose the {chosen_key}.")

    while not check_key(keys, chosen_key):
        print(f"The {chosen_key} did not open the door.")
        chosen_key = select_key(keys)
        print(f"You chose the {chosen_key}.")

    print(f"The {chosen_key} opens the door!")
    print("Congratulations, you've completed Level 1!")
    level_2(lives, chosen_weapon)

def randomize_n_check_final_riddle():
    """
    Randomly select and check the final riddle for the player to win the game.
    :return: True if the riddle is answered correctly, False otherwise.
    """
    riddle_data = random.choice(riddles)
    if ask_riddle(riddle_data):
        print("Congratulations! You've won the game!")
        return True
    else:
        return False

def level_1():
    """
    The first level of the game where the player solves riddles and chooses keys/weapons.
    """
    lives = 3
    print("\nWelcome to Level 1!")

    while check_lives(lives):
        print(f"\nYou have {lives} lives remaining.")
        riddle_data = random.choice(riddles)
        if ask_riddle(riddle_data):
            print("Correct answer!")
            select_weapon_n_key(weapons, keys, lives)
            break
        else:
            print("Wrong answer! You lose a life.")
            lives -= 1

def level_2(lives, chosen_weapon):
    """
    The second level of the game where the player uses a weapon to defeat a villain.
    :param lives: The number of lives the player has left.
    :param chosen_weapon: The weapon chosen by the player.
    """
    print("\nWelcome to Level 2!")

    if lives < 3:
        lives += 1
        print(f"You've been granted an extra life! You now have {lives} lives.")

    weapons = ["Sword", "Bow", "Magic Staff"]
    correct_weapon = "Magic Staff"

    while not check_weapon(correct_weapon, chosen_weapon):
        print("Wrong weapon! Choose the right weapon again and select the right key to defeat the villain.")
        select_weapon_n_key(weapons, keys, lives)

    print(f"You defeated the villain with the {correct_weapon}!")
    print("Final Riddle: ")
    riddle_data = random.choice(riddles)
    if ask_riddle(riddle_data):
        print("Congratulations! You've won the game!")
    else:
        print("Wrong answer! Answer Again.")
        while not randomize_n_check_final_riddle():
            print("Wrong answer! Answer Again.")

def start_game():
    """
    The main function to start the game and introduce the player to the gameplay.
    """
    print("Welcome to the Text-Based Adventure Game!")
    print("You will solve riddles, choose weapons, and keys to progress.")
    print("Your mission is to defeat the villain and complete the game!")

    level_1()


if __name__ == "__main__":
    start_game()
