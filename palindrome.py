n=int(input())
rev=0
r=0
a=n
while n!=0:
   r=n%10
   rev=rev*10+r
   n=n//10
if(rev==a):
  print("yes")
else:
  print("no")
