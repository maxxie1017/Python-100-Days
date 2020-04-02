daffodils = []
for k in range(100,1000):
    print(k)
    unit = k%10
    ten = (k-unit)%100/10
    hundred = (k-ten*10-unit)/100
    print(hundred, ten, unit)
    if k == unit**3+ten**3+hundred**3:
        daffodils.append(k)
print(daffodils)




