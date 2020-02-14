from apscheduler.schedulers.blocking import BlockingScheduler
import functions as fuk
from dxy_json import DxyJson
__Author__ = "OhiyoX"


def run():
    # 下载
    json_file.update()

    # 比较
    if json_file.num > 1:
        fuk.make_comparision(json_file)


if __name__ == '__main__':

    url = "https://file1.dxycdn.com/2020/0130/492/3393874921745912795-115.json?t=26356697"

    # 创建一个DxyJson类
    json_file = DxyJson(url)

    scheduler = BlockingScheduler()
    scheduler.add_job(run, 'interval', minutes=30)
    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemExit):
        pass


