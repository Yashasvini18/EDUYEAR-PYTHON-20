print("Enter the range ")
n= int(input())
m= int(input())
for i in range(n , m+1):
    if((i%7==0) and (i%5==0)):
        print(i)
