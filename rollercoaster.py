print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("you can ride a rollercoaster!")
    age = int(input("What is your age? "))

    if age < 12:
        bill += 400
        print("Child ticket is ￥400 ")
    elif age <= 18:
        bill += 800
        print("Youth ticket is ￥800 ")
    elif age >=45 and age<=55:
        print("Every thing is going to be ok. Have a free ride on us!")
    else:
        bill += 1200
        print("Adult ticket is ￥1200")

    want_photo = input("Do you want to photo taken? Y or N. ")
    if want_photo == "Y":
        bill += 150

    print(f"Your final bill is: ￥{bill}")

else:
    print("sorry you have to grow taller before you can ride.")