import random

def roll_dice_game():
    dice_list = [1, 2, 3, 4, 5, 6]
    collected_numbers = []
    for _ in range(3):
        random_number = random.choice(dice_list)
        collected_numbers.append(random_number)
    return collected_numbers

play_again = "Yes"

while play_again == "Yes":
    print("hello player")
    name = input("what is your name? ")
    print("hello " + name + ".")

    answer = input("Do you want to play a dice game with me? Yes or No? ")

    if answer == "Yes":
        print("lets get started")
        print("We will each roll a dice three times and see who can roll a higher total score based on what value the dice lands on each time. For example if I roll a 2 then a 3 then a 4, my total is 9. If you roll a sum of 7 I win.")
        proceed = input("is that cool with you? Yes or No?") 
        if proceed == "Yes": 
            print("I will go first")
            collected_numbersC = roll_dice_game()
            print("I rolled:", collected_numbersC)

            play = input("It's your turn. Do you want to roll? Yes or No? ")

            if play == "No":
                print("Okay hope we can play again sometime")

            if play == "Yes":
                collected_numbersP = roll_dice_game()
                print("You rolled:", collected_numbersP)

                totalC = sum(collected_numbersC)
                totalP = sum(collected_numbersP)

                print("I scored " + str(totalC))
                print("You scored " + str(totalP))

                if totalC > totalP:
                    print("I win! Thanks for playing!")
                elif totalP > totalC:
                    print("You win! Thanks for playing with me!")
                else:
                    print("It's a tie! Thanks for playing!")

            elif play == "No":
                print("I'm sorry. Maybe some other time.")

    elif answer == "No":
        print("alrighty! next time!")

    play_again = input("Do you want to play again? Yes or No ")

print("Thanks for playing! Goodbye!")
