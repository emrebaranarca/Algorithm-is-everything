# y = a0 + a1*xi + a2*xi^2 + e

xi=[-3,-1,1,3]
yi=[15,5,1,5]

n=len(xi)
xi_sum=sum(xi)
xi_sum2=0
xi_sum3=0
xi_sum4=0

xiyi=0
xi2yi=0

yi_sum=sum(yi)

for i in range(n):
    xi_sum2+=xi[i]**2
    xi_sum3+=xi[i]**3
    xi_sum4+=xi[i]**4
    xiyi+=xi[i]*yi[i]
    xi2yi+=xi[i]**2*yi[i]

print(n,xi_sum,xi_sum2,yi_sum,xi_sum,xi_sum2,xi_sum3,xiyi,xi_sum2,xi_sum3,xi_sum4,xi2yi)

# [4 0 20 | 26]
# [0 20 0| -34]     
# [20 0 164| 186]

# denklem çapraz baskın ise Jacobi 

count=0
relativeError=1
tol=0
a0,a1,a2=0,0,0
while(relativeError > tol):
    tempa0=a0
    tempa1=a1
    tempa2=a2
    # a0,a1,a2= #, #, #    yukardaki matrisi a0 a1 a2 denklemiyle yazıp ayrı ayrı bulup yazıyoruz
    count+=1
    relativeErrora0=abs((a0-tempa0)/a0)*100
    relativeErrora1=abs((a0-tempa1)/a1)*100
    relativeErrora2=abs((a0-tempa2)/a2)*100

    relativeError=max(relativeErrora0,relativeErrora1,relativeErrora2)

print(a0,a1,a2)



