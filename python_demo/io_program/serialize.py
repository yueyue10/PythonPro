import json
import pickle

print('''---------------------序列化---------------------
''')

# 在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：
d = dict(name='Bob', age=20, score=88)

# 可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。
# 如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。

# 我们把变量从内存中变成可存储或传输的过程称之为序列化，
# 在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
#
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# Python提供了pickle模块来实现序列化。


# 首先，我们尝试把一个对象序列化并写入文件：
d = dict(name='Bob', age=20, score=88)
byte1 = pickle.dumps(d)
print(byte1)

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
print("保存完毕！")
# 看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
# 我们打开另一个Python命令行来反序列化刚才保存的对象：
f = open("dump.txt", "rb")
d = pickle.load(f)
f.close()
print("读取dump.txt文件内容：", d)

# # # # # # # # # # #
# # # # # # # # # # # JSON # # # # # # # # # # # # #
# # # # # # # # # # #

# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，
# 比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，
# 可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
# JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
js = json.dumps(d)
print("\n转成json:", js)

# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
#
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
ob = json.loads(json_str)
print("将str转成ob对象", ob)


# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。

# # # # # # # # # # #
# # # # # # # # # # # JSON进阶 # # # # # # # # # # # # #
# # # # # # # # # # #

# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，
# 我们更喜欢用class表示对象，比如定义Student类，然后序列化：

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)
try:
    print(json.dumps(s))
except Exception as e:
    print("\n", e)


# 报错： TypeError: Object of type Student is not JSON serializable

# 如果连class的实例对象都无法序列化为JSON，这肯定不合理！
#
# 别急，我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数：
#
# 这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，
# 是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
#
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


# 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
print(json.dumps(s, default=student2dict))
# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(s, default=lambda obj: obj.__dict__))


# *****************JSON反序列化******************
# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，
# loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
# 打印出的是反序列化的Student实例对象。

# 练习
# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
obj = dict(name='小明', age=20)
print("\n", json.dumps(obj))
s = json.dumps(obj, ensure_ascii=True)
print(s)
