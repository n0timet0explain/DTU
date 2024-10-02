#Opgave 3.1 + 3.2 + 3.3
temperature=25
""" 
if temperature<0:
    print("It's freezing")
elif temperature>=0 and temperature<=15:
    print("It's cold")
elif temperature>15 and temperature<=25:
    print("It's pleasant")
elif temperature>25:
    print("It's hot")
 """
    
#Opgave 3.4
""" 
month="December"
day=24

if month=="December":
    if day!=24:
        print("Can we listen to Last Christmas?")
    if day==24:
        print("Let's open presents!")
    else:
        print("No presents today :(")
else:
    print("No presents today :(")
 """   

#Opgave 3.7
""" 
x = 1
y = 2
z = 6

# Compute the largest of three numbers
if x > y and x > z:
    max_of_xyz = x
elif y > z and y > x:
    max_of_xyz = y
else:
    max_of_xyz = z
print(max_of_xyz) 
 """

""" 
day_of_week = "Monday"
if day_of_week == ("Saturday" or "Sunday"):
    print("Weekend")
else:
    print("Work work.")

 """
#opgave 3.8
""" 
digit=0

if digit==1:
    print(str(digit)+"st")
elif digit==2:
    print(str(digit)+"nd")
elif digit==3:
    print(str(digit)+"rd")
elif digit>0 and digit<10:
    print(str(digit)+"th")
else:
    print("Uden for opgaven ;)")
 """

#Opgave 3.9

number_of_experiments = 10
number_of_successes = 30
if number_of_experiments==0:
    print("The probability of success is undefined, since the number of experiments is 0")
else:
    probability_of_success = number_of_successes / number_of_experiments
    print(probability_of_success)
