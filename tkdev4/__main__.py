import urllib.request
from os import mkdir, environ, system, remove
from os.path import exists, expanduser
from sys import executable
from time import sleep


def console(text):
    print("控制台输出 : " + text)


def is64():
    return 'PROGRAMFILES(X86)' in environ


pbar = 0


def show_progress(block_num, block_size, total_size):
    global pbar
    pbar = pbar + block_size
    progress = tqdm(total=total_size, colour="#728efd", ncols=120, position=0)
    progress.set_description("安装进度")
    progress.update(pbar)
    progress.close()


def install(url_file, path):
    global pbar
    import requests
    import zipfile

    console("开始下载 : " + url_file)

    urllib.request.urlretrieve(url_file, path, show_progress)
    file = zipfile.ZipFile(path, "r")
    console("开始检验压缩包是否损坏...")
    file.testzip()
    pbar = 0
    # for list in file.namelist():
    #    console("压缩包内的文件 : " + list)


user_path = expanduser("~")
tkdev_path = user_path + "\\.tkdev4"
if exists(tkdev_path):
    pass
else:
    mkdir(tkdev_path)
tkdev_tools_path = tkdev_path + "\\tools"
if exists(tkdev_tools_path):
    pass
else:
    mkdir(tkdev_tools_path)

if is64():
    tkdev_winico_path = tkdev_tools_path + "\\Winico64.zip"
    tkdev_twapi_path = tkdev_tools_path + "\\twapi.zip"
else:
    tkdev_winico_path = tkdev_tools_path + "\\Winico32.zip"
    tkdev_twapi_path = tkdev_tools_path + "\\twapi.zip"
from tqdm import tqdm, trange
if exists(tkdev_winico_path):
    console("检测到已经安装好Winico！")
else:
    console("未检测到Winico！")
    console("准备开始安装...")
    if is64():
        install("https://tkdev-docs.netlify.app/_files/Winico64.zip", tkdev_winico_path)
    else:
        install("https://tkdev-docs.netlify.app/_files/Winico32.zip", tkdev_winico_path)
if exists(tkdev_twapi_path):
    console("检测到已经安装好twApi！")
else:
    console("未检测到twApi！")
    console("准备开始安装...")
    install("https://tkdev-docs.netlify.app/_files/twapi.zip", tkdev_twapi_path)

console("安装完成！")
console("初始化完毕！")

system("pause")
