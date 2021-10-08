import requests


class BaseApi:
    headers = {
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.14(0x18000e2a) NetType/WIFI Language/zh_CN',
        'Referer': 'https://servicewechat.com/wxc60d1bd661abf316/47/page-frame.html'
    }
    host = 'https://okr.35.com/api/v2'

    def base_request_get(self, path, params=None, **kwargs):
        url = self.host + path
        return requests.get(url, headers=self.headers, params=params, **kwargs)

    def base_request_post(self, path, data=None, **kwargs):
        url = self.host + path
        return requests.post(url, headers=self.headers, data=data, **kwargs)
