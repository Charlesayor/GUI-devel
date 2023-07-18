## GUI Calculator

# Code Analysis:

The code developed showcases a functional calculator interface, allowing users to perform basic arithmetic operations. 

It has been created using the popular tkinter library, which is widely used for GUI development in Python. The code demonstrates how to create a window, text display field, and various buttons for user input and interaction.

To begin with using tutorial video, the tkinter library was imported using the short form tk. Along with The Lambda class which was imported from the ast library, 

The Lambda class is used for creating anonymous functions in Python, while the 

The ast library in Python stands for Abstract Syntax Trees. It provides a set of functions and classes for working with the abstract syntax tree (AST) of Python code

This library provides a range of modules and functions necessary for GUI development.
 
Within the code,  the Text, Button, and grid methods were used from tkinter to create the necessary components.

several functions were defined within the code to handle different operations. 


The add_to_calculation() function concatenates the provided symbol to the calculation string, updating the text display accordingly. 


The evaluate_calculation() function evaluates the current calculation using the eval() function, displaying the result or an error message as appropriate. 

The clear_field() function resets the calculation field and text display.

The layout of the calculator GUI is achieved using the grid() method. By specifying row and column positions, we position the buttons and text display field accordingly, creating a familiar calculator interface

## Credits

This project is based on the work of [Neuralnine](https://youtu.be/NzSCNjn4_RI). I would like to acknowledge their contribution to the initial codebase, which served as a reference for this project.

## Modifications

I made the following modifications to the original code:

1. In the `evaluate_calculation()` function, I changed the line `calculation = " "` to `calculation = calculation.strip()`. This modification ensures that any leading or trailing spaces in the calculation are removed before evaluating it.

2. In the `clear_field()` function, I added the line `text_result.insert(1.0, calculation)` after deleting the contents of the `text_result` widget. This change updates the widget to display the cleared calculation.

These modifications address the issues in the original code that were causing the calculator to not provide any output. By removing the spaces and updating the display, the calculator can now evaluate and display the desired results.

Feel free to explore the code to see the specific changes I made. If you have any further questions or need additional clarification, please let me know!