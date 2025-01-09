#DANIYAL ARAIN
from tkinter import *

# Create the main window
root = Tk()
root.title("Calculator")
root.geometry("500x450")  # Increased window size
root.configure(background="#6D7B8D")  

# Global variable to store the current expression
expression = ""
 
# Function to update the expression variable
def update_expression(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the expression
def evaluate():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except Exception as e:
        equation.set("Error")
        expression = ""

# Function to clear the expression
def clear():
    global expression
    expression = ""
    equation.set("")

# Function to delete the last character
def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

# Create a entry field to display the expression
equation = StringVar()
expression_field = Entry(root, textvariable=equation, width=35,  font=('Lucida', 18, 'bold'), justify=LEFT, bd=5, cursor="xterm")
expression_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create number buttons
button_7 = Button(root, text="7", width=8, height=2,bd=4 , font=('Lucida', 14, 'bold'), command=lambda: update_expression(7))
button_7.grid(row=1, column=0, padx=5, pady=5)

button_8 = Button(root, text="8", width=8, height=2, bd=4 , font=('Lucida', 14, 'bold'), command=lambda: update_expression(8))
button_8.grid(row=1, column=1, padx=5, pady=5)

button_9 = Button(root, text="9", width=8, height=2, bd=4 , font=('Lucida', 14, 'bold'), command=lambda: update_expression(9))
button_9.grid(row=1, column=2, padx=5, pady=5)

button_4 = Button(root, text="4", width=8, height=2, bd=4 , font=('Lucida', 14, 'bold'), command=lambda: update_expression(4))
button_4.grid(row=2, column=0, padx=5, pady=5)

button_5 = Button(root, text="5", width=8, height=2, bd=4 , font=('Lucida', 14, 'bold'), command=lambda: update_expression(5))
button_5.grid(row=2, column=1, padx=5, pady=5)

button_6 = Button(root, text="6", width=8, height=2, bd=4 , font=('Lucida', 14, 'bold'), command=lambda: update_expression(6))
button_6.grid(row=2, column=2, padx=5, pady=5)

button_1 = Button(root, text="1", width=8, height=2, bd=4 , font=('Lucida', 14, 'bold'), command=lambda: update_expression(1))
button_1.grid(row=3, column=0, padx=5, pady=5)

button_2 = Button(root, text="2", width=8, height=2, bd=4 , font=('Lucida', 14, 'bold'), command=lambda: update_expression(2))
button_2.grid(row=3, column=1, padx=5, pady=5)

button_3 = Button(root, text="3", width=8, height=2, bd=4 , font=('Lucida', 14, 'bold'), command=lambda: update_expression(3))
button_3.grid(row=3, column=2, padx=5, pady=5)

button_0 = Button(root, text="0", width=8, height=2, bd=4 , font=('Lucida', 14, 'bold'), command=lambda: update_expression(0))
button_0.grid(row=4, column=0, padx=5, pady=5)

button_dot = Button(root, text=".", width=8, height=2, bd=4 , font=('Lucida', 14, 'bold'), command=lambda: update_expression("."))
button_dot.grid(row=4, column=1, padx=5, pady=5)

# Create operator buttons
button_add = Button(root, text="+", width=8, height=2, bd=4 , bg="grey", font=('Lucida', 14, 'bold'), command=lambda: update_expression("+"))
button_add.grid(row=1, column=3, padx=5, pady=5)

button_subtract = Button(root, text="−", width=8, height=2, bd=4 , bg="grey", font=('Lucida', 14, 'bold'), command=lambda: update_expression("-"))
button_subtract.grid(row=2, column=3, padx=5, pady=5)

button_multiply = Button(root, text="*", width=8, height=2, bd=4 , bg="grey", font=('Lucida', 14, 'bold'), command=lambda: update_expression("*"))
button_multiply.grid(row=3, column=3, padx=5, pady=5)

button_divide = Button(root, text="/", width=8, height=2, bd=4 , bg="grey", font=('Lucida', 14, 'bold'), command=lambda: update_expression("/"))
button_divide.grid(row=4, column=3, padx=5, pady=5)


button_clear = Button(root, text="C", width=17, height=2, bd=4 , bg="red", font=('Lucida', 14, 'bold'), command=clear)
button_clear.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

button_equal = Button(root, text="=", width=17, height=2, bd=4 , font=('Lucida', 14, 'bold'), command=evaluate)
button_equal.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


button_backspace = Button(root, text="←", width=8, height=2, bd=4 , font=('Lucida', 14, 'bold'), command=backspace)
button_backspace.grid(row=4, column=2, padx=5, pady=5)

# Start the main loop
root.mainloop()
 
