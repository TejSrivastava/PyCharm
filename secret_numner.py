secret_number =9
chances=1
while(chances<=3):
    guess=int(input("Guess: "))
    chances+=1

    if (guess == secret_number):
        print("You win")
        break
    else:
        print("Sorry,you have failed")

