#program which takes student score util entering 'exit'and finally calculates average

count_score=0
sum_score=0


while True:
        score=input("enter student's score or enter eixt to finish:")
        
        if score=="exit":
                break

        elif float(score)<0 or float(score)>20:
                print("invalid score")
        else:
                count_score=count_score+1
                sum_score=sum_score+float(score)

average=sum_score/count_score
print("your average:", average)