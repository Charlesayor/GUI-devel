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

I made the following modifications to the original code to enhance the calculator:

1. **Added Background Colors:** I customized the calculator's appearance by adding background colors to the main window and various widgets. The background color of the main window is set to "lightgray" using `root.configure(bg="lightgray")`. The `text_result` widget, which displays the calculation and results, has a white background using `bg="white"`. Each button is also assigned a background color: numeric buttons (1 to 9, 0) have "lightblue" background, arithmetic operation buttons (+, -, *, /) have "orange" background, "C" button has "red" background, and "=" button has "green" background. You can easily 

modify these colors to suit your preferences by changing the values of the `bg` parameter.

2. **Responsive Resizing:** I made the calculator GUI responsive by configuring the columns and rows to resize proportionally. This allows the calculator to adapt its size when the window is resized. The `root.columnconfigure(i, weight=1, minsize=50)` and `root.rowconfigure(i, weight=1, minsize=50)` lines inside the `for` loop ensure that all six columns and rows are configured to resize appropriately. This modification ensures that the calculator layout remains consistent and user-friendly regardless of the window's size.

3. **Improved Evaluation Logic:** In the `evaluate_calculation()` function, I replaced the line `calculation = " "` with 

`calculation = calculation.strip()`. This change ensures that any leading or trailing spaces in the calculation are removed before evaluating it. This fix prevents potential syntax errors or invalid calculations that could arise due to accidental spaces.

4. **Enhanced Display Logic:** In the `clear_field()` function, I added the line `text_result.insert(1.0, calculation)` after deleting the contents of the `text_result` widget. This improvement updates the widget to display the cleared calculation after the "C" button is pressed. The result is a more intuitive user experience, as the display is now consistent with the internal state of the calculator.

Feel free to explore the code to see these specific changes. If you have any further questions or need additional clarification, please let me know! These modifications enhance the calculator's functionality, appearance, and responsiveness, making it more user-friendly and visually appealing.
