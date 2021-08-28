def check_guess(guess,answer):
    global score
    still_guessing=True
    attempt=0

    while still_guessing and attempt<3:
        if guess.lower()==answer.lower():
            print("Correct Answer!!!")
            score=score+1
            still_guessing=False
        else:
            if attempt<2:
                guess=input("Sorry Wrong answer, try again  \n ")
            attempt=attempt+1
    if attempt==3:
        print("The correct answer is",answer)

score=0
print("Guess the animal")
guess1=input("Which bear lives at the North Pole? ")
check_guess(guess1,"Polar Bear")
guess2=input("Which is the fastest land Animal? ")
check_guess(guess2,"Cheetah")
guess3=input("Which animal has the best sense of smell? ")
check_guess(guess3,"Dog")
guess4=input("What kind of animal is a doe? ")
check_guess(guess4,"Deer")
guess5=input("I have stripes and belong to the genus Equus, what animal am 1? ")
check_guess(guess5,"Zebra")
print ("Your Score is "+str(score)+"/5")