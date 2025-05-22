from project import quad, y_quad, plot_equ
import pytest
import os

def main():
    test_quad()
    test_y_quad()
    test_plot_equ()

def test_quad():
    result = quad(1, 6, 5)
    assert 'Roots: -1.00, -5.00' in result

def test_y_quad():
    result = y_quad(1, 6, 5)
    assert 'Y-axis Intercept: (0, 5)' in result
    assert 'Vertex: (-3.00, -4.00)' in result

def test_plot_equ():
    filename = 'quad.png'

    # does file exist already
    if os.path.exists(filename):
        os.remove(filename)

    # create the plot
    quad_info = "Test Equation: x² - 3x + 2"
    y_quad_info = "Test Info"
    plot_equ(1, -3, 2, filename, quad_info, y_quad_info)

    # if file exists then pass
    assert os.path.exists(filename)

if __name__ == '__main__':
    main()