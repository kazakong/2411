def Hello(world):
    print('Hello',world)

Hello("python")

def hello_return(world):
    val = "Hello" + str(world)
    return val

str = hello_return("Python")
print(str)

def send_sms(world):
    print('send_sms',world)

send_sms("안녕하세요, 날씨가 춥습니다")

def fun_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1,y2,y3]
val1,val2,val3 = fun_mul(100)
print(val1,val2,val3)
print(type(val1),val1,val2,val3)


