##################### OPGAVE 1 #####################

# def event_probability(T,n):
#     P=1-((1-(1/T))**n)
#     return P


##################### OPGAVE 2 #####################

# new_arrival=[]

# def arrival_times(schedule, delay):
#     for time_str in schedule:
# #opdel i timer og minutter
#         hours=int(time_str.split(":")[0])
#         minutes=int(time_str.split(":")[1])
# #konverter til total minutantal
#         total_minutes=hours*60+minutes+delay
# #Håndter hvis det går over dagen
#         total_minutes%=1440 #Total antal min på en dag
# #Udregn nye tider
#         new_hour=total_minutes//60
#         new_minute=total_minutes%60
# #Formater
#         new_time=f"{new_hour:02}:{new_minute:02}"
#         new_arrival.append(new_time)

#     return new_arrival

# print(arrival_times(['12:37', '08:10'], 25))


##################### OPGAVE 3 #####################

# liste_1=[2, 8, 11, 3, 5, 7, 5, 8, 7, 11, 3, 12, 3, 7, 7, 5, 7, 2, 6]
# liste=[2, 6, 7, 7, 7, 10, 9, 4, 5, 7, 7, 2, 9, 3, 11, 8, 5, 6, 7, 4, 10]


# def special_occurrence(sequence):
#     for i in range(len(sequence)):
#         if sequence[i]==5:
#             if (sequence[i+1]==7 and sequence[i+2]!=7) or (sequence[i+1]!=7 and sequence[i+2]==7):
#                 return i

# print(special_occurrence(liste))


##################### OPGAVE 4 #####################

# text = ("Sara and Emma like to travel, bike, and hike, and when they are " +
#         "traveling they always take their bikes, hiking shoes, and sleeping bags. " +
#         "Last year, Sarah and Emma traveled to Italy, France, and Spain. And that " +
#         "was fun, and, according to Sara and Emma, very expensive!")


# def punctuation_ratio(text):
#     # Define the target substring
#     target = ' and '
    
#     # Initialize counters
#     comma_before_count = 0
#     no_comma_before_count = 0
    
#     # Iterate through the text to find occurrences of ' and '
#     index = text.find(target)
#     while index != -1:
#         # Check if there is a comma before the substring
#         if index > 0 and text[index - 1] == ',':
#             comma_before_count += 1
#         else:
#             no_comma_before_count += 1
        
#         # Move to the next occurrence of ' and '
#         index = text.find(target, index + len(target))
    
#     # Calculate and return the ratio
#     if no_comma_before_count == 0:  # Avoid division by zero
#         return 0
    
#     return comma_before_count / no_comma_before_count

# result = punctuation_ratio(text)
# print(result)


##################### OPGAVE 5 #####################

# import numpy as np

# A = np.array([[ 1.42, 4.0, 55.56, 63.0],
#               [ 2.22, 2.22, 33.73, 40.11],
#               [12.1, 17.24, 18.0, 33.5],
#               [21.15, 14.76, 17.3, 22.1],
#               [ 5.34, 6.0, 9.8, 8.18]])

# # print((A[0])[0])

# def checkerboard_sum(checker):
#     lige=0
#     ulige=0
#     for i in range(0,len(checker),2):
#         række=checker[i]
#         for i in række[::2]:
#             lige=lige+i
#     for i in range(1,len(checker),2):
#         række=checker[i]
#         for i in række[1::2]:
#             lige=lige+i
#     return lige+ulige

# print(checkerboard_sum(A))


##################### OPGAVE 6 #####################

# def collatz_conjecture(n):
#     counter=0
#     if n <=0:
#         print("Something went wrong")
#     while n!=1:
#         if n%2==0:
#             n=n/2
#             counter+=1
#         else:
#             n=3*n+1
#             counter+=1
#     print(n)
#     return counter

# print(collatz_conjecture(15))

##################### OPGAVE 7 #####################




##################### OPGAVE 8 #####################

# phonebook = {'Liv': ['55511112', '18777890'] ,
#             'Mads': ['27274445', '48533336'],
#             'Steve': ['45455555', '25455525']}
# second_phonebook = {'Anna': ['89577772'] ,
#                     'Steve': ['25257755', '25455525'],
#                     'Mads': ['48533336', '27274445']}

# def phonebook_merger(book_1,book_2):
#     for i in range(0,len(book_2)):
#         for key in book_2:
#             if key not in book_1:
#                 book_1[key]=[]
#             for number in book_2[key]:
#                 if number not in book_1[key]:
#                     book_1[key].append(number)

# phonebook_merger(phonebook,second_phonebook)




