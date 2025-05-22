import math
from sympy import symbols, diff, solve
import matplotlib.pyplot as plt
import numpy as np
import re
import os

def main():
    while True:
        value = input("Provide the values for the quadratic equation.\n(e.g., '1 6 5' or '1,6,5' or '1-6-5' or '1_6_5'): ")
        try:
            # Split the input (space, comma, dash, underscore)
            values = re.findall(r'-?\d+', value)
            if len(values) != 3:
                raise ValueError
            a, b, c = map(int, values)
            if a == 0:
                print('x² must not have a coefficient of zero')
                continue
        except ValueError:
            print("Invalid input, Please enter three valid integers separated by spaces, commas, dashes, or underscores.")
            continue
        break
    
    while True:
        filename = input("Enter the filename to save the plot (e.g., 'quadratic_plot.png'): ")
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            print("Invalid File extention, filename must end with 'png', 'jpg' or 'jpeg'.")
            continue
        if os.path.exists(filename):
            overwrite = input(f"The file '{filename}' already exists. Do you want to overwrite it? (y/n): ").strip().lower()
            if overwrite != 'y':
                continue
        break
    quad_info = quad(a, b, c)
    y_quad_info = y_quad(a, b, c)
    plot_equ(a, b, c, filename, quad_info, y_quad_info)

def quad(a, b, c):
    equation = f"{a}x² + {b}x + {c}"
    print("Equation:", equation)

    discriminant = (b ** 2) - (4 * a * c)
    if discriminant < 0:
        return 'Error: No Real Solution.'

    sqrt_discriminant = math.sqrt(discriminant)

    if discriminant > 0:
        root1 = float(((-1 * b) + sqrt_discriminant) / (2 * a))
        root2 = float(((-1 * b) - sqrt_discriminant) / (2 * a))
        roots_info = f"Roots: {root1:.2f}, {root2:.2f}"
        #print(roots_info)
        return f"Equation: {equation}\nDiscriminant: {discriminant}\n{roots_info}"

    elif discriminant == 0:
        root = float((-1 * b) / (2 * a))
        root_info = f"Root: {root:.2f}"
        #print(root_info)
        return f"Equation: {equation}\nDiscriminant: {discriminant}\n{root_info}"

def y_quad(a, b, c):
    x = symbols('x')
    equation = (a * (x ** 2)) + (b * x) + c
    y_intercept = c
    intercept_info = f"Y-axis Intercept: (0, {y_intercept})"
    #print(intercept_info)

    min_max_eq = diff(equation, x)
    min_max_coordinate = solve(min_max_eq, x)
    x_coordinate = min_max_coordinate[0]
    y_coordinate = (a * (x_coordinate ** 2)) + (b * x_coordinate) + c
    vertex_info = f"Vertex: ({x_coordinate:.2f}, {y_coordinate:.2f})"
    #print(vertex_info)

    if a < 0:
        return f"{intercept_info}\nMax Vertex Equation: {min_max_eq} = 0\n{vertex_info}"
    else:
        return f"{intercept_info}\nMin Vertex Equation: {min_max_eq} = 0\n{vertex_info}"

def plot_equ(a, b, c, filename, quad_info, y_quad_info):
    x_values = np.linspace(-10, 10, 400)
    y_values = a * (x_values ** 2) + b * x_values + c

    plt.figure(figsize=(8, 8))
    plt.plot(x_values, y_values, label=f'{a}x² + {b}x + {c}', color='blue')

    discriminant = (b ** 2) - (4 * a * c)
    if discriminant >= 0:
        sqrt_discriminant = math.sqrt(discriminant)
        root1 = float(((-1 * b) + sqrt_discriminant) / (2 * a))
        root2 = float(((-1 * b) - sqrt_discriminant) / (2 * a))
        plt.scatter([root1, root2], [0, 0], color='Black')
        plt.text(root1, 0, f'{root1:.2f}', ha='right', fontsize=10, color='black')
        plt.text(root2, 0, f'{root2:.2f}', ha='right', fontsize=10, color='black')

    x_vertex = -b / (2 * a)
    y_vertex = a * (x_vertex ** 2) + b * x_vertex + c
    plt.scatter([x_vertex], [y_vertex], color='green')
    plt.text(x_vertex, y_vertex, f'Vertex: ({x_vertex:.2f}, {y_vertex:.2f})', ha='left', fontsize=10, color='black')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title(f'Plot of {a}x² + {b}x + {c}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)

    # Adding quad_info and y_quad_info at the bottom of the plot
    plt.figtext(0.1, -0.1, f"{quad_info}\n{y_quad_info}", wrap=True, horizontalalignment='left', fontsize=12)

    plt.savefig(filename, bbox_inches='tight')

    print(f"Plot saved as {filename}")

if __name__ == "__main__":
    main()
