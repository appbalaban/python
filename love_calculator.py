print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1 + name2
lo_names = names.lower()

true = (lo_names.count("t") + lo_names.count("r") + lo_names.count("u") + lo_names.count("e"))

love = (lo_names.count("l") + lo_names.count("o") + lo_names.count("v") + lo_names.count("e"))

score = int(f"{true}{love}")

if score <=10 or score >=90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >=40 and score <=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
