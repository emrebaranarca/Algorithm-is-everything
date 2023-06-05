# y = a0 + a1*xi + a2*xi^2 + e

xi=[0,1,2,3,4,5]
yi=[2.1,7.7,13.6,27.2,40.9,61.1]

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

print(xi_sum,xi_sum2,xi_sum3,xi_sum4,xiyi,xi2yi,yi_sum,n)

# [6 15 55 | 152.6]
# [15 55 225| 585.6]     
# [55 225 979| 2488.8]

# denklem çapraz baskın değil Jacobi ya da Gauss Seitel iterasyon kullanamayız.
# jauss gordon ile çözülüp a0 a1 a2 bulunur
# https://matrixcalc.org/slu.html
# a0 = 2.47857  a1 = 2,35929 a2 = 1.86071   
# 
# y = 2.47857 + 2,35929x + 1.86071x2
a0 = 2.47857
a1 = 2,35929
a2 = 1.86071
print("y = " + str(a0) + " + " + str(a1) + "x"+" + " + str(a2)+"x^2")


