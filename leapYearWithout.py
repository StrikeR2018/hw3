# Name: Mingxuan Li
# Class: CS362
# Description:check if user input is a leap year
# Due: 04/10/2021


year = int(input("Specify a year: "))


if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(year, "is a leap year!")
       else:
           print(year, "is not a leap year!")
   else:
       print(year, "is a leap year!")
else:
   print(year, "is not a leap year!")
   
