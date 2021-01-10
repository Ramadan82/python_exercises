
year = int(input("Which year do you want to check? "))



# if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#   print("leap year")
# elif year % 4 != 0:
#   print("Not leap year")
# elif year % 100 != 0:
#   print("leap year")
# elif year % 400 != 0:
#   print("Not leap year")
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("leap year")
else:
  print("Not leap year")
