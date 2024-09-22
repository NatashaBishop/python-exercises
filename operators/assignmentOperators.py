# inspired by https://www.geeksforgeeks.org/python-operators/
'''
=	Assign the value of the right side of the expression to the left side operand 	x = y + z
+=	Add AND: Add right-side operand with left-side operand and then assign to left operand	a+=b     a=a+b
-=	Subtract AND: Subtract right operand from left operand and then assign to left operand	a-=b     a=a-b
*=	Multiply AND: Multiply right operand with left operand and then assign to left operand	a*=b     a=a*b
/=	Divide AND: Divide left operand with right operand and then assign to left operand	a/=b     a=a/b
%=	Modulus AND: Takes modulus using left and right operands and assign the result to left operand	a%=b     a=a%b
//=	Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand	a//=b     a=a//b
**=	Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand	a**=b     a=a**b
&=	Performs Bitwise AND on operands and assign value to left operand	a&=b     a=a&b
|=	Performs Bitwise OR on operands and assign value to left operand	a|=b     a=a|b
^=	Performs Bitwise xOR on operands and assign value to left operand	a^=b     a=a^b
>>=	Performs Bitwise right shift on operands and assign value to left operand	a>>=b     a=a>>b
<<=	Performs Bitwise left shift on operands and assign value to left operand	a <<= b     a= a << b

'''
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a # equivalent to b = b << a
print(b)


#Output
# 10
# 20
# 10
# 100
# 102400

# example 4 b <<= a
b = 5   # 5 in binary is 101
a = 2

b <<= a # b becomes b << a, which is 5 << 2
# 5 in binary is 101. Shifting left by 2 positions: 101 becomes 10100, which is 20 in decimal. Thus, after b <<= a, the value of b will be 20.

# Example: Let's take 5 in binary (101):

#    In binary: 101 (which is 5 in decimal)
#    Shift it left by 1 position (<< 1):
#       The 101 becomes 1010 (which is 10 in decimal).
# Original:    101   (this is 5 in binary)
# Shift left:  1010  (this is 10 in binary)



