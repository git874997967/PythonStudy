# 注释 # 号后面 最好保留一个space
# 如果表示数字过大  可以使用_连接数字 
# 二进制数字使用0b开头  八进制数字 使用  0o开头   十六进制数字使用 0h开头  但是输出的时候都是  十进制表示 
print(0.1 + 0.2 )
# 相同引号不可以嵌套 使用 三重引号 表示长字符
print('子曰："学而时习之 不亦乐乎"')
print('子曰:\'学而时习之, 不亦乐乎\'')
poem = '''
锄禾日当午,
汗滴禾下土,
谁之盘中餐,
粒粒皆辛苦.'''
# append for the string  字符串只能和字符串进行拼接  
poem = poem.__add__('abc') # must be string 
# poem = poem.__add__('23')
#print(poem,'\u16a1','\u1c00')
# placeholder  
message = 'hello%s'%poem # the second % will bring the var into the first string 
# if we want to use the list for placeholder then use the ()
# %s for string 
# %d for int 
# %f for decimal   .nf for how many digits
message = 'hello %s, I am %s'%(poem,'abc')
message2 = 'my name is %s and my age is %d also, my salary is %.2f'%('zac yang',29,533.2)
# print( message)
result = f'message = {message}, message2 = {message2}'
#print(result)
# practise use 4 methods to output  welcome xxx 光临 where xxx is your name 
#method 0 
string = 'welcome'
name = ' sophia huang'
end = ' 光临'
#method 0
print(string,name,end)
# method 1
string1 = string.__add__(name).__add__(end)
print(string1)
string2 = 'welcome%s%s'%(name,end)
print(string2)
#method3 
string3 = f'{string}{name}{end}'
print(string3 * 2)
# 类型检查 
a = 123
b = '123'
print(f'{a}{b}')

def is_number(s):
    #print(s.isdigit()," this is from isnumeric method")
    try:
        float(s)
        return True
    except ValueError :
        pass
    try :
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass
    return False

print(is_number(a))
print(is_number(b))
print(is_number("abc"))
print(id(a), type(a), a)
#类型转换  将一个类型的对象转换为另一个
a = 'hello' 
b = '123'
c = 123
print(int(b) + c)

# 类型转换  函数  int()  float() bool()  str()  

print(bool(a), bool(b),bool(0))