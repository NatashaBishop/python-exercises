# compute factorial of a given numbers. Results r printed on a single line, comma-separated. 
#  input data supplied  is a console input

# For Python 3.4+, use fact(x) from the new statistics module to calculate the facorial:
from statistics import fact
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))
