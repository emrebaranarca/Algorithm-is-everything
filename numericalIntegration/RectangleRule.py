def f(x):
    return 1/x

a,b=0,1
n=8
delta=(b-a)/n
area=0
for i in range(n):
    area+= delta*f(a)  
    a+=delta

print(area)  
 