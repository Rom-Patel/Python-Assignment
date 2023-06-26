a = 5
b = 10
print("Operators:")

print("\nArithmetic Operator")
plus =  a+b
minus = a-b
multiply = a*b
divide = b/a
floor_div=  b//a
exponent = a**2
print("Addition: ",plus)
print("Subtraction: ",minus)
print("Multiplication: ",multiply)
print("Division: ",divide)
print("Floor Division",floor_div)
print("Exponent: ",exponent)

print("\nAssignment Operator")
c = 5
d = 10
a+=4
b*=5
c//=5
d/=2
print("Plus equal to: ",a)
print("Multiply equal to: ",b)
print("Floor Division equal to: ",c)
print("Division equal to: ",d)

print("\nComparison Operator")
a = 5
b = 10
c = a>b
d = a<b
e = a!=b
f = a==b
print("a greater than b: ",c)
print("a less than b: ",d)
print("a not equal to b: ",e)
print("a equal to b: ",f)

print("\nLogical Operator")
m = True
n = False
print("m and n: ",m and n)
print("m or n: ",m or n)
print("not m: ",not m)

print("\nBitwise Operator")
a = 5
b = 10
Or = a|b
And = a&b
Xor = a^b
shl = a<<3
shr = b>>2
print("a OR b: ",Or)
print("a AND b: ",And)
print("a XOR b: ",Xor)
print("Shift a to left by 3: ",shl)
print("Shift b to right by 2: ",shr)

print("\nIdentity Operator")
a = 5
m = a is 5
print("a is 5: ",m)
n = a is not 5
print("a is not 5: ",n)

print("\nMembership Operator")
f = "Hello"
g = "l" in f
h = "h" in f
i = "w" in f
j = "H" in f
print("l is in string 'Hello': ",g)
print("h is in string 'Hello': ",h)
print("w is in string 'Hello': ",i)
print("H is in string 'Hello': ",j)
