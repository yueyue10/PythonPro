import re
from string import digits


def get_bqb_name(url_path):
    bqb_name_str = url_path.replace('https://www.v2fy.com/p/', '').replace('/', '')
    bqb_name_str1 = bqb_name_str.translate(str.maketrans('', '', digits))
    # print(bqb_name_str1)
    bqb_name_str2 = bqb_name_str1.strip('BQB_')
    if bqb_name_str2.find('_') >= 0:
        bqb_name_str2 = bqb_name_str2[bqb_name_str2.rfind('_') + 1:]
    return bqb_name_str2


def get_url_name(url_str):
    if not url_str:
        url_str = "https://www.v2fy.com/p/076Moe可爱萝莉_BQB/"
    bqb_name_str = url_str.replace('https://www.v2fy.com/p/', '').replace('/', '')
    return get_chinese_str(bqb_name_str)


def get_chinese_str(name_str):
    bqb_name = re.findall('[\u4e00-\u9fa5]+', name_str)
    print(bqb_name[0])


if __name__ == '__main__':
    urls = ["https://www.v2fy.com/p/077TuHi_土嗨_BQB/",
            "https://www.v2fy.com/p/076Moe可爱萝莉_BQB/", "https://www.v2fy.com/p/075Vtuber_虚拟youtuberBQB/",
            "https://www.v2fy.com/p/073腾讯与老千妈BQB/", "https://www.v2fy.com/p/072PaiYiPai_微信拍一拍👋BQB/",
            "https://www.v2fy.com/p/059_Couple_Head_沙雕情侣头像BQB/", "https://www.v2fy.com/p/058_2020Coronavirus_冠状病毒BQB/",
            "https://www.v2fy.com/p/048SpongeBob_海绵宝宝BQB/"]
    for url in urls:
        name = get_bqb_name(url)
        print(name)
    # print('www.example.com'.strip('cmowz.'))
