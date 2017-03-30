from sympy import symbols
from numpy import linspace
from sympy import lambdify
import matplotlib.pyplot as plotter
import math as math
import sympy as sp

def eval_func(func_type):
    x_vals = []
    y_vals = []
    if func_type == 1:
        x = symbols('x')
        y = 2 - 3 * x + 10 * (x ** 4) - 5 * (x ** 9) + 6 * (x ** 14)
        lam_x = lambdify(x, y, modules=['numpy'])

        x_vals = linspace(-20, 20, 100)
        y_vals = lam_x(x_vals)
    else:
        x = symbols('x')
        y = sp.exp(-5*((x - 0.3)**2)) + 0.5 * sp.exp(-100*((x - 0.5)**2)) + 0.5 * sp.exp(-100*((x - 0.75)**2))
        lam_x = lambdify(x, y, modules=['numpy'])

        x_vals = linspace(-20, 20, 500)
        y_vals = lam_x(x_vals)
    plotter.plot(x_vals, y_vals)
    plotter.show()

eval_func(1)
