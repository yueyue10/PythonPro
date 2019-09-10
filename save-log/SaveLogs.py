import os

from configs.DbConfig import LogTaskSql
from dbutils.MySql import MySql
from utils.LogUtils import Log

m_filter = [".log"]  # 设置过滤后的文件类型 当然可以设置多个类型


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
                result.append(apath)
    return result


def save_log(log_name, log_info):
    try:
        mysql = MySql()
        info_val = [log_name, log_info]
        mysql.update(LogTaskSql.log_insert, info_val)
        mysql.end(option='commit')
    except Exception as e:
        Log.info(e)


def clear_logs():
    try:
        mysql = MySql()
        logs = mysql.remove(LogTaskSql.remove_list)
        mysql.end(option='commit')
        print("清空数据成功!")
        return logs
    except Exception as e:
        Log.info(e)


def get_logs():
    try:
        mysql = MySql()
        logs = mysql.get_all(LogTaskSql.log_list)
        mysql.end(option='commit')
        return logs
    except Exception as e:
        Log.info(e)


def print_log():
    logs = get_logs()
    if logs:
        print('共有', len(logs), "条数据")
    else:
        print("暂无数据")
        return
    index = input("请输入提取的数据条目")
    try:
        index = int(index)
        log = logs[index - 1]
        b = log.get("content")
        print(str(b, encoding="utf-8"))
    except Exception as e:
        print('请输入数字编号')


def save_logs(dir_path):
    file_paths = get_all_file_path(dir_path)
    for file in file_paths:
        with open(file, "r", encoding='utf-8') as f:
            log_content = f.read()
            # print(os.path.basename(file) + "\n")
            # print(log_content + "\n")
            save_log(os.path.basename(file), log_content)
    print("保存数据成功!")


if __name__ == '__main__':
    path = "E:/Users/Python/save-log"
    # clear_logs()
    # save_logs(path)
    print_log()
