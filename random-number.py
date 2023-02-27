import random 

print("You will be prompted to give two numbers, a lower and upper limit.")
print("I will randomly choose a number in between the two options (inclusively).")
print("There are three modes, Easy, Medium, Hard.")
print("Easy = 10 guesses, Medium = 6 guesses, Hard = 3 guesses.")

upper_limit = int(input("Upper Limit: "))
lower_limit = int(input("Lower Limit: "))

flag = True
while flag:
    mode = input("Enter mode (easy, medium, hard): ")
    mode = mode.lower()
    if mode == "easy" or mode == "medium" or mode == "hard":
       flag = False


random_number = random.randint(lower_limit,upper_limit)

print("Chosen Num:", random_number)

chances = 10
if mode == "medium":
    chances = 6
elif mode == "hard":
    chances = 3

count = 0
while count < chances:
    count += 1 
    guess = int(input("What is your guess: "))

    if guess == random_number:
        print("You got my number! It took you", count, "guesses.")
        break
    elif guess > random_number:
        print("My number is lower than that!")
    elif guess < random_number:
        print("My number is higher than that!")
    
    if count >= chances:
        print("You've run out of guesses :(")
        print("My number was", random_number)
        break
   
    
