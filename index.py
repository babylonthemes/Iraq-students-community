a=[4,2,1,6,2]


for i in range(len(a) -1):
    a[i] = a[i] + 1 if a[i] >=2 else a[i]

print(a)
