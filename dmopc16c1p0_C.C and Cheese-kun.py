W = int(input()) # 1 <= W <= 3
C = int(input()) # 0 <= C <= 100

order = "C.C. is ''  satisified with her pizza"

if W > 3 and C <= 95:
    print('abssolutely')
elif W < 1 and C <=50:
    print('fairly')
else:
    print('very')