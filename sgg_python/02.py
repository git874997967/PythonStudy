a = '123.2'
print(float(a),int(float(a)))
a = 10 / 4 
b = 10 % 4
c = 10 // 3
print(a,b,c)
a = True 
b = not a
print( b)
print(" please input the number you want to tell")
# a = input()
# a = int(a)
# if a > 10 and a < 20:
#     print(f" a :{a} is between 10 and 20")
# elif 21 < a < 30 :
#     print(f" a :{a} is between 20 and 30")
# else:
#     print(f" a :{a} is higher than 30 ")

 # 判断狗狗年龄 
age = float(input(" please input the age of the dog"))

if age < 0: 
     print(" please input the correct age")
elif age <= 2:
    print(f"the age of the dog is {age * 10.5}")
else:
    print(f"the age of the dog is {21 + (age - 2) * 4}")   