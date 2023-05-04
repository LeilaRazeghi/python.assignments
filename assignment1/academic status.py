scoreA=float(input("enter scoreA:"))
scoreB=float(input("enter scoreB:"))
scoreC=float(input("enter scoreC:"))

average=(scoreA+scoreB+scoreC)/3
print(average)

if scoreA<0 or scoreB<0 or scoreC<0 or scoreA>20 or scoreB>20 or scoreC>20:
     print("invalid score")
else:
  if average>=17:
     print("you done great")

  elif average<17 and average>=12:
     print("your status is normal")

  elif average<12:
      print("you are failed")
     
