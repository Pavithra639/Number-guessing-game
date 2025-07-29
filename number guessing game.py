import random

print("Wecome to number guessing game!")
print("i am guessing number between 1 to 100")

guessed_number=random.randint(1,100)
attempts=0

while True:
    guess=int(input("enter the guess:"))
    attempts+=1
    
    if(guess<guessed_number):
        print("too low!,try again")
    elif(guess>guessed_number):
        print("too high!,try again")
    else:
        print(f"Congradulations you guessed it in {attempts} attempts.")
        break
        
