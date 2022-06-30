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
#    DESCRIPTION: {Create a random number of four digits in the main function and then pass it to the guessing_game function. Ask the user to guess the random 4 digit number generated in the main function.Tell the user if they got any number(s) correct from the number that they input. Keep asking the user their next choice of numbers and give them hints until they get the number correct. Once they guessed the number ask them if they would like to keep playing. If they want to keep playing run the program again, if not stop the program and print a farewell statement. if the number that they input the first time was correct, print a congratulations statement and ask them if they want to keep playing. }
#
#  *****************************************************************************

import random

def guessing_game(num):
    #print(num)
    guess=(input("Guess the 4-digit number: "))
    print()
  
  #conversion of the random number created in the main function to a string, so it can be indexed
    random_number_str=(str(num))
  
    right_numbers=0
    output=""
    total_guesses=1
  
  #Check if the guess is correct
    if guess == random_number_str:
       print(f"Wow! You guessed the number in just 1 try! You're lucky!")
       print()
      
      #ask the user if they want to keep playing
       keep_playing=input("Do you want to keep playing? (Yes/No) ")
       if keep_playing == 'Yes':
          main()
       else:
          print()
          print("Try again soon!")
         
    #if the guess is not correct at the first time check what numbers they got correct
    elif guess != random_number_str:
      while guess != random_number_str and right_numbers <= 4:
        total_guesses+=1
        for i in range(4):
          if guess[i] == random_number_str[i]:
            right_numbers+=1
            output+=guess[i]
          else:
            output+="X"
        print(f"Not quite number,But you did get {right_numbers} digit correct! These were the numbers in your input that were correct.\n{output}")
        right_numbers=0
        output=""
        print()
        
        #keep asking the user until they get it right 
        guess=(input("Enter your next choice of numbers: "))
        if guess == random_number_str:
          print(f"That's a match!\nIt took you only {total_guesses} tries.")
          print()
          
        #after they get it right ask them if they want to keep playing
          keep_playing2=input("Do you want to keep playing? (Yes/No) ")
          if keep_playing2 == 'Yes':
            print()
            main()
          else:
            print()
            print("Try again soon!")          

def main():
  # randrange(1000,10000) : Gives a random four digit numbers.
    num=random.randrange(1000,10000)
    guessing_game(num)


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()