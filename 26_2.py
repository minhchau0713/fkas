
    
f = open('26_2.txt')
N = int(f.readline())
M = int(f.readline())
L = []
for x in f:
    a, b = map(int, x.split())
    L.append([a / b, b])
L.sort(reverse=True)
new = L[:M]
ma = max(a for a, b in new)
mi = min(b for a, b in new)
print(int(ma), mi)
f.close()