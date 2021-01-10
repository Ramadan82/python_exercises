#  Don't change the code below 
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#  Don't change the code above 

#Write your code below this line 

combined_name = name1 + name2
name = combined_name.lower()
# true = name.count("t") + name.count("r") + name.count("u") + name.count("e") 
# love = name.count("l") + name.count("o") + name.count("v") + name.count("e")  
# true = str(true)
# love = str(love)
# score = int(true + love)
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
true = t + r + u + e
l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
love = l + o + v + e
score = int(str(true) + str(love))
#score = int(score)
if (score < 10) or (score > 90):
  print(f"youre score is {score} you go together like coke and mentos")
elif (score >= 40) and (score <= 50):
  print(f"your score is {score} you are alright together.")
else:
  print(f"your score is {score}")