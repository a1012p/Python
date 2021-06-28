try:
    a = [1,2]
    print(a[2])
    4 / 0
    f = open("write.txt",'r')
except IndexError as i:
    print(i)
except ZeroDivisionError as z:
    print(z)
except FileNotFoundError as f:
    print(f)