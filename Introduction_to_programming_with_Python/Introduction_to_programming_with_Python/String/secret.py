# writing an program for a secret number game
# if the user guesses the number correctly, the program will print "You win!"
# if the user guesses the number incorrectly, the program will print "You lose!"

secret = 5
answer = ''
guess = int(input("Guess the secret number: "))
# print(guess == secret)
if(guess > secret):
    answer = answer + "TOO HIGH!!"
elif(guess < secret):
    answer = answer + "TOO LOW!!"
else:
    answer = answer + 'same'
print(answer)

 

    