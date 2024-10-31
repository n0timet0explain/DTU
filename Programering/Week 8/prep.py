# book = {"Title": "The Hitchhiker's Guide to the Galaxy", "Author": "Douglas Adams", "Genre": "Science fiction"}
# print(book)
# print(type(book))



# print(book["Title"])
# print(book["Author"])
# print(book["Genre"])



# city = {"name": "Mumbai", 
#         "population": 21673000, 
#         "gps_coordinates": ["19.07'53.2", "72.54'51.0"]}

# print(type(city["gps_coordinates"]))



# timeline = {1982: "Started school", 
#             1992: "Started high school", 
#             2002: "Started university"}
# print(timeline[1982])



# lengths = {0.16: "Standard smartphone length",
#            1.71: "Average male height",
#            1.59: "Average female height",
#            1.90: "Standard car height",
#            2.00: "Standard door height"}

# print(lengths[1.71])

# my_dictionary = {"first": 5, "second": 10, "first": 15, "second": 20}

# print(my_dictionary)



# try_this = {"1": "first", 1: "one", 1.0: "uno"}
# print(try_this)



# person = {}
# print(person)  
# person["first_name"] = "Alice"
# person["last_name"] = "Baker"
# print(person)  
# person["age"] = 34
# person["children"] = ["Emma", "Maria", "Jacob"]
# print(person)  



# person = {}
# person["first_name"] = "Alice"
# print(person)
# person["first_name"] = "Josefine"
# print(person)



# person = {"first_name": "Alice", "last_name": "Baker", "age": 34}
# print(person)
# del person['last_name']
# print(person)



# popular_names = {2023: "Olivia", 2018: "Emma", 2013: "Sophia", 2010: "Isabella"}
# test = popular_names
# print(test)
# popular_names[2007] = "Emily"
# print(test)



# def update_dict(dictionary, key, value):
#     dictionary[key] = value

# grades = {"Josefine": 12, "Jakob": 10, "Alice": 7, "Morten": 10}
# print(grades)
# update_dict(grades, "Alice", 12)  
# print(grades)



# a = {"first": 1008, "second": 2123}
# b = a
# a = {"first": 897, "second": 426}
# print(b)



# my_dict = { "a" : 100 , "b" : 200 }

# print("a" in my_dict)
# print("c" in my_dict)   
# print(100 in my_dict)
# print(200 in my_dict)



# letter_frequency = {"a": 399, "e": 20, "n": 120}

# for letter in "abcdefghijklmnopqrstuvwxyz":
#     if letter in letter_frequency:
#         print(f'{letter}:{letter_frequency[letter]}')
#     else:
#         print(f'{letter} not in letter_frequency')
    


# country_capitals = {"Denmark": "Copenhagen", 
#             "Germany": "Berlin", 
#             "France": "Paris", 
#             "Sweden": "Stockholm"}

# for something in country_capitals:
#     print(something)



# country_capitals = {"Denmark": "Copenhagen", 
#             "Germany": "Berlin", 
#             "France": "Paris", 
#             "Sweden": "Stockholm"}

# for country in country_capitals:
#     print(country_capitals[country])



# point = (2, 8)
# print(point)
# print(point[0])
# print(point[1])
# print(type(point))



# point = 2, 8
# print(point)
# print(point[0])
# print(point[1])
# print(type(point))



# sandwich = ("bacon", "lettuce", "tomato")
# print(sandwich) 
# print(sandwich[1])
# print(type(sandwich))



# something = 15, 'last name', 27.5, True
# print(something)
# print(something[2])
# print(something[1:])
# print(type(something))
# print(type(something[1]))
# print(type(something[1:2]))



# something = (15)
# print(type(something))

# something = (15,)
# print(type(something))

# something = 15,
# print(type(something))



# fruits = ("banana", "apple", "watermelon", "pineapple")
# print(fruits[0])
# fruits[0] = "pear"  



# fruits = ("banana", "apple", "watermelon", "pineapple")
# print(fruits)
# fruits = ("pear",) + fruits[1:]
# print(fruits)



# fruits = ("banana", "apple", "watermelon", "pineapple")

# for i in range(len(fruits)):
#     print(fruits[i])

# for fruit in fruits:
#     print(fruit)



# town, street, number = "Holte", "Hovedgaden", 10
# print(town)
# print(street)
# print(number)



# a, b, c = [10, 100, 1000]
# print(a, b, c)



a, b, c, d = 19, 29, 128, 134

print(type(a))



# def calc_min_and_max(numbers):
#     min_val = min(numbers)
#     max_val = max(numbers)
#     return min_val, max_val 

# numbers = [28, 34, 50, 97, 76]
# something = calc_min_and_max(numbers)
# print(something)
# print(type(something))

# min_val, max_val = calc_min_and_max(numbers)
# print(min_val)
# print(max_val)



# students = [("Alice", 90), ("Bob", 92), ("Charlie", 85)]
# for student in students:
#     name, score = student
#     if score > 90:
#         print(name)