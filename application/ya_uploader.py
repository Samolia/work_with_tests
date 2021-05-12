import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def create_dir(self, dir_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': dir_name}
        headers = {'Authorization': self.token}
        response = requests.put(url, params=params, headers=headers)
        return response.status_code
