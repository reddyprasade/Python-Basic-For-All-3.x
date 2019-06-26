year = int(input("Enter a Year:"))
#year=2018
if(year%4)==0:
  if (year%100)==0:
    if (year%400)==0:
      print("{0} is a Leap Year".format(year))
    else:
      print("{0}  is a not Leap Year".format(year))
  else:
    print("{0} is a Leap Year".format(year))
else:
  print("{0}  is a not Leap Year".format(year))
