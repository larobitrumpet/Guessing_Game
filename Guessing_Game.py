import random
roun = 0
p1Score = 0
p2Score = 0
def Score(n):
   if n == 0:
      print("It was a tie")
   else:
      print("P" + str(n) + "wins!")
      print("")
      print("               Score:")
      print("P1 Score: " + str(p1Score) + "  |  P2 Score: " + str(p2Score))
print("In this game, two players guess a number between 0 and 9.")
print("Who ever guesses closest gets a point.")
print("")
c = raw_input("Press 'enter' to continue")
for roun in range(0, 6):
   print("")
   print("-----------------------------------")
   print("")
   print("Round " + str(roun))
   print("")
   p1 = input("P1 guess number: ")
   p2 = input("P2 guess number: ")
   print("")
   num = int(10 * random.random())
   print("The number was " + str(num))
   print("")
   if abs(num - p1) < abs(num - p2):
      p1Score = p1Score + 1
      Score(1)
   elif abs(num - p1) > abs(num - p2):
      p2Score = p2Score + 1
      Score(2)
   else:
      p1Score = p1Score + 1
      p2Score = p2Score + 1
      Score(0)
   print("")
   c = raw_input("Press 'enter' to continue")
print("")
print("-----------------------------------")
print("")
if p1Score > p2Score:
   Score(1)
elif p1Score < p2Score:
   Score(2)
else:
   Score(0)
print("")
print("Thank you for playing!")
print("")
e = raw_input("Press 'enter' to exit")
