print('''---------------------sorted---------------------
''')
# Python内置的sorted()函数就可以对list进行排序：
print("sorted([36, 5, -12, 9, -21])=\t", sorted([36, 5, -12, 9, -21]))
# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print("sorted([36, 5, -12, 9, -21], key=abs)=\t", sorted([36, 5, -12, 9, -21], key=abs))
print("sorted(['bob', 'about', 'Zoo', 'Credit'])=\t", sorted(['bob', 'about', 'Zoo', 'Credit']))
print("sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)=\t",
      sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print("sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)=\t",
      sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。

# 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# 请用sorted()对上述列表分别按名字排序,再按成绩从高到低排序：
def by_score(t):
    t1 = t[1]
    print(t1)
    return t1


L2 = sorted(L, key=by_score)
print("\nL2=", L2)
