n=int(input("enter your number:"))
for i in range(2,n):
    if(n%i)==0:
        print("number is not prime")
        break
    else:
        print("number is a prime")
num=int(input("enter your number:"))
sum=0
while(i<n):
 sum+=i
 i+=1
 print(sum)