d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
print(list(d.items())[1][0])
c =1
f ={}
for a in d:
    f[c] = d[a]
    c += 1

print(f)