from tkinter import *

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
        tip = "Eat nutritious food and increase protein intake."

    elif bmi <= 24.9:
        category = "Normal Weight"
        tip = "Maintain a balanced diet and exercise regularly."

    elif bmi <= 29.9:
        category = "Overweight"
        tip = "Reduce junk food and increase physical activity."

    else:
        category = "Obese"
        tip = "Consult a healthcare professional."

    result_label.config(
        text=f"BMI: {round(bmi, 2)}\nCategory: {category}"
    )

    tip_label.config(text=f"Health Tip: {tip}")

root = Tk()
root.title("BMI Calculator")
root.geometry("400x300")

heading = Label(root, text="BMI Calculator", font=("Arial", 16, "bold"))
heading.pack(pady=10)

Label(root, text="Enter Weight (kg):").pack()
weight_entry = Entry(root)
weight_entry.pack()

Label(root, text="Enter Height (m):").pack()
height_entry = Entry(root)
height_entry.pack()

Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

result_label = Label(root, text="", font=("Arial", 12))
result_label.pack()

tip_label = Label(root, text="", wraplength=350)
tip_label.pack(pady=10)

root.mainloop()