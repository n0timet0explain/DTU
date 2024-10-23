# ##6.1
# my_name=["Lars", "Løkke", "Rasmussen"]
# print("My first name is "+my_name[1]+" and my last name is "+my_name[-1])
# print("In total i have "+str(len(my_name))+" names")

# ##6.2
# n=4

# po2=[]

# for i in range(1,n+1):
#     a=2**i
#     po2.append(a)
# print(po2)

# ## 6.3
# b=0
# for i in range(len(po2)):
#     b=b+po2[i]
#     c=b/len(po2)
# print(c)

# ##6.4
# months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# spring=[months[2:5]]
# print(spring)
# summer=[months[5:8]]
# print(summer)
# quarter_s=[months[0:13:3]]
# print(quarter_s)
# quarter_e=[months[2:13:3]]
# print(quarter_e)
# rev=[months[-1:-13:-1]]
# print(rev)
# winter=[months[11]]
# winter.extend(months[0:2])
# print(winter)

##6.5
months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a=30
pos=[i for i,x in enumerate(days) if x>a]
mwm=[]
print(pos)

for i in range(len(pos)):
    mwm.append=(months[pos[i]])

print(mwm)
