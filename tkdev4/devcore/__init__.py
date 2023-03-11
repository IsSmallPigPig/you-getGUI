import tkinter as tk
from tkdev4.devicon import Icon_TkinterDev


def EmptyFunc():
    pass


class DevAction(object):
    def __init__(self, text: str = "", icon: str = None, command=EmptyFunc, bg="white", fg="black", active_bg="white", active_fg="black"):
        """
        用于重复组件的快速调用。
        """
        self._text = text
        self._icon = icon
        self._command = command
        self._bg = bg
        self._fg = fg
        self._active_bg = active_bg
        self._active_fg = active_fg

    @property
    def icon(self) -> str:
        """
        用于获取图标
        """
        return self._icon

    @icon.setter
    def icon(self, icon: tk.PhotoImage) -> None:
        """
        用于设置图标
        """
        self._icon = icon

    @property
    def text(self) -> str:
        """
        用于获取文本
        """
        return self._text

    @text.setter
    def text(self, text: str = None) -> None:
        """
        用于设置文本
        """
        self._text = text

    @property
    def command(self):
        """
        用于获取被触发的函数
        """
        return self._command

    @command.setter
    def command(self, command=None) -> None:
        """
        用于设置被触发的函数
        """
        self._command = command

    @property
    def background(self):
        """
        用于获取背景颜色
        """
        return self._bg

    @background.setter
    def background(self, backgroud=None) -> None:
        """
        用于设置背景颜色
        """
        self._bg = backgroud

    @property
    def foreground(self):
        """
        用于获取前景颜色
        """
        return self._fg

    @foreground.setter
    def foreground(self, foregroud=None) -> None:
        """
        用于设置前景颜色
        """
        self._fg = foregroud

    @property
    def active_background(self):
        """
        用于获取触发时的背景颜色
        """
        return self._active_bg

    @active_background.setter
    def active_background(self, backgroud=None) -> None:
        """
        用于设置触发时的背景颜色
        """
        self._active_bg = backgroud

    @property
    def active_foreground(self):
        """
        用于获取出发时的前景颜色
        """
        return self._active_fg

    @active_foreground.setter
    def active_foreground(self, foregroud=None) -> None:
        """
        用于设置出发时的前景颜色
        """
        self._active_fg = foregroud


class DevSysTray(object):
    def __init__(self, name: str = "", title: str = "", icon: str = Icon_TkinterDev):
        from PIL import Image
        self.menu = []
        self.name = name
        self.title = title
        self.icon = Image.open(icon)

    def add_menu(self, title: str = "", command=EmptyFunc):
        """
        用于添加菜单
        """
        from pystray import MenuItem
        self.menu.append(MenuItem(text=title, action=command))

    def add_action(self, action: DevAction):
        """
        获取DevAction组件的参数，并使用add_menu添加
        """
        self.add_menu(title=action.text, command=action.command)

    def show(self):
        """
        用于显示
        """
        from pystray import Icon
        self.Icon = Icon(name=self.name, title=self.title, menu=self.menu, icon=self.icon)
        self.Icon.run()

    def stop(self):
        """
        用于关闭
        """
        self.Icon.stop()

    def notify(self, message: str = "", title: str = ""):
        self.Icon.notify()
