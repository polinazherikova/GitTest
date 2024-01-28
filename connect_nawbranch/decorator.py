#1
# import time
# def povtor(function):
#     def decorator(func):
#         time_func= 0
#         def wrapper(*args,**kwargs):
#             nonlocal time_func
#             time1=time.time()
#             if time1-time_func>=function:
#                 time_func=time1
#                 return func(*args, **kwargs)
#             else:
#                 print(f"function {func.__name__} lasts")
#         return wrapper
#     return decorator
# @povtor(10)
# def time_function():
#     print("function start")
# for i in range(10):
#     time_function()
#     time.sleep(3)
#2
def loging_function(func):
    def wrapper(*args):
        print(f"Function '{func.__name__}' with {args}")
        result=func(*args)
        print(f"Function '{func.__name__}' result- {result}")
        return result
    return wrapper
@loging_function
def function(x,y):
    return x*y
result = function(10,3)
#3
def check(func):
    def wrapper(aunthetic=True,*args,**kwargs):
        if aunthetic:
            return func(*args, **kwargs)
        else:
            print("WRONG!!!")
    return wrapper
@check
def function(*args,**kwargs):
    print("Verified")
function(aunthetic=True)
function(aunthetic=False)
#4
def checkType(*type):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for i,j in zip(args,type):
                if isinstance(i,j):
                    continue
                print(f"WRONG!Check types!")
            result = func(*args, **kwargs)
            if isinstance(result, type[-1]):
                return result
            print(f"WRONG!Check types!")
        return wrapper
    return decorator
@checkType(int, int, int)
def function(a,b,c):
    return a*b**c
print(f"Result:a*b**c={function(5,3,2)}")
#5
def optfun(func):
    cash=0
    times=3
    now_count = 0
    def wrapper(*args,**kwargs):
        nonlocal cash,now_count
        if now_count<times:
            now_count+=1
            return cash if cash!=0 else func(*args,**kwargs)
        now_count=1
        result=func(*args,**kwargs)
        cash=result
        print("Clearing cash.Let's start over")
        return result
    return wrapper
@optfun
def function(x,y):
    print("Cash calculation")
    return x*y
first=function(5,8)
print(first)
second=function(5,7)
print(second)
third=function(2,5)
print(third)
fourth =function(5,5)
print(fourth)
