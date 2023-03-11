import tkinter
from typing import Optional


WM_MOUSEMOVE = "WM_MOUSEMOVE"
WM_LBUTTONDOWN = "WM_LBUTTONDOWN"
WM_LBUTTONUP = "WM_LBUTTONUP"
WM_LBUTTONDBLCLK = "WM_LBUTTONDBLCLK"
WM_RBUTTONDOWN = "WM_RBUTTONDOWN"
WM_RBUTTONUP = "WM_RBUTTONUP"
WM_RBUTTONDBLCLK = "WM_RBUTTONDBLCLK"
WM_MBUTTONDOWN = "WM_MBUTTONDOWN"
WM_MBUTTONUP = "WM_MBUTTONUP"
WM_MBUTTONDBLCLK = "WM_MBUTTONDBLCLK"

WM_EVENT = (WM_MOUSEMOVE,
            WM_LBUTTONDOWN, WM_LBUTTONUP, WM_LBUTTONDBLCLK,
            WM_RBUTTONDOWN, WM_RBUTTONUP, WM_RBUTTONDBLCLK,
            WM_MBUTTONDOWN, WM_MBUTTONUP, WM_MBUTTONDBLCLK)

ICON_APPLICATION = "application"
ICON_ASTERISK = "asterisk"
ICON_ERROR = "error"
ICON_EXCLAMATION = "exclamation"
ICON_HAND = "hand"
ICON_QUESTION = "quesiton"
ICON_INFORMATION = "information"
ICON_WARNING = "warning"
ICON_WINLOGO = "winlogo"

ICON_MODE_ICON = "icon"
ICON_MODE_LOAD = "load"
ICON_MODE_NONE = "none"

ICONS = ("application", "asterisk", "error", "exclamation", "hand", "question", "information", "warning", "winlogo")

ID_ADD = "add"
ID_MODIFY = "modify"
ID_DELETE = "delete"

import os


def Is64Windows():
    return 'PROGRAMFILES(X86)' in os.environ


def download_winico():
    """
    安装所需要的一些文件资源。
    """
    from sys import executable
    from os.path import exists, split
    from os import system
    from time import sleep
    tcl = split(executable)[0] + "\\tcl\\"
    if exists(tcl):
        if not exists(tcl + "Winico64"):
            print("已经检测到tcl目录存在，准备开始下载...")
            sleep(3)
            import zipfile
            from os.path import expanduser
            if Is64Windows():
                file = expanduser("~") + "\\.tkdev4\\tools\\Winico64.zip"
            else:
                file = expanduser("~") + "\\.tkdev4\\tools\\Winico32.zip"
            if exists(file):
                ZipFile = zipfile.ZipFile(file, mode='r')
                for Names in ZipFile.namelist():
                    File = ZipFile.extract(Names, tcl)  # 解压到zip目录文件下
                    print("已经解压完成文件 ： " + File)
                ZipFile.close()
                print("下载完毕")
            else:
                print(executable + " -m tkdev4")
                system(executable + " -m tkdev4")
        else:
            print("已经检测到下载文件")
    print("准备开始安装")
    sleep(3)
    from os import rmdir
    import shutil
    try:
        shutil.move(tcl + 'Winico64\\pkg', tcl)
        shutil.move(tcl + 'Winico64\\src', tcl)
    except shutil.Error:
        print("你已经安装好，无需再次安装")
    else:
        print("安装完成！")
    shutil.rmtree(tcl + 'Winico64\\')


def example_func(event=None, icon_id=None, icon=None, x=None, y=None, window: tkinter.Tk = None):
    """
    示例函数
    """
    if event == WM_LBUTTONDOWN:
        window.deiconify()
    elif event == WM_RBUTTONDOWN:
        def close():
            icon.delete(icon_id)
            window.destroy()

        menu = tkinter.Menu(tearoff=False)
        menu.add_command(label="发送“Hello”到控制台", command=lambda: print("Hello"), activebackground="#3369d6")
        menu.add_separator()
        menu.add_command(label="退出应用程序", command=lambda: close(), activebackground="#3369d6")
        menu.tk_popup(x, y)


def example():
    """
    示例
    """
    Window = tkinter.Tk()
    Window.protocol("WM_DELETE_WINDOW", lambda: Window.withdraw())
    Tray = DevTray(Window, "示例", icon=ICON_APPLICATION, icon_mode=ICON_MODE_LOAD,
                   menu_func=lambda event=None, icon_id=None, icon=None, x=None, y=None: example_func(event=event,
                                                                                                      icon_id=icon,
                                                                                                      icon=Tray, x=x,
                                                                                                      y=y,
                                                                                                      window=Window))
    Tray.taskbar(id="add")
    Window.mainloop()


class DevTray(object):
    def __init__(self, master: tkinter.Tk, text: str = "托盘图标", icon=None, icon_mode="none", menu_func=None,
                 use_winico: bool = True, auto_install: bool = True):
        """
        使用tcl扩展winico制作的托盘图标组件。

        :param master: 设置父组件。
        :param text: 设置托盘图标上的提示文本，默认是"托盘图标"。
        :param icon: 设置托盘图标上的图标图片，默认是winico的"tkchat.ico"，需要使用createfrom转换，或使用load获取图标。
        :param icon_mode: 设置默认的图标模式，icon_mode如果是"icon"，那么将会使用createfrom来设置图标。icon_mode如果是load，
                          将会使用load来设置图标，如果图标是icon是none，将由你自己设置图标
        :param menu_func: 设置托盘图标的事件。返回给你三个参数，event事件名，x为X坐标，y为Y坐标。
        :param use_winico: 选择是否启用自动Winico。如果取消，之后还可以使用use_winico()方法启用。
        :param auto_install: 选择是否自动下载Winico，如果未检测到主文件，将会开始下载。
        """
        from os.path import exists, split
        from sys import executable
        if auto_install:
            if not exists(split(executable)[0] + "\\tcl\\pkg\\pkgIndex.tcl"):
                download_winico()
        self._master = master
        self._text = text
        if use_winico:
            self.use_winico()
        if icon is None:
            from os.path import split
            from sys import executable
            self._icon = self.createfrom(split(executable)[0] + "\\tcl\\pkg\\tkchat.ico")
        else:
            if icon_mode == "icon":
                self._icon = self.createfrom(icon)
                self._id = self._icon
            elif icon_mode == "load":
                self._icon = self.load(icon, None)
                self._id = self._icon
            elif icon_mode == "none":
                if icon == "empty":
                    self._icon = None
                    self._id = None
                else:
                    self._icon = icon
                    self._id = self._icon
        self._id = self._icon
        if menu_func is None:
            self._menu_func = self.menu
        else:
            self._menu_func = menu_func

    @property
    def master(self):
        """
        父组件
        """
        return self._master

    @master.setter
    def master(self, master):
        self._master = master

    @property
    def text(self):
        """
        提示文本
        """
        return self._text

    @text.setter
    def text(self, text: str):
        self._text = text

    @property
    def icon(self):
        """
        图标
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        self._icon = icon

    @property
    def menu_func(self):
        """
        事件处理
        """
        return self._menu_func

    id = icon

    @menu_func.setter
    def menu_func(self, menu_func):
        self._menu_func = menu_func

    def use_winico(self):
        """
        使用winico组件
        """
        self._master.tk.call('package', 'require',
                             'Winico')

    def application(self):
        """
        从系统获取的应用程序图标
        """
        return self.load(ICON_APPLICATION, None)

    def asterisk(self):
        """
        从系统获取的信息图标
        """
        return self.load(ICON_ASTERISK, None)

    def error(self):
        """
        从系统获取错误图标
        """
        return self.load(ICON_ERROR, None)

    def exclamation(self):
        """
        从系统获取感叹号图标
        """
        return self.load(ICON_EXCLAMATION, None)

    def hand(self):
        """
        从系统获取手图标
        """
        return self.load(ICON_HAND, None)

    def question(self):
        """
        从系统获取疑问号图标
        """
        return self.load(ICON_QUESTION, None)

    def information(self):
        """
        从系统获取通知图标
        """
        return self.load(ICON_INFORMATION, None)

    def winlogo(self):
        """
        从系统获取Logo图标
        """
        return self.load(ICON_WINLOGO, None)

    def waring(self):
        """
        从系统获取错误图标
        """
        return self.load(ICON_WARNING, None)

    def createfrom(self, icon):
        """
        创建图标，返回图标ID
        """
        return self._master.tk.call('winico', 'createfrom',
                                    icon)

    def taskbar(self, id="add"):
        """
        用于将图标加入托盘，但是需要安装winico，如果没安装，请使用download_winico()安装

        :param id: 默认是add，其他选项还有modify和delete
        """
        self._master.tk.call('winico', 'taskbar', id, self._icon,
                             '-callback', (self._master.register(self._menu_func), '%m', '%i', self, '%x', '%y'),
                             '-pos', 0,
                             '-text', self._text)

    def taskbar_add(self):
        self.taskbar(id="add")

    def taskbar_modify(self):
        self.taskbar(id="modify")

    def taskbar_delete(self):
        self.taskbar(id="delete")

    def taskbar_delete_me(self):
        self.delete(id=self._icon)

    show = taskbar_add

    hide = taskbar_delete

    def load(self, resourcename, filename=None):
        """
        用于加载一些可执行文件上的资源。
        """
        return self._master.tk.call('winico', 'load', resourcename, filename)

    def setwindow(self, windowid, size="big"):
        """
        :param windowid: 设置主窗口，可以是Tk窗口，可以是窗柄。注意：必须映射窗口。如果不是，则可能会失败或崩溃。
        :param size: 用于调整大小，默认是big，可选small。
        """
        self._master.tk.call('winico', 'setwindow', windowid, size, )

    def info(self, id):
        """
        需要ID参数，然后托盘信息

        :param id: 为图标的ID，在
        """
        return self._master.tk.call("winico", "info", id)

    def delete(self, id):
        """
        删除托盘图标
        :param id: 为删除托盘图标的ID，可以使用createfrom()获取到。
        """
        return self._master.tk.call("winico", "delete", id)

    def menu(self, event, icon_id, icon, x, y):
        """
        内置菜单，用于初始化。
        """
        if event == WM_RBUTTONDOWN:
            menu = tkinter.Menu(tearoff=False)
            menu.add_command(label="退出", command=self.master.quit)
            menu.tk_popup(x, y)


class DevTwApi(object):
    def __init__(self, master: tkinter.Tk):
        from win32gui import GetParent
        self._master = master

        self._hwin = GetParent(self._master.winfo_id())

    def twapi(self, command, hwin):
        return self._master.tk.call(f"twapi::{command}", hwin)

    def get_hwin(self):
        return self._hwin

    def find_windows(self):
        return self._master.tk.call("twapi::find_windows")

    def get_parent_window(self):
        return self.twapi("get_parent_window")

    def get_window_text(self, hwin):
        return self._master.tk.call('twapi', "get_window_text")

    def minimize_window(self, hwin):
        return self.twapi("minimize_window", hwin)

    def window_maximized(self, hwin):
        return self.twapi("window_maximized", hwin)

    def window_minimized(self, hwin):
        return self.twapi("window_minimized", hwin)

    def use_twapi_all(self):
        self._master.tk.call('package', 'require', "twapi")
        self._master.tk.call('package', 'require', "twapi_com")
        self._master.tk.call('package', 'require', "twapi_msi")
        self._master.tk.call('package', 'require', "twapi_base")
        self._master.tk.call('package', 'require', "twapi_ui")


if __name__ == '__main__':
    root = tkinter.Tk()
    DevTray(root).show()
    root.mainloop()
