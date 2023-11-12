print("Welcomn to the pizza hut,")
need=input("Do you need a pizza? y or n!")
size=input("Which size of pizza do you need? s,m or l?")
want_pepperoni=input("Do you need pepperoni? y/n ")
want_cheese=input("Need cheese ,Dont forget to ask! y/n")
bill=0
if need=="y":
 if size=="s":
  bill +=15
 elif size=="m":
  bill +=18
 elif size=="l":
  bill +=20
 if want_pepperoni=="y":
  if size=="s":
   bill +=2
  else:
   bill +=3
 if want_cheese=="y":
  if size=="s":
   bill +=1
 else:
  bill +=2
 

else:
 print("Okk plz get out.")
print(f"Your total bill = ${bill} doller")

