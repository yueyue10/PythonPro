import os, base64
import time

from aip import AipOcr


# base64写入图片
def base64_to_image():
    # str = r"iVBORw0KGgoAAAANSUhEUgAAANwAAAAoCAIAAAAaOwPZAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAQuSURBVHhe7ZptmoMgDIR7rh6o5+lpvEwP01XUGshAokgX+8z+7PKRTF6SoN7e/KMCnSlw68wemkMF3oSSEHSnAKHsLiQ0iFCSge4UIJTdhYQGEUoy0J0ChLK7kNAgQkkGulOAUHYXEhpEKMlAdwpcG8rhcRv/HkN3stIgW4F88DYoX89nObjmANuOc0eMXpHHcyX9+mowhgHKmdlChM0BZzvzet6DSSW7xjEWk8Hu+/O1x7zF1237/Uu4t/O46V6sZuARoZb9KqbO7On4rJlykqcYYnNAjSbx3Gmrj6WTzxirVlA+90F82G+nm4fX3zOxgqyKqRaUU7b8FpRDOeyjJa7k5oByT1yWse4mxfDC3NrrprnQtQeUMuUXoURmCGHdKfl/oTS8MElxu2mudO0BXUCZL8efVGU0EmsQjkGpM2H8y/CwGtW1C3el8ywxhHKWxgOlaPNj0VcRRW+OoiKvCXF0o6YeXWLQDaNQyMf1Clhsi22D9HUNXOBCVZamaBmiO5BxRdRQOt3M3oFUAD4/HDolSChx7AvXzRIJQtgsUfMu6HB+HglNLc5d5KiwpcAqTH7Idk/lvLD9Z0rUx4vYWL2UJ4WY6XbdL91ML57+EjsRNEMnw/LCrKklN9NNkbuLvKsdabjM/ZMByh+PDWuuw6kDEYXPzeSfzGARlNG1M1ENRCfGLlUuJ5MVTg+UyxGzC+1+KN/DkDyuTSVbqo7vNnagfKPTrH9b8pQtgQ/PRCifDTaUJaIWw8adUycklLrcppkyCZfkJ5cYlSZnQTkmsYf58OYAlMpg6JnlhYlC9uxhIdWvbr1NS8Ahc9pgQlkkai3fOorVUK4JGeYTJIgVTm+mnCqrmSfOgDJ0mOlOlhcmClk3M0KmPzeF0mnDGVB6LjqbmKB8p5GRQ34DStRCdpEpp5MRNWRNocwsjk9i7nyqugzPYTWUSZuqe0qVucAT5tgH9ITmxEdCdihjpcCVAgfI8uJ4pgx3K3UhgBeRQ9dtbJmjp1TnYmsKoSH1UGqKE23mxlrsri4yKsuAFnZ5BrAugypw0/IdSvHmxHJbEI6lREzj0asuOc7TR8BONdd9pNKCo4LRNY9CdgCEXjqObDhQvsFpy7z7DsqHP9khxp9DzNeKbSR+Iy3/n31tqVFYe17xFUZkTu507+4px4USFwBRm32lbzFyXphgRMtn3cwqqaef8a0UrMHlaJYM8RC1Iq2DeOXvKUdVjALmzromST8+4N+Egm9rrwzl/DpAVlddnE9su36Jyx6ECtkUxufaUMJOzfwQsxldUbnTLyO/ckCcNsS112yDmkkGF/4xKL8rHndrowChbKMrV61QgFBWiMepbRQglG105aoVChDKCvE4tY0ChLKNrly1QgFCWSEep7ZRgFC20ZWrVihAKCvE49Q2ChDKNrpy1QoF/gDXIhmWmc+CSAAAAABJRU5ErkJggg=="
    str = "iVBORw0KGgoAAAANSUhEUgAAAGQAAAAtCAIAAADX11mnAAACkUlEQVR42u3Zv0sDMRQH8HOygy5Vq4iICIKCUsFF/BdER3Gzf0DB0f9ARSelDkJBVATdOks3BxGnTroUkbqI6CTiIJwPDs5wuUte7t4ld7Hhu5SmP+7DSy6XOG63oZtjwTWM7DX5kHzzVm9f7rFO3m8gen6L9cpxZWkj871yPww9srTVPC8b5ixthWYPlgYyMqzN19McmZYW3iAmKwu87CajH4ad4w02fIfG6g4+0P98fggf6d/7mvr0o0rmpMcURWYQi5XysXRXloCJJzOFFZDKBJb0rYxjTQ8X+JBhiWcovkPAgm/Vj2eI/1JpSsJLGagsqRTfTYoVaMmxQqUgc7M1Y1iLnVYGsQKlFHgJXngyh7aswCuKLBSrvjvmRQNW1NIBT0aGVSz3QHwyJFbalcXTCOYsKRlxZXlkEPBi+YxghbpIJ3gBmRxrpnwVFczUzuPqx5IKpj5nIe+DprCiRHRglQqPbKiwMHAJ159JsO6L22w0VVb7uwkRY0Wpqa7axRw5HoYYMtUHHbFFzrBCP6I0MKMEMRbmsS6vx70k9MVjhZJhIGyoLBIvjIJVWJhtiVAvJIFtWDG88ARdrMhNGHz07TrE7l+rtCD/CwvjJejskbFwXSxUZ48spefHo5UXY9vKaWAluSHyWO3+Cz98DT5VliA0WAP3+xCSaSu2FI+1NrnOhl+a/l3b7WEgoXdDPJm8ssRkMQ4saMsKvFgpjw85u8Go1DcMkRCEZSV94iFckaWC5aocsgoIBCesyGdp2uWrDizx8b3SWbSrchwdY2P+YLQhSFpYUjLxVoxg6BEyZaWyBGTIEUe+s5xRrInBZSro+tkdxM1qo6ksQq8sk5ENQ1ovmyuLyqv68xBIprB+Afw0p95qshrYAAAAAElFTkSuQmCC"
    img_data = base64.b64decode(str)
    file = open('code.jpg', 'wb')
    file.write(img_data)
    file.close()


def _get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 调用百度图片识别
def baidu_discern(image):
    """ 你的 APPID AK SK """
    APP_ID = '17788488'
    API_KEY = 'MUcPtsje9zlvXN7cItnbUC1H'
    SECRET_KEY = 'WRKeQ4rq85P9yyARMENFT6yeBuV3Mm4N'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # 普通识别模式
    # ret = client.webImage(image)
    # 高精度识别
    ret = client.basicAccurate(image)
    # print(ret)
    words = ret.get('words_result')
    if words:
        return ''.join(words[0]['words'].split(' '))
    else:
        return ''


# 识别图片里面的二维码
def baidu_1(filename='code.jpg'):
    # 一、从图片里面获取数据
    image = _get_file_content(filename)
    ret1 = baidu_discern(image)
    print(ret1)
    return ret1


# 识别base64里面的二维码
def baidu_2(base64_str=''):
    # 二、从base64里面获取数据
    if not base64_str:
        base64_str = "iVBORw0KGgoAAAANSUhEUgAAAGQAAAAtCAIAAADX11mnAAACkUlEQVR42u3Zv0sDMRQH8HOygy5Vq4iICIKCUsFF/BdER3Gzf0DB0f9ARSelDkJBVATdOks3BxGnTroUkbqI6CTiIJwPDs5wuUte7t4ld7Hhu5SmP+7DSy6XOG63oZtjwTWM7DX5kHzzVm9f7rFO3m8gen6L9cpxZWkj871yPww9srTVPC8b5ixthWYPlgYyMqzN19McmZYW3iAmKwu87CajH4ad4w02fIfG6g4+0P98fggf6d/7mvr0o0rmpMcURWYQi5XysXRXloCJJzOFFZDKBJb0rYxjTQ8X+JBhiWcovkPAgm/Vj2eI/1JpSsJLGagsqRTfTYoVaMmxQqUgc7M1Y1iLnVYGsQKlFHgJXngyh7aswCuKLBSrvjvmRQNW1NIBT0aGVSz3QHwyJFbalcXTCOYsKRlxZXlkEPBi+YxghbpIJ3gBmRxrpnwVFczUzuPqx5IKpj5nIe+DprCiRHRglQqPbKiwMHAJ159JsO6L22w0VVb7uwkRY0Wpqa7axRw5HoYYMtUHHbFFzrBCP6I0MKMEMRbmsS6vx70k9MVjhZJhIGyoLBIvjIJVWJhtiVAvJIFtWDG88ARdrMhNGHz07TrE7l+rtCD/CwvjJejskbFwXSxUZ48spefHo5UXY9vKaWAluSHyWO3+Cz98DT5VliA0WAP3+xCSaSu2FI+1NrnOhl+a/l3b7WEgoXdDPJm8ssRkMQ4saMsKvFgpjw85u8Go1DcMkRCEZSV94iFckaWC5aocsgoIBCesyGdp2uWrDizx8b3SWbSrchwdY2P+YLQhSFpYUjLxVoxg6BEyZaWyBGTIEUe+s5xRrInBZSro+tkdxM1qo6ksQq8sk5ENQ1ovmyuLyqv68xBIprB+Afw0p95qshrYAAAAAElFTkSuQmCC"
    image = base64.b64decode(base64_str)
    ret2 = baidu_discern(image)
    print(ret2)
    return ret2


if __name__ == '__main__':
    start = int(time.time())
    # base64_to_image()
    # baidu_1()
    baidu_2()
    time_elapsed = time.time() - start
    print('The code run {:.0f}s'.format(time_elapsed))

