import chardet

print('''---------------------chardet---------------------
''')

# 字符串编码一直是令人非常头疼的问题，尤其是我们在处理一些不规范的第三方网页的时候。
# chardet这个第三方库正好就派上了用场。用它来检测编码，简单易用。
#
# *********** 安装chardet ***********
#
# 如果安装了Anaconda，chardet就已经可用了。否则，需要在命令行下通过pip安装：
#
# $ pip install chardet
# 如果遇到Permission denied安装失败，请加上sudo重试。

# *********** 使用chardet ***********
# 当我们拿到一个bytes时，就可以对其检测编码。用chardet检测编码，只需要一行代码：
print("chardet.detect(b'Hello, world!')=\t", chardet.detect(b'Hello, world!'))

# 我们来试试检测GBK编码的中文：
data = '离离原上草，一岁一枯荣'.encode('gbk')
print("chardet.detect(data)=\t", chardet.detect(data))

# 对UTF-8编码进行检测：
data = '离离原上草，一岁一枯荣'.encode('utf-8')
print("chardet.detect(data)=\t", chardet.detect(data))

# 我们再试试对日文进行检测：
data = '最新の主要ニュース'.encode('euc-jp')
print("chardet.detect(data)=\t", chardet.detect(data))

# 可见，用chardet检测编码，使用简单。获取到编码后，再转换为str，就可以方便后续处理。
# 使用chardet检测编码非常容易，chardet支持检测中文、日文、韩文等多种语言。