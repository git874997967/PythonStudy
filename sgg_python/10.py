#functions 
def fn1(index):
    return True if index % 3 ==0 else False

l = range(0,20)
result = filter(fn1,l)
#print(list(result))
result2 =  filter( lambda i : i % 3 ==0, l)
#print(list(result2))
result3 =  map( lambda i :  i * 3, l)

#print(list(result3))
myList = ['aaa','bb','c','ddddd','eeee']
myList.sort(key = len,reverse= True)
#print(myList)

# 闭包 
#   将操作 对象 object 放在  两个嵌套函数之前 据为私有   防止 暴露于全局   被他人访问  
#   在函数 内部 返回内部 函数
# def make_ave():
#     num =[]
#     def ave(n):
       
#         num.append(n)
#         return sum(num) / len(num)
#     return ave
# averager = make_ave()
# print(averager(50))
# print(averager(30))

def make_ave():
    num = []
    def ave(n):
        num.append(n)
        return sum(num) / len(num)
    return ave
averager = make_ave() # averager is the actual function name which takes one arg also that is the return(function) of the make_ave
print(averager(10))
print(averager(40))
 

def print_line():
    print(" this is one sinlge line")
def add(a,b):
    return a+ b
def multi(a,b):
    return a * b

def begin_end(function_name):   ## param is the old function name which we should wrap
    def new_function(*args,**kargs):
        print("function starts")
        result = function_name(*args,**kargs)
        print("function ends")
        return result           # we need result 
    return new_function    # closure

new_add = begin_end(add)
new_multi = begin_end(multi)
new_print = begin_end(print_line)
print(new_add(1,2),new_multi(3,5),new_print())

@begin_end
def pows(a,b):
    return a ** b

print( pows(3,5))
