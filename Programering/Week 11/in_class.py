# class scorekeeping:
#     def __init__(self):
#         self.highscore=("",0)
#         self.second_highscore=("No-one",0)
#     def add_score(self, name, score):
#         if score>=self.highscore[1] and score is not self.highscore[1]:
#             self.second_highscore=self.highscore
#             self.highscore=(name, score)
#             return
#         if score>=self.second_highscore[1] and score is not self.highscore[1]:
#             self.second_highscore=(name, score)
#     def print(self):
#         print("!!HIGHSCORES!!:")
#         print(f"Highscore:            {self.highscore}")
#         print(f"Second highest score: {self.second_highscore}")
#     def __add__(self,other):
#         if self.highscore>other.highscore>self.second_highscore:
#             self.second_highscore=other.highscore
#         if other.highscore>self.highscore>other.second_highscore:
#             self.second_highscore=self.highscore
#             self.highscore=other.highscore


            


# score=scorekeeping()
# score.add_score("John", 10)
# score.print()
# score.add_score("Dennis", 30)
# score.print()
# score.add_score("Jørgen", 5)
# score.print()
# score.add_score("Jørgen", 40)
# score.print()
# print("\n")
# score2=scorekeeping()
# score2.add_score("Dennis", 79)
# score2.print()
# score2.add_score("Jørgen", 5)
# score2.print()
# score2.add_score("Dennis", 79)
# score2.print()


# # score3=scorekeeping()
# # score3=score+score2
# # score.print()



# # Opgave 11.3

# class IntegerMod4:
#     def __init__(self, tal):
#         self.tal=tal
#         self.udregn=self.tal//4
#     def __str__(self) -> str:
#         return f"{self.udregn}"
#     def __add__(self, other):
#         resplus=self.udregn+other.udregn
#         return resplus
#     def __mul__(self, other):
#         resgange=self.udregn*other.udregn
#         return resgange

        



# e0 = IntegerMod4(0)
# e1 = IntegerMod4(5)
# e2 = IntegerMod4(2)
# e3 = IntegerMod4(3)
# Z4 = [e0, e1, e2, e3]

# print("-----------+-----------")
# for i in Z4:
#     for j in Z4:
#         print(f'{i} + {j} = {i + j}')
#     print()
# print("-----------*-----------")
# for i in Z4:
#     for j in Z4:
#         print(f'{i} * {j} = {i * j}')
#     print()


###### PROBLEM SOLVING ############

class BankAccount():
    def __init__(self, bal):
        self.balance=bal
    def deposit(self, amount):
        self.balance=self.balance+amount
    def withdraw(self, amount):
        if (self.balance-amount)>0:
            self.balance=self.balance-amount
            return amount
        else:
            return 0
    def get_balance(self):
        return self.balance


# my_account = BankAccount(1000)
# print(my_account.get_balance())
# print(my_account.deposit(500))
# print(my_account.get_balance())
# print(my_account.withdraw(200))
# print(my_account.get_balance())
# print(my_account.withdraw(2000))
# print(my_account.get_balance())

class OverdraftAccount(BankAccount):
    def __init__(self, bal, limit):
        self.balance=bal
        self.limit=0-limit
    def withdraw(self, amount):
        if (self.balance-amount)>self.limit:
            self.balance=self.balance-amount
            return amount
        else:
            return 0


my_account = OverdraftAccount(0,500)
print(my_account.get_balance())
print(my_account.deposit(1000))
print(my_account.get_balance())
print(my_account.withdraw(1300))
print(my_account.get_balance())
print(my_account.withdraw(500))
print(my_account.get_balance())  