<h2>Explanation</h2>

    Function Definitions:
        add(x, y): Returns the sum of x and y.
        subtract(x, y): Returns the difference of x and y.
        multiply(x, y): Returns the product of x and y.
        divide(x, y): Returns the quotient of x divided by y, with a check to prevent division by zero.

    Main Function:
        main(): This function prompts the user to input two numbers and choose an arithmetic operation. It performs the chosen operation and displays the result. The loop continues until the user chooses to exit (option 5).

    Input Handling:
        The program uses float(input()) to ensure that the user inputs are treated as floating-point numbers, allowing for decimal calculations.
        A try-except block is used to catch invalid numerical inputs and prompt the user to enter valid numbers.

    User Interaction:
        The program presents a menu of operations and reads the user's choice.
        It performs the corresponding calculation based on the user's choice and prints the result.
        The loop continues, allowing the user to perform multiple calculations until they choose to exit.

<h2>Running the Application</h2>

To run the application, save the code to a file (e.g., simple_calculator.py) and execute it with Python:

python3 simple_calculator.py

<h2>This will start the command-line interface for the calculator, allowing you to perform basic arithmetic operations interactively.</h2>
