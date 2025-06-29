import random
def risk_level_choice():
    print("Select Your Risk Level:")
    print("1. Easy (0-5) return 2x points")
    print("2. Medium (0-10) return 3x points")
    print("3. Hard (0-15) return 5x points")
    input_level = input("Enter your choice (1/2/3): ")
    if input_level == '1':
        print("You chose Easy mode.")
    elif input_level == '2':
        print("You chose Medium mode.")
    elif input_level == '3':
        print("You chose Hard mode.")
    else:
        print("Invalid choice, defaulting to Easy mode.")
        risk_level_choice()
    return input_level




print("--"*10, "Welcome to the Guessing Game!", "--"*10,end="\n\n\n")
risk= int(risk_level_choice())
while True:
    inp=int(input(f"Enter a number between 0 and {risk*5}: "))
    guess = random.randint(0, (risk*5))
    if guess == inp:
        print("You are a Genius!")
    else:
        print("Try again.")
    print(f"Your guess: {inp}, Computer number: {guess}")
    if input("Do you want to continue? (yes/no): ").lower() != 'yes':
        print("Thanks for playing!")
        break


