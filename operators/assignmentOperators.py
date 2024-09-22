# inspired by https://www.geeksforgeeks.org/python-operators/
''
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
''
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





