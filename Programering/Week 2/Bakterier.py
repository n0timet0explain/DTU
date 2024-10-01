bStart=500
bGrowthMin=600
bGrowthMax=800
#Her kan værdier ændres
hour=3
bacteria_amount=2500

#Udregning
final_bacteria_min=bStart+(bGrowthMin*hour)
final_bacteria_max=bStart+(bGrowthMax*hour)
print(final_bacteria_min)
print(final_bacteria_max)

is_contaminated=final_bacteria_min>=bacteria_amount or bacteria_amount>=final_bacteria_max

#Den endelige udregning
print("Contaminated: " + str(is_contaminated))