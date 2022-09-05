a=()
b=()
while a!=0 and b!=0:
    a=float(input('number 1:'))
    b=float(input('number 2:'))
    if a>b:
        print(a)
    if b>a:
        print(b)
    if a==0 and b==0:
        break
    