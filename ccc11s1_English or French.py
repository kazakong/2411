n =int(input())
if n < 0 or n > 10000:
    exit()
elif 0 < n < 10000:
    tcount = 0
    Tcount = 0
    scount = 0
    Scount = 0

for i in range(n):
    line = input()
    tcount = tcount + line.count('t')
    Tcount = Tcount + line.count('T')
    scount = scount + line.count('s')
    Scount = Scount + line.count('S')

if tCount + TCount > sCount + SCount:
    print('English')
elif tCount + TCount <= sCount + SCount:
    print('French')