height=float(input("Enter your height in meter : "))
weight=float(input("Enter your weight in kg. (Decimal numn available): "))
bmi=float(round(weight/height**2))
print(f"Your bmi is {bmi}")
if (bmi<18.5):
    print("You are underweight.")
elif(bmi<25):
    print("You have a normal weight.")
elif(bmi<30):
    print("You are overweight.")
elif(bmi<35):
    print("You are obse.")
elif(bmi>35):
    print("You need immediate treatment otherwise you will die.You are clinically obse.")
else:
    print("Try again")