# Q1 print fibonacci series
n=10 # number of terms
a=0
b=1
for i in range(n):
    print(a, end=" ")
    temp=a+b
    a=b
    b=temp
    
# Q2 fibonacci nTH term
# method1
n=7 
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(b)
else:
    for i in range(3,n+1):
        temp=a+b
        a=b
        b=temp
    print(b)
    
# Method 2
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(7))

# Q3 check prime number
n=int(input("enter the number"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime number")
else:
    print("composit number")

# Q3 all prime number is range
start=10
end=30

for num in range(start,end+1):
    if num>1:
        count=0
        for i in range(1,num+1):
            if num%i==0:
                count+=1
        if count==2:
            print(num,end=" ")
            