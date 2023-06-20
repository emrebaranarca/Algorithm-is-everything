MAX_ITER=250

def f(x,a,b,c):
    return a*x**2+b*x+c

def f_derivative(x,a,b,c):
    return 2*a*x + b

a=int(input("ax^2+bx+c | a:"))
b=int(input("ax^2+bx+c | b:"))
c=int(input("ax^2+bx+c | c:"))


x1=int(input("first estimation for first root:"))

for i in range(MAX_ITER):
    x2=x1-f(x1,a,b,c)/f_derivative(x1,a,b,c)
    x1=x2

print("root is",x1)