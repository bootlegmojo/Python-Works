elemnum = int(input("Enter number of elements : ")) 
  
numlist = list(map(int,input("Enter the numbers followed by a space : ").strip().split()))[:elemnum] 
  
print("\nYour Numbers", numlist) 

answer = []

for n in numlist:
    if n not in answer:
        answer.append(n)

print("Sum of non repeated numbers is: ", sum(answer))
