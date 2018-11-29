import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException


try:
    response = requests.get('http://www.baidu.com', timeout=0.005)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
except HTTPError:
    print('Http error')
except RequestException:
    print('Error')
