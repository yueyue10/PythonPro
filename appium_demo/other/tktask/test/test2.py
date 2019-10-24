import os

from other.tktask import save_path
from utils.string_utils import validate_title


class FileSys():
    m_files = []

    def get_files(self, file_dir):
        for root, dirs, files in os.walk(file_dir):
            # print(root)  # 当前目录路径
            # print(dirs)  # 当前路径下所有子目录
            # print(files)  # 当前路径下所有非目录子文件
            # print("长度：", len(files))
            return files

    def contain_file(self, video_name):
        if self.m_files:
            in_dir = self.m_files.__contains__(video_name + '.mp4')
        else:
            self.m_files = self.get_files(save_path)
            in_dir = self.m_files.__contains__(video_name + '.mp4')
        return in_dir


if __name__ == '__main__':
    filesys = FileSys()
    con = filesys.contain_file("让智能机器人走进千家万户已经离我们不远了……")
    file_name = '老是有人问参数，光圈/快门/感光度没有固定组合，根据环境和需要做调整 #中国好摄影 @抖音小助手.mp4'
    file_name = validate_title(file_name)
    print(file_name)
