from tkinter import *

def miles_to_km():
    miles = round(int(input.get()) * 1.6, 2)
    label_result_km.config(text=miles)


window = Tk()
window.config(padx=40, pady=40)


##Miles Input
input = Entry(width = 10)
input.grid(column=1, row=0)

#miles Text
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)
label_miles.config(padx=10, pady=10)

#is_equal_to Text
label_is_equal_to = Label(text="is equal to")
label_is_equal_to.grid(column=0, row=1)
label_is_equal_to.config(padx=10, pady=10)

#Result Text
label_result_km = Label(text="0")
label_result_km.grid(column=1, row=1)
label_result_km.config(padx=10, pady=10)

#km Text
label_km = Label(text="km")
label_km.grid(column=2, row=1)

#Calc Button
button_calc = Button(text="Calculate", command=miles_to_km)
button_calc.grid(column=1, row=3)

window.mainloop()