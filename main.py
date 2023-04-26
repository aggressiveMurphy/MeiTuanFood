import requests  # 数据请求模块

# 1.发送请求，对于店铺数据包发送请求
url = 'https://gz.meituan.com/meishi/api/poi/getPoiList'
# 字典
data = {
    'cityName': '广州',
    'cateId': '0',
    'areaId': '0',
    'page': '3',
    'userId': '2833243488',
    'uuid': '4aa1460f13b24110a9c2.1682254284.1.0.0',
    'platform': '1',
    'partner': '126',
    'originUrl': 'https://gz.meituan.com/meishi/pn3/',
    'riskLevel': '1',
    'optimusCode': '10',
    '_token': 'eJyFkNuOokAQht+lb4fYTTfNwWQuHEFABBQVVyZzgQrKoMhJQDb77tvO7prdq00qqa+q/vpTqe+gNA9gyCOkIMSBJirBEPADNBABB+qKTUQZY0oFhVIic2D/T08kVOTArvRVMHynWOREpHw8Gh6r33ksI07C6IP7haLMEAssHhqTScCprvNqCOGxH1yipL6F2WB/vUDG1SmBeUYgO+N/IgwBM7ysHoZEEjlF5tkWkeiTBEb4SeSLCKdI4pOkL8KcQvm/iNmmD1uWw9+5/lPb7FFMWiXHjFE0bc/9indHvbZ+c8dSbqh5zG/1+8K3Tt7Ko4vxnASR08W5oWR2uj8lNy38ljiz1PDOq34SuoHhL7Va9mfOcX6at1OlWTsalD7hXJfi3SjNtweSZbfEL0zBvQv+WNJxPIGeVZ17Va+tbtdQ23eKmebefK/t12asUa839n2qr4PRoqwsk5j3wtmEEHX2VT/YVz6q/CKcykbjjjAxzHNPSrVBsP50jM3GPWwlbHSTVA2Wgbh+ObxtrEU2r16CYn++wk2EKp/v7re4mrRLz5Lb11fw4yej2awJ'
}
# 请求头
# User-Agent 浏览器基本信息
# Referer 防盗链 告诉服务器，我们发送请求的url地址是从哪里跳转过来的
headers = {
    'Referer': 'https://gz.meituan.com/meishi/pn3/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}
response = requests.get(url=url, params=data, headers=headers)
# <Response [200]>对象 200状态码 成功
print(response)
