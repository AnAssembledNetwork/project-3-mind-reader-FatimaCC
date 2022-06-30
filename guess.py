# """
#  *****************************************************************************
#    FILE:        guess.py
#
#    AUTHOR:      {Fatima Carolina Chairez}
#
#    ASSIGNMENT:  Mind Reader
#
#    DATE:        June 23, 2022
#
#    DESCRIPTION: {Create a random number of four digits in the main function and then pass it to the guessing_game functio. Ask the user to guess the random 4 digit number generated in the main function.Tell the user if they got any number(s) correct from the number that they input. Keep asking the user their next choice of numbers and give them hints until they get the number correct. Once they guessed the number ask them if they would like to keep playing. If they want to keep playing run the program again, if not stop the program and print a farewell statement. if the number that they input the first time was correct, print a congratulations statement and ask them if they want to keep playing. }
#
#  *****************************************************************************

import random

def guessing_game(num):
  print(num)
  keep_running=True
  while keep_running:
    guess=int(input("Guess the 4-digit number:"))
    print()
    guess_str=str(guess)
    random_number_str=(str(num))
    right_numbers=0
    output=""
    total_guesses=1
    if guess_str == random_number_str:
       print(f"Wow! You guessed the number in just 1 try! You're lucky!")
       print()
       keep_playing=input("Do you want to keep playing? (Yes/No) ")
       if keep_playing == 'Yes':
          keep_running=True
       else:
          print()
          print("Try again soon!")
          keep_running=False
    elif guess_str != random_number_str:
      while guess_str != random_number_str and right_numbers <= 4:
        total_guesses+=1
        for i in range(4):
          if guess_str[i] == random_number_str[i]:
            right_numbers+=1
            output+=guess_str[i]
          else:
            output+="X"
        print(f"Not quite number,But you did get {right_numbers} digit correct! These were the numbers in your input that were correct.\n{output}")
        right_numbers=0
        output=""
        print()
        guess=int(input("Enter your next choice of numbers: "))
        print()
        guess_str=str(guess)
        if guess_str == random_number_str:
          print(f"That's a match!\nIt took you only {total_guesses} tries.")
          print()
          keep_playing2=input("Do you want to keep playing? (Yes/No) ")
          if keep_playing2 == 'Yes':
            print()
            keep_running=True
          else:
            print()
            print("Try again soon!")
            keep_running=False
          
     
    


def main():
    """The main function is the first function that runs in our code."""
  # randrange(1000,10000) : Gives a random four digit numbers.
    num=random.randrange(1000,10000)
    guessing_game(num)


if __name__ == "__main__":
    main()