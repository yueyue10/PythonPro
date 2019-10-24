"""
文件操作工具类
"""


# 读取文件内容:得到的数据是list{每个item是每行的数据}
def read_file(file_path='cursors.txt'):
    with open(file_path, 'r', encoding='utf-8') as f:
        _cursors = f.readlines()
    return _cursors


def save_file(file_path='data.txt', string=''):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(string)


if __name__ == '__main__':
    txt = read_file(r'E:\Users\Python\PythonPro\appium_demo\other\tktask\cursors.txt')
    print(txt)
