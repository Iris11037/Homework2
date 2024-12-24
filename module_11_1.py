import requests

requ = requests.get('https://developer.mozilla.org/ru/docs/Web/HTTP/Methods')

print(requ.encoding)
print(requ.ok)
print(requ.content[0:1000])
print(requ.status_code)
print(requ.history)
