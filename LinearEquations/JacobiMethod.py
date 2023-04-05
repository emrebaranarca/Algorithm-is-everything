# x+y+6z=8
# x+5y-z=5
# 4x+2y-2z=4

# [1 1 6 | 8]
# [1 5 -1| 5]     
# [4 2 -2| 4]

# [4 2 -2| 4]
# [1 5 -1| 5]     
# [1 1 6 | 8]

# x=(4-2*y+2*z)/4
# y=(5+z-x)/5
# z=(8-x-y)/6

# accept relative error= %0

count=0
relativeError=1
tol=0
x,y,z=0,0,0
while(relativeError > tol):
    tempX=x
    tempY=y
    tempZ=z
    x,y,z= (4-2*y+2*z)/4, (5+z-x)/5, (8-x-y)/6
    count+=1
    relativeErrorX=abs((x-tempX)/x)*100
    relativeErrorY=abs((x-tempY)/y)*100
    relativeErrorZ=abs((x-tempZ)/z)*100

    relativeError=max(relativeErrorX,relativeErrorY,relativeErrorZ)

print(x,y,z)
print(count)

