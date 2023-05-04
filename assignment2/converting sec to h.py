
# converting second to hour program (sec to 00:00:00)

sec=int(input("enter the second:"))

sec_hr=sec//3600
sec_min=(sec%3600)//60
second=(sec%3600)%60

print("sec_hr:, sec_min:, second:")