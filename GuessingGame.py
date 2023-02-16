import random

if __name__ == "__main__":
    min_val = 1
    max_val = 100
    computer_num = random.randint(min_val,max_val)
    user_input = None
# returns numbers including 0 and 10

    while user_input != computer_num:
        try:
            user_input = int(input(f"Guess a number between {min_val} and {max_val}:"))

            if user_input > computer_num:
                print('Too Big')
            elif user_input < computer_num:
                print('Too Small')
        except Exception:
        # If input is not an integer
            print('Error: Please provide a number with no charaacters')
            user_input = None
    
    print(f"Correct!{computer_num} was the correct number!")
