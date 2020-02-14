from apscheduler.schedulers.blocking import BlockingScheduler
import functions as fuk
from dxy_json import DxyJson
__Author__ = "OhiyoX"


def run():

    # 比较
    if json_file.num > 1:
        fuk.make_comparision(json_file)


url = "https://file1.dxycdn.com/2020/0130/492/3393874921745912795-115.json?t=26356697"

# 创建一个DxyJson类
json_file = DxyJson(url)
json_file.res_full_path = "json/1-2020-02-11-22-44-35.json"
json_file.old_res_full_path = "json/0-2020-02-11-21-58-02.json"
json_file.json = json_file.load_json(json_file.res_full_path)
json_file.old_json = json_file.load_json(json_file.old_res_full_path)
json_file.num = 2
run()