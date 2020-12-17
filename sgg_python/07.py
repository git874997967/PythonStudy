# set   集合中存储不可变对象  
# 集合中对象是无序的 
# set 集合中的元素是唯一的
#  使用 {}  或者 .set()  创建集合 
# 集合没有索引 要先转换成list 在操作下标
def my_set():
    set1 = {1,2,3,4,56}
    print(set1,type(set1))
    set2 = set([1,2,3,4,5])
    set2.union(set1)
    print(set2)
    set1.add(100)
    set2.update(set1)  # 添加 另一个集合 
    print(set2)
#my_set()
