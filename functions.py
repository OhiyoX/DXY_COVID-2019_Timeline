import os
import time
import json


def process_json(json):
    # 处理id和modifyTime
    id_arr = []
    json_data = json['data']
    # 建立一个简化的data数组,记录id和modifytime
    for data in json_data:
        id_arr.append({'id': data['id'], 'modifyTime': data['modifyTime']})

    return id_arr


def make_record(json_file, index):
    """当新闻不存在时，作记录"""
    folder = os.path.exists('records')
    if not folder:
        os.makedirs('records')

    with open('records/' + str(json_file.num-1) + '-' + time.strftime("%Y-%m-%d", time.localtime()) + ".json",
              'a', encoding="UTF-8") as record:
        data = json_file.old_json['data']
        case = data[index]
        json.dump(case, record, ensure_ascii=False)
        record.write(",")


def make_comparision(json_file):
    data_json_new = process_json(json_file.json)
    data_json_old = process_json(json_file.old_json)

    # 循环比较两个json
    flag = True
    for case_old in data_json_old:
        if case_old in data_json_new:
            pass
        else:
            flag = False
            index = data_json_old.index(case_old)
            make_record(json_file, index)

    if flag:
        os.remove(json_file.old_res_full_path)
