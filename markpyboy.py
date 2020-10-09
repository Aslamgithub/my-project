print('......................................................................')
print('......................................................................')
A= int(input ("enter Maths marks:"))
B= int(input ("enter Tamil marks:"))
C= int(input ("enter Arabic marks:"))
Total=(A+B+C)
Average=(A+B+C)/3
print "Total=",Total
print "Average=",Average
if (Total>=150):
    print('congatulation you got great passed')
elif (Total>=100):
    print('congatulation you got passed') 
else:
    print ('sorry you are fail')
if (Average>50):
    print('great average')
elif (Average >30.33):
    print("nice average")
else:
    print("average should be improved")
