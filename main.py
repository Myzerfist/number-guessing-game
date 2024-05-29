import random

def generate_random_number():
    return random.randint(0, 100)

def main():
    tries_left = 3
    random_number = generate_random_number()

    while True:
        try:
            usr_input = input("Guess a number between 0 and 100: ")

            if usr_input == str(random_number):
                print("You guessed correctly!")
                break
            else:
                if usr_input > str(random_number):
                    print("Too High!")
                elif usr_input < str(random_number):
                    print("Too Low!")

                tries_left -= 1
                print("You guessed incorrectly. You have " + str(tries_left) + " tries left.")
                
                # print(random_number) # For debugging purposes

            if tries_left == 0:
                break

        except ValueError:
            break


if __name__ == '__main__':
    main()