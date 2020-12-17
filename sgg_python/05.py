#range   生成自然数序列
def rang(): 
    for index in range(1,20):
        if  index % 2 ==0 :
            break
        else:
            print(index,end = '\t')
#rang()
#tuple   不可变数组  
def tup():
    for index in (1,2,3,4,5,6):
       print(index,end = "\t")
    my_tup = (1,2,3)
   
tup()
#y用元组 交换值
def switch(a,b):
    a,b = b,a
    print(f"{a}= a and {b}  = b")
#switch(3,5)
