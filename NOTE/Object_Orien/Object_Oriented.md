
# 面向对象

## 定义类
```python
	class Garen:
		camp=‘demacia’
		def __init__(self,nickname):
			self.nick=nickname
		def attack(self,enemy):
			print(“%s attack %s”%(self.nick,enemy))
```
## 类：
  * 实例化：    g = Garen()
  * 引用类的变量： print(Garen.camp)
  * 引用类的函数： Garen.attack(1321414)    需要传一个参数进去
## 使用一个对象：
```python
g1 = Geren()
print(g1.camp)
g2 = Geren()
```
  * 引用名字：对象名.变量名
  * 引用绑定方法：对象名.绑定方法
## 可以对类和对象的变量进行增删改查！！！
* 查：print(Geren.camp)
* 删：del Geren.camp
* 增：Geren.x = 1
* 改：Geren.camp = 'aaa'

  对象g1有同样的使用方法。
 
## 查看类的命名空间
	print(Geren.__dict__)
## 查看对象的命名空间
	print(g1.__dict__)

## 类的变量通常定义成不可变类型

## 继承和派生
```python
class A:pass
class B:pass
class C(A):pass
class D(A,B):pass
```
	-- 查看继承：print(D.__bases__)
```python	
class Hero:
	def __init__(self,nickname,life_value):
		self.nickname = nickname
		self.life_value	= life_value
	def attack(self,enemy):
		print("attack from Hero")
class Garen(Hero):
	def __init__(self,nickname,life_value,script):
		Hero.__init__(self,nickname,life_value)
		self.script = script
	def attack(self,enemy):
		Hero.attack	(self,enemy)
		print('attack from garen')
	camp = "ggggg"
class Riven(Hero):
	camp = 'rrrrr'

g = Garen('garen',20,'hello world')
r = Riven('riven',30)
print(g.attack(r))
print(g.script)
```
## 组合
	* 对比继承来说也是用来减少代码重用的，组合描述的是一种‘有’的关系。
	* 老师有课程，学生有成绩....
```python
class Course:
	def __init__(self,name,price,period):
			self.name=name
			self.price=price
			self.period=period
	class Teacher:
		def __init__(self,name,course):
			self.name=name
			self.course=course
	class Student:
		def __init__(self,name,course):
			self.name=name
			self.course=course
python=Course("python",100,'3m')
t = Teacher('egg',python)
s = Student('Ale',python)

print(s.course.name)
print(t.course.period)
print(t.course.price)
```
## 接口与归一化设计
	python中没有接口，用继承的关系来解决，有接口是为了让使用者有统一的用法
## 主动抛出异常
```python
	raise Attributeerror('..........')
```
## 抽象类
```python
import abc
	class Animal(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def run(self):
		pass
	#与普通类额外的特点：加了装饰器的函数，子类必须实现它们
```
## 新式类的继承原理
	* 在查找属性时遵循：广度优先
	* 查看继承顺序：print(F.__mro__)
	* mro，算出继承关系的列表。
## super函数的用法
	* super(自己的类，self).父类的函数名
	* super只能用于新式类

```python
	class People:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def speak(self):
		pass
	class Chinese(People):
		def __init__(self,name,age,language='chinese'):
			super().__init__(name,age)
		def speak(self,x):
			super().speak()
			print('x')				
```
## 多态与多态性
	* 多态是同一种事物的多种形态。
	* 多态性：定义统一的接口，可以传入不同类型的值，但是调用的逻辑都一样，执行的结果却不一样。
	* 多态性依赖于：继承；
```python
class Animal:
	def run(self):
		pass
	def speak(self):
		pass
	class People(Animal):
		def run(self):
			print('renzaizou')

	class Pig(Animal):
		def run(self):
			print("pig is walking")
	peo1 = People()
	pig1 = Pig()

	def func(obj):
		obj.run()
	func(peo1)
	func(pig1)
```
## 封装
```python	
class A:
	__x = 1
	def __test():
		print('form A')
	#print(A.__x)会报错，因为__x变成了_A__x的形式
	print(A.__dict__)
	a = A()
```
	a.__x也是调不到的
	__名字，这种语法，只在定义的时候才会有变形的效果，如果类或者对象已经产生了，就不会有变形效果。
		
	
	 * 外部想访问x的值，可以这样：
	class A:
	def __init__(self):
		self.__x=1
	def tell(self):
		print(self.__x)
	a = A()
	a.tell()
	
	 * 父类中以__开头函数不会被子类覆盖，例如：
	class A:
	def __fa(self):
		print("from A")
	def test(self):
		self.__fa()

	class B(A):
		def __fa(self):
			print('from B')
	b = B()
	b.test()
## property
    property是一种特殊的属性，访问它时会执行一段代码，返回结果。
    被property装饰的属性会优先于对象的属性被使用。
    被property装饰的属性，如name，分成三种：
        #propert（查询）
        #name.setter（赋值）
        #name.deleter（删除）
```python
    import math
    class Circle:
        def __init__(self,radius):
            self.radius = radius

        @property
        def area(self):
            return math.pi*self.radius**2

        @property
        def perimeter(self):
            return 2*math.pi*self.radius
    c = Circle(10)
    print(c.radius)
    print(c.area)
    print(c.perimeter)


   class People:
	def __init__(self,name):
		self.name= name
		@property
		def name(self):
		return self.__Name

	@name.setter
	def name(self,value):
		if not isinstance(value,str):
			raise TypeError("名字必须是字符串")
		self.__Name = value

	@name.deleter
	def name(self):
		del self.__Name

	p = People('swefegf')
	print(p.name)
	p.name = 'egg'

	print(p.name)

	del p.name
	# print(p.name)
```
## staticmethod
    类的工具包
    但凡是定义在类的内部，并且没有被任何装饰器修饰过的方法，都是绑定方法，有自动传值功能。
    但凡是定义在类的内部，并且被任何装饰器修饰过的方法，都是解除绑定方法，实际上就是函数，没有自动传值的功能。


## classmethod
    把一个方法绑定给类，类.绑定到类的方法()，会把类本身当作第一个参数自动传给绑定方法
## __str__
    定义在类内部，必须返回一个字符串类型；打印由这个类产生的对象时，会触发执行。
```python
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        msg = '(name:%s,age:%s)'%(self.name,self.age)
        return msg

    p = People('egg',19)
    print(p)
```

## 关于staticmethod和classmethod,当不用这两个装饰器的时候，类里面的函数是自动绑定给对象的，也就是说会把对象自动传给函数的第一个参数self，若加上@staticmethod，这个函数就不绑定了，类和对象都能用，当作普通函数来用。加上@classmethod，就会把这个函数自动绑定给类，也就是会把对象自动传给函数的第一个参数cls,这时候即使对象在调用这个函数，传进去的也是对象的类。
# property，就是搞接口用的
	* property可以把函数func()编程变量那样的属性来用，需要return这个值。
	* func_setter可以修改这个func()所隐藏的参数，直接用对象.func='xxxx'可以直接修改。
	* func_deletter则是删除。
## 反射
    通过字符串的形式操作对象的属性。
   ### hasattr(object,name),返回True或False
        print(hasattr(p,'name')) <=======相同=======>print('name' in p.__dict__)
   ### getattr()
        print(getattr(p,'country')) <=====相同=========>print(p.country)

        f = getattr(p,'test')
        f() <=====相同=========>p.test()
        print(getattr(p,'xxxxxxx','bucunzai'))
        -- 在'xxxxxxx'属性不存在时候，在getattr后面再加一句提示，保证程序不会抛出异常，这时候显示的就是后面的’bucunzai‘提示。
        -- 或者加个判断
            if hasattr(p,'test'):
                f = getattr(p,'test')
                f()
   ### setattr()
        setattr(p,'age',12)<=====相同=========>p.age=12
        print(p.age,p.__dict__)
   ### delattr()
        delattr(p,'name')<=====相同=========>del p.name
   ### 反射当前模块的属性
```python
        import sys
        def s1():
            print('s1')
        def s2():
            print('s2')
        print(__name__)
        this_module = sys.modules[__name__]#拿到当前模块的对象
        print(this_module.s1)
        print(hasattr(this_module,'s1'))#返回True或False
        print(getattr(this_module,'s2'))#返回一个函数地址，加括号就能运行,与this_module.s1一样，this_module.s1()就可以直接运行
        f = getattr(this_module,'s2')
	f()
```
## 反射的应用
## 反射实现可插拔机制
   ### 客户端代码(Client.py)：
```python
class FtpClient:
    def __init__(self,addr):
        print("connecting......")
        self.addr = addr
    def put(self):
        print('putting....')
```
   ### 服务端：
 ```python
    import Client
    obj = Client.FtpClient('192.168.1.111')
    print(obj.addr)
    if hasattr(obj,'get'):
        f = getattr(obj,'get')
        f()
    else:
        print('还未实现')
```
## attr系列
```python
   __setattr__()
    __delattr__()
    __getatte__()
```
## 定制自己的数据类型		
### 基于继承的原理进行类型加工
```python
	class LIST(list):
		def append(self,object):
			if not isinstance(object,int):
				raise TypeError('must be int')
			super().append(object)
		def insert(self,locate,object):
			if not isinstance(object,int):
				raise TypeError('must be int')
			super().insert(locate,object)
	l = LIST([1,2,3])
	l.append(4)
	print(l)

	l.insert(0,5)
	print(l)
```
### 授权方式实现定制自己的数据类型
```python
	import time
	class OPEN:
		def __init__(self,filepath,mode='r',encode='utf-8'):
			self.fp = open(filepath,mode=mode)
			self.filepath = filepath
			self.mode = mode
			self.encode = encode

		def write(self,line):
			print('----->自定义write')
			t = time.strftime("%Y-%m-%d %X")
			self.fp.write('%s %s'%(t,line))
		def __getattr__(self, item):
			return getattr(self.fp,item)

	ff = OPEN("a.txt",'w')
	ff.write('11111111\n')
	ff.write('11111111\n')
	ff.write('11111111\n')
	ff.write('11111111\n')
	ff.close()
	fr = OPEN('a.txt','r')
	print(fr.read())
	fr.seek(0)
	print('---->'+fr.read())
```
## 通过字符串倒入模块
	import importlib
	t = importlib.import_module('time')
	print(t.time())
## 定制自己的数据类型:'__getattr__()'在什么时候用到？？？
```python
    import time
    class LIST:
        def __init__(self,x):
            self.l = list(x)
        @property
        def mid(self):
            mid = len(self.l)//2
            return self.l[mid]
        def append(self,value):
            if not isinstance(value,str):
                print('must be str')
            self.l.append(value)
        def __getattr__(self,item):
            return getattr(self.l,item)
        def __str__(self):
            return str(self.l)
    ll = LIST([1,2,3])
    print(ll.mid)
    ll.append(3)
    print(ll.mid)
    ll.insert(0,2242354)
    print(ll)
```
## item 系列---->把对象操作属性模拟成字典的形式
```python
    class Foo:
        def __init__(self,name):
            self.name = name
        def __getitem__(self,item):
            print("getitem")
            return self.__dict__[item]
        def __setitem__(self,key,value):
            print("setitem")
            self.__dict__[key] = value
        def __delitem__(self,key):
            print("delitem")
            self.__dict__.pop(key)
    f = Foo('egg')
    f['age'] = 18 #调用setitem
    print(f.__dict__)
    n = f['name'] #调getitem
    print(n)
    del f['age'] #调用delitem
    print(f.__dict__)
```
## __slots__()方法：当类中定义了它以后，类所生成的对象的属性只能是slot中包含的，不能识别的，而且对象也不生成自己的__dict__
```python
	class Foo:
	    __slots__ = ['x','y','z']

	f = Foo()
	f.x = 1
	f.y = 2
	f.z = 3
	print(f.x,f.y,f.z)
	# f.m = 4#会报错
	print(Foo.__dict__)
```
## __next__和__iter__实现迭代器协议
```python
	class Foo:
	    def __init__(self,start):
		self.start = start
	    def __next__(self):
		if self.start > 10:
		    raise StopIteration
		n = self.start
		self.start += 1
		return n
	    def __iter__(self):
		return self

	f = Foo(0)#f下面有__iter__和__next__方法
	for i in f:
	    print(i)
```
## __module__:当前操作的对象在哪个模块
## __class__：表示当前操作的对象的类是什么
## __del__()
    析构方法，当对象在内存中被释放时，自动触发执行。此方法一般无需定义。
## 上下文管理协议，即with语句，为了让一个对象兼容with语句，必须在这个对象的类中声明__enter__()和__exit__()方法。
    ### __enter__()
    ### __exit__()
```python
    import time
    class Open:
        def __init__(self,pathfile,mode='r',code='utf-8'):
            self.f = open(pathfile,mode = mode)
            self.pathfile = pathfile
            self.mode = mode
        def __getattr__(self,item):
            return getattr(self.f,item)
        def __del__(self):
            print("----del")
            self.f.close()
        def __enter__(self):
            # print("出现with语句，对象的__enter__被触发，有返回值则赋值给as声明的变量")
            print('-->enter')
        def __exit__(self,exc_type,exc_val,exc_tb):
            # print("with代码块执行完毕之后执行")
            print('===>exit')

    # fp = Open('a.txt','w')
    # f1 = fp
    # del fp
    # print('=========')
    with Open('a.txt') as f:
        print('.....with .. as ..')
```
    用途或者说好处：
    1.使用with语句的目的就是把代码块放入with中执行，with结束后，自动完成清理工作，无须手动干预
    2.在需要管理一些资源比如文件，网络连接和锁的编程环境中，可以在__exit__中定制自动释放资源的机制，你无须再去关系这个问题，这将大有用处
## __call__() 方法：对象后面加括号，触发执行。
```python
    class Foo:
        def __init__(self):
            pass
        def __call__(self,*args,**kwargs):
            print('__call__')
    obj = Foo()#执行__init__
    obj()#对象加括号就能运行，执行__call__
 ```
## 元类：就是类的类，可以用它来控制类的行为.
    http://www.cnblogs.com/linhaifeng/articles/6204014.html#_label13
```python
    class Mymeta(type):
        def __init__(self,class_name,class_bases,class_dic):
            for key in class_dic:
                if not callable(class_dic[key]):continue
                if not class_dic[key].__doc__:
                    raise TypeError("you need to write doc")
    class Foo(metaclass = Mymeta):
        x = 1
        def run(slef):
            'nwefgnjerg'
            print('running')
    Foo = Mymeta("Foo",(object,),{'x':1,'run':'run'})
    print(Foo.__dict__)
```
