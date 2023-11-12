year=float(input("Give me the year : "))
if( year%400==0 ):
        print("This is a leap year. ")

else:
 if year%4==0:
   if year%100==0:
     print("this is a not leap year")
   else:
      print("This is a leap year.")
 else:
    print("This is not one of the leap years.")