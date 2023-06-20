# dy/dx = -y/x
# y(4) = 0.75
# y(7) = ?

def f(x,y):
    return (-y/x)

a = 4
y = 0.75

b=7

h = 0.1 
                   
n = int((b-a)/h)           

for i in range(n):
    y +=f(a,y)*h
    a += h
print(y)                 