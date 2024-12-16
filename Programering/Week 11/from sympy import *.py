from sympy import *

t=symbols("t")

integral=integrate((2*t**2+6*t+1)*exp(-t**2))
print(integral)