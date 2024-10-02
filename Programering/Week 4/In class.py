#Opgave 4.1

# for _ in range(72):
#     print("Around the world, around the world")

#Opgave 4.2
# x=""
# for element in range(1,21):
#     x=x+str(element)+" "
# print(x)

# n=10
# x=0
# for tal in range(1,n+1):
#     x=x+tal
# print(x)

#Opgave 4.3

# n=10
# x=0
# b=""
# for tal in range(1,n+1):
#     x=x+tal
#     if tal==n:
#         break
#     b=b+str(tal)+" + "
# b=b+str(tal)+" "+"= "+str(x)
# print(b)

#Opgave 4.4
# kage=100
# min_kage=0.01
# while True:
#     kage=kage-(kage/2)
#     if kage<min_kage:
#         break
#     print(kage)

#Opgave 4.5

# x=10
# liste=""
# for gange in range(1,x+1):
#     if liste!="":
#         liste=liste+"\n"
#     for tal in range(1,x+1):
#         liste=liste+str(tal*gange)+((3-len(str(tal*gange)))*" ")

# print(liste)

#Opgave 4.6
# n=10
# liste=""
# res=1
# for i in range(1,n+1):
#     res=res*i
#     if liste!="":
#         liste=liste+"*"+str(i)
#     else:
#         liste=liste+str(i)
#     print(str(i)+"! = "+liste+" = "+str(res))


#Opgave 4.7
# height=5
# stjerner=1
# for i in range(1,height+1):
#     if i==1:
#         print(height*" "+(stjerner*"*"))
#     else:
#         print(height*" "+(stjerner*"*"))
#     height=height-1
#     stjerner=stjerner+2


#Opgave 4.8
# height=30
# stjerner=1
# dybde=height
# #top
# for i in range(1,height+1):
#     print(dybde*" "+(stjerner*"*"))
#     dybde=dybde-1
#     stjerner=stjerner+2
# stjerner=stjerner-4
# dybde=dybde+2
# #bund
# for i in range(height):
#     print((dybde)*" "+(stjerner*"*"))
#     dybde=dybde+1
#     stjerner=stjerner-2

#Opgave 4.9
# R=0.9
# amount=2.5
# t=10
# for i in range(t):
#     amount=amount*R
#     print("The amount left after "+str(i)+" hours is "+str(amount))


#Opgave 4.10
# R=0.75
# amount_s=6.5
# amount_e=amount_s
# t=0
# while amount_e>=(amount_s/2):
#     t=t+1
#     amount_e=amount_e*R
#     print("The amount left after "+str(t)+" hours is "+str(amount_e))
# print("The amount is below half after "+str(t)+" hours")


#Opgave 4.11
# R=0.25
# pop=15000
# licenses=1000
# years=10

# for i in range(1,years+1):
#     pop=pop+(0.25*pop)-licenses
#     print("The population after "+str(i)+" years is "+str(pop//1))


#Opgave 4.12
# n=27
# s=0
# while n!=1:
#     if (n%2)==0:
#         n=n/2
#         s=s+1
#     else:
#         n=(n*3)+1
#         s=s+1
# print("Stopped after "+str(s)+" steps")
