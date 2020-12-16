# num = 1 
# while num < 5:
#     print("hello")
#     num += num 
# else :
#     print("stopped")
# stop = 10
# for num in [0,stop]:
#     print(f"{num},hello")
#     num += 1
# else:
#     print("stopped")
## 100 以内  奇数之和 
def add_odd():
    num = 1
    sum = 0
    while num < 100:
        print(f" number {num} will be added")
        sum += num
        num = num << 1
        
    else:
        print(sum)
#add_odd()
def add_seven():
    num = 0
    sum = 0
    while num < 100:
        print(f"the num {num} is added")
        sum += num
        num += 7
    else:
        print(f" sum is {sum}")
#add_seven()
#  求水仙花数 

def get_flower():
    num = 0
    while num < 1000:
        num += 1 
        if 10 < num < 100:
            if ( num % 10 ) **2 + (num /10 ) **2 == num:
                print(f"{num} is the flowerNumber")       
        else:
            hundard = num // 100
            single = num % 10
            tens = (num -single)/ 10 % 10
            if  hundard **3 + tens ** 3 + single ** 3 == num:
                print(f"{num} is the flowerNumber")
#get_flower()

def is_factor(num):
    flag = True
    a = 2
    while a <= num ** 0.5:
        if num % a == 0:
            flag = False
            break
        a += 1
    return flag
num = 2 
# while num < 1000:
#     if is_factor(num) :
#      print(f"{num}prime")
#     num += 1

# 乘法表 

def multi():
   row = 1
   while row < 10: 
       col = 1 
       print("\n")
       while col <= row :
           print(f"|{col} * {row} = ", col * row,end = '')
           col += 1
       row = row + 1
multi()