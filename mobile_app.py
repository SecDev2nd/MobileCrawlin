import requests

url = 'https://shop.cashwalk.com/shop/event/13759'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; SM-G965N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'com.cashwalk.cashwalk',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
}
data = {
    'cashwalkAccessToken': '2ca254b4ab1d8dd8ce7603a2a149f63a6e80edfbbe2e1e7f',
    'cashwalkUserAppVersion': '1.26.46',
    'cashwalkDevice': 'android',
    'cashwalkDeviceModel': 'SM-G965N',
    'mindKeyVersion': '1',
    'cashwalkDeviceId': 'e22cf1d1d7c18248'
}

response = requests.post(url, headers=headers, data=data)


with open('tmp2.html',"w") as file:
    file.write(response.text)
print(response.text)
