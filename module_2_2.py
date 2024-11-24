first = f = int(input())
second = s = int(input())
third= t = int(input())
if f==s and f==t:
    print(3)
elif f==s or f==t or s==t:
    print(2)
else:
    print(0)