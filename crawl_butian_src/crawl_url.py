import requests
import json
import threadpool
import time
from bs4 import BeautifulSoup
import threading
from requests.exceptions import RequestException


lock = threading.Lock()
def crawl_company_number(url, page):
    headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "16",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "xxxx", # 填入自己登陆该网站后的cookie信息
        "Host": "butian.360.cn",
        "Origin": "https://butian.360.cn",
        "Referer": "https://butian.360.cn/Reward/plan",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"}
    data = {
        "s": "1",
        "p": page,
        "token": " "
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return json.loads(response.text)
        return None
    except RequestException:
        return "Error, None data."


def request_target(url):
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
               "Cookie": "xxx",# 填入自己登陆该网站后的cookie信息
               "Host": "butian.360.cn",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return "Error, None data."


def write_company_info(company_id, company_name, real_url):
    with open('360gy_src_info', 'a', encoding='utf-8') as f:
        f.write(company_id + ' ' + company_name + ' ' + real_url +  '\n')


def write_company_domain(real_url):
    with open('360gy_src_url', 'a', encoding='utf-8') as f:
        f.write(real_url +  '\n')


def mul_thread(i):
    time.sleep(1)
    url = "https://butian.360.cn/Reward/pub"
    company_info = crawl_company_number(url, i)
    # current_page = company_info['data']['current']
    current_list = len(company_info['data']['list'])
    try:
        lock.acquire()
        for j in range(0, current_list):
            company_name = company_info['data']['list'][j]['company_name']
            company_id = company_info['data']['list'][j]['company_id']
            url1 = "https://butian.360.cn/Loo/submit?cid=" + str(company_id)
            data = request_target(url1)
            soup = BeautifulSoup(data, 'lxml')
            real_url = soup.find_all(name='input', attrs={"name": "host"})
            write_company_info(company_id, company_name, real_url[0].attrs['value'])
            write_company_domain(real_url[0].attrs['value'])
    finally:
        lock.release()

if __name__ == '__main__':
    num = []
    for i in range(1, 172):
        num.append(i)

    pool = threadpool.ThreadPool(40)  # 建立线程池，控制线程数量为40
    reqs = threadpool.makeRequests(mul_thread, num)  # 构建请求，mul_thread为要运行的函数，num为要多线程执行函数的参数
    [pool.putRequest(req) for req in reqs]  # 多线程一块执行
    pool.wait()  # 线程挂起，直到结束