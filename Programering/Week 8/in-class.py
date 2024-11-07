# #Opgave 8.1
# inventory = {
#     "apples": 10,
#     "bananas": 5,
#     "oranges": 8,
#     "kiwis": 7
# }

# def restock_inventory(inv,x):
#     for i in inv:
#         inv[i]=inv[i]+x


# print(inventory)

# restock_inventory(inventory,5)

# inventory['melon'] = inventory.pop("apples")
# print(inventory)


# #Opgave 8.2
# spacing=32
# WS={
#     "station_name": "CPH Airport Weather",
#     "is_operational": True,
#     "city": "Kastrup",
#     "country": "Denmark",
#     "construktion_year": "2016",
# }

# tr=[20.1, 21.3, 19.8, 22.0]
# wsr=[5.2, 3.4, 7.1, 15.6]

# WS["temperature_readings"]=tr
# WS["wind_speed_readings"]=wsr

# for category in WS:
#     print(f"{category:{spacing}} {WS[category]}")

# avg={}

# def average_reading(x):
#     for category in x:
#         if type(x[category])==list:
#            avg[category+" average"]={sum(x[category])//len(x[category])}
#     return avg

# average_reading(WS)

# for category in avg:
#     print(f"{category:{spacing}} {avg[category]}")




# Opgave 8.3
import math

experiment_name = "standard_values"
experiment_values = [1.30, -0.01,  1.35,  0.31,  0.35, -1.61,  1.39,  1.19, -1.07,  0.34]

def data_statistics(name, value):
    
    name={
        "experiment_name":name,
        "experiment_values":value,
        "mean_val":(sum(value)//len(value))+(sum(value)%len(value)),
        "standard_deviation":(sqrt.math(for i in range(len(value+1): i-mean)**2)/len(value)),
        "max_val":3,
        "min_val":5,
    }


def data_statistics(name, value):
    
    name={
        "experiment_name":experiment_values,
        "experiment_values":experiment_values,
        "mean_val":(sum(experiment_values)/len(experiment_values)),
        standard_deviation:
        max_val:"",
        min_val:"",
    }