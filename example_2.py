# *args,*kwargs

def args_func(*args):
    print(args)

args_func('kim')
args_func('kim','Park','Lee')

def args_func(*args):
    for t in args:
        print(t)

#def args_func(*args):
    #for i,v in enumerate(arg):
        #print(i,v)

def kwargs_func(**kwargs):
    print(kwargs)

kwargs_func(name1='Kim', name2='Park', name3='Lee')
print(kwargs_func)


def kwargs_func(**kwargs):
    for k,n in kwargs.items():
        print(k,v)

def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1,arg2, args, kwargs)

example_mul(10,20)
    

