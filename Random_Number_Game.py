import random
import math
#Give a greeting and text header.
print("Welcome to the random number game - Guess the number the machine created")
name = input("What's your name?   ")
print ("Hello {}, I hope your ready to play, this is a game of high risk high reward!".format(name))
#Be shown the highscore (least amount of tries)
highscore = 0

while True:#could set a variable here and make it true
    try:
        lower_bounds = int(input("What is the start of the range you want to play \n Please use an integer:  ")) 
        upper_bounds = int(input("What is the end of the range you want to play \n Please use an integer:  "))
    except ValueError:
       print("Your value doesn't work \nPlease enter your guess as an integer like 1,2,3...")
    else:
        #shown the number of attempts
        score = (abs(lower_bounds)+abs(upper_bounds))+1 #ex 11 so the top possible points is 10
        num_attempts = 0
        guess = 0
        #A random number should be generated
        #if asked to play again changes number
        random_number = random.randrange(lower_bounds,upper_bounds)
        print (random_number)
        #Catches errors and reports errors in a meaningful way
        #Asked to guess again until right
        while guess != random_number:
            try:
                guess = int(input("What is the number you want to to guess?   "))
                if guess < lower_bounds or guess > upper_bounds:
                    raise ValueError("The number {} is out of range try again".format(guess))
            except ValueError as error:
                print("{}.Your guess doesn't work \nPlease enter your guess as an integer like 1,2,3...10   ".format(error))
            else: #Should be told if the number is higher or lower
 #If range is (1-10) and user puts 12 should be told the range is between 1-10
                if guess < random_number:
                    print ("You're guess is too low, try going higher")
                elif guess > random_number:
                    print ("You're too high, guess lower")
                num_attempts +=1
                score -= 1
    #when done give an ending message to the player
        print ("Congrats {} on guessing the correct number!".format(name))
        if score < 0:
            score = 0
        if highscore < score:
            highscore = score
        print ("Youre score:{} and attempts:{}".format(score,num_attempts))
        print ("The current highscore: {}".format(highscore))
        Choice = input("Do you want to play again? Yes or No   ")
        #Asked to play again
        while Choice.lower() != 'yes' and Choice.lower() != 'no':
            Choice = input("Please type Yes or No   ")
        if Choice.lower() == 'no':
            print("Thank you for playing {}!".format(name))
            break #replace with variable and set it to false
