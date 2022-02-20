import requests
from requests import Request

import hhru


class HeadHunter:
    def __init__(self, **kwargs):
        self.url = hhru.API_URL
        kwargs = dict(kwargs)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})

        self.headers = headers
        self.params = params

    def connect(self):
        return requests.get(self.url, headers=self.headers)

    def get_vacancies(self, text, page):
        url = self.url + "/vacancies"
        params={'text':text,
                'page': page}
        return requests.get(url, params=params, headers=self.headers).json()


