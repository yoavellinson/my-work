import numpy as np
import sympy
from sympy.plotting import plot
from sympy import Sum
m = 50
an = 0
bn = 0
x = sympy.symbols('x')
n = sympy.symbols('n')
func = x**3 + 14*x + 4
a0 = sympy.integrate(func, (x, -np.pi, np.pi))*1/np.pi
# calcs an and bn for every n
an = (sympy.integrate((func*sympy.cos(n*x)),
      (x, -np.pi, np.pi))*(1/np.pi))
bn = (sympy.integrate((func*sympy.sin(n*x)),
      (x, -np.pi, np.pi))*(1/np.pi))

AnBn = Sum((an*sympy.cos(n*x))+(bn*sympy.sin(n*x)), (n, 1, m)).doit()

fur = a0/2 + AnBn

p1 = plot(fur, show=False, line_color='b')
p1.title = f'Fourier series of {func} with {m} iterations'
fun = plot(func, show=False, line_color='r')
p1.append(fun[0])
p1.show()
