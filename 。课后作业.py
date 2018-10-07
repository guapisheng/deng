1.。
class Animal():
    name = ''
    def call():
        print('super Animal')

class Dog(Animal):
    def call():
        print("wang wang")

class Cat(Animal):
    def call():
        print("maio miao")


2。

def fib(x):
    if x <= 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

3。

lst = [print(i) for i in range(0,101)if i % 2 == 1]

4

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

import pdb
def test():
    try:
        print("try")
        print(add(10,0))
        print(sub(10,0))
        print(mul(10,0))
        print(div(10,0))
    except:
        print(sys.exc_info())

5.音氏

