from tkinter import *

height_metric = 'in'
weight_metric = 'lbs'


# --------------------------------FUNCTIONALITY-----------------------------

def convert_measure():
    global height_metric
    global weight_metric
    if height_metric == 'in':
        height_metric = 'cm'
        height_label.config(text=f"Enter your height in {height_metric}: ")
    else:
        height_metric = 'in'
        height_label.config(text=f"Enter your height in {height_metric}: ")

    if weight_metric == 'lbs':
        weight_metric = 'kg'
        weight_label.config(text=f"Enter your weight in {weight_metric}: ")
    else:
        weight_metric = 'lbs'
        weight_label.config(text=f"Enter your weight in {weight_metric}: ")


def check_bmi():
    global height_metric
    global weight_metric
    height = float(height_entry.get())
    weight = float(weight_entry.get())

    if height_metric == 'cm':
        height_in_metre = height / 100
        bmi = weight / height_in_metre ** 2
        bmi_label.config(text=f"Your BMI is: {round(bmi, 2)}")
    else:
        bmi = (weight / height ** 2) * 703
        bmi_label.config(text=f"Your BMI is: {round(bmi, 2)}")


# ------------------------------------UI----------------------------------------
windows = Tk()
windows.config(pady=50, padx=20)
windows.title("BMI checker")
canvas = Canvas(height=200, width=200, highlightthickness=0)
image_icon = PhotoImage(file="Images/bgt.png")
canvas.create_image(100, 100, image=image_icon)
canvas.grid(column=1, row=1)

# ------------------BMI INFORMATION LABELS-----------------------------
information_label = Label(text="BMI Categories:\n"
                               "Underweight = <18.5\n"
                               "Normal weight = 18.5–24.9\n"
                               "Overweight = 25–29.9\n"
                               "Obesity = BMI of 30 or greater")
information_label.grid(column=2, row=1)

height_label = Label(text=f"Enter your height in {height_metric}: ")
height_label.grid(column=0, row=2)

weight_label = Label(text=f"Enter your weight in {weight_metric}: ")
weight_label.grid(column=0, row=3)

height_entry = Entry()
height_entry.grid(column=1, row=2)

weight_entry = Entry()
weight_entry.grid(column=1, row=3)

convert_btn = Button(text="Change to\n preferred measure", command=convert_measure)
convert_btn.grid(column=2, row=2, rowspan=2)

check_bmi_btn = Button(text="Check your BMI: ", command=check_bmi)
check_bmi_btn.grid(column=1, row=4)

bmi_label = Label(text=f"Your BMI is: ")
bmi_label.grid(column=1, row=5)
windows.mainloop()
