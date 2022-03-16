import math
a, b, c = map(int, input().split())
x = (a) / 2
y = (b) / 2
z = (c) / 2
d1 = float(x) - int(x)
d2 = float(y) - int(y)
d3 = float(z) - int(z)
if abs(d1) > 0 and abs(d2) > 0 and abs(d3) > 0:
	print('WIN')
elif d1  == 0 and d2 == 0 and d3 == 0:
    print('WIN')
else:
    print('FAIL')