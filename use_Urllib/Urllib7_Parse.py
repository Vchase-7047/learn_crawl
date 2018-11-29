from urllib import parse


# urlparse()
result = parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(result, '\n')
print(type(result), result.scheme, result[0], result.netloc, result[1], sep='\n')

# urlunparse()
data = ['http', 'www.baidu.com', 'index.html', 'user', 'id=6', 'commant']
print(parse.urlunparse(data))

# urlsplit()
result1 = parse.urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result1)

# urlunsplit()
data1 = ['http', 'www.baidu.com', 'index.html', 'id=6', 'commant']
print(parse.urlunsplit(data1))

# urlencode()
params = {
    'name': 'vchase',
    'age': '21'
}
base_url = 'http://www.baidu.com?'
url = base_url + parse.urlencode(params)
print(url)

# parse_qs()
query = 'name=vchase&age=21'
print(parse.parse_qs(query))

# quote()
keyword = '壁纸'
url1 = 'https://www.baidu.com/s?wd=' + parse.quote(keyword)
print(url1)

# unquote()
url2 = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(parse.unquote(url2))