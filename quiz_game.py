print("Welcome to my teaser quiz!")

playing = input("Do you want to play? ")
# print(playing)

if playing.lower() !="yes":
    quit()

print("Okay!, Lets play :)")
score = 0

answer= input("What is the capital of Japan? ")
# print(answer)yes
if answer.lower() == "tokyo":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

answer= input("What year was the United Nations established? ")
# print(answer)yes
if answer.lower() == "1945":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

answer= input("How many elements are in the periodic table? ")
# print(answer)yes
if answer.lower() == "118":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

answer= input("Which planet has the most moons? ")
# print(answer)yes
if answer.lower() == "saturn":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

answer= input("What country has won the most World Cups? ")
# print(answer)yes
if answer.lower() == "brazil":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/5)) *100  + "%")
