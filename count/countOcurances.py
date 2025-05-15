s = "Green tree"
s.count("e")
#output: 4

#or:
"Green tree".count(e)

#count in sub-string
#If the second (start) and third (end) arguments are specified, count() only searches within the substring [start:end].

print(s.count('e', 1, 4))
# output: 2

print(s[1:4])
# output: ree


