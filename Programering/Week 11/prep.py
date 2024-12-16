# class NameTracker:

#     def __init__(self):
#         self.longest = ''
#         self.shortest = ''
    
#     def add(self, name):
#         if len(name) > len(self.longest):
#             self.longest = name
#         if len(name) < len(self.shortest) or self.shortest=='':
#             self.shortest = name
    
#     def print(self):
#         print('Names tracked so far')
#         print('  Longest :', self.longest)
#         print('  Shortest:', self.shortest)


# # girls = NameTracker()
# # girls.add('Mary')
# # girls.print()
# # girls.add('Augusta')
# # girls.print()
# # girls.add('Josephine')
# # girls.print()
# # girls.add('Pippilotta Rullegardinia')
# # girls.print()



# class CarefulNameTracker(NameTracker):

#     def __init__(self, forbidden_characters):
#         self.forbidden_characters = forbidden_characters
#         super().__init__()
    
#     def add(self, name):
#         valid = True
#         for char in self.forbidden_characters:
#             if char in name:
#                 valid = False
#         if valid:
#             super().add(name)

#     def print_lengths(self, name):
#         print('Lengths of names tracked so far')
#         print('  Longest :', len(self.longest))
#         print('  Shortest:', len(self.shortest))            
            
# girls_first = NameTracker()
# girls_second = CarefulNameTracker([' ', '-', '_', '&'])

# for name in ['Mary', 'Augusta', 'Josephine', 'Pippilotta Rullegardinia', 'I-I', 'Pippi', 'Pippilotta Rullegardinia', 'Pippi_Longstocking']:
#     girls_first.add(name)
#     girls_second.add(name)

# girls_first.print()
# print()
# girls_second.print()
# # print(girls_second.forbidden_characters)

# # print(girls_second.shortest)
# # print(girls_second.longest)

# girls_test = NameTracker()
# girls_test.add('Mary')
# girls_test.print_lengths()



class Time:
    
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def increment_hours(self, ):
        self.hours += 1
        if self.hours == 24:
            self.hours = 0
    
    def increment_minutes(self, ):
        self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.increment_hours()
    
    #def print(self):
       # print(f"{self.hours:02}:{self.minutes:02}")

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __eq__(self, other):
        return (self.hours == other.hours) and (self.minutes == other.minutes)

    def __add__(self, other):
        minutes = self.minutes + other.minutes
        hours = self.hours + other.hours
        if minutes >= 60:
            minutes = minutes - 60
            hours = hours + 1
        if hours >= 24:
            hours = hours - 24
        return Time(hours, minutes)

my_time = Time(13, 55)


first_time = Time(13, 45)
second_time = Time(13, 45)
third_time = Time(8, 15)
# print(first_time==first_time)
# print(first_time==second_time)
# print(second_time==second_time)
# print(first_time==third_time)

print(first_time+first_time)




class Number:
    def __init__(self, nr):
        self.value = nr
    def __add__(self, other):
        return Number(self.value + other.value)
a = Number(5)
b = Number(6)
c = a + b
print(c.value)