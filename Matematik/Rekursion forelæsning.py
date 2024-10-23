#Opgave 1

# def fac(n):
#     if n == 1: # This is the base case
#         return 1
#     else: # This is the recursive case
#         return(fac(n-1)*n)

# print(fac(5))



def h(n):
    if n == 1: # This is the base case
        return 11
    else: # This is the recursive case
        return(h(n**2-5*n+7))

print(h(4))