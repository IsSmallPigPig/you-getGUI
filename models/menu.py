import ctypes
import os
import threading
import darkdetect
from tkdev4 import DevManage
import sv_ttk
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox, filedialog
import tools.tool as t
import models.constants as c
import Core.you_get as y
import platform
import tools.proxy as p


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


class App():
    def __init__(self):
        # 获得用户主目录
        self.home = os.path.expanduser('~')
        # 真伪
        self.flag = 1

    def root_create(self):
        # 超类调用
        super(App, self).__init__()
        # 创建窗口
        self.root = tk.Tk()
        # 更改窗口大小
        self.root.geometry('1060x700')
        # 禁止变更大小
        self.root.resizable(False, False)
        # 更换标题
        self.root.title('Video Download Tools')
        # 去除 icon
        self.root.iconbitmap('.\icon32.ico')
        # 接管窗口
        self.manage = DevManage(self.root)
        # 主题
        self.theme_var = tk.IntVar()

        # 设置部分控件风格
        style = Style()
        style.configure('myCheck.TCheckbutton')
        style.configure('myButton.TButton')

        # 适配 dpi
        if 'Windows' == platform.system():
            # 调用api设置成由应用程序缩放
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
            # 调用api获得当前的缩放因子
            ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
            # 设置缩放因子
            self.root.call('tk', 'scaling', ScaleFactor / 75)
            # 设置缩放因子
            self.root.tk.call('tk', 'scaling', ScaleFactor / 75)

        if darkdetect.isDark():
            # 由于调用函数逻辑与主题颜色相反（即获取sv_ttk是黑色则改白色），所以使用这种方式
            print('dark')
            sv_ttk.set_theme('light')
            self.theme_var.set(1)
        else:
            sv_ttk.set_theme('dark')
            self.theme_var.set(0)


    def var_create(self):
        # 设置 CheckButton 默认状态
        # m3u8
        self.m3u8_var = tk.IntVar()
        self.m3u8_var.set(0)
        # rename
        self.rename_var = tk.IntVar()
        self.rename_var.set(1)
        # overwrite
        self.overwrite_var = tk.IntVar()
        self.overwrite_var.set(0)
        # check size
        self.check_size_var = tk.IntVar()
        self.check_size_var.set(0)
        # captions
        self.captions_var = tk.IntVar()
        self.captions_var.set(1)
        # merge
        self.merge_var = tk.IntVar()
        self.merge_var.set(1)
        # debug
        self.debug_var = tk.IntVar()
        self.debug_var.set(0)
        # SSL
        self.ssl_var = tk.IntVar()
        self.ssl_var.set(0)
        # proxy
        self.proxy_var = tk.IntVar()
        self.proxy_var.set(0)
        # only for extracting
        self.proxy_only_for_extracting_var = tk.IntVar()
        self.proxy_only_for_extracting_var.set(0)
        # use proxy
        self.use_proxy_var = tk.IntVar()
        # 禁用批量
        self.disable_batch_var = tk.IntVar()
        self.disable_batch_var.set(0)
        # cookies
        self.cookies_var = tk.StringVar()
        self.cookies_var.set('Firefox Cookies')
        # command
        self.command_var = tk.StringVar()
        self.command_var.set('Build The Command')
        # 存储路径
        self.save_path_var = tk.StringVar()
        self.save_path_var.set('Set Output Path')
        # 批量下载文件
        self.batch_var = tk.StringVar()
        self.batch_var.set('Save URLs File Path')
        # playlist
        self.playlist_var = tk.IntVar()
        self.playlist_var.set(1)

    def disabled_proxy_command(self):
        if self.proxy_var.get() == 1:
            self.only_use_extracting.config(state='disable')
            self.http_host_entry.config(state='disable')
            self.http_port_entry.config(state='disable')
            self.socks_host_entry.config(state='disable')
            self.socks_port_entry.config(state='disable')
            self.socks_username_entry.config(state='disable')
            self.socks_password_entry.config(state='disable')
            self.use_socks_check.config(state='disable')
            self.use_http_check.config(state='disable')
            # self.use_socks_check.de
        else:
            self.only_use_extracting.config(state='active')
            self.http_host_entry.config(state='active')
            self.http_port_entry.config(state='active')
            self.socks_host_entry.config(state='active')
            self.socks_port_entry.config(state='active')
            self.socks_username_entry.config(state='active')
            self.socks_password_entry.config(state='active')
            self.use_socks_check.config(state='active')
            self.use_http_check.config(state='active')

    def only_for_extracting_command(self):
        if self.proxy_only_for_extracting_var.get() == 1:
            self.use_socks_check.config(state='disable')
            self.socks_host_entry.config(state='disable')
            self.socks_port_entry.config(state='disable')
            self.socks_username_entry.config(state='disable')
            self.socks_password_entry.config(state='disable')
            # self.use_socks_var.set(0)
        else:
            self.use_socks_check.config(state='active')

    def use_proxy_command(self):
        if self.use_proxy_var.get() == 1:
            self.http_host_entry.config(state='active')
            self.http_port_entry.config(state='active')
            self.socks_host_entry.config(state='disable')
            self.socks_port_entry.config(state='disable')
            self.socks_username_entry.config(state='disable')
            self.socks_password_entry.config(state='disable')
            # self.use_socks_var.set(0)
        else:
            self.socks_host_entry.config(state='active')
            self.socks_port_entry.config(state='active')
            self.socks_username_entry.config(state='active')
            self.socks_password_entry.config(state='active')
            self.http_host_entry.config(state='disable')
            self.http_port_entry.config(state='disable')


    def save_path_command(self):
        self.save_path_var.set(filedialog.askdirectory(initialdir=self.home, title='Open the storage path'))

    def set_all_command(self):
        y.cmd_list = [r".\depend\you-get.exe"]
        # 获得所有输入框内容
        self.timeout = self.socket_time_entry.get().replace('Socket Timeout', '')
        self.http_host = self.http_host_entry.get().replace('HTTP Proxy(HOST)', '')
        self.http_port = self.http_port_entry.get().replace('HTTP Proxy(PORT)', '')
        self.sock5_host = self.socks_host_entry.get().replace('SOCK5 Proxy(HOST)', '')
        self.sock5_port = self.socks_port_entry.get().replace('SOCK5 Proxy(PORT)', '')
        self.sock5_username = self.socks_username_entry.get().replace('SOCK5 Proxy(USERNAME)', '')
        self.sock5_password = self.socks_password_entry.get().replace('SOCK5 Proxy(PASSWORD)', '')
        self.filename = self.save_filename_entry.get().replace('Set Output Filename', '')
        self.path = self.save_path_entry.get().replace('Set Output Path', '')
        self.url = self.url_entry.get().replace('Video URL(Required)', '')
        self.cookies = self.cookies_entry.get().replace('Firefox Cookies', '')
        self.urls_path = self.input_file_entry.get().replace('Save URLs File Path', '')

        if self.url != '' or self.playlist_var.get() == 0:
            y.video_url(self.url)
        elif self.url == '':
            self.nourl = messagebox.showerror('No URL was entered',
                                              'Please enter the URL, otherwise the download operation cannot be performed')
            self.flag = 0
            return None

        if self.path != '':
            y.output_dir(self.path)
        elif self.path == '':
            self.nopath = messagebox.askyesno('You did not enter a save path',
                                              'The default save path is the user folder (%s), whether to continue' % self.home)
            if self.nopath == True:
                y.output_dir(self.home)
            else:
                self.flag = 0
                return None

        if self.filename != '':
            y.filename(self.filename)

        if self.cookies != '':
            y.cookies_file(self.cookies)
        elif self.cookies == '':
            self.nocookies = messagebox.askyesno('No cookies are submitted',
                                                 'If you do not submit cookies, you will not be able to download VIP and HD videos')
            if self.nocookies == False:
                self.flag = 0
                return None

        if self.urls_path != '':
            y.input_file(self.urls_path)

        if self.proxy_only_for_extracting_var.get() == 1:
            if self.http_host != '' and self.http_port != '':
                if p.check_proxy(self.http_host, self.http_port):
                    y.extractor_proxy(self.http_host, self.http_port)
                else:
                    self.flag = 0
                    t.show_info(title='Agent error', message='Your proxy address is not available, please check')
                    return None
        if self.use_proxy_var.get() == 1:
            if self.http_host != '' and self.http_port != '':
                if p.check_proxy(self.http_host, self.http_port):
                    y.http_proxy(self.http_host, self.http_port)
                else:
                    self.flag = 0
                    t.show_info(title='Agent error', message='Your proxy address is not available, please check')
                    return None
        if self.use_proxy_var.get() == 2:
            if self.sock5_host != '' and self.sock5_port != '':
                if p.check_proxy(self.http_host, self.http_port):
                    y.socks5_hp(self.sock5_host, self.sock5_port)
                else:
                    self.flag = 0
                    t.show_info(title='Agent error', message='Your proxy address is not available, please check')
                    return None
            elif self.sock5_host != '' and self.sock5_port != '' and self.sock5_password != '' and self.sock5_username != '':
                if p.check_proxy(self.http_host, self.http_port):
                    y.socks5_up(self.sock5_username, self.sock5_password, self.sock5_host, self.sock5_port)
                else:
                    self.flag = 0
                    t.show_info(title='Agent error', message='Your proxy address is not available, please check')
                    return None

        if self.playlist_var.get() == 1:
            y.playlist()
        # 输入值
        if self.m3u8_var.get() == 1:
            y.m3u8()
        if self.rename_var.get() == 1:
            y.auto_rename()
        if self.overwrite_var.get() == 1:
            y.force()
        if self.check_size_var.get() == 1:
            y.skip_existing_file_size_check()
        if self.captions_var.get() == 0:
            y.no_caption()
        if self.merge_var.get() == 0:
            y.no_merge()
        if self.debug_var.get() == 1:
            y.debug()
        if self.ssl_var.get() == 1:
            y.insecure()
        if self.proxy_var.get() == 1:
            y.no_proxy()
        if self.debug_var.get() == 1:
            y.debug()

    def already_thread(self):
        """
        创建线程并防止多次创建
        :param args: 不用填形参
        :return: 不返回值
        """

        def already_command():
            """
                确认信息
                :return: 无返回值
                """
            # 传入真伪判断值

            # 清空列表
            y.cmd_list = [r".\depend\you-get.exe"]
            self.set_all_command()
            c.CMD = y.get_cmd_information()
            print(y.get_cmd_information(y.cmd_list))
            if self.flag == 1:
                print("通过")
                # 禁用控件
                self.download_button.config(state='disable')
                self.already_button.config(state='disable')
                self.stream_combobox.config(state='disable')
                # 提示用戶不要亂搞
                t.show_info(title='Do not close the main program window',
                            message='The URL is now being resolved and may take a long time. Please wait.\nDo not close the terminal')
                if self.disable_batch_var.get() == 1 or self.playlist_var.get() == 1:
                    # 下载json
                    t.write("%s/video_json.json" % self.home, t.get_json(self.url, cookies=self.cookies))
                    flag_json = t.get_json_stream("%s/video_json.json" % self.home)
                    if flag_json == 1:
                        # 获得所有键
                        c.STREAM_KEYS_LIST = list(c.STREAM_DICT.keys())
                        # 获得所有值
                        c.STREAM_VALUES_LIST = list(c.STREAM_DICT.values())
                        print(c.STREAM_VALUES_LIST)
                        # 配置下拉框
                        self.stream_combobox.config(values=c.STREAM_VALUES_LIST)

                        # 启用
                        self.download_button.config(state='active')
                        self.already_button.config(state='active')
                        self.stream_combobox.config(state='readonly')

                        # 获得指令内容
                        c.CMD = y.get_cmd_information()
                        # 清除上次生成的指令
                        self.command_var.set("Build The Command")
                        # 显示指令
                        self.command_var.set(c.CMD)
                        # 切换
                        self.download_button.config(style='Accent.TButton')
                        self.already_button.config(style='')
                    else:
                        # 启用
                        self.download_button.config(state='active')
                        self.already_button.config(state='active')
                        self.stream_combobox.config(state='readonly')
                        t.show_info(title='something was wrong',
                                    message='You entered the wrong information and could not start the download operation')
                else:
                    # 获得指令内容
                    c.CMD = y.get_cmd_information()
                    # 清除上次生成的指令
                    self.command_var.set("Build The Command")
                    # 显示指令
                    self.command_var.set(c.CMD)
                    # 切换
                    self.download_button.config(style='Accent.TButton')
                    self.already_button.config(style='')
                    # 启用
                    self.download_button.config(state='active')
                    self.already_button.config(state='active')
                    # self.stream_combobox.config(state='readonly')

            else:
                print("未通过")
                # 清空显示指令框
                self.command_var.set("Build The Command")
                # 禁用下载按钮
                self.download_button['state'] = 'disabled'
                # 重置为能通过状态
                self.flag = 1
                # 启用
                self.already_button['state'] = 'active'
        # 创建线程
        self.makesure = threading.Thread(target=already_command, args='')

        # 启动线程
        if self.makesure.is_alive() is False:
            self.makesure.start()

    def combobox_command(self, event):
        """
        响应下拉框操作
        :param args: 不填形参
        :return: 不返回值
        """

        # 获得当前下拉框选项所对应的清晰度代码
        c.STREAM_ID = c.STREAM_DICT_VK.get(self.stream_combobox.get())
        print(c.STREAM_ID)

    def download_video(self):
        """
        启动下载
        :param args:不用填形参
        :return: 返回执行结果
        """
        print(y.cmd_list)
        y.stream_id(c.STREAM_ID)
        y.download_cmd(y.cmd_list)
        # print(c.CMD)

        # 解除禁用控件
        self.already_button['state'] = 'active'
        self.stream_combobox['state'] = 'readonly'
        # return self.cmd_info

    def download_command(self):
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
            y.stream_id(c.STREAM_ID)
            print(c.STREAM_ID)
            # 发送下载指令
            self.download_video()
            # 显示对话框
            t.show_info(title='The download is complete', message='The video has been saved to the path you specified')
            # 结束后显示下载结果
            # self.command_text.insert('insert', self.cmd)
            # 切换状态
            self.download_button.config(style='', state='disable')
            self.already_button.config(style='Accent.TButton')

        # 下载过程中禁止调用
        self.already_button['state'] = 'disabled'
        self.stream_combobox['state'] = 'disabled'

        # 创建开始下载操作的线程
        cmd_thread = threading.Thread(target=start_download, args='')
        if cmd_thread.is_alive() is False:  # 判断线程的状态
            # 启动线程
            cmd_thread.start()

    def auto_get_cookies(self):
        self.cookies_var.set(t.get_firefox_cookie_path())

    def import_cookies(self):
        self.cookies_var.set(filedialog.askopenfilename(title='Open the Cookies path', initialdir=self.home,
                                                        filetypes=[('cookies.sqlite', 'cookies.sqlite'),
                                                                   ('cookies.txt', 'cookies.txt'),
                                                                   ('*', "*.")]))
    def open_urls(self):
        self.batch_var.set(filedialog.askopenfilename(title='Open the URLs File path', initialdir=self.home,
                                                        filetypes=[('txt', '.txt'),
                                                                   ('*', "*.")]))

    def theme_config(self):
        # 如果是明亮主题
        if sv_ttk.get_theme() == 'light':
            # 更改标题栏
            self.manage.dwm_set_window_attribute_use_dark_mode()
            # 更改配色
            sv_ttk.set_theme('dark')
            # 设置终端
            self.command_text.config(highlightbackground='#2f2f2f', highlightcolor='#57c8ff')
            # 设置为黑
            self.theme_var.set(1)
        elif sv_ttk.get_theme() == 'dark':
            print(1)
            # 更改标题栏
            self.manage.dwm_set_window_attribute_use_light_mode()
            # 更改配色
            sv_ttk.set_theme('light')
            # 设置终端
            self.command_text.config(highlightbackground='#ebebeb', highlightcolor='#0560b6')
            # 设置为白
            self.theme_var.set(0)

    def download_options(self):
        def disable_force():
            if self.rename_var.get() == 1:
                self.force_file_check.config(state='disable')
            else:
                self.force_file_check.config(state='active')
        def disable_rename():
            if self.overwrite_var.get() == 1:
                self.auto_rename_check.config(state='disable')
            else:
                self.auto_rename_check.config(state='active')
        # 下载选项的背景框
        self.download_labelframe = LabelFrame(text='Download Options', padding=15)
        # m3u8 检查按钮
        self.m3u8_check = Checkbutton(self.download_labelframe, text='Using m3u8 URL', state='normal',
                                      style='myCheck.TCheckbutton', variable=self.m3u8_var)
        # 自动重命名 检查按钮
        self.auto_rename_check = Checkbutton(self.download_labelframe, text='Auto Rename', state='normal',
                                             style='myCheck.TCheckbutton', variable=self.rename_var, command=disable_force)
        # 强制覆盖重名文件 检查按钮
        self.force_file_check = Checkbutton(self.download_labelframe, text='Overwrite Files', state='disable',
                                            style='myCheck.TCheckbutton', variable=self.overwrite_var, command=disable_rename)
        # 不检查文件大小检查按钮
        self.skip_check_check = Checkbutton(self.download_labelframe, text='Skip Check File Size', state='normal',
                                            style='myCheck.TCheckbutton', variable=self.check_size_var)
        # 不下载字幕检查按钮
        self.no_caption_check = Checkbutton(self.download_labelframe, text='Download Captions', state='normal',
                                            style='myCheck.TCheckbutton', variable=self.captions_var)
        # 不合并视频
        self.no_merge_check = Checkbutton(self.download_labelframe, text='Merge Video Parts', state='normal',
                                          style='myCheck.TCheckbutton', variable=self.merge_var)
        # 忽略 ssl 错误
        self.ignore_ssl_check = Checkbutton(self.download_labelframe, text='Ignore SSL Errors', state='normal',
                                            style='myCheck.TCheckbutton', variable=self.ssl_var)
        # debug 模式下载
        self.debug_check = Checkbutton(self.download_labelframe, text='Debug Mode', state='normal',
                                            style='myCheck.TCheckbutton', variable=self.debug_var)
        # 套接字延时
        self.socket_time_entry = EntryWithPlaceholder(self.download_labelframe, 'Socket Timeout')

        self.m3u8_check.pack(fill='x', pady=5, padx=5)
        self.ignore_ssl_check.pack(fill='x', pady=5, padx=5)
        self.skip_check_check.pack(fill='x', pady=5, padx=5)
        self.auto_rename_check.pack(fill='x', pady=5, padx=5)
        self.force_file_check.pack(fill='x', pady=5, padx=5)
        self.no_caption_check.pack(fill='x', pady=5, padx=5)
        self.no_merge_check.pack(fill='x', pady=5, padx=5)
        self.debug_check.pack(fill='x', pady=5, padx=5)
        self.socket_time_entry.pack(fill='x', pady=5, padx=5)
        self.download_labelframe.place(x=10, y=10, width=230, height=400)

    def batch_options(self):
        """
        批量下载区域
        :return:
        """
        def disable_input_file():
            if self.playlist_var.get() == 1:
                self.input_file_entry.config(state='disable')
                self.input_file_button.config(state='disable')
                self.input_file_label.config(state='disable')
                self.url_entry.config(state='active')
            else:
                self.input_file_entry.config(state='active')
                self.input_file_button.config(state='active')
                self.input_file_label.config(state='active')
                self.url_entry.config(state='disable')
        def disable_batch_options():
            print(self.disable_batch_var.get() == 1)
            if self.disable_batch_var.get() == 1:
                print('disable')
                self.playlist_var.set(0)
                self.input_file_entry.config(state='disable')
                self.input_file_button.config(state='disable')
                self.input_file_label.config(state='disable')
                self.playlist_check.config(state='disable')
                self.stream_combobox.config(state='disable')
                self.url_entry.config(state='active')
            else:
                self.playlist_check.config(state='active')
                self.playlist_var.set(1)
        # 批量下载选项的背景框
        self.batch_labelframe = LabelFrame(text='Batch Download Options', padding=15)
        self.disable_batch_check = Checkbutton(self.batch_labelframe, text='Disable Batch Options', state='normal',
                                               style='myCheck.TCheckbutton', variable=self.disable_batch_var, command=disable_batch_options)
        self.playlist_check = Checkbutton(self.batch_labelframe, text='Download Playlist', state='normal',
                                          style='myCheck.TCheckbutton', variable=self.playlist_var, command=disable_input_file)
        self.input_file_entry = Entry(self.batch_labelframe, textvariable=self.batch_var, state='disable')
        self.input_file_button = Button(self.batch_labelframe, text='Open Save URLs File', command=self.open_urls, state='disable')

        self.input_file_label = Label(self.batch_labelframe, state='disable', text='Automatically download videos\nwith multiple links')

        self.disable_batch_check.pack(fill='x', pady=5, padx=5)
        self.playlist_check.pack(fill='x', pady=5, padx=5)
        self.input_file_entry.pack(fill='x', pady=5, padx=5)
        self.input_file_button.pack(fill='x', pady=5, padx=5)
        self.input_file_label.pack(fill='both', pady=5, padx=5)
        self.batch_labelframe.place(x=10, y=420, height=260, width=230)


    def proxy_options(self):
        # 代理选项的背景框
        self.proxy_labelframe = Labelframe(text='Proxy Options', padding=15)
        # 分割线
        self.http_separator = Separator(self.proxy_labelframe)
        # 禁止使用代理检查按钮
        self.no_proxy = Checkbutton(self.proxy_labelframe, text='Disabled Proxy', state='normal',
                                    style='myButton.TCheckbutton', variable=self.proxy_var,
                                    command=self.disabled_proxy_command)
        # 仅使用代理进行解析
        self.only_use_extracting = Checkbutton(self.proxy_labelframe, text='Only For Extracting', state='normal',
                                               style='myButton.TCheckbutton',
                                               variable=self.proxy_only_for_extracting_var,
                                               command=self.only_for_extracting_command)

        # 使用 http 代理
        self.use_http_check = Radiobutton(self.proxy_labelframe, text='Use HTTP Proxy', state='normal', variable=self.use_proxy_var,
                                          command=self.use_proxy_command, value=1)
        # http 代理主机输入框
        self.http_host_entry = EntryWithPlaceholder(self.proxy_labelframe, 'HTTP Proxy (HOST)')
        self.http_host_entry.config(state='disable')
        # http 代理端口输入框
        self.http_port_entry = EntryWithPlaceholder(self.proxy_labelframe, 'HTTP Proxy (PORT)')
        self.http_port_entry.config(state='disable')

        # 使用 socks 代理
        self.use_socks_check = Radiobutton(self.proxy_labelframe, text='Use SOCKS Proxy', state='normal', variable=self.use_proxy_var,
                                           command=self.use_proxy_command, value=2)
        # 分割线
        self.socks_separator = Separator(self.proxy_labelframe)
        # socks5 代理主机输入框
        self.socks_host_entry = EntryWithPlaceholder(self.proxy_labelframe, 'SOCKS Proxy (HOST)')
        self.socks_host_entry.config(state='disable')
        # socks5 代理端口输入框
        self.socks_port_entry = EntryWithPlaceholder(self.proxy_labelframe, 'SOCKS Proxy (PORT)')
        self.socks_port_entry.config(state='disable')
        # socks5 用户名输入框
        self.socks_username_entry = EntryWithPlaceholder(self.proxy_labelframe, 'SOCKS Proxy (USERNAME)')
        self.socks_username_entry.config(state='disable')
        # socks5 密码输入框
        self.socks_password_entry = EntryWithPlaceholder(self.proxy_labelframe, 'SOCKS Proxy (PASSWORD)')
        self.socks_password_entry.config(state='disable')

        self.no_proxy.pack(fill='x', padx=5, pady=5)
        self.only_use_extracting.pack(fill='x', padx=5, pady=2)
        self.http_separator.pack(fill='x', padx=5, pady=10)
        self.use_http_check.pack(fill='x', padx=5, pady=5)
        self.http_host_entry.pack(fill='x', padx=5, pady=5)
        self.http_port_entry.pack(fill='x', padx=5, pady=5)

        self.socks_separator.pack(fill='x', padx=5, pady=10)
        self.use_socks_check.pack(fill='x', padx=5, pady=2)
        self.socks_host_entry.pack(fill='x', padx=5, pady=5)
        self.socks_port_entry.pack(fill='x', padx=5, pady=5)
        self.socks_username_entry.pack(fill='x', padx=5, pady=5)
        self.socks_password_entry.pack(fill='x', padx=5, pady=5)
        self.proxy_labelframe.place(x=250, y=10, height=480, width=230)

    def save_options(self):
        # 保存文件的背景框
        self.save_labelframe = Labelframe(text='Save Options', padding=15)
        # 保存路径输入框
        self.save_path_entry = Entry(self.save_labelframe, textvariable=self.save_path_var)
        # 保存名称
        self.save_filename_entry = EntryWithPlaceholder(self.save_labelframe, 'Set Output Filename')

        # 打开保存路径
        self.open_save_path_button = Button(self.save_labelframe, text='Open Save Path', command=self.save_path_command)

        self.save_filename_entry.pack(fill='x', padx=5, pady=5)
        self.save_path_entry.pack(fill='x', pady=5, padx=5)
        self.open_save_path_button.pack(fill='x', padx=5, pady=5)
        self.save_labelframe.place(x=250, y=500, height=180, width=230)

    def start_options(self):
        # 开始选项的背景框
        self.start_labelframe = Labelframe(text='Start Options', padding=15)
        # 下载链接输入框
        self.url_entry = EntryWithPlaceholder(self.start_labelframe, 'Video URL(Required)')
        # 分割线
        self.url_separator = Separator(self.start_labelframe)
        # Cookies 输入框
        self.cookies_entry = Entry(self.start_labelframe, textvariable=self.cookies_var)
        # 获得火狐Cookies
        self.get_cookies_button = Button(self.start_labelframe, text='Get Cookies(Auto)', command=self.auto_get_cookies)
        # 导入火狐Cookies
        self.import_cookies_button = Button(self.start_labelframe, text='Import Cookies(Manual)',
                                            command=self.import_cookies)
        # 分割线
        self.already_separator = Separator(self.start_labelframe)
        # 准备好了按钮
        self.already_button = Button(self.start_labelframe, text='Complete', style='Accent.TButton',
                                     command=self.already_thread)
        # 分割线
        self.already_separator_last = Separator(self.start_labelframe)
        # 命令生成显示
        self.command_entry = Entry(self.start_labelframe, textvariable=self.command_var)
        # 清晰度下拉框
        self.stream_combobox = Combobox(self.start_labelframe, state='disable')
        self.stream_combobox.bind('<<ComboboxSelected>>', self.combobox_command)
        # 分割线
        self.download_separator = Separator(self.start_labelframe)
        # 开始下载按钮
        self.download_button = Button(self.start_labelframe, text='Download', command=self.download_command,
                                      state='disable')
        # 分割线
        self.download_separator_last = Separator(self.start_labelframe)
        # 终端
        self.command_text = tk.Text(self.start_labelframe, bd=2, relief='flat', highlightthickness=2,
                                    highlightbackground='#ebebeb', highlightcolor='#005fb8')

        self.url_entry.pack(fill='x', padx=5, pady=5)
        self.url_separator.pack(fill='x', padx=5, pady=10)
        self.cookies_entry.pack(fill='x', padx=5, pady=5)
        self.get_cookies_button.pack(fill='x', padx=5, pady=5)
        self.import_cookies_button.pack(fill='x', padx=5, pady=5)
        self.already_separator.pack(fill='x', padx=5, pady=10)
        self.already_button.pack(fill='x', padx=5, pady=5)
        self.already_separator_last.pack(fill='x', padx=5, pady=10)
        self.command_entry.pack(fill='x', padx=5, pady=5)
        self.stream_combobox.pack(fill='x', padx=5, pady=5)
        self.download_separator.pack(fill='x', padx=5, pady=10)
        self.download_button.pack(fill='x', padx=5, pady=5)

        self.download_separator.pack(fill='x', padx=5, pady=10)
        self.download_button.pack(fill='x', padx=5, pady=5)
        self.download_separator_last.pack(fill='x', padx=5, pady=10)

        # self.command_text.pack(fill='x', padx=5, pady=5)
        self.start_labelframe.place(x=490, y=10, width=300, height=670)

    def about_program(self):
        # 关于程序的背景框
        self.about_labelframe = Labelframe(text='About Program', padding=15)
        # 暗黑模式切换
        self.change_theme_check = Checkbutton(self.about_labelframe, text='Dark Theme', state='normal',
                                              style="Switch.TCheckbutton", command=self.theme_config,
                                              variable=self.theme_var)
        # 打开配置文件按钮
        self.open_options_button = Button(self.about_labelframe, text='Open Options')
        # 打开帮助
        self.help_button = Button(self.about_labelframe, text='View Help')
        # 关于作者
        self.about_us_labelframe = Labelframe(self.about_labelframe, text='About Us')
        # 项目开发者
        self.developer_label = Label(self.about_us_labelframe, text='Developer: SmallPigPig')
        # 项目贡献者
        self.contributors_label = Label(self.about_us_labelframe, text='Contributors: None')
        # 当前代码版本
        self.version_label = Label(self.about_us_labelframe, text='Version: v1.0.1')
        # 交流群
        self.contact_label = Label(self.about_us_labelframe,
                                   text='Contact Us:\nQQ Groups: 473542615\nEmail: 3552354372@qq.com')
        # 许可证
        self.license_label = Label(self.about_us_labelframe, text='Licence: MIT License')
        # 基于项目
        self.project_based = Label(self.about_us_labelframe, text='Project-based:\nyou-get\nsv-ttk')

        self.change_theme_check.pack(fill='x', padx=5, pady=5)
        # self.open_options_button.pack(fill='x', padx=5, pady=5)
        # self.help_button.pack(fill='x', padx=5, pady=5)
        self.about_us_labelframe.pack(fill='x', padx=5, pady=5)
        self.contributors_label.pack(fill='x', padx=5, pady=5)
        self.version_label.pack(fill='x', padx=5, pady=5)
        self.contact_label.pack(fill='x', padx=5, pady=5)
        self.license_label.pack(fill='x', padx=5, pady=5)
        self.project_based.pack(fill='x', padx=5, pady=5)
        self.developer_label.pack(fill='x', padx=5, pady=5)
        self.about_labelframe.place(x=800, y=10, height=670, width=250)

    def run(self):
        # 创建窗口
        self.root_create()
        # 设定变量
        self.var_create()
        # 下载选项控件
        self.download_options()
        # 调试选项控件
        self.batch_options()
        # 代理选项控件
        self.proxy_options()
        # 保存选项控件
        self.save_options()
        # 开始选项控件
        self.start_options()
        # 设置主题
        self.theme_config()
        # 关于
        self.about_program()
        # 运行代码
        self.root.mainloop()
