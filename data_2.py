#"010-7777-9999"
q7 = "010-7777-9999"
print("7. ",q7[0:3]+q7[4:8]+q7[9:13])

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 . : "http://daum.net"

url = "http://daum.net"
print("8.",url[7:15])

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력. : "NiceMan"
q9 = "NiceMan"
print("9.",q9.upper())
print("9.", q9.lower())


# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력 : "abcdefghijklmn"

q10 = "abcdefghijklmn"
print("10.",q10[2:5])

# 11. 다음 리스트에서 "Apple" 항목만 삭제 : ["Banana", "Apple", "Orange"]
q11 = ["Banana", "Apple", "Orange"]
q11.remove("Apple")
print("11.",q11)

# 12. 다음 튜플을 리스트로 변환 : (1,2,3,4)
t = (1,2,3,4)
print("12.",list(t))


# 13. 다음 항목을 딕셔너리(dict)으로 선언 : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
q13_dict = {'성인' : 100000 , '청소년' : 70000 , '아동' : 30000}

print("13.",dict(q13_dict))


# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가
q13_dict["소아"]  = 0
print("14.",q13_dict)


# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력
q13_dict = {'성인' : 100000 , '청소년' : 70000 , '아동' : 30000}
print("15.",q13_dict.keys())

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해
q13_dict = {'성인' : 100000 , '청소년' : 70000 , '아동' : 30000}
print("16.",q13_dict.values())