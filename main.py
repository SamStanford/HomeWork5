import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': file_path}
        headers = {'Authorization': 'OAuth ' + self.token}

        response = requests.get(url, headers=headers, params=params)
        if 200 <= response.status_code < 300:
            data = response.json()

            url = data['href']
            with open(path_to_file, 'rb') as f:
                response = requests.put(url, files={'file': f})
            return response.status_code


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'photo_2023-04-13_13-17-49.jpg'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

