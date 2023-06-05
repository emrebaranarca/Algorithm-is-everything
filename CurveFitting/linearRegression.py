# yi = a0 + a1*xi + e

xi=[1,2,3,4,5,6,7]
yi=[0.5,2.5,2,4,3.5,6,5.5]
xiyi=0
xi2=0
n=len(xi)
for i in range (n):
    xiyi+=xi[i]*yi[i]
    xi2+=xi[i]**2

a1= (n*xiyi - sum(xi)*sum(yi)) / (n*xi2-sum(xi)**2)
a0= sum(yi)/n - (sum(xi)/n) * a1 

print("y = " + str(a0) + " + " + str(a1) + "x")
