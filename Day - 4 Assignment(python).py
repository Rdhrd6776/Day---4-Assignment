Q1. Python program to print Highest Common Factor (HCF) of two numbers
Example : Take values according to you

#ANS

x = 100
y = 200
if x > y:
   x, y = y, x
for i in range(1,x+1):
  if x%i == 0 and y%i == 0:
    hcf = i

print("HCF of", x, "and", y, "is:", hcf)

Q2. What will be the output of the following Python code?

i=0
def change(i):
    i=i+1
    return i
change(1)
print(i)

a) 1
b) Nothing is displayed
c) 0
d) An exception is thrown

#ANS

c

3. What will be the output of the following Python code?

def a(b):
    b = b + [5]
    c = [1, 2, 3, 4]
a(c)
print(len(c))

#ANS

error 
c is not defined


4. What will be the output of the following Python code?

a=10
b=20
def change():
    global b
    a=45
    b=56
change()
print(a)
print(b)

a) 10 56
b) 45 56
c) 10 20
d) Syntax Error

#ANS
a


5. What will be the output of the following Python code?

def change(i = 1, j = 2):
    i = i + j
    j = j + 1
    print(i, j)
change(j = 1, i = 2)

a) An exception is thrown because of conflicting values
b) 1 2
c) 3 3
d) 3 2

#ANS

d