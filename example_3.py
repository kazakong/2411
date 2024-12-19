#중첩함수(클로저)

def nested_func(num):
    def func_in_func(num):
        print('>>>>',num)
    print(" in func")
    func_in_func(num + 10000)

nested_func(10000)

#힌트
def func_mul2(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return[y1,y2,y3]

print(func_mul2(5))

#람다
#메모리 절약, 가독성 향상, 코드 간결
#함수는 객체 생성 -> 리소스(메모리) 할당
#람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func)
print(type(var_func))

print(var_func(10))

lambda_mul10 = lambda num : num * 10

print('>>>>',lambda_mul10(10))

def func_final(x,y,func):
    print(x * y * func(10))

func_final(10,10,lambda_mul10)
print(func_final(10,10,lambda x : x * 1000))
