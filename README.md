# Quadratic Equation Solver and Graph Plot
#### Video Demo:  <URL HERE>
#### Description:

This project is a Python application that solves quadratic equations and generates a corresponding plot of the equation. The application performs the following tasks:

1. **Data Handling and Validation:**
    - User input for the quadratic equation is accepted in various formats (space-separated, comma-separated, dash-separated, or underscore-separated)
    - If user input is outside of this formats then the user is prompted with an message and stuck in loop until a valid input is given.

2. **Quadratic Equation (quad() function):**
    - The application calculates the discriminant to calculate the number of real roots the equation has.
    - Based on the Discriminant, it identifies either 2 real roots, 1 real root, or no real roots, and prints the output.

3. **Y-Intercept and Vertex (y_quad() function):**
    - The application calculates the y-intercept and the vertex of the quadratic equation.
   - The vertex is identified as a minimum or maximum point depending on the sign of the leading coefficient.

4. **Plotting the Equation (plot_equ() function):**
   - Using Matplotlib the application creates a plot of the quadratic equation.
   - The plot includes the parabola, the roots (if any), and the vertex. The calculated information from the `quad()` and `y_quad()` functions is added on the plot.
   - The plot is saved as an image file with a user-defined name.

5. **Testing (`test_project.py` file):**
   - The project includes a test suite using `pytest` to validate the correctness of the `quad()`, `y_quad()`, and `plot_equ()` functions.
   - The tests ensure that the functions return the expected results and that the plot is generated successfully.


 
"# CS50P-Quadratic-Solver" 
