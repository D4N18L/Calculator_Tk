from tkinter import *
import parser

root = Tk()
root.title("Calculator")

# place the user input into the text field
i = 0


def place_variables(num):
    # announce the global variable(i) in this function
    global i
    display.insert(i, num)
    # increments the index on the text field
    i += 1


def place_operators(operator):
    # announce the global variable(i) in this function
    global i
    # get the length of the operator as some are more than one index
    length = len(operator)
    display.insert(i, operator)
    i += length


def Calculate():
    all_string = display.get()  # Selects the whole textfield
    try:
        equals = parser.expr(all_string).compile()  # compiles the content of the textfield
        result = eval(equals)  # evaluate it
        ClearAll()  # clears textfield
        display.insert(0, result)  # insert the result

    except Exception:
        ClearAll()
        display.insert(0, "Attempt Failed")


# def factorial(num):
# if num == 0:
#   return 1
# else:
#  return num * factorial(num-1)

def ClearAll():
    display.delete(0, END)


def ClearOne():
    all_string = display.get()
    if len(all_string):
        new_string = all_string[:-1]
        ClearAll()
        display.insert(0, new_string)
    else:
        ClearAll()
        display.insert(0, "Empty Textfield")


# adding the input to the calculator
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W + E)  # spans the field from the west to the east

# First row of buttons
Button(root, text="1", command=lambda: place_variables(1)).grid(row=2, column=0)
Button(root, text="4", command=lambda: place_variables(4)).grid(row=3, column=0)
Button(root, text="7", command=lambda: place_variables(7)).grid(row=4, column=0)

# Second row of buttons
Button(root, text="2", command=lambda: place_variables(2)).grid(row=2, column=1)
Button(root, text="5", command=lambda: place_variables(5)).grid(row=3, column=1)
Button(root, text="8", command=lambda: place_variables(8)).grid(row=4, column=1)

# Third row of buttons
Button(root, text="3", command=lambda: place_variables(3)).grid(row=2, column=2)
Button(root, text="6", command=lambda: place_variables(6)).grid(row=3, column=2)
Button(root, text="9", command=lambda: place_variables(9)).grid(row=4, column=2)

# Action Buttons
Button(root, text="Clear All", command=lambda: ClearAll()).grid(row=6, column=0)
Button(root, text="0", command=lambda: place_variables(0)).grid(row=5, column=1)
Button(root, text="Calculate", command=lambda: Calculate()).grid(row=6, column=2)
Button(root, text="Clear One", command=lambda: ClearOne()).grid(row=6, column=1)

# Operator Buttons
Button(root, text="+", command=lambda: place_operators("+")).grid(row=2, column=3)
Button(root, text="-", command=lambda: place_operators("-")).grid(row=3, column=3)
Button(root, text="*", command=lambda: place_operators("*")).grid(row=4, column=3)

Button(root, text="/", command=lambda: place_operators("/")).grid(row=2, column=4)
Button(root, text="%", command=lambda: place_operators("%")).grid(row=3, column=4)
Button(root, text="pow", command=lambda: place_operators("**")).grid(row=4, column=4)

Button(root, text="pi", command=lambda: place_operators("*3.14")).grid(row=2, column=5)
Button(root, text="(", command=lambda: place_operators("(")).grid(row=3, column=5)
# Button(root, text="x!", command=lambda: place_operators("!")).grid(row=4, column=5)
Button(root, text="^3", command=lambda: place_operators("**3")).grid(row=4, column=5)

Button(root, text=")", command=lambda: place_operators(")")).grid(row=2, column=6)
Button(root, text="^2", command=lambda: place_operators("**2")).grid(row=3, column=6)

root.mainloop()
