from sympy import *


# U=12.6
# R1=3
# R2=7

# u, I1,I2  = symbols('u I1 I2')




# equation1 = Eq(U - u, R1 * I1)
# equation2 = Eq(u, R2 * I2)
# equation3 = Eq(0, I1-I2)

# solutions=linsolve((equation1,equation2,equation3),(u,I1,I2))


# print(solutions)

# numerical_solution = {key: value.subs({U: 12.6, R1: 3, R2: 7}) for key, value in solutions.items()}
# print(numerical_solution)

# # # # # # U=19
# # # # # # R1=5
# # # # # # u=15.3

# # # # # # R2,I1,I2  = symbols('R2 I1 I2')

# # # # # # equation1 = Eq(U - u, R1 * I1)
# # # # # # equation2 = Eq(u, R2 * I2)
# # # # # # equation3 = Eq(0,I1-I2)


# # # # # # solutions=linsolve((equation1,equation2,equation3),(R2,I1,I2))


# # # # # # print(solutions)


from sympy import *
U = 19
R1 = 5
u = 15.3

# Definer symboler for variabler
R2, I1, I2 = symbols('R2 I1 I2')

# Opsæt ligninger
equation1 = Eq(U - u, R1 * I1)   # Første ligning
equation2 = Eq(u, R2 * I2)        # Anden ligning
equation3 = Eq(I1, I2)            # Tredje ligning (ændret til at sige I1=I2)

# Løs ligningssystemet
solutions = linsolve((equation1, equation2, equation3), (R2, I1, I2))

# Udskriv løsninger
print(solutions)

##Opgave 2

# U=22
# R1=6
# R2=6
# R3=6# R4=12

# I1,I2,I3,I4,I5,u  = symbols('I1 I2 I3 I4 I5 u')

# lign1 = Eq(U - u, R1 * I1)
# lign2 = Eq(u, R2 * I2)
# lign3 = Eq(0, I1-I2)


# solutions=linsolve((lign1,lign2,lign3),(R2,I1,I2))

# print(U-u)
# print(solutions)