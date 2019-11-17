import json
import os
import time

m_filter = [".mp4"]  # 设置过滤后的文件类型 当然可以设置多个类型
rename_ext = '.mp4'


class File(object):
    def __init__(self, old_name, new_name):
        self.old_name = old_name
        self.new_name = new_name


def get_all_file_path(dirname):
    result = []  # 所有的文件
    for maindir, subdir, file_name_list in os.walk(dirname):
        # print("1:", maindir)  # 当前主目录
        # print("2:", subdir)  # 当前主目录下的所有目录
        # print("3:", file_name_list)  # 当前主目录下的所有文件
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)  # 合并成一个完整路径
            ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
            if ext in m_filter:
                result.append(File(filename, ''))
        # 不再查找子目录
        break
    return result


def get_time_stamp():
    t = time.time()
    time_stamp = int(round(t * 1000000))
    time_str = str(time_stamp)
    # print(time_str)  # 微秒级时间戳
    return time_str + rename_ext


def save_json_str(json_str):
    name = path.split("/")[-1]
    json_path = os.path.join(path, name + '.json')
    with open(json_path, 'w') as f:
        f.write(json_str)


def rename_files(dir_path):
    files = get_all_file_path(dir_path)
    for file in files:
        file.new_name = get_time_stamp()
        old_file_path = os.path.join(path, file.old_name)
        new_file_path = os.path.join(path, file.new_name)
        # print(old_file_path, "---------", new_file_path)
        os.rename(old_file_path, new_file_path)
        time.sleep(0.1)
    json_str = json.dumps(files, default=lambda o: o.__dict__, sort_keys=True, indent=2)
    save_json_str(json_str)
    # print(json_str)
    print("修改文件名成功!", "保存文件名成功!")


if __name__ == '__main__':
    path = "E:/迅雷下载/抖音视频/pet-smart"
    rename_files(path)
    # get_time_stamp()
