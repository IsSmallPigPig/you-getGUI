import requests
import shutil
import threading
import tkinter.ttk
from tkinter import filedialog
import Core.you_get as c
import Tool.menu as m
import os
import json
import Tool.constants as v
from tkinter import messagebox

# 获得父目录
pwd = os.getcwd()
father_path = pwd
# 获得用户主目录
home = os.path.expanduser('~')
# 是否通过检查
flag = 1
# 清晰度
item = ''


def check_http_proxy(ip, port):
    """
    验证代理有效性
    :param port: 端口
    :param ip: 主机
    :return: 返回真假
    """
    import requests

    proxies = {'http': '%s:%s' % (ip, port),
               'https': '%s:%s' % (ip, port),
               }
    url = "http://www.baidu.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=5)
        print(response.text)
    except Exception as e:
        print(f"请求失败，代理IP无效！{e}")
        return 0
    else:
        print("请求成功，代理IP有效！")
        return 1


def check_socks5_proxy(ip, port, username, password):
    """
    验证 socks5 代理是否有效
    :param ip: 主机
    :param port: 端口
    :param username: 用户名
    :param password: 密码
    :return: 返回真假
    """
    if ip != '' and port != '':
        try:
            # requests.get('http://www.baidu.com/', proxies={"http":"http://"+ip+':'+port},timeout=2)
            # session = Session()
            proxy = {
                "http": "socks5://" + ip + ':' + port,
                "https": "socks5://" + ip + ':' + port
            }
            url = "http://www.baidu.com/"
            req = requests.get(url, proxies=proxy)
            print(req)

        except:
            print('connect failed')
            return 0
        else:
            return 1
    elif ip != '' and port != '' and username != '' and password != '':
        try:
            # requests.get('http://www.baidu.com/', proxies={"http":"http://"+ip+':'+port},timeout=2)
            # session = Session()
            proxy = {
                "http": "socks5://" + ip + ':' + port + "@" + username + ":" + password,
                "https": "socks5://" + ip + ':' + port + "@" + username + ":" + password,
            }
            url = "http://www.baidu.com/"
            req = requests.get(url, proxies=proxy)
            print(req)

        except:
            print('connect failed')
            return 0
        else:
            return 1


def set_cmd(*args):
    """
    准备指令
    :param args: 不需要填形参
    :return: 无返回值
    """
    global flag

    # 禁用下载按钮
    m.download_Button['state'] = 'disabled'
    # 禁用确认按钮
    m.makesure_Button['state'] = 'disabled'
    # 禁用下拉框
    m.combobox['state'] = 'disabled'

    # 检查视频链接输入框是否有填写
    if m.url_Entry.get() != "" and m.url_Entry.get() != '视频下载链接':
        # 设为常量
        v.URL = m.url_Entry.get()
        # 填入链接
        c.video_url(v.URL)
    else:
        messagebox.showerror(message="请输入视频链接")
        flag = 0
        return None

    # 检查输出文件名称输入框是否有填写
    if m.filename_Entry.get() != "" and m.filename_Entry.get() != '输出文件名称':
        # 设为常量
        v.FILENAME = m.filename_Entry.get()
        # 填入文件名
        c.filename(v.FILENAME)
    else:
        pass

    # 检查文件保存路径输入框是否有填写
    if m.filepath_Entry.get() != "" and m.filepath_Entry.get() != '文件保存路径':
        # 设为常量
        v.SAVE_PATH = m.filepath_Entry.get()
        # 填入保存路径
        c.output_dir(v.SAVE_PATH)
    else:
        result = messagebox.askquestion(message="默认以用户目录作为下载位置，是否继续")
        if result == "yes":
            v.SAVE_PATH = home
            c.output_dir(v.SAVE_PATH)
        else:
            flag = 0
            return None

    # 检查cookies保存路径输入框是否有填写
    if m.cookiespath_Entry.get() != "" and m.cookiespath_Entry.get() != 'cookies 路径':
        print(v.COOKIES_PATH)
        # 设为常量
        v.COOKIES_PATH = m.cookiespath_Entry.get()
        # 填入cookies位置
        c.cookies_file(v.COOKIES_PATH)
        print(v.COOKIES_PATH)
    else:
        result = messagebox.askquestion(message="未填写 cookies 将无法下载会员和高清视频，是否继续")
        print(result)
        print(v.COOKIES_PATH)

        if result == "yes":
            # 设为常量
            v.COOKIES_PATH = ''
        else:
            flag = 0
            return None

    # 检查指定播放器输入框是否有填写
    if m.player_Entry.get() != "" and m.player_Entry.get() != '指定播放链接视频的本地播放器':
        # 设为常量
        v.PLAYER_NAME = m.player_Entry.get()
        # 填入指定播放器
        c.player(v.PLAYER_NAME)
    else:
        pass

    # 检查套接字延时输入框是否有填写
    if m.second_Entry.get() != "" and m.second_Entry.get() != '套接字延时':
        # 设为常量
        v.SECONDS = m.second_Entry.get()
        # 填入延迟秒数
        c.seconds(v.SECONDS)
    else:
        pass

    # 检查http_host输入框是否有填写
    if m.httphost_Entry.get() != "" and m.httphost_Entry.get() != 'HOST' and m.httpport_Entry.get() != "" and m.httpport_Entry.get() != 'PORT':
        # 设为常量
        v.HTTP_HOST = m.httphost_Entry.get()
        v.HTTP_PORT = m.httpport_Entry.get()
        # 检查代理有效性
        flag = check_http_proxy(v.HTTP_HOST, v.HTTP_PORT)

        if flag == 1:
            # 填入http
            c.http_proxy(v.HTTP_HOST, v.HTTP_PORT)

            check_http_proxy(v.HTTP_HOST, v.HTTP_PORT)

        else:
            messagebox.showerror(title="代理无效", message="请检查代理是否有效")

    else:
        pass

    if m.sockshost_Entry.get() != "" and m.sockshost_Entry.get() != 'HOST' and m.socksport_Entry.get() != "" \
            and m.socksport_Entry.get() != 'PORT' and m.socksusername_Entry.get() != "" \
            and m.socksusername_Entry.get() != 'USERNAME' and m.sockspassword_Entry.get() != "" \
            and m.sockspassword_Entry.get() != 'PASSWORD':

        # 设为常量
        v.SOCKS_HOST = m.sockshost_Entry.get()
        v.SOCKS_PORT = m.socksport_Entry.get()
        v.SOCKS_USERNAME = m.socksusername_Entry.get()
        v.SOCKS_PASSWORD = m.sockspassword_Entry.get()
        # 验证代理
        flag = check_socks5_proxy(v.SOCKS_HOST, v.SOCKS_PORT, v.SOCKS_USERNAME, v.SOCKS_PASSWORD)

        if flag == 1:
            # 填入socks
            c.socks5_up(v.SOCKS_HOST, v.SOCKS_PORT, v.SOCKS_USERNAME, v.SOCKS_PASSWORD)
        else:
            messagebox.showerror("代理无效", '请检查 socks5 代理是否正确填写')

    # 检查socks_host输入框是否有填写
    elif m.sockshost_Entry.get() != "" and m.sockshost_Entry.get() != 'HOST' and m.socksport_Entry.get() != "" and m.socksport_Entry.get() != 'PORT':
        # 设为常量
        v.SOCKS_HOST = m.sockshost_Entry.get()
        v.SOCKS_PORT = m.socksport_Entry.get()
        if flag == 1:
            # 填入socks
            c.socks5_hp(v.SOCKS_HOST, v.SOCKS_PORT)
        else:
            messagebox.showerror("代理无效", '请检查 socks5 代理是否正确填写')

    else:
        pass

    # 开启自动重命名
    if m.autorename_var.get() == 1:
        c.auto_rename()
    else:
        pass

    # 开启多P下载
    if m.playlist_var.get() == 1:
        c.playlist()
    else:
        pass

    # 开启忽略SSL错误
    if m.skipssl_var.get() == 1:
        c.insecure()
    else:
        pass

    # 开启 m3u8
    if m.m3u8_var.get() == 1:
        c.m3u8()
    else:
        pass

    # 开启调试
    if m.debug_var.get() == 1:
        c.auto_rename()
    else:
        pass

    # 关闭下载字幕
    if m.caption_var.get() == 0:
        c.no_caption()
    else:
        pass

    # 开启校验文件
    if m.check_var.get() == 1:
        c.postfix()
    else:
        pass

    # 关闭合并视频
    if m.merge_var.get() == 1:
        c.no_merge()
    else:
        pass

    # 关闭检查大小
    if m.checksize_var.get() == 0:
        c.skip_existing_file_size_check()
    else:
        pass

    # 获得信息
    if m.getinformation_var.get() == 1:
        v.GET_INFORMATION = c.info(v.URL)
        m.download_Button['state'] = 'disabled'
        m.output_cmd.insert('insert', v.GET_INFORMATION)
        return None
    elif m.getinformation_var.get() == 1 and v.COOKIES_PATH != '':
        v.GET_INFORMATION = c.info(v.URL, cookies=v.COOKIES_PATH)
        m.download_Button['state'] = 'disabled'
        m.output_cmd.insert('insert', v.GET_INFORMATION)
        return None
    else:
        m.download_Button['state'] = 'disabled'

    # 获得解析 url
    if m.geturl_var.get() == 1:
        v.GET_URL = c.get_url(v.URL)
        m.download_Button['state'] = 'disabled'
        m.output_cmd.insert('insert', v.GET_URL)
        return None
    elif m.geturl_var.get() == 1 and v.COOKIES_PATH != '':
        v.GET_URL = c.get_url(v.URL, cookies=v.COOKIES_PATH)
        m.download_Button['state'] = 'disabled'
        m.output_cmd.insert('insert', v.GET_URL)
        return None
    else:
        m.download_Button['state'] = 'disabled'

    # 获得解析 json
    if m.getjson_var.get() == 1:
        v.GET_JSON = c.get_json(v.URL)
        m.download_Button['state'] = 'disabled'
        m.output_cmd.insert('insert', v.GET_JSON)
        return None
    elif m.getjson_var.get() == 1 and v.COOKIES_PATH != '':
        v.GET_JSON = c.get_json(v.URL, cookies=v.COOKIES_PATH)
        m.download_Button['state'] = 'disabled'
        m.output_cmd.insert('insert', v.GET_JSON)
        return None
    else:
        m.download_Button['state'] = 'disabled'

    # 查看版本号
    if m.getversion_var.get() == 1:
        v.GET_VERSION = c.get_version(v.URL)
        m.download_Button['state'] = 'disabled'
        m.output_cmd.insert('insert', v.GET_VERSION)
        return None
    else:
        m.download_Button['state'] = 'disabled'

    # 是否覆盖重名文件
    if m.getjson_var.get() == 1:
        c.force()
    else:
        pass
    # 启用下载按钮
    # m.download_Button['state'] = 'active'
    # 启用确认按钮
    # m.makesure_Button['state'] = 'active'
    # 启用下拉框
    # m.combobox['state'] = 'active'

def makesure_thread(*args):
    """
    创建线程并防止多次创建
    :param args: 不用填形参
    :return: 不返回值
    """
    # 创建线程
    makesure = threading.Thread(target=makesure_command, args='')

    # 启动线程
    if makesure.is_alive() is False:
        makesure.start()

    else:
        pass


def save_path_command(*args):
    """
    实现打开目录操作
    :param args:不用填形参
    :return:返回用户打开的路径
    """
    open_save_path = filedialog.askdirectory(title='打开保存路径', initialdir=home)
    print(open_save_path)
    m.save_path_var.set(open_save_path)
    return open_save_path


def open_cookies(*arg):
    """
    上传 cookies 操作
    :param arg:不用填形参
    :return:用户选择的文件路径
    """
    cookies_file = filedialog.askopenfilename(title='打开 cookies 存储路径', initialdir=home)
    print(cookies_file)
    m.cookiespath_var.set(cookies_file)
    return cookies_file


def combobox_commands(*args):
    """
    响应下拉框操作
    :param args: 不填形参
    :return: 不返回值
    """

    # 获得当前下拉框选项所对应的清晰度代码
    v.STREAM_ID = v.STREAM_DICT_VK.get(m.combobox.get())
    print(v.STREAM_ID)


def disabled_startdownload(check: tkinter.IntVar):
    """
    禁止启动下载操作
    :param check: 检查按钮，以便获得状态
    :return: 不返回值
    """
    if check.get() == 1:
        m.download_Button['state'] = 'disabled'
    else:
        m.download_Button['state'] = 'disabled'


def write(filename, string):
    """
    写入操作函数
    :param filename: 文件路径
    :param string: 写入内容
    :return: 无返回值
    """
    with open(filename, 'w', encoding='utf-8') as file_object:
        file_object.write(string)


def download_json(url: str):
    """
    下载视频 json 到本地
    :param url: 视频链接
    :return: 无返回值
    """
    video_json = c.get_json(url)
    write("%s/video_json.json" % home, video_json)


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
            v.STREAM_DICT[item] = json_stream[item]['quality']
            # 获得便于查询的字典
            v.STREAM_DICT_VK[json_stream[item]['quality']] = item
            m.download_Button['state'] = 'disabled'
        return 1
    except:
        messagebox.showerror(title="链接错误",
                             message="链接有误，请检查链接是否是 you-get 支持的网站或者链接是否填写正确")
        return 0




def bilibili_stream(*args):
    """
    针对B站做的清晰度选择
    :param args: 不用填形参
    :return: 无返回值
    """
    print(father_path)
    stream_id = get_json_stream("%s/video_json.json" % home)
    # 获得所有值
    items = []
    for i in stream_id:
        items.append(stream_id.get(i))
    return items


def makesure_command(*args):
    """
    确认信息
    :return: 无返回值
    """
    # 传入真伪判断值
    global flag
    # 清空列表
    c.cmd_list = [r".\Core\you-get.exe"]
    set_cmd()
    if flag == 1:
        print("通过")
        # 下载json
        write("%s/video_json.json" % home, c.get_json(v.URL, cookies=v.COOKIES_PATH))
        flag_json = get_json_stream("%s/video_json.json" % home)
        if flag_json == 1:
            # 获得所有键
            v.STREAM_KEYS_LIST = list(v.STREAM_DICT.keys())
            # 获得所有值
            v.STREAM_VALUES_LIST = list(v.STREAM_DICT.values())
            print(v.STREAM_VALUES_LIST)
            print(v.COOKIES_PATH)
            # 配置下拉框
            m.combobox.config(values=v.STREAM_VALUES_LIST)

            # 启用
            m.download_Button['state'] = 'active'
            # 启用
            m.makesure_Button['state'] = 'active'
            # 启用
            m.combobox['state'] = 'readonly'

            # 获得指令内容
            v.CMD = c.get_cmd_information()
            # 清除上次生成的指令
            m.cmd_var.set("生成指令")
            # 显示指令
            m.cmd_var.set(v.CMD)
        else:
            return None

    else:
        print("未通过")
        # 清空显示指令框
        m.cmd_var.set("生成指令")
        # 禁用下载按钮
        m.download_Button['state'] = 'disabled'
        # 重置为能通过状态
        flag = 1
        # 启用
        m.makesure_Button['state'] = 'active'


def download_command(*args):
    """
    发送下载请求
    :param args:不用填形参
    :return:不返回值
    """

    def start_download(*args):
        """
        启动下载方法
        :param args:不用填形参
        :return: 无返回值
        """
        # 发送清晰度指令
        c.stream_id(v.STREAM_ID)
        # 发送下载指令
        cmd = c.download_video()

        # 结束后显示下载结果
        m.output_cmd.insert('insert', cmd)

    # 下载过程中禁止调用
    m.makesure_Button['state'] = 'disabled'
    m.combobox['state'] = 'disabled'

    # 启动进度条
    m.progressbarOne.start()
    # 创建开始下载操作的线程
    cmd_thread = threading.Thread(target=start_download, args='')
    if cmd_thread.is_alive() is False:  # 判断线程的状态
        # 启动线程
        cmd_thread.start()


def get_firfox_cookie_path(*args):
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
    # v.COOKIES_PATH = os.path.join(cookie_path, 'cookies.sqlite')
    m.cookiespath_var.set(os.path.join(cookie_path, 'cookies.sqlite'))
    return os.path.join(cookie_path, 'cookies.sqlite')


if __name__ == '__main__':
    shutil.move('Download', home)
