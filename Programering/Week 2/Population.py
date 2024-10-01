import math
#Input
population_goal=100000

#def
initial_size=1000
rate_per_year=0.15





time=(1/rate_per_year)*math.log(population_goal/initial_size)

year=round(time//1)
month=round(time%1*12)

print("Time to population of " + str(population_goal)+ " is " + str(year) + " year(s) and " + str(month) + " month(s)")





