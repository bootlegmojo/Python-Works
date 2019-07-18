usin=int(input("Type a number"))

print(usin)

newlist = []
for x in range(1,usin+1):
    newlist.append(x)

print(newlist)

n=0

for i in newlist:
    newlist[n] = (i * 10)
    n+=1
print(newlist)
