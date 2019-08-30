import hashlib

print('''---------------------hashlib---------------------
''')

# 摘要算法简介
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

# 我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print("MD5\t", md5.hexdigest())

md51 = hashlib.md5()
md51.update('how to use md5 in '.encode('utf-8'))
md51.update('python hashlib?'.encode('utf-8'))
print("MD5\t", md51.hexdigest())

# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print("\nsha1", sha1.hexdigest())


# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。

# 练习
# 根据用户输入的口令，计算出存储在数据库中的MD5口令：
def calc_md5(password):
    md52 = hashlib.md5()
    md52.update(password.encode('utf-8'))
    return md52.hexdigest()


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
def login(user, password):
    return db.get(user) == calc_md5(password)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('测试ok')


# 由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
# 这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：


def calc_md5(password):
    return calc_md5(password + 'the-Salt')
# 经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。
