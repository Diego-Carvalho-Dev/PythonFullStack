#set é o counjunto
#não permite dados repetidos

x = [1,1,1,1,1,12,2,2,2,3,3,3,]

x = set(x)

print(x)


# union = UNIR os conjuntos
z = {1,2,3,4,5,6}
y = {1,3,7,8,9,10}

z = z.union(y)
print(z)

#intersection = verifica qual tem nos conjuntos
z = z.intersection(y)
print(z)

#diference = verifica as diferentes

z = z.difference(y)
print(z)