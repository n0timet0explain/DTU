m=1
f=0

#Input
weight=75   #i KG
height=1.78 #I meter
age=34      #I år
sex=m    #f for kvinde m for mand

#BMI calculate
bmi_min=18.5
bmi_max=25

bmi=weight/(height**2)
print(bmi)
weight_normal_range=bmi_min<=bmi and bmi<=bmi_max

#Body fat calculate
pbf=1.20*bmi+0.23*age-10.8*sex-5.4


#Resultat
print("BMI is: " + str(bmi))
print("BMI is in normal range: " + str(weight_normal_range))
print("PBF is: " + str(pbf))


#Normal range
weight_min=int(bmi_min*(height**2), 0)
weight_max=int(bmi_max*(height**2), 0)

print("For a height of "+str(height)+" m, the normal weight range is between "+str(weight_min)+" and "+str(weight_max)+" kg.")

