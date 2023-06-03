print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_people = int(input("How many people to split the bill? "))
tip_left = percentage_tip / 100
total_tips = total_bill * tip_left
total_bill_w_tips = total_bill + total_tips
to_pay_pr_person = float(total_bill_w_tips) / int(split_people)
final_amount = round(to_pay_pr_person, 2)
final_amount = "{:.2f}".format(to_pay_pr_person)
print(f"Each person should pay: ${final_amount}")
