residentArr = [10,3,2,5,7,1]

copyResidentArr = residentArr.copy()

copyResidentArr.sort(reverse=True)

length = len(residentArr)

tot = 0

for n in copyResidentArr:
    tot += n
    x = residentArr.index(n)
    p = x-1
    q = x+1
    if p >= 0:
        if residentArr[p] in copyResidentArr:     
            copyResidentArr.remove(residentArr[p])
    if q <= (length - 1):
        if residentArr[q] in copyResidentArr:
            copyResidentArr.remove(residentArr[q])


print(tot)
