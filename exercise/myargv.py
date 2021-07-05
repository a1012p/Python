import sys

args = sys.argv[1:]
str="+".join(args)
print(eval(str))

sum = 0
for i in args:
    sum += int(i)
print(sum)