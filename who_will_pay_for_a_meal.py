import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

result = len(names)
final_result = random.randint(0, (result -1))
print(f"{names[final_result]} is going to buy the meal today! Congratulation!")
