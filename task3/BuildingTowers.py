from statistics import mode
m = input('')
g = []
a = input('')
l = a.split()
for i in range(len(l)):
    l[i] = int(l[i])
for k in l:
    if k not in g:
        g.append(k)
m = len(g)
print(l.count(mode(l)), m)
