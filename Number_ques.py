# Q1 find Factorial
n=int(input("enter the number"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
# method 2 (using Recursion)
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5))

# Q2 Find largest 0f 3 numbers
a=5
b=10
c=23
largest=a
if b>largest:
    largest=b
if c>largest:
    largest=c
print(largest) 

# Q3 find the smallest
a=5
b=1
c=88
if a<=b and a<=c:
    print("a is smallest")
elif b<=a and b<=c:
    print("b is smallest")
else:
    print(" c is smallest")

# Q4 second largest number is array
arr=[23,34,55,66]
first=1
second=1
for num in arr:
    if num>first:
        second=first
        first=num
    elif num>second and num!=first:
        second=num
print(second)

# Q5 first largest digit in a number

a=12345
max=0
while a>0:
    digit=a%10
    if digit>max:
      max=digit
    a=a//10
print(max)
    
# Q6 count number of digit in a number
n=1234534211
count=0
while n>0:
    count+=1
    n=n//10
print(count)

# Q7 sum of digit of a number
#method 1
a=1234
s=0
while a>0:
    digit=a%10
    s=s+digit
    a=a//10
print(s)
#method2 (using string)
n = 1234
s = 0
for ch in str(abs(n)):
    s = s + int(ch)
print(s)

# Q8 first smallest digit in a number
n=3222321
min=9
if n==0:
    min=0
else:
    while n>0:
        digit=n%10
        if digit < min:
            min=digit
        n=n//10
print(min)
# method 2 using slicing
n=123345
s=str(n)
min=9
for i in s:
    if int(i)<min:
        min=int(i)
print(min)


# Q9 count vowels and consonants
s="hello world"
vowel=0
cons=0
for i in s:
    if i in "aeiouAEIOU":
        vowel+=1
    elif i.isalpha():
        cons+=1
print(vowel)
print(cons)

# Q10- find len of string without len()
s="python"
count=0
for i in s:
    count+=1
print(count)