from tkinter.ttk import *
from tkinter import IntVar, StringVar
import Tool.tools as t
import Tool.constants as v
import tkinter as tk
import sv_ttk
import ctypes


class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", foreground='grey'):
        super().__init__(master)

        self.default_fg_color = self['foreground']
        self.placeholder = placeholder
        self.placeholder_color = foreground

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self.config(foreground=self.placeholder_color)

    def foc_in(self, *args):
        print(self['foreground'])
        if self.cget('foreground') == self.placeholder_color:
            self.delete('0', 'end')
            self.config(foreground=self.default_fg_color)

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


def progress_start(*args):
    progressbarOne.start()


def progress_stop(*args):
    progressbarOne.stop()


root = tk.Tk()
sv_ttk.set_theme('dark')
root.geometry('810x900')
root.resizable(False, False)
# 告诉操作系统使用程序自身的dpi适配
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# 获取屏幕的缩放因子
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
# 设置程序缩放
root.tk.call('tk', 'scaling', ScaleFactor / 75)

# 可选列表
values = ['360P', '720P', '1080P']
# 设定默认值
value = StringVar()
value.set("720P")

# 指令
cmd_var = StringVar()
cmd_var.set("生成指令")

# 保存路径
save_path_var = StringVar()
save_path_var.set("文件保存路径")

# cookies路径
cookiespath_var = StringVar()
cookiespath_var.set("cookies 路径")

# 是否自动重命名
autorename_var = IntVar()
autorename_var.set(1)
# 多P视频
playlist_var = IntVar()
playlist_var.set(0)
# 按页下载
pagesize_var = IntVar()
pagesize_var.set(0)
# 忽略SSL错误
skipssl_var = IntVar()
skipssl_var.set(0)
# m3u8
m3u8_var = IntVar()
m3u8_var.set(0)
# 调试模式
debug_var = IntVar()
debug_var.set(0)
# 是否下载字幕
caption_var = IntVar()
caption_var.set(0)
# 是佛校验文件
check_var = IntVar()
check_var.set(0)
# 是否合并视频
merge_var = IntVar()
merge_var.set(0)
# 是否检查大小
checksize_var = IntVar()
checksize_var.set(1)
# 是否获得信息
getinformation_var = IntVar()
getinformation_var.set(0)
# 是否获得解析 url
geturl_var = IntVar()
geturl_var.set(0)
# 是否获得json
getjson_var = IntVar()
getjson_var.set(0)
# 是否查看版本号
getversion_var = IntVar()
getversion_var.set(0)
# 是否覆盖重名文件
force_var = IntVar()
force_var.set(0)

# 基础设置文本框
simple_Label = Label(text="基础设置", font=("微软雅黑", 12, "bold"))
# 高级设置文本框
ununsual_Label = Label(text="高级设置", font=("微软雅黑", 12, "bold"))
# 多P下载文本框
# playlist_Label = Label(text="多P下载设置（全部下载不填）", font=("微软雅黑", 12, "bold"))
# 按页下载文本框
# pagesize_Label = Label(text="按页下载设置", font=("微软雅黑", 12, "bold"))
# http代理设置文本框
http_Label = Label(text="http 代理设置", font=("微软雅黑", 12, "bold"))
# socks代理设置文本框
socks_Label = Label(text="Socks5 代理设置", font=("微软雅黑", 12, "bold"))
# 其他选项文本框
other_Label = Label(text="其他设置", font=("微软雅黑", 12, "bold"))
# 下载属性文本框
downloadconfig_Label = Label(text="下载属性", font=("微软雅黑", 12, "bold"))

# 视频下载链接输入框
url_Entry = EntryWithPlaceholder(root, "视频下载链接")
# 输出文件名输入框
filename_Entry = EntryWithPlaceholder(root, "输出文件名称")
# 文件保存路径输入框
filepath_Entry = EntryWithPlaceholder(root, "文件保存路径")
filepath_Entry.config(textvariable=save_path_var)
# cookies路径输入框
cookiespath_Entry = EntryWithPlaceholder(root, "cookies 路径")
cookiespath_Entry.config(textvariable=cookiespath_var)

# 起始集数输入框
# start_Entry = EntryWithPlaceholder(root, "起始集数")
# 结束集数输入框
# last_Entry = EntryWithPlaceholder(root, "结束集数")
# 下载页数字输入框
# pagenumber_Entry = EntryWithPlaceholder(root, "下载页数字（第几页）")
# 指定播放器输入框
player_Entry = EntryWithPlaceholder(root, "指定播放链接视频的本地播放器")
# 套接字延时输入框
second_Entry = EntryWithPlaceholder(root, "套接字延时")
# HOST 输入框
httphost_Entry = EntryWithPlaceholder(root, "HOST")
# PORT 输入框
httpport_Entry = EntryWithPlaceholder(root, "PORT")
# HOST 输入框
sockshost_Entry = EntryWithPlaceholder(root, "HOST")
# PORT 输入框
socksport_Entry = EntryWithPlaceholder(root, "PORT")
# USERNAME 输入框
socksusername_Entry = EntryWithPlaceholder(root, "USERNAME")
# PASSWORD 输入框
sockspassword_Entry = EntryWithPlaceholder(root, "PASSWORD")
# 显示指令
cmd_Entry = Entry(root, textvariable=cmd_var, state='disabled', foreground='grey')

# 打开文件保存路径按钮
opensavepath_Button = Button(root, text="打开文件存储路径", command=t.save_path_command)
# 打开 cookies 存储路径按钮
opencookiespath_Button = Button(root, text="提交其他 cookies", command=t.open_cookies)
# 确认信息按钮
makesure_Button = Button(root, text="确认信息", command=t.makesure_command)
# 开始下载按钮
downlaod_Button = Button(root, text="开始下载", state='disabled', command=t.download_command)
# 自动获得 cookies
autogetcookies_Button = Button(root, text="自动获得火狐cookies", state='active', command=t.get_firfox_cookie_path)

# m3u8 检查按钮
m3u8_Check = Checkbutton(root, text='m3u8 视频', state='normal', variable=m3u8_var)
# debug 检查按钮
debug_Check = Checkbutton(root, text='调试模式', state='normal', variable=debug_var)
# 不下载字幕检查按钮
nocaption_Check = Checkbutton(root, text='不下载字幕', state='normal', variable=caption_var)
# 不校验文件检查按钮
skipcheck_Check = Checkbutton(root, text='不校验文件', state='normal', variable=check_var)
# 不合并视频检查按钮
skipmerge_Check = Checkbutton(root, text='不合并视频', state='normal', variable=merge_var)
# 不检查大小检查按钮
skipchecksize_Check = Checkbutton(root, text='不检查大小', state='normal', variable=checksize_var)
# 获得信息检查按钮
getinfomation_Check = Checkbutton(root, text='获得信息', state='normal', variable=getinformation_var,
                                  command=lambda: t.disabled_startdownload(getinformation_var))
# 获得url检查按钮
geturl_Check = Checkbutton(root, text='获得 url', state='normal', variable=geturl_var,
                           command=lambda: t.disabled_startdownload(geturl_var))
# 获得json检查按钮
getjson_Check = Checkbutton(root, text='获得 json', state='normal', variable=getjson_var,
                            command=lambda: t.disabled_startdownload(getjson_var))
# 查看版本号检查按钮
getversion_Check = Checkbutton(root, text='查看版本号', state='normal', variable=getversion_var,
                               command=lambda: t.disabled_startdownload(getversion_var))
# 覆盖重名文件检查按钮
force_Check = Checkbutton(root, text='覆盖重名文件', state='normal', variable=force_var)
# 自动重命名检查按钮
autorename_Check = Checkbutton(root, text='自动重命名', state='normal', variable=autorename_var)
# 多P视频检查按钮
playlist_Check = Checkbutton(root, text='多P视频', state='normal', variable=playlist_var)
# 按页下载检查按钮
pagesize_Check = Checkbutton(root, text='按页下载', state='normal', variable=pagesize_var)
# 忽略SSL检查按钮
skipSSL_Check = Checkbutton(root, text='忽略SSL错误', state='normal', variable=skipssl_var)

# 进度条
progressbarOne = Progressbar(root, length=600, mode='indeterminate', orient=tk.HORIZONTAL)

# 终端
output_cmd = tk.Text(root, bd=2, relief='flat', highlightthickness=1, highlightcolor='#57c8ff')

# 下拉框
combobox = Combobox(
    root,
    height=10,  # 高度,下拉显示的条目数量
    width=20,  # 宽度
    state='disabled',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
    cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
    font=('', 20),  # 字体
    textvariable=value,  # 通过StringVar设置可改变的值
    values=values,  # 设置下拉框的选项
    exportselection=False
)

# 绘制基础设置文本框
simple_Label.place(x=10, y=20, width=80, height=25)
# 绘制高级设置文本框
ununsual_Label.place(x=410, y=20, width=80, height=25)
# 绘制多P下载文本框
# playlist_Label.place(x=10, y=330, width=280, height=25)
# 绘制按页下载文本框
# pagesize_Label.place(x=10, y=400, width=260, height=25)
# 绘制 http文本框
http_Label.place(x=410, y=130, width=280, height=25)
# 绘制 socks 文本框
socks_Label.place(x=410, y=210, width=280, height=25)
# 绘制其他设置文本框
other_Label.place(x=10, y=350, width=120, height=25)
# 绘制下载属性文本框
downloadconfig_Label.place(x=10, y=520, width=120, height=25)

# 绘制视频下载链接输入框
url_Entry.place(x=10, y=50, width=380, height=30)
# 绘制输出文件名称输入框
filename_Entry.place(x=10, y=90, width=380, height=30)
# 绘制文件保存路径输入框
filepath_Entry.place(x=10, y=130, width=380, height=30)
# 绘制cookies路径输入框
cookiespath_Entry.place(x=10, y=210, width=380, height=30)
# 绘制起始集数输入框
# start_Entry.place(x=10, y=360, width=180, height=30)
# 绘制结束集数输入框
# last_Entry.place(x=210, y=360, width=180, height=30)
# 绘制下载页数字输入框
# pagenumber_Entry.place(x=10, y=430, width=380, height=30)
# 绘制指定视频播放器输入框
player_Entry.place(x=410, y=50, width=380, height=30)
# 绘制套接字延时输入框
second_Entry.place(x=410, y=90, width=380, height=30)
# 绘制 httphost 输入框
httphost_Entry.place(x=410, y=170, width=180, height=30)
# 绘制 httpport 输入框
httpport_Entry.place(x=610, y=170, width=180, height=30)
# 绘制 sockshost 输入框
sockshost_Entry.place(x=410, y=250, width=180, height=30)
# 绘制 socksport 输入框
socksport_Entry.place(x=610, y=250, width=180, height=30)
# 绘制 socksusername 输入框
socksusername_Entry.place(x=410, y=290, width=180, height=30)
# 绘制 sockspassword 输入框
sockspassword_Entry.place(x=610, y=290, width=180, height=30)
# 绘制指令
cmd_Entry.place(x=10, y=590, width=790, height=30)

# 绘制打开文件保存路径按钮
opensavepath_Button.place(x=10, y=170, width=380, height=30)
# 绘制打开 cookies 按钮
opencookiespath_Button.place(x=10, y=250, width=180, height=30)
# 绘制获得cookies 按钮
autogetcookies_Button.place(x=210, y=250, width=180, height=30)
# 绘制确认信息按钮
makesure_Button.place(x=10, y=470, width=790, height=30)
# 绘制开始下载按钮
downlaod_Button.place(x=10, y=630, width=790, height=30)

# 绘制自动重命名检查按钮
autorename_Check.place(x=10, y=300, width=110, height=30)
# 绘制覆盖重名文件检查按钮
force_Check.place(x=140, y=300, width=140, height=30)
# 绘制下载多P视频检查按钮
# playlist_Check.place(x=160, y=300, width=110, height=30)
# 绘制不下载字幕检查按钮
nocaption_Check.place(x=490, y=380, width=120, height=30)
# 绘制不校验文件检查按钮
skipcheck_Check.place(x=330, y=380, width=110, height=30)
# 绘制不合并视频检查按钮
skipmerge_Check.place(x=180, y=420, width=110, height=30)
# 绘制不检查文件大小检查按钮
skipchecksize_Check.place(x=650, y=380, width=110, height=30)
# 绘制获得视频信息检查按钮
getinfomation_Check.place(x=330, y=420, width=90, height=30)
# 绘制获得 url 检查按钮
geturl_Check.place(x=10, y=420, width=90, height=30)
# 绘制获得 json 检查按钮
getjson_Check.place(x=490, y=420, width=90, height=30)
# 绘制查看版本号检查按钮
getversion_Check.place(x=650, y=420, width=90, height=30)
# 绘制m3u8检查按钮
m3u8_Check.place(x=10, y=380, width=110, height=30)
# 绘制调试检查按钮
debug_Check.place(x=180, y=380, width=90, height=30)
# 绘制按页下载检查按钮
# pagesize_Check.place(x=190, y=300, width=90, height=30)
# 绘制忽略SSL错误检查按钮
# skipSSL_Check.place(x=280, y=300, width=90, height=30)

# 绘制进度条
progressbarOne.place(x=10, y=670, width=790, height=20)
output_cmd.place(x=10, y=700, width=790, height=190)

# 绘制下拉框
combobox.place(x=10, y=550, width=790, height=30)
