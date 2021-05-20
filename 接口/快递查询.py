import requests

urlstr = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-773058962040428-shentong-KUAIDI1621064031652.html'

s = requests.session()
r = s.post(urlstr)

print(r.json())
print(r.json()['data'][0]['context'])

