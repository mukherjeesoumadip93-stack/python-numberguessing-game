secret=9
i=0
guessing_limit=3
while i<guessing_limit:
    guess = int(input("Guess the number"))
    if guess == secret:
        print("Correct")
        break
    i=i+1
else:
    print("wrong answer")



