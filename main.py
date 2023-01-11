score = 0 

answer1 = input("What is the color of the sky: ").lower()
if answer1 == "blue":
    score = score + 1
    print("Correct")
else: 
    print("Incorrect")

answer2 = input("What is day is Canada's day on: ").lower()
if answer2 == "july 1" or answer2 == "july 1st" or answer2 == "july first": 
    score = score + 1 
    print("Correct")
else: 
    print("Incorrect")

answer3 = input("How many wheels on a standard bicycle: ").lower()
if answer3 == "two" or answer3 == "2": 
    score = score + 1 
    print("Correct")
else: 
    print("Incorrect")

answer4 = input("What is the legal drinking age in Alberta: ").lower()
if answer4 == "18" or answer4 == "eighteen":
    score = score + 1
    print("Correct")
else: 
    print("Incorrect")

percentage = (score / 4) * 100
print("Score: " + str(score) + "/4 (" + str(percentage) + "%)")
if percentage == 100:
    print("Great Job!")
elif percentage == 75: 
    print("Good.")
elif percentage == 50:
    print("Could do better.")
else: 
    print("You Failed.")
    



