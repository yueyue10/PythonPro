import re


def format_str_list(str_list):
    strs = []
    for str in str_list:
        str = format_str_info(str)
        if str != '':
            strs.append(str)
    return strs


def format_str_info(format_info):
    if format_info:
        format_info = format_info.replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').replace('\'',
                                                                                                                 '\"')
        format_info.lstrip()
        format_info = filter_emojis(format_info)
    else:
        format_info = ""
    return format_info


def filter_emojis(desstr, restr=''):
    """    过滤表情[\ud83c\udc00-\ud83c\udfff]|[\ud83d\udc00-\ud83d\udfff]|[\u2600-\u27ff]
    """
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)
