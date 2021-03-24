import logging

def use_logging(func):

    def wrapper(*args,**kwargs):
        logging.warning("%s is running"%func.__name__)
        return func(*args,**kwargs)
    return wrapper


#@符号是装饰器的语法糖，在定义函数的时候使用，避免再一次赋值操作
@use_logging
def foo(i=2):
    print(i)
    print('i am foo')

#使用装饰器
foo(i=4)



#不使用装饰器实现
# foo = use_logging(foo)
# foo(i=4)

