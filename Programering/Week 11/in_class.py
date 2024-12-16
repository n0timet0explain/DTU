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



# Opgave 11.3

class IntegerMod4:
    def __init__(self) -> None:
        