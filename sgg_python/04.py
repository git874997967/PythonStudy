# 列表  list
# python 对象  object
# 切片 获取 列表的局部
mylist = [1,2,3,4,5,6,7,8,9,10]
print(mylist, type(mylist))
print(mylist[-2:-1])
start = 3
end = 9
step =2
print(mylist[start:end:step] * 2)
#   in  检查  元素是否在列表中
 
#遍历列表 
def  ems():
    emp = []
    while(True):
        print("\n请选择操作\n1 显示员工列表\n 2 添加员工\n 3 删除员工\n 4 退出系统 ")
        choice = input()
        if choice == "1":   
            if len(emp) == 0:
                print("没有员工")
            else:
               
                for index in emp:
                    print(index,end=" ")
            pass
        elif choice == "2":   
            print("请输入姓名")
            name = input()
            emp.append(name)
            print(f" 添加员工{name} 成功 ！")
            pass
        elif choice == "3": 
            print("请输入 员工姓名")
            name = input()
            if name in emp:
                emp.remove(name)
                print(f"删除员工{name} 成功！")
            else:
                print("员工不在列表中")
            pass
        elif choice == "4":
            print("Good Bye")
            break
        else:
            print(f"{choice} please input again")
            pass
         
ems()
 