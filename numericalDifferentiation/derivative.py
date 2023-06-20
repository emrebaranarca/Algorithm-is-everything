# x^3-2x^2+x  calculate numberical differentitation

def f(x):
    return (x**3-2*x**2+x)

point=1
h=0.001

deriative=(f(point+h)-f(point))/h
#deriative=(f(point)-f(point-h))/h
secondDeriative=(f(point)-2*f(point-h)+f(point-2*h))/h**2

print(deriative)
print(secondDeriative)

