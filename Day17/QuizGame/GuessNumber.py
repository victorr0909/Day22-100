from random import randint
EASY_MODE = 10
HARD_MODE = 5

def set_difficulty():
   level=input("Select mode : Easy or Hard")
   if level=="Easy":
      return EASY_MODE
   else:
      return HARD_MODE

def check_answer(turns,answer,guess):
   if answer>guess:
      print("Too high")
      turns-=1
   elif answer<guess:
      print("Too Low")
      turns-=1
   else:
      print("Congratulations you have made the right guess!")      
   
   
def game():
   
   print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.")
   turns=set_difficulty()
   print(f"You have {turns} lives")
   answer= randint(1,100)
   guess = 0
   while guess != answer:
      print(f"You have {turns} attempts remaining to guess the number.")
      guess= int(input("Enter your guess"))
      turns = check_answer(guess, answer, turns)
   if turns == 0:
      print("You've run out of guesses, you lose.")
      return
   elif guess != answer:
      print("Guess again.")
   
game()   
   
      
      