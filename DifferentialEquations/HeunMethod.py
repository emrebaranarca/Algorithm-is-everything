# dy/dx = -y/x
# y(4) = 0.75
# y(7) = ?

def f(x,y):
    return (-y/x)
a=4
b=7
y=0.75
h=0.1                    
n=int((b-a)/h)   

for i in range(n):
    y0 = y + f(a,y) * h
    y +=(f(a,y)+f(a+h,y0))*h/2
    a += h
print(y)                 