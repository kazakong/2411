# 리스트 함수(순서o,중복o,수정o,삭제o)
c = [50,60,70,80]
c.append(90)
print(c)
c.remove(60)
print(c)
c.pop( )
print(c)

d = [50,40,20,30]
d.sort()
print(d)

#튜플 함수(순서o,중복o,수정x,삭제x)
z = (5,2,1,3,4)
print(z)
print(3 in z)
print(z.index(4))
print(z.count(1))
