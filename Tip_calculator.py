# understanding data type and how to manipulate string

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? ￥"))
tip = int(input("How much tip would like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

bill_with_tips = tip / 100 * bill + bill
bill_per_person = bill_with_tips / people
total_amount = round(bill_per_person, 2)

print(f"Each person should pay: ￥{total_amount}")