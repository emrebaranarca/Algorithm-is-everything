# 9x+3y+z=13
# -6x+8z=2
# 2x+5y-z=6

# solution with Gauss-Seidel

# x=(13-3*y-z)/9
# y=(6+z-2*x)/5
# z=(2+6*x)/8

# [9 3 1]
# [-6 0 8]     
# [2 5 -1]
#..
# [9 3 1]
# [2 5 -1]
# [-6 0 8]



# x,y,z=0,0,0

# for i in range(30):
#     x=(13-3*y-z)/9
#     y=(6+z-2*x)/5
#     z=(2+6*x)/8

# print(x,y,z)




# x+y+6z=8
# x+5y-z=5
# 4x+2y-2z=4

# [1 1 6]
# [1 5 -1]     
# [4 2 -2]
#..convert
# [4 2 -2 | 4]
# [1 5 -1 | 5]
# [1 1 6 | 8 ]

# x=(4-2*y+2*z)/4
# y=(5+z-x)/5
# z=(8-x-y)/6

# accept relative error= %0
count=0
x,y,z=0,0,0
relativeError=1
tol=0
while(relativeError > tol):
    tempX=x
    tempY=y
    tempZ=z
    count+=1
    x=(4-2*y+2*z)/4
    y=(5+z-x)/5
    z=(8-x-y)/6

    relativeErrorX=abs((x-tempX)/x)*100
    relativeErrorY=abs((x-tempY)/y)*100
    relativeErrorZ=abs((x-tempZ)/z)*100

    relativeError=max(relativeErrorX,relativeErrorY,relativeErrorZ)


print(x,y,z)
print(count)












