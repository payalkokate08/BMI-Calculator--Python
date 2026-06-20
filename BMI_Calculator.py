weight = float(input("Enter the weight (in kg):"))
height = float(input("Enter the height (in m)"))
bmi = weight / (height ** 2)
print("The bmi value is :",round(bmi,2))
if bmi < 18.5 :
    print("Category : Underweight")
elif bmi <= 24.9 :
    print("Category : Normal Weight")
elif bmi <= 29.9:
    print("Category : Overweight")
else :
    print("Category : Obese")

