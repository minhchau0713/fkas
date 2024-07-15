

# среднее арифметическое количества работников в одном отделе ппродаж должо быть больше 7
f = open('26_4.txt')
N = int(f.readline())
M = int(f.readline())
L = []
for x in f:
    a, b, c = map(int, x.split())
    L.append([a / b, b, c])
L.sort(key=lambda x: (x[0], x[2]), reverse=True)
new = L[:M]
su = sum(c for a, b, c in new) / M
chet = M
while su < 7 and chet < N:
    new[-1] = L[chet]
    chet += 1
    su = sum(c for a, b, c in new) / M
su = sum(c for a, b, c in new) / M
sr = sum(b for a, b, c in new) / M
print(su, sr)