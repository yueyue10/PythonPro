print('''---------------------循环---------------------
''')

# Python的循环有两种，一种是for...in循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print ("遍历names：" + name)

# Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
print ("\n利用range生成从0到5的整数序列:", list(range(5)))

sum = 0
for x in range(101):
    sum = sum + x
print("\n计算0到100整数和sun=", sum)

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print("\n计算100以内所有奇数之和:", sum)

# break
# 在循环中，break语句可以提前退出循环
print ("\n")
n = 1
while n <= 100:
    if n > 3:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('break提前退出：END')

# continue
# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
print ("\ncontinue跳过之后的逻辑进入下一次循环：")
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
