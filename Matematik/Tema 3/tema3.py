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

# U=19
# R1=5
# u=15.3

# R2,I1,I2  = symbols('R2 I1 I2')

# equation1 = Eq(U - u, R1 * I1)
# equation2 = Eq(u, R2 * I2)
# equation3 = Eq(0,I1-I2)

# solutions=linsolve((equation1,equation2,equation3),(R2,I1,I2))


# print(solutions)



# ##Opgave 2 a

# U=22
# R1=6
# R2=6
# R3=6
# R4=12
# R5=12


# I1,I2,I3,I4,I5=symbols("I1:6")
# u1,u2=symbols("u1:3")


# lign1 = Eq(U - u1, R1 * I1)
# lign2 = Eq(u1, R2 * I2)
# lign3 = Eq(U - u2, R3 * I3)
# lign4 = Eq(u2, R4 * I4)
# lign5 = Eq(u2-u1, R5 * I5) #u2-u1 skal ændres til U i opgave b
# lign6 = Eq(0, I1-I2+I5)
# lign7 = Eq(0, I3-I4-I5)

# solutions=linsolve((lign1,lign2,lign3,lign4,lign5,lign6,lign7),(I1,I2,I3,I4,I5,u1,u2))

# solu=solutions.args[0] #Bruges så de kommer i en liste
# print(solutions)


# print("Opgave A")
# print(f"I1+I3: {solu[0]+solu[2]:.3f}")
# print(f"I2+I4: {solu[1]+solu[3]:.3f}")
# print(f"\nOpgave B")
# print(f"I1+I3+I5: {solu[0]+solu[2]+solu[4]:.3f}")
# print(f"I1+I3+I5: {solu[0]+solu[2]+solu[4]:.3f}")


# ##Opgave 2 b

# U=22
# R1=6
# R2=6
# R3=6
# R4=12
# R5=12


# I1,I2,I3,I4,I5=symbols("I1:6")
# u1,u2=symbols("u1:3")


# lign1 = Eq(U - u1, R1 * I1)
# lign2 = Eq(u1, R2 * I2)
# lign3 = Eq(U - u2, R3 * I3)
# lign4 = Eq(u2, R4 * I4)
# lign5 = Eq(U, R5 * I5)
# lign6 = Eq(0, I1-I2)
# lign7 = Eq(0, I3-I4)

# solutions=linsolve((lign1,lign2,lign3,lign4,lign5,lign6,lign7),(I1,I2,I3,I4,I5,u1,u2))

# solu=solutions.args[0] #Bruges så de kommer i en liste
# print(solutions)


# print("Opgave A")
# print(f"I1+I3: {solu[0]+solu[2]:.3f}")
# print(f"I2+I4: {solu[1]+solu[3]:.3f}")
# print(f"\nOpgave B")
# print(f"I1+I3+I5: {solu[0]+solu[2]+solu[4]:.3f}")
# print(f"I2+I4+I5: {solu[1]+solu[3]+solu[4]:.3f}")



##Opgave 3

# U=21
# R1=6
# R2=6
# R3=6
# R4=7
# R5=4


# I1,I2,I3,I4,I5=symbols("I1:6")
# u1,u2=symbols("u1:3")


# lign1 = Eq(U - u1, R1 * I1)
# lign2 = Eq(u1, R2 * I2)
# lign3 = Eq(U - u2, R3 * I3)
# lign4 = Eq(u2, R4 * I4)
# lign5 = Eq(u2-u1, R5 * I5)
# lign6 = Eq(0, I1-I2)
# lign7 = Eq(0, I3-I4)

# solutions=linsolve((lign1,lign2,lign3,lign4,lign5,lign6,lign7),(I1,I2,I3,I4,I5,u1,u2))

# solu=solutions.args[0] #Bruges så de kommer i en liste
# print(solu)
# print(f"{solu[4]:.3f}")





# #Spørgsmål 2 fra PDF som kontrol
# U=12.6
# R1=7
# R2=3
# R3=7
# R4=3
# R5=4


# I1,I2,I3,I4,I5=symbols("I1:6")
# u1,u2=symbols("u1:3")


# lign1 = Eq(U - u1, R1 * I1)
# lign2 = Eq(u1, R2 * I2)
# lign3 = Eq(U - u2, R3 * I3)
# lign4 = Eq(u2, R4 * I4)
# lign5 = Eq(u2-u1, R5 * I5)
# lign6 = Eq(0, I1-I2+I5)
# lign7 = Eq(0, I3-I4-I5)

# solutions=linsolve((lign1,lign2,lign3,lign4,lign5,lign6,lign7),(I1,I2,I3,I4,I5,u1,u2))

# solu=solutions.args[0] #Bruges så de kommer i en liste
# print(solu)
# print(f"{solu[4]:.3f}")



# ##Opgave 4a
# U=16
# R1=R2=R3=R4=R5=R6=R7=R8=R9=R10=R11=R12=4

# I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12=symbols("I1:13")
# u1,u2,u3,u4,u5,u6,u7,u8=symbols("u1:9")

# lign1 = Eq(U-u2, R1*I1)#Første
# lign2 = Eq(U-u3, R2*I2)#Første
# lign3 = Eq(u2-u4, R3*I3)
# lign4 = Eq(u3-u4, R4*I4)
# lign5 = Eq(U-u5, R5*I5)#Første
# lign6 = Eq(u2-u6, R6*I6)
# lign7 = Eq(u3-u7, R7*I7)
# lign8 = Eq(u4, R8*I8)#Sidste
# lign9 = Eq(u5-u6, R9*I9)
# lign10 = Eq(u5-u7, R10*I10)
# lign11 = Eq(u6, R11*I11)#Sidste
# lign12 = Eq(u7, R12*I12)#Sidste
# lign13 = Eq(0, I1-I3-I6)#u2
# lign14 = Eq(0, I2-I4-I7)#u3
# lign15 = Eq(0, I3+I4-I8)#u4
# lign16 = Eq(0, I5-I9-I10)#u5
# lign17 = Eq(0, I6+I9-I11)#u6
# lign18 = Eq(0, I7+I10-I12)#u7


# solutions=linsolve((lign1,lign2,lign3,lign4,lign5,lign6,lign7,lign8,lign9,lign10,lign11,lign12,lign13,lign14,lign15,lign16,lign17,lign18),(I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,u2,u3,u4,u5,u6,u7))


# solu=solutions.args[0] #Bruges så de kommer i en liste
# print(solu)
# print(f"{solu[0]+solu[1]+solu[4]:.3f}")
# print(f"{solu[7]+solu[10]+solu[11]:.3f}")


# ##Opgave 4b
# U=16
# R1=R2=R3=R4=R5=R6=R7=R8=R9=R10=R11=R12=4
# R13=9

# I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,I13=symbols("I1:14")
# u1,u2,u3,u4,u5,u6,u7,u8=symbols("u1:9")

# lign1 = Eq(U-u2, R1*I1)#Første
# lign2 = Eq(U-u3, R2*I2)#Første
# lign3 = Eq(u2-u4, R3*I3)
# lign4 = Eq(u3-u4, R4*I4)
# lign5 = Eq(U-u5, R5*I5)#Første
# lign6 = Eq(u2-u6, R6*I6)
# lign7 = Eq(u3-u7, R7*I7)
# lign8 = Eq(u4, R8*I8)#Sidste
# lign9 = Eq(u5-u6, R9*I9)
# lign10 = Eq(u5-u7, R10*I10)
# lign11 = Eq(u6, R11*I11)#Sidste
# lign12 = Eq(u7, R12*I12)#Sidste
# lign13 = Eq(0, I1-I3-I6)#u2
# lign14 = Eq(0, I2-I4-I7)#u3
# lign15 = Eq(0, I3+I4-I8)#u4
# lign16 = Eq(0, I5-I9-I10)#u5
# lign17 = Eq(0, I6+I9-I11)#u6
# lign18 = Eq(0, I7+I10-I12)#u7
# lign19 = Eq(U, R13*I13)


# solutions=linsolve((lign1,lign2,lign3,lign4,lign5,lign6,lign7,lign8,lign9,lign10,lign11,lign12,lign13,lign14,lign15,lign16,lign17,lign18,lign19),(I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,I13,u2,u3,u4,u5,u6,u7))


# solu=solutions.args[0] #Bruges så de kommer i en liste
# print(solu)
# print(f"{solu[0]+solu[1]+solu[4]+solu[18]:.3f}")
# print(f"{solu[7]+solu[10]+solu[11]+solu[18]:.3f}")

# print(f"{11.2-4.8:.3f}")


# # ##Opgave 5a
# U=10
# R1=R2=R3=R4=R5=R6=R7=R8=R9=R10=R11=R12=6
# # R13=5

# I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12=symbols("I1:13")
# u1,u2,u3,u4,u5,u6,u7,u8=symbols("u1:9")

# lign1 = Eq(u1-u2, R1*I1)
# lign2 = Eq(u3-u1, R2*I2)
# lign3 = Eq(u2-u4, R3*I3)
# lign4 = Eq(u3-u4, R4*I4)
# lign5 = Eq(u1-u5, R5*I5)
# lign6 = Eq(u2-u6, R6*I6)
# lign7 = Eq(U-u3, R7*I7)
# lign8 = Eq(u4, R8*I8)
# lign9 = Eq(u5-u6, R9*I9)
# lign10 = Eq(U-u5, R10*I10)
# lign11 = Eq(u6, R11*I11)
# lign12 = Eq(U, R12*I12)
# lign13 = Eq(0, I1-I3-I6)#u2
# lign14 = Eq(0, I7-I2-I4)#u3
# lign15 = Eq(0, I3+I4-I8)#u4
# lign16 = Eq(0, I10+I5-I9)#u5
# lign17 = Eq(0, I9+I6-I11)#u6
# lign18 = Eq(0, I2-I1-I5)#u1


# solutions=linsolve((lign1,lign2,lign3,lign4,lign5,lign6,lign7,lign8,lign9,lign10,lign11,lign12,lign13,lign14,lign15,lign16,lign17,lign18),(I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,u1,u2,u3,u4,u5,u6))


# solu=solutions.args[0] #Bruges så de kommer i en liste
# print(solu)
# print(f"{solu[6]+solu[9]+solu[11]:.3f}")
# print(f"{solu[7]+solu[10]+solu[11]:.3f}")




##Opgave 5b
U=10
R1=R2=R3=R4=R5=R6=R7=R8=R9=R10=R11=R12=6
R13=9

I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,I13=symbols("I1:14")
u1,u2,u3,u4,u5,u6,u7,u8=symbols("u1:9")

lign1 = Eq(u1-u2, R1*I1)
lign2 = Eq(u3-u1, R2*I2)
lign3 = Eq(u2-u4, R3*I3)
lign4 = Eq(u3-u4, R4*I4)
lign5 = Eq(u1-u5, R5*I5)
lign6 = Eq(u2-u6, R6*I6)
lign7 = Eq(U-u3, R7*I7)
lign8 = Eq(u4, R8*I8)
lign9 = Eq(u5-u6, R9*I9)
lign10 = Eq(U-u5, R10*I10)
lign11 = Eq(u6, R11*I11)
lign12 = Eq(U, R12*I12)
lign13 = Eq(0, I1-I3-I6)#u2
lign14 = Eq(0, I7-I2-I4)#u3
lign15 = Eq(0, I3+I4-I8)#u4
lign16 = Eq(0, I10+I5-I9)#u5
lign17 = Eq(0, I9+I6-I11)#u6
lign18 = Eq(0, I2-I1-I5-I13)#u1
lign19 = Eq(u1, R13*I13)

solutions=linsolve((lign1,lign2,lign3,lign4,lign5,lign6,lign7,lign8,lign9,lign10,lign11,lign12,lign13,lign14,lign15,lign16,lign17,lign18,lign19),(I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,u1,u2,u3,u4,u5,u6,I13))


solu=solutions.args[0] #Bruges så de kommer i en liste
print(solu)
print(f"{solu[6]+solu[9]+solu[11]:.3f}")
print(f"{solu[7]+solu[10]+solu[11]+solu[18]:.3f}")





##Opgave 5c
# U=10
# R1=R2=R3=R4=R5=R6=R7=R8=R9=R10=R11=R12=6
# R13=9

# I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12=symbols("I1:13")
# u1,u2,u3,u4,u5,u6,u7,u8=symbols("u1:9")

# lign1 = Eq(u1-u2, R1*I1)
# lign2 = Eq(u3-u1, R2*I2)
# lign3 = Eq(u2-u4, R3*I3)
# lign4 = Eq(u3-u4, R4*I4)
# lign5 = Eq(u1-u5, R5*I5)
# lign6 = Eq(u2-u6, R6*I6)
# lign7 = Eq(U-u3, R7*I7)
# lign8 = Eq(u4, R8*I8)
# lign9 = Eq(u5-u6, R9*I9)
# lign10 = Eq(U-u5, R10*I10)
# lign11 = Eq(u6, R11*I11)
# # lign12 = Eq(U, R12*I12)
# lign13 = Eq(0, I1-I3-I6)#u2
# lign14 = Eq(0, I7-I2-I4)#u3
# lign15 = Eq(0, I3+I4-I8)#u4
# lign16 = Eq(0, I10+I5-I9)#u5
# lign17 = Eq(0, I9+I6-I11)#u6
# lign18 = Eq(0, I2-I1-I5-I12)#u1
# lign19 = Eq(u1, R13*I12)

# solutions=linsolve((lign1,lign2,lign3,lign4,lign5,lign6,lign7,lign8,lign9,lign10,lign11,lign13,lign14,lign15,lign16,lign17,lign18,lign19),(I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,u1,u2,u3,u4,u5,u6))
# print(solutions)

# solu=solutions.args[0] #Bruges så de kommer i en liste
# print(solu)
# print(f"{solu[6]+solu[9]:.3f}")
# print(f"{solu[7]+solu[10]+solu[11]+solu[11]:.3f}")