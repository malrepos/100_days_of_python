# bmi = weight / height^2(m^2)

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / height**2

print(f"Your BMI is {int(bmi)}")
