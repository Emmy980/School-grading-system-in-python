# Grading system
print("Grading system")

name = input("enter your name: ")
score = int(input("Enter your score: "))

if score >= 80 and score <=100:
    print(f"{name}, you got an A!!!")
elif score >= 70 and score <=79:
    print(f"{name}, you got a B!!!")
elif score >= 60 and score <=69:
    print(f"{name}, you got a c!!!")
elif score >= 45 and score <=59:
    print(f"{name}, you got a D!!!")
elif score >= 35 and score <=44:
    print(f"{name}, you got an E!!!")
elif score >= 0 and score <=34:
    print(f"{name}, you got a F!!!")
else:
    print("Wrong score input!!!")
    print("Enter a score between 0 and 100")



