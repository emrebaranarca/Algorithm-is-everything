# f(x)=1/x

def f(x):
    return (1/x)

a,b = 0,5
n=50
delta=(b-a)/n
area=0
for i in range(n):
    area+= delta*(f(a)+f(a+delta))/2  
    a+=delta

print(area)   