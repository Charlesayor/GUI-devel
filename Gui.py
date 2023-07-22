from ast import Lambda
import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation

    try:
        calculation = str(eval(calculation.strip()))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x275")
root.title("Charles Calculator")
root.configure(bg="purple")  # Set background color for the window

# Configure columns and rows to resize proportionally
for i in range(6):
    root.columnconfigure(i, weight=1, minsize=50)
    root.rowconfigure(i, weight=1, minsize=50)

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24), bg="white")
text_result.grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")

# Buttons from 1 to 9 with respective background colors
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14), bg="lightblue")
btn_1.grid(row=1, column=0)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14), bg="lightblue")
btn_2.grid(row=1, column=1)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14), bg="lightblue")
btn_3.grid(row=1, column=2)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14), bg="lightblue")
btn_4.grid(row=2, column=0)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14), bg="lightblue")
btn_5.grid(row=2, column=1)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14), bg="lightblue")
btn_6.grid(row=2, column=2)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14), bg="lightblue")
btn_7.grid(row=3, column=0)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14), bg="lightblue")
btn_8.grid(row=3, column=1)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14), bg="lightblue")
btn_9.grid(row=3, column=2)

# Remaining buttons with background colors
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14), bg="lightblue")
btn_0.grid(row=4, column=1)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14), bg="orange")
btn_plus.grid(row=1, column=3)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14), bg="orange")
btn_minus.grid(row=2, column=3)
btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14), bg="orange")
btn_mul.grid(row=3, column=3)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14), bg="orange")
btn_div.grid(row=4, column=3)
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14), bg="orange")
btn_open.grid(row=4, column=0)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14), bg="orange")
btn_close.grid(row=4, column=2)
btn_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial", 14), bg="red")
btn_clear.grid(row=5, column=0, columnspan=2)
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14), bg="green")
btn_equals.grid(row=5, column=2, columnspan=3)

root.mainloop()
