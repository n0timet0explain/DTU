# #Tema-øvelse 1.

# #Målet med denne tema-øvelse er at opnå en bedre forståelse af geometrien i den komplekse
# #talplan. Især vil vi studere en bestemt type funktioner fra C til C kaldet affine transformationer.
# #Du vil også lære at udføre simple beregninger med komplekse tal i commandoline-versionen af
# #Python.

# #Del I: arbejde med komplekse tal i commandline-versionen af Python

import cmath
import math

# z=complex(2,3)

# print(z.real)
# print(z.imag)

# print(-z)
# print(1/z)
# print(z**-1)
# print((2/13)-(3/13))
# print(0.1538-0.2307)
# print((z**-1)==((2/13)-(3/13)))

# w=complex(4,5)

# #Man kan gange to komplekse tal sammen
# print(z*w)

# #Polære koordinater
# print(cmath.polar(z))

# #Modulus af z
# print(cmath.polar(z)[0])

# #Hovedargumentet
# print(cmath.polar(z)[1])

# y=complex(1+1j)

# print(y)

# print(cmath.polar(y))

# print(((math.sqrt(2))/2)/((math.sqrt(2))/2))

# print(cmath.rect(1.4142135623730951, 0.7853981633974483))


# z1=2
# z2 = 1 + 1j
# z3 = -2 + 3j

# # Definér funktionen f(z) = i * z
# def f(z):
#     return z*cmath.

# # Beregn f(z) for hvert tal
# f_z1 = f(z1)
# f_z2 = f(z2)
# f_z3 = f(z3)

# # Udskriv resultaterne
# print(f"f(2) = {f_z1}")
# print(f"f(1 + i) = {f_z2}")
# print(f"f(-2 + 3i) = {f_z3}")

# x1=2

# f(x1)=







# #Opgave 1

# z1=complex(9,9)
# z2=complex(-7,1)
# z3=complex()


# z=(1/(z1+z2**3))

# z=(1/((z1)+(z2)**3))

# print(z1,z2)

# print(z)

# print(z.real)
# print(z.imag)


 #Opgave 2



# #>>>cmath.polar(z)

# (2.236067977,-.4636476090)

# #>>>cmath.rect(2.236067977,-.4636476090)

# z=complex(2,1)

# print(cmath.polar(z))
# print(2.236067977,-.4636476090)

#Opg 4

# pi3=cmath.exp(complex(0,2*math.pi/3))


# z=complex(1.666666666,1.100000000)

# print(z*pi3)


#opg 5

# Definér funktionen f(z) = z*e^ia

z=complex(5,1)
res=complex(4.701663558,1.973413232)

argz=cmath.phase(z)
argres=cmath.phase(res)

print(argz)
print(argres)

alpha=argres-argz

print(alpha)