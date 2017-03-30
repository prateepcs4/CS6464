from sympy import symbols
from numpy import linspace
from sympy import lambdify
import matplotlib.pyplot as plotter
import sympy as sp
import numpy as np
import random
import numpy.polynomial.polynomial as poly

def eval_func(func_type):
    x_vals = []
    y_vals = []
    if func_type == 1:
        x = symbols('x')
        y = 2 - 3 * x + 10 * (x ** 4) - 5 * (x ** 9) + 6 * (x ** 14)
        lam_x = lambdify(x, y, modules=['numpy'])

        x_vals = linspace(-0.5, 0.5, 10000)
        y_vals = lam_x(x_vals)
    else:
        x = symbols('x')
        y = sp.exp(-5*((x - 0.3)**2)) + 0.5 * sp.exp(-100*((x - 0.5)**2)) + 0.5 * sp.exp(-100*((x - 0.75)**2))
        lam_x = lambdify(x, y, modules=['numpy'])

        x_vals = linspace(-0.5, 0.5, 10000)
        y_vals = lam_x(x_vals)
    # plotter.plot(x_vals, y_vals)
    # plotter.show()
    return x_vals, y_vals


# Evaluate the function: Options - 1 / 2
x, y = eval_func(2)

# Randomly select points
num_sample = 100
rand_index = random.sample(range(0, len(x)), num_sample)
rand_x = x[rand_index]
rand_y = y[rand_index]

# Add Gaussian noise
noise = np.random.normal(0,1,num_sample)
noise_y = np.add(rand_y, noise)

# Fit a polynomial
degree = 2
coeffs = poly.polyfit(rand_x, noise_y, degree)
ffit = poly.Polynomial(coeffs)

# Plot the result
plotter.plot(rand_x, ffit(rand_x), 'r.', rand_x, noise_y, 'b.')
plotter.show()