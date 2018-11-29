from urllib.request import ProxyHandler, build_opener
from urllib.request import URLError


proxy_handler = ProxyHandler(
    {
        'http': 'http://127.0.0.1:59576',
        'https': 'https://127.0.0.1:59576'
    }
)

open = build_opener(proxy_handler)
try:
    response = open.open('https://httpbin.org/get')
    print(response.read().decode('utf8'))
except URLError as e:
    print(e.reason)