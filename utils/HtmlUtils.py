# download pic by url，no support proxies
import re

import requests

from filters.LogUtils import Log
from utils import TimeUtils


def download_html(url, headers=None):
    st = 0
    try:
        redirect_url = get_redirect_url(url)
        response = requests.get(redirect_url, headers=headers, allow_redirects=False, timeout=(5, 60))
        if response.status_code == 200:
            st = 1
            content = response.text
        else:
            content = ''
    except Exception as e:
        content = ''
        Log.error(e, 'download html error,because of proxy,url:%s' % (url,))
        TimeUtils.sleep_short()

    return st, content


def get_redirect_url(base_url):
    redirect_url = base_url
    header = {
        'User-Agen': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    try:
        while True:
            # 请求
            response = requests.get(base_url, headers=header, allow_redirects=False)
            # 获取host
            host_obj = get_host(base_url)
            if host_obj is None:
                return None
            # 获取跳转的url
            if 'Location' in response.headers.keys():
                url = response.headers.get('Location')
                if 'http' not in url:
                    url = host_obj['header'] + '://' + host_obj['host'] + redirect_url  # 拼接host域名
                redirect_url = url
            else:
                break
            print("while get_redirect_url")
        return redirect_url
    except Exception as e:
        if hasattr(e, 'reason'): print('请求失败，原因：', e.reason)
        return None


def get_host(url):
    pattern = re.compile(r'(.*?)://(.*?)/', re.S)
    response = re.search(pattern, url)
    if response:
        return {'header': str(response.group(1)).strip(), 'host': str(response.group(2)).strip()}
    else:
        return None
