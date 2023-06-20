# y = a0 + a1*xi + a2*xi^2 + a3*xi^3

xi=[6,5,2,-1]
yi=[38,74,50,80]

n=len(xi)
xi_sum=sum(xi)
xi_sum2=0
xi_sum3=0
xi_sum4=0
xi_sum5=0
xi_sum6=0

xiyi=0
xi2yi=0
xi3yi=0

yi_sum=sum(yi)

for i in range(n):
    xi_sum2+=xi[i]**2
    xi_sum3+=xi[i]**3
    xi_sum4+=xi[i]**4
    xi_sum5+=xi[i]**5
    xi_sum6+=xi[i]**6
    xiyi+=xi[i]*yi[i]
    xi2yi+=xi[i]**2*yi[i]
    xi3yi+=xi[i]**3*yi[i]

print(n,xi_sum,xi_sum2,yi_sum,xi_sum,xi_sum2,xi_sum3,xiyi,xi_sum2,xi_sum3,xi_sum4,xi2yi,xi_sum3,xi_sum4,xi_sum5,xi3yi)