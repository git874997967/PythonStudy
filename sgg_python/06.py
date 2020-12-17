#dict
#字典用来存储对象 
def my_dic(index):
    dic = {1:'1',
            2:'2',
            3:'3'
          }
    print(4 in dic , 3 in dic)
    print(dic.get(4,"without this key"),len(dic))
    dic[index] ='5'
    dic[6] ='6'
    dic.pop(666,"without this key")
    dic2 = dic.copy() # will not copy
    #print(dic[index],len(dic))
    for key in dic.keys():
        print( key)
    for value in dic.values():
        print(value )
    for k,v in dic.items():
        print(k,v)
my_dic(3)
