from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

print('''---------------------collections---------------------
''')

# collections是Python内建的一个集合模块，提供了许多有用的集合类。

# *********** namedtuple ***********
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，
# 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print("namedtuple", p)
# 我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
print("isinstance(p, Point)=", isinstance(p, Point))
# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# *********** deque ***********
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print("\ndeque", q)
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

# *********** defaultdict ***********
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print("\ndd['key1']=", dd['key1'])  # key1存在
print("dd['key2']=", dd['key2'])  # key2不存在，返回默认值

# *********** OrderedDict ***********
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#
# 如果要保持Key的顺序，可以用OrderedDict：
d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print("\nd=", d)  # dict的Key是无序的
print("od =", od)  # OrderedDict的Key是有序的

# *********** ChainMap ***********
# ChainMap可以把一组dict串起来并组成一个逻辑上的dict。
# ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
#
# 组合成ChainMap:
# combined = ChainMap(command_line_args, os.environ, defaults)

# *********** Counter ***********
# Counter是一个简单的计数器，例如，统计字符出现的个数：
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print("\nc=", c)
# Counter实际上也是dict的一个子类，上面的结果可以看出，
# 字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。
