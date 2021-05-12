import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def create_dir(self, dir_name):
        """
        Создает папку на яндекс диске
        """
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': dir_name}
        headers = {'Authorization': self.token}
        response = requests.put(url, params=params, headers=headers)
        if response.status_code == 201:
            return 'Папка создана на яндекс диске!'
        else:
            # status_code = f'Код ответа - {response.status_code}\n'
            # error_message = response.json()['message']
            return 'Папка с таким именем уже есть!'

    def get_href_to_upload(self, file_name, dir_name=None):
        """
        Получает ссылку для загрузки файла
        """
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Authorization': self.token}
        if dir_name:
            params = {'path': dir_name + '/' + file_name}
        else:
            params = {'path': file_name}
        response = requests.get(url, params=params, headers=headers)
        if response.ok:
            print('Ссылка получена!')
            return True, response.json()['href']
        else:
            status_code = f'Код ответа - {response.status_code}.\n'
            error_message = response.json()['message']
            return False, f'{status_code}{error_message}\n'

    def upload(self, file_name: str, dir_name=None):
        """
        Метод загружает файл file_path на яндекс диск
        """
        status, result = self.get_href_to_upload(file_name, dir_name)
        if status is True:
            href = result
            with open(file_name, encoding='utf-8') as f:
                response = requests.put(href, files={'file': f})
            if response.status_code == 201:
                return f'Файл "{file_name}" успешно загружен на яндекс диск!\n'
            else:
                status_code = f'Код ответа - {response.status_code}.\n'
                error_message = response.json()['message']
                return f'Упс... Что-то пошло не так!\n{status_code}{error_message}\n'
        else:
            return result
