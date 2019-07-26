n=int(input())
k=int(input())
sum=0
j=0
for i in range(1,n+1):
    sum=sum+i
    j=j+1 
    if(j==k):
        break
print(sum)
