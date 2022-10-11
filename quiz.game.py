print("Welcome to my Game!")

playing = input("Do you want to play my Game? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")
score = 0 

answer = input("How many Elements are in the Periodic Table? ")
if answer == "118":
    print("Correct!")
    score += 10
else: 
    print("I am sorry. That is incorrect!")

answer = input("What Company was originally called Cadabra? ")
if answer.upper() == "AMAZON":
    print("Correct!")
    score += 10
else: 
    print("I am sorry. That is incorrect!")

answer = input("What Country has won the most World Cups? ")
if answer.upper() == "BRAZIL":
    print("Correct!")
    score += 10
else: 
    print("I am sorry. That is incorrect!")

answer = input("What is a group of Pandas known as? ")
if answer.lower() == "embarrassment":
    print("Correct!")
    score += 10
else: 
    print("I am sorry. That is incorrect!")

answer = input("What is the 4th letter in the Greek Alphabet? ")
if answer.lower() == "delta":
    print("Correct!")
    score += 10
else: 
    print("I am sorry. That is incorrect!")

print("Your total is " + str(score) + " for this quiz!")