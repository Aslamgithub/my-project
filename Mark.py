A= int(input ("enter Maths marks:"))
B= int(input ("enter English marks:"))
C= int(input ("enter Arabic marks:"))
Total=(A+B+C)
Average=(A+B+C)/3
print "Total=",Total
print "Average=",Average
if (Total>=150):
    print('congatulation you got first class')
elif (Total>=100):
    print('congatulation you got second class') 
else:
    print ('sorry you are fail')
if (Average>50):
    print('great average')
elif (Average >30.33):
    print("nice average")
else:
    print("average should be improved")
