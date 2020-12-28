# class([父类])
# __init(self, *args)
# method(self, *args)
#不要尝试调用特殊方法   特殊方法特殊时刻自动调用 
class Person:
    def __init__(self , name):
        self.name = name
    def sayHello(self):
        print(f"hello I am {self.name}")

p1 = Person("abc")
p1.sayHello()
p2 = Person("bcd")
p2.sayHello()

class Dog():
    # add properties to the class
    def __init__(self, name , age , gender , height , weight, sounds, speed, strength ):
        self.hiddden_name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.sounds = sounds
        self.speed = speed
        self.strength = strength
    # 不可设置 去掉  getter
    def getter_name(self):
        return self.hiddden_name
    #  只读  去掉  set  setter 数据验证 
    def setter_name(self,name):
        self.hiddden_name = name
    def bark(self):
        print( f"{self.hiddden_name} bark like {self.sounds}")
        pass
    def bit(self):
        print(f"{self.hiddden_name} bit strengh is {self.strength} N")
        pass
    def run(self):
        print(f"{self.hiddden_name} can run as fast as {self.speed} KM/h")
        
d = Dog("D1", 8 , "male" , 30 , 50 , "哈哈" , 49 , 600)
d.bit()
d.bark()
d.run()


class  Animal:
    def __init(self, name):
        self._name = name
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self, name):
        self._name = name
    def  run(self):
        print(" I can run")
        pass
    def  sleep(self):
        print(" I can sleep")
        pass
#  子类实例会 重写父类中的同名方法

class Cat(Animal):
    def __init__(self, name ,age):
        #  直接用 supe  返回 
        #super().__init__(name)
         self._name = name
         self._age = age
    def run(self):
        print(f" cat {self._name} is running")
        pass
    def bark(self):
        print("I can bark")
        pass
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age

c = Cat('abc',10)
c.name = "sophia"
c.age = 10
c.run()
c.bark()

class A(object):
    def test(self):
        print("from A")
        pass
class B(object):
    def test2(self):
        print("from B")
        pass
class C(A,B):
    pass
c = C()
c.test()
c.test2()