from sympy import *


U=12.6
R1=3
R2=7

u, I1,I2  = symbols('u I1 I2')




equation1 = Eq(U - u, R1 * I1)
equation2 = Eq(u, R2 * I2)
equation3 = Eq(0, I1-I2)

solutions=linsolve((equation1,equation2,equation3),(u,I1,I2))


print(solutions)

# numerical_solution = {key: value.subs({U: 12.6, R1: 3, R2: 7}) for key, value in solutions.items()}
# print(numerical_solution)



