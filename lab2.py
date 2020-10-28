a = float(input('1 катет 1 трикутника(додатнє число): '))
b = float(input('2 катет 1 трикутника(додатнє число): '))
c = float(input('1 катет 2 трикутника(додатнє число): '))
d = float(input('2 катет 2 трикутника(додатнє число): '))

Div1 = a/c 
Div2 = b/d
Div3 = a/d
Div4 = b/c

if Div1 == Div2:
    res = 1
else:
    if Div3 == Div4:
        res = 1
    else:
        res = 0

print(res)