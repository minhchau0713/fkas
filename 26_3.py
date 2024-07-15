

f = open('26_3.txt')
N = int(f.readline())
M = int(f.readline())
L = []
new = []
for x in f:
    a, b = map(int, x.split())
    if b <= 3:
        new.append([a / b, b])
    else:
        L.append([a / b, b])
L.sort(reverse=True)
chet = M - len(new)
new = new + L[:chet]
sr = sum(a for a, b in new) / M
ma = max(b for a, b in new)
print(int(sr), ma)




