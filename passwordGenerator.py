# generate a password with length "passlen" with no duplicate characters in the password

# importing library to call random.sample that takes allowed caracters as string and also the length of generated string
import random
# specifying allowed caracters in the password
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# the length of the password
passlen = 8
# Randomly take unique characters from 's' and join them to form a string. saving them into string p - the final password
# "".join(...): This method concatenates the list of characters into a single string
p =  "".join(random.sample(s,passlen ))
print p
