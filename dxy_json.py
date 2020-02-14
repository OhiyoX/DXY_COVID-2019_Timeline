import time
import os
import json
import requests


class DxyJson:
    """json对象"""
    def __init__(self, url):
        self.url = url
        self.num = 0
        self.res = 'json'
        self.res_full_path = ''
        self.old_res_full_path = ''
        self.json = {}
        self.old_json = {}

    def update(self):
        """下载文件"""
        # 更新旧json
        if self.num != 0:
            self.old_json = self.json
            self.old_res_full_path = self.res_full_path

        the_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        name = str(self.num) + "-" + str(the_time) + ".json"
        self.res_full_path = self.res + '/' + name

        # 下载json
        folder = os.path.exists(self.res)
        if not folder:
            os.makedirs(self.res)

        json = requests.get(self.url)
        with open(self.res_full_path, 'wb') as f_json:
            f_json.write(json.content)
        self.json = self.load_json(self.res_full_path)

        self.num += 1

    def load_json(self, path):
        with open(path, 'r', encoding='UTF-8') as f_json:
            return json.loads(f_json.read())
