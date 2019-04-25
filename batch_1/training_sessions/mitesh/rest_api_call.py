import urllib.request as req

# response = req.urlopen('https://www.amazon.com')
url="https://www.amazon.com"
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

reqWithHeader = req.Request(url, headers = headers)
response = req.urlopen(reqWithHeader)

data = response.read()

print(data)
