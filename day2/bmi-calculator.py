print("Welcome to BMI Calculator")

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / (float(height)) ** 2

bmi_as_int = int(bmi)
print(bmi_as_int)