# # Opgave 1 - practice

# class WeatherStation:
#     def __init__(self, station_name, is_operational):
#         self.station_name=station_name
#         self.is_operational=is_operational
#         self.wind_readings=[]
#         self.temperature_readings=[]
#     def take_daily_wind_readings(self,readings):
#         if self.is_operational==True:
#             if type(readings)==list:
#                 self.wind_readings=readings
#             else:
#                 print(f"{readings} is not a list.")
#         else:
#             print("Stations is not operational.")
#     def take_daily_temperature_readings(self,readings):
#         if self.is_operational==True:
#             if type(readings)==list:
#                 self.temperature_readings=readings
#             else:
#                 print(f"{readings} is not a list.")
#         else:
#             print("Stations is not opeational.")
#     def get_highest_readings(self):
#         if self.wind_readings!=[] and self.temperature_readings!=[]:
#             max_readings=(max(self.wind_readings),max(self.temperature_readings))
#             return max_readings
#         else:
#             return
            



# cph_station=WeatherStation("Copenhagen", True)


# cph_station.take_daily_wind_readings([3.5, 6.2, 7.1, 12.1])
# cph_station.take_daily_temperature_readings([18.1, 18.3, 19.0, 18.5])
# print(cph_station.wind_readings)
# print(cph_station.temperature_readings)

# max_wind,max_temp=cph_station.get_highest_readings()
# print(max_wind)
# print(max_temp)

# # Problem solving 
# Opgave 1
