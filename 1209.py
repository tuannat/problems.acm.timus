from math import sqrt

def check(x):
	x = (sqrt(8*x -7) - 1)/2
	return "1" if x == int(x) else "0"
	
n = int(raw_input())
a = []
for i in range(n):
	x = int(raw_input())
	a.append(x)
	
print " ".join([check(x_) for x_ in a])
	