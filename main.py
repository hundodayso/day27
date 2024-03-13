from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("First GUI")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="Here's a Label", font=("Arial", 24, "bold"))
my_label.config(text="dribbles")
my_label.grid(column=0, row=0)

#Button
button = Button(text="Click Me!", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Button 2")
button2.grid(column=2, row=0)
#Entry...
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=3)




window.mainloop()