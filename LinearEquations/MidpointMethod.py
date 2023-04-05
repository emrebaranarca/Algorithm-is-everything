MAX_ITER=250
def g(x,a,b,c):
    return a*x**2-3*x-4

def f(func,x,a,b,c):
    return func(x,a,b,c)


a=int(input("ax^2+bx+c | a:"))
b=int(input("ax^2+bx+c | b:"))
c=int(input("ax^2+bx+c | c:"))


x1=int(input("first estimation for first root:"))
x2=int(input("second estimation for second root:"))

if(f(g,x1,a,b,c)*f(g,x2,a,b,c)==0):
    if(f(g,x1,a,b,c)==0):
        print("root is",x1)
    if(f(g,x2,a,b,c)==0):
        print("root is",x2)
    if(f(g,x1,a,b,c)==0 and f(g,x2,a,b,c)==0):
        print("roots are",x1,"and",x2)

elif(f(g,x1,a,b,c)*f(g,x2,a,b,c)>0):
    print("there isn't root in your between of estimates.")

else:
    for i in range(MAX_ITER):
        midPoint=(x1+x2)/2
        if(f(g,midPoint,a,b,c)==0):
            print("root is",midPoint)
            break
        elif(f(g,midPoint,a,b,c)*f(g,x1,a,b,c)<0):
            x2=midPoint
        else:
            x1=midPoint


