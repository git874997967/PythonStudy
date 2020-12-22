#function
# use tuple to pass varied length parames

def sum(*nums) :
    result = 0
    for n in nums:
        result += n
    print( result)
sum(1,2,3,6,5,67)
#   C 必须使用关键字 
def sum1(a,*b,c):
    print ("a =  ",a)
    print ("b = ", b)
    print("c = ", c)
sum1(1,2,3,4,5,c= 6)
def sum2(*a,b,c):
    print ("a =  ",a)
    print ("b = ", b)
    print("c = ", c)
sum2(1,2,3,b=(4,5),c= 6)
# **a  将所有 参数保存到字典中 
# 参数的解包
# *对元组解包  ** 对字典解包 
def fun1(a:int, b:str,c:bool):
     """
     this is a doc of the function 
     
     
     """
     print(210)
help(fun1)

 