x = '123456789'
print('global variable: ' + x)
def myfunc():
  x = 'qwertyuio'
myfunc()
print('local variable: ' + x)
# output: 
#global variable: 123456789
# local variable: qwertyuio
