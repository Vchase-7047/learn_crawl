# 抓取猫眼电影的TOP100的电影名称、时间、评分、图片等信息 -->https://maoyan.com/board/4
import requests
import re
import json
from requests.exceptions import RequestException
import time
import os


# get_one_page()获取首页的源代码
def get_one_page(url):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/70.0.3538.77 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)'
                         '</p>.*?releasetime.*?>(.*?)</p>.*?(\d\.).*?(\d).*?</dd>', re.S)
    results = re.findall(pattern, html)
    for result in results:
        yield {  # 使用yield，使该函数变成generator的函数，调用时遇到yield就返回一次，此时for循环可以看作被“暂停了”，
            # 下次调用就保持上次循环的状态进入下一次循环，有点类似break；等到遍历完results就结束
            'sort': result[0],
            'image': result[1],
            'title': result[2].strip(),
            'star': result[3].strip()[3:] if len(result[3]) > 3 else '',
            'time': result[4].strip()[5:] if len(result[4]) > 5 else '',
            'score': result[5].strip() + result[6].strip()
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for result in parse_one_page(html):  # 调用一次就返回一个dict，所以需要用到循环
        write_to_file(result)


if __name__ == '__main__':
    my_file = 'result.txt'
    if os.path.exists(my_file):
        os.remove(my_file)
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)  # 防止速度过快被检测到导致无响应