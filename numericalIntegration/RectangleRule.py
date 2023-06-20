def f(x):
    return (2.47857+2.35929*x+1.86071*x**2)

a,b=0,5
n=50
delta=(b-a)/n
area=0
for i in range(n):
    area+= delta*f(a)  
    a+=delta

print(area)  
 