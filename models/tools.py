import json
import os
import Core.you_get as y
import models.menu as m
import models.constants as c
from tkdev4 import Icon_Empty

# 加载控件信息

# 尝试更改值
def change():
    # app =
    m.App().captions_var.set(0)

def write(filename, string):
    """
    写入操作函数
    :param filename: 文件路径
    :param string: 写入内容
    :return: 无返回值
    """
    with open(filename, 'w', encoding='utf-8') as file_object:
        file_object.write(string)

def get_firefox_cookie_path(*args):
    """
    从火狐获得cookies路径
    :param args: 不用填写
    :return: 返回cookies路径
    """
    cookiepath_common = os.environ['APPDATA'] + r"\Mozilla\Firefox\Profiles"
    folds_arr = os.listdir(cookiepath_common)
    folds_end = [os.path.splitext(file)[-1][1:] for file in folds_arr]

    if 'default-release' in folds_end:
        cookie_fold_index = folds_end.index('default-release')
    else:
        cookie_fold_index = folds_end.index('default')
    cookie_fold = folds_arr[cookie_fold_index]
    cookie_path = os.path.join(cookiepath_common, cookie_fold)
    return os.path.join(cookie_path, 'cookies.sqlite')

def load_json(json_path):
    """
    加载 json 文件
    :return: 返回转换好的对象
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        video_json = json.load(f)
        # print(video_json)
        return video_json

def get_json_stream(json_obj):
    """
    获得视频清晰度
    :param json_obj: 要解析的json路径
    :return: 返回清晰度列表
    """
    # 转为json对象
    global item
    try:
        json_obj = load_json(json_obj)
        # 获得储存信息的streams
        json_stream = json_obj["streams"]

        # 读取
        for item in json_stream:
            # 获得清晰度中文的字典
            c.STREAM_DICT[item] = json_stream[item]['quality']
            # 获得便于查询的字典
            c.STREAM_DICT_VK[json_stream[item]['quality']] = item
        return 1
    except:
        return 0

def get_json(url: str, cookies=''):
    """
    获得json
    :param url: 网页链接
    :param cookies: 可选 cookies
    :return: 返回json（
    """
    if cookies == '':
        return y.run_cmd([r".\depend\you-get.exe", '--json', url])
    else:
        return y.run_cmd([r".\depend\you-get.exe", '--json', url, '-c', cookies])

def show_info(title, message, time=10):
    from plyer import notification
    notification.notify(
        title=title,
        message=message,
        app_icon='icon.ico',
        timeout=time,
    )

