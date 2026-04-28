# rev a string
s = "hello"
rev = ""
for ch in s:
    rev=ch+rev
print(rev)

# rev a number
# method1
a=1223
while a>0:
    print(a%10)
    a=a//10
#method2
n=1234
rev=0
while n>0:
    a=n%10
    rev=rev*10+a
    n=n//10
print(rev)

#method3
n=1234
s=str(n)
rev=""
for i in s:
    rev=i+rev
print(int(rev))

#negative number reverse
n = -123
sign = -1 if n < 0 else 1
n = abs(n)

rev = 0
while n > 0:
    rev = rev * 10 + (n % 10)
    n = n // 10

print(sign * rev)

# palindrome
n=int(input("enter the number"))
rev=0
temp=n
while n>0:
    a=n%10
    rev=rev*10+a
    n=n//10
if temp==rev:
    print("number is palindrome")
else:
    print("Not palindrome")
    
#eg.
a="nikjhil"
print(a[::-1])

# palindrome string
n=input("string")
rev=""
temp=n
for i in n:
    rev=i+rev
if rev==temp:
    print("palindrome")
else:
    print("Not palindrome")
    
# print last 2  number
n=12234
print(str(n)[-2:])
# print first 3 numbers
print(str(n)[:3])
# skip digit
print(str(n)[::2])



# swap two numbers without temp variable
# method1
a=5
b=10
a,b=b,a
print(a,b)
# Method 2
a=a+b
b=a-b
a=a-b
print(a,b)

