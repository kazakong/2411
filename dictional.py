#딕셔너리(Dictionary) : 순서x,중복x,수정o,삭제o
a = {'name' : 'kim','phone' :'010-777-7777', 'birth':870214}
b = {0:'Hello Python',1:'Hello Coding'}
c= {'arr':[1,2,3,4,5]}

print(type(a))
print(a['name'])
print(a.get('name'))
print(a.get('adress'))
print(c['arr'][1:2])

a['adress'] = 'seoul'
print(a)
a['rank'] =[1,3,4]
print(a)
print(a.keys())

temp = list(a.keys())
print(temp[1:3])
print(a.values())
print(a.items())
print(list(a.items()))
