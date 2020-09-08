from tkinter import *
import parser


root = Tk()
root.title("Calculator")

# adding the input to the calculator
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W + E)  # spans the field from the west to the east

# First row of buttons
Button(root, text="1").grid(row=2, column=0)
Button(root, text="4").grid(row=3, column=0)
Button(root, text="7").grid(row=4, column=0)

# Second row of buttons
Button(root, text="2").grid(row=2, column=1)
Button(root, text="5").grid(row=3, column=1)
Button(root, text="8").grid(row=4, column=1)

# Third row of buttons
Button(root, text="3").grid(row=2, column=2)
Button(root, text="6").grid(row=3, column=2)
Button(root, text="9").grid(row=4, column=2)

# Action Buttons
Button(root, text="Clear All").grid(row=6, column=0)
Button(root, text="0").grid(row=5, column=1)
Button(root, text="Calculate").grid(row=6, column=2)
Button(root, text="C").grid(row=6, column=1)

# Operator Buttons
Button(root, text="+").grid(row=2, column=3)
Button(root, text="-").grid(row=3, column=3)
Button(root, text="*").grid(row=4, column=3)

Button(root, text="/").grid(row=2, column=4)
Button(root, text="%").grid(row=3, column=4)
Button(root, text="pow").grid(row=4, column=4)

Button(root, text="pi").grid(row=2, column=5)
Button(root, text="(").grid(row=3, column=5)
Button(root, text="x!").grid(row=4, column=5)

Button(root, text=")").grid(row=2, column=6)
Button(root, text="^2").grid(row=3, column=6)
Button(root, text="^3").grid(row=4, column=6)

root.mainloop()
