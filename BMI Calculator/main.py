height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / height**2
bmi_as_int = int(bmi)
print(bmi_as_int)