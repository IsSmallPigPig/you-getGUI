try:
    import ctypes
except:
    pass
import tkinter as tk
import tkinter.ttk as ttk

try:
    from ctypes import POINTER, Structure, windll
    from ctypes.wintypes import DWORD, ULONG, BOOL, HRGN
except:
    pass
from enum import Enum

from tkdev4.devplyer import set_auto_install_plyer, install_plyer, DevNotification, DevEmail
from tkdev4.devicon import Icon_Empty, Icon_Folder, Icon_TkinterDev
from tkdev4.devcore import DevAction
from tkdev4.devtcl import (DevTray, ICON_APPLICATION, ICON_MODE_LOAD)

try:
    from deprecated.sphinx import deprecated
except ImportError:
    pass

try:
    from win32gui import *
    from win32con import *
    from win32api import *
    from win32ui import *
    from win32com import *
except ImportError:
    pass
try:
    import darkdetect
except ImportError:
    pass

try:
    taskbar_height = GetMonitorInfo(MonitorFromPoint((0, 0))).get("Monitor")[3] - \
                     GetMonitorInfo(MonitorFromPoint((0, 0))).get("Work")[3]
except NameError:
    pass
Auto = "auto"
Light = "light"
Dark = "dark"

DWMWA_USE_IMMERSIVE_DARK_MODE = 20


def AddShortCut(File, Link="link.lnk", Path: str = ".//"):
    """
    给文件添加一个快捷键到指定位置

    :param File: 指定文件，
    :param Link: 指定快捷键名称。
    :param Path: 指定保存的位置。
    """

    from win32com.client import Dispatch
    from shutil import move
    Shell = Dispatch("WScript.Shell")
    ShortCut = Shell.CreateShortCut(Link)
    ShortCut.TargetPath = File
    ShortCut.save()
    move(Link, Path)


def AddStartMenu(File: str):
    from getpass import getuser
    from shutil import move
    move(File, f"C:\\Users\\{getuser()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs")


def AutoStart(File: str, Name: str = "Application"):
    try:
        Key = RegOpenKey(HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, KEY_ALL_ACCESS)
        RegSetValueEx(Key, Name, 0, REG_SZ, File)
        RegCloseKey(Key)
    except:
        print('Add Error')


def Package(File, Ofter="-w", StartMenu: bool = True):
    """
    用于打包Python文件。
    """

    try:
        import pyinstaller
    except:
        Install("pyinstaller")
    import sys
    import os.path

    os.system(os.path.split(sys.executable)[0] + f"\\Scripts\\pyinstaller.exe {Ofter} {File}")

    if StartMenu:
        from getpass import getuser
        print("asdas")
        name = os.path.splitext(os.path.split(File)[1])[0]
        print(name)
        if os.path.exists("dist\\" + name + ".exe"):
            path = "dist\\" + name + ".exe"
        elif os.path.exists("dist\\" + name + "\\" + name + ".exe"):
            path = "dist\\" + name + "\\" + name + ".exe"
        print(path)
        print(os.getcwd())
        from win32com.client import Dispatch
        from shutil import move
        Shell = Dispatch("WScript.Shell")
        ShortCut = Shell.CreateShortCut(name + ".lnk")
        ShortCut.TargetPath = os.getcwd() + "\\" + path
        ShortCut.save()
        move(name + ".lnk", f"C:\\Users\\{getuser()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs")


def UpGrade(Library, Basic: bool = True, Preview: bool = False, Pypi="https://pypi.tuna.tsinghua.edu.cn/simple/"):
    import os
    import sys
    Pre = ""
    if Basic:
        Librarys = f"-i {Pypi}"
    if Preview:
        Pre = f"--pre"
    print(f"{sys.executable} -m pip install {Library} {Librarys} {Pre} --upgrade")
    os.system(f"{sys.executable} -m pip install {Library} {Librarys} {Pre} --upgrade")


def Install(Library, Basic: bool = True, Preview: bool = False, Pypi="https://pypi.tuna.tsinghua.edu.cn/simple/"):
    import os
    import sys
    Pre = ""
    if Basic:
        Librarys = f"-i {Pypi}"
    if Preview:
        Pre = f"--pre"
    print(f"{sys.executable} -m pip install {Library} {Librarys} {Pre}")
    os.system(f"{sys.executable} -m pip install {Library} {Librarys} {Pre}")


def Install_ALL(Basic=True, Preview: bool = False, Pypi="https://pypi.tuna.tsinghua.edu.cn/simple/"):
    import sys
    Install("win10toast", Basic=Basic, Pypi=Pypi, Preview=Preview)
    Install("pywin32", Basic=Basic, Pypi=Pypi, Preview=Preview)
    if sys.platform == "win32" and sys.getwindowsversion().build >= 22000:
        Install("win32mica", Basic=Basic, Pypi=Pypi, Preview=Preview)
    Install("BlurWindow", Basic=Basic, Pypi=Pypi, Preview=Preview)
    Install("darkdetect", Basic=Basic, Pypi=Pypi, Preview=Preview)
    Install("tkcap", Basic=Basic, Pypi=Pypi, Preview=Preview)
    Install("plyer", Basic=Basic, Pypi=Pypi, Preview=Preview)


def UnInstall(Library):
    import os
    import sys
    if Basic:
        print(f"{sys.executable} -m pip uninstall {Library}")
        os.system(f"{sys.executable} -m pip uninstall {Library} ")


def Empty_Func():
    pass


class AccentState(Enum):
    ACCENT_DISABLED = 0,
    ACCENT_ENABLE_GRADIENT = 1,
    ACCENT_ENABLE_TRANSPARENTGRADIENT = 2,
    ACCENT_ENABLE_BLURBEHIND = 3,
    ACCENT_ENABLE_ACRYLICBLURBEHIND = 4,
    ACCENT_INVALID_STATE = 5,


class WindowComPositionAttribute(Enum):
    WCA_UNDEFINED = 0,
    WCA_NCRENDERING_ENABLED = 1,
    WCA_NCRENDERING_POLICY = 2,
    WCA_TRANSITIONS_FORCEDISABLED = 3,
    WCA_ALLOW_NCPAINT = 4,
    WCA_CAPTION_BUTTON_BOUNDS = 5,
    WCA_NONCLIENT_RTL_LAYOUT = 6,
    WCA_FORCE_ICONIC_REPRESENTATION = 7,
    WCA_EXTENDED_FRAME_BOUNDS = 8,
    WCA_HAS_ICONIC_BITMAP = 9,
    WCA_THEME_ATTRIBUTES = 10,
    WCA_NCRENDERING_EXILED = 11,
    WCA_NCADORNMENTINFO = 12,
    WCA_EXCLUDED_FROM_LIVEPREVIEW = 13,
    WCA_VIDEO_OVERLAY_ACTIVE = 14,
    WCA_FORCE_ACTIVEWINDOW_APPEARANCE = 15,
    WCA_DISALLOW_PEEK = 16,
    WCA_CLOAK = 17,
    WCA_CLOAKED = 18,
    WCA_ACCENT_POLICY = 19,
    WCA_FREEZE_REPRESENTATION = 20,
    WCA_EVER_UNCLOAKED = 21,
    WCA_VISUAL_OWNER = 22,
    WCA_LAST = 23


class DWM_BLURBEHIND(ctypes.Structure):
    _fields_ = [
        ('dwFlags', DWORD),
        ('fEnable', BOOL),
        ('hRgnBlur', HRGN),
        ('fTransitionOnMaximized', BOOL)
    ]


class DwmWindowAttribute(Enum):
    DWMWA_NCRENDERING_ENABLED = 1
    DWMWA_NCRENDERING_POLICY = 2
    DWMWA_TRANSITIONS_FORCEDISABLED = 3
    DWMWA_ALLOW_NCPAINT = 4
    DWMWA_CAPTION_BUTTON_BOUNDS = 5
    DWMWA_NONCLIENT_RTL_LAYOUT = 6
    DWMWA_FORCE_ICONIC_REPRESENTATION = 7
    DWMWA_FLIP3D_POLICY = 8
    DWMWA_EXTENDED_FRAME_BOUNDS = 9
    DWMWA_HAS_ICONIC_BITMAP = 10
    DWMWA_DISALLOW_PEEK = 11
    DWMWA_EXCLUDED_FROM_PEEK = 12
    DWMWA_CLOAK = 13
    DWMWA_CLOAKED = 14
    DWMWA_FREEZE_REPRESENTATION = 15
    DWMWA_PASSIVE_UPDATE_MODE = 16
    DWMWA_USE_HOSTBACKDROPBRUSH = 17
    DWMWA_USE_IMMERSIVE_DARK_MODE = 18
    DWMWA_WINDOW_CORNER_PREFERENCE = 19
    DWMWA_BORDER_COLOR = 20
    DWMWA_CAPTION_COLOR = 21
    DWMWA_TEXT_COLOR = 22
    DWMWA_VISIBLE_FRAME_BORDER_THICKNESS = 23
    DWMWA_LAST = 24


class Accent_Poltcy(Structure):
    """ 设置客户区的具体属性 """
    _fields_ = [
        ('AccentState', DWORD),
        ('AccentFlags', DWORD),
        ('GradientColor', DWORD),
        ('AnimationId', DWORD),
    ]


class WindowComPositionAttributeData(Structure):
    _fields_ = [
        ('Attribute', DWORD),
        ('Data', POINTER(Accent_Poltcy)),  # POINTER()接收任何ctypes类型，并返回一个指针类型
        ('SizeOfData', ULONG),
    ]


class MARGINS(Structure):
    _fields_ = [
        ("cxLeftWidth", ctypes.c_int),
        ("cxRightWidth", ctypes.c_int),
        ("cyTopHeight", ctypes.c_int),
        ("cyBottomHeight", ctypes.c_int),
    ]


def Error(text):
    try:
        from colorama import Fore
    except ImportError:
        print(text)
    else:
        print(Fore.RED + text + Fore.RESET)


class DevManage(object):
    def __init__(self, master: tk.Tk):
        """
        用于管理窗口高级功能。

        :param master: 管理的组件。
        """
        self._master = ctypes.windll.user32.GetParent(master.winfo_id())
        self._master_tk = master
        self.DwmApi = ctypes.windll.dwmapi
        self.Win32 = ctypes.windll.user32
        self.UXTheme = ctypes.windll.uxtheme
        self.Shcore = ctypes.windll.shcore
        self.DwmSetWindowAttribute = self.DwmApi.DwmSetWindowAttribute
        self.DwmGetWindowAttribute = self.DwmApi.DwmGetWindowAttribute
        self.DwmGetColorizationColor = self.DwmApi.DwmGetColorizationColor
        self.DwmEnableBlurBehindWindow = self.DwmApi.DwmEnableBlurBehindWindow
        self.DwmIsCompositionEnabled = self.DwmApi.DwmIsCompositionEnabled
        self.DwmExtendFrameIntoClientArea = self.DwmApi.DwmExtendFrameIntoClientArea
        self.DwmRegisterThumbnail = self.DwmApi.DwmRegisterThumbnail

        self.SetWindowCompositionAttribute = self.Win32.SetWindowCompositionAttribute

        self.DWMSBT_AUTO = 0
        self.DWMSBT_NONE = 1
        self.DWMSBT_MAINWINDOW = 2
        self.DWMSBT_TRANSIENTWINDOW = 3
        self.DWMSBT_TABBEDWINDOW = 4

        self.DWMNCRP_USEWINDOWSTYLE = 0
        self.DWMNCRP_DISABLED = 1
        self.DWMNCRP_ENABLED = 2
        self.DWMNCRP_LAS = 3

        self.DWMWCP_DEFAULT = 0
        self.DWMWCP_DONOTROUND = 1
        self.DWMWCP_ROUND = 2
        self.DWMWCP_ROUNDSMALL = 3

        self.ACCENT_DISABLED = 0,
        self.ACCENT_ENABLE_GRADIENT = 1,
        self.ACCENT_ENABLE_TRANSPARENTGRADIENT = 2,
        self.ACCENT_ENABLE_BLURBEHIND = 3,  # Aero效果
        self.ACCENT_ENABLE_ACRYLICBLURBEHIND = 4,  # 亚克力效果
        self.ACCENT_INVALID_STATE = 5

        self.DWM_BB_ENABLE = 0x00000001
        self.DWM_BB_BLURREGION = 0x00000002
        self.DWM_BB_TRANSITIONONMAXIMIZED = 0x00000004

        self.DWMWA_NCRENDERING_ENABLED = 1
        self.DWMWA_NCRENDERING_POLICY = 2
        self.DWMWA_TRANSITIONS_FORCEDISABLED = 3
        self.DWMWA_ALLOW_NCPAINT = 4
        self.DWMWA_CAPTION_BUTTON_BOUNDS = 5
        self.DWMWA_NONCLIENT_RTL_LAYOUT = 6
        self.DWMWA_FORCE_ICONIC_REPRESENTATION = 7
        self.DWMWA_FLIP3D_POLICY = 8
        self.DWMWA_EXTENDED_FRAME_BOUNDS = 9
        self.DWMWA_HAS_ICONIC_BITMAP = 10
        self.DWMWA_DISALLOW_PEEK = 11
        self.DWMWA_EXCLUDED_FROM_PEEK = 12
        self.DWMWA_CLOAK = 13
        self.DWMWA_CLOAKED = 14
        self.DWMWA_FREEZE_REPRESENTATION = 15
        self.DWMWA_PASSIVE_UPDATE_MODE = 16
        self.DWMWA_USE_HOSTBACKDROPBRUSH = 17
        self.DWMWA_CAPTION_COLOR = 19
        self.DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        self.DWMWA_LAST = 24
        self.DWMWA_WINDOW_CORNER_PREFERENCE = 33
        self.DWMWA_BORDER_COLOR = 34
        self.DWMWA_TEXT_COLOR = 36
        self.DWMWA_VISIBLE_FRAME_BORDER_THICKNESS = 37
        self.DWMWA_SYSTEMBACKDROP_TYPE = 38

        self.DWMSC_DOWN = 0
        self.DWMSC_UP = 1
        self.DWMSC_DRAG = 2
        self.DWMSC_HOLD = 3
        self.DWMSC_PENBARREL = 4
        self.DWMSC_NONE = 5
        self.DWMSC_ALL = 6

        self.rgbRed = 0x000000FF
        self.rgbGreen = 0x0000FF00
        self.rgbBlue = 0x00FF0000
        self.rgbBlack = 0x00000000
        self.rgbWhite = 0x00FFFFFF

    def high_dpi(self):
        try:
            self.Shcore.SetProcessDpiAwareness(2)
        except:
            self.Win32.SetProcessDPIAware()
        ScaleFactor = self.Shcore.GetScaleFactorForDevice(0)
        self._master_tk.tk.call('tk', 'scaling', ScaleFactor / 75)

    def window_screenshot(self):
        from tkcap import CAP
        return CAP(self._master).capture(image_name)

    def dwm_set_window_attribute(self, type, attribute, size):
        """
        用于对非客户区进行设置。
        """
        self.DwmSetWindowAttribute(
            self._master,
            type,
            attribute,
            size
        )

    def dwm_get_window_attribute(self, type, size):
        """
        用于对非客户区进行设置。
        """
        return self.DwmGetWindowAttribute(
            self._master,
            type,
            size
        )

    def dwm_set_window_attribute_use_dark_mode(self):
        """
        设置窗口主题为黑暗模式，标题栏会有所改变。
        """
        Value = ctypes.c_int(2)
        self.dwm_set_window_attribute(
            self.DWMWA_USE_IMMERSIVE_DARK_MODE,
            ctypes.byref(Value),
            ctypes.sizeof(Value)
        )

    def dwm_get_window_attribute_use_dark_mode(self):
        """
        设置窗口主题为黑暗模式，标题栏会有所改变。
        """
        Value = ctypes.c_int(self.DWMWA_USE_IMMERSIVE_DARK_MODE)
        self.dwm_get_window_attribute(
            self.DWMWA_USE_IMMERSIVE_DARK_MODE,
            ctypes.sizeof(Value)
        )

    def dwm_set_window_attribute_use_light_mode(self):
        """
        设置窗口主题为明亮模式，标题栏会有所改变。
        """
        Value = ctypes.c_int(0)
        self.dwm_set_window_attribute(
            self.DWMWA_USE_IMMERSIVE_DARK_MODE,
            ctypes.byref(Value),
            ctypes.sizeof(Value)
        )

    def dwm_set_window_attribute_systembackdrop_type(self, type=1):
        Value = ctypes.c_int(type)
        self.dwm_set_window_attribute(self.DWMWA_SYSTEMBACKDROP_TYPE, ctypes.byref(Value), ctypes.sizeof(Value))

    def dwm_set_window_attribute_systembackdrop_type_auto(self):
        self.dwm_set_window_attribute_systembackdrop_type(self.DWMSBT_AUTO)

    def dwm_set_window_attribute_systembackdrop_type_none(self):
        self.dwm_set_window_attribute_systembackdrop_type(self.DWMSBT_NONE)

    def dwm_set_window_attribute_systembackdrop_type_mainwindow(self):
        self.dwm_set_window_attribute_systembackdrop_type(self.DWMSBT_MAINWINDOW)

    def dwm_set_window_attribute_systembackdrop_type_transient_window(self):
        self.dwm_set_window_attribute_systembackdrop_type(self.DWMSBT_TRANSIENTWINDOW)

    def dwm_set_window_attribute_systembackdrop_type_tabbed_window(self):
        self.dwm_set_window_attribute_systembackdrop_type(self.DWMSBT_TABBEDWINDOW)

    def dwm_set_window_attribute_visible_frame_border_thickness(self, value):
        self.Value = ctypes.c_int(value)
        self.dwm_set_window_attribute(self.DWMWA_VISIBLE_FRAME_BORDER_THICKNESS, ctypes.byref(self.Value),
                                      ctypes.sizeof(self.Value))

    def dwm_set_window_attribute_ncrendering_policy(self, value=2):
        Value = ctypes.c_int(value)
        self.dwm_set_window_attribute(self.DWMWA_NCRENDERING_POLICY,
                                      ctypes.byref(Value), ctypes.sizeof(Value))

    def dwm_set_window_attribute_border_color(self, color=0x00FF0000):
        Value = ctypes.c_int(color)
        self.dwm_set_window_attribute(self.DWMWA_BORDER_COLOR, ctypes.byref(Value), ctypes.sizeof(Value))

    def dwm_set_window_attribute_text_color(self, color=0x00FF0000):
        Value = ctypes.c_int(color)
        self.dwm_set_window_attribute(self.DWMWA_TEXT_COLOR, ctypes.byref(Value), ctypes.sizeof(Value))

    def dwm_set_window_attribute_caption_color(self, color=0x00FF0000):
        Value = ctypes.c_int(color)
        self.dwm_set_window_attribute(self.DWMWA_CAPTION_COLOR, ctypes.byref(Value), ctypes.sizeof(Value))

    def dwm_set_window_round(self, value):
        Value = ctypes.c_int(value)
        self.dwm_set_window_attribute(
            self.DWMWA_WINDOW_CORNER_PREFERENCE,
            ctypes.byref(Value),
            ctypes.sizeof(Value)
        )

    def dwm_set_window_round_default(self):
        self.dwm_set_window_round(self.DWMWCP_DEFAULT)

    def dwm_set_window_round_donot_round(self):
        self.dwm_set_window_round(self.DWMWCP_DONOTROUND)

    def dwm_set_window_round_round(self):
        self.dwm_set_window_round(self.DWMWCP_ROUND)

    def dwm_set_window_round_round_small(self):
        self.dwm_set_window_round(self.DWMWCP_ROUNDSMALL)

    def dwm_get_window_attribute(self, type, put):
        """
        获取非客户区的属性。
        """
        return self.DwmGetWindowAttribute(
            self._master,
            type,
            put
        )

    def dwm_get_colorization_color(self):
        return self.DwmGetColorizationColor()

    def dwm_enable_blurbehind_window(self, flags=0x00000001, enable: bool = True, rgn_blur=1,
                                     transition_on_maximized: bool = True):
        BlurBehid = DWM_BLURBEHIND()
        BlurBehid.dwFlags = flags
        BlurBehid.fEnable = enable
        BlurBehid.hRgnBlur = rgn_blur
        BlurBehid.TransitionOnMaximized = transition_on_maximized
        return self.DwmEnableBlurBehindWindow(self._master, ctypes.byref(BlurBehid))

    def dwm_is_composition_enabled(self):
        return self.DwmIsCompositionEnabled()

    def dwm_extend_frame_into_client_area(self, margins=[-1, -1, -1, -1]):
        Margins = MARGINS(margins[0], margins[1], margins[2], margins[3])
        return self.DwmExtendFrameIntoClientArea(self._master, ctypes.byref(Margins))

    def dwm_register_thumbnail(self, id):
        return self.DwmRegisterThumbnail(self._master, self.find_window("Program", NULL), id)

    def use_mica(self, is_dark=False):
        """
        使用Windows11的云母特效。

        :param is_dark: 用来设置是否是黑暗模式
        """
        from win32mica import ApplyMica
        return ApplyMica(self._master, is_dark)

    def use_mica_mode_light(self):
        """
        使用Windows11的云母特效。设置为明亮模式
        """
        return self.use_mica(False)

    def use_mica_mode_dark(self):
        """
        使用Windows11的云母特效。设置为暗黑模式
        """
        return self.use_mica(True)

    def use_mica_mode_auto(self):
        """
        使用Windows11的云母特效。主题会变成和系统一样颜色的。
        """
        import darkdetect
        if darkdetect.isLight():
            self.use_mica_mode_light()
        elif darkdetect.isDark():
            self.use_mica_mode_dark()

    def use_acrylic(self, is_dark=False, hex_color: bool = False, acrylic: bool = False):
        """
        使用Windows10的亚克力特效。

        :param is_dark: 用来设置是否是黑暗模式
        """
        from BlurWindow import blurWindow
        return blurWindow.GlobalBlur(self._master, Dark=is_dark, hexColor=hex_color, Acrylic=acrylic)

    def use_acrylic_mode_light(self, hex_color: bool = False, acrylic: bool = False):
        """
        使用Windows10的亚克力特效。设置为明亮模式
        """
        return self.use_acrylic(False, hex_color, acrylic)

    def use_acrylic_mode_dark(self, hex_color: bool = False, acrylic: bool = False):
        """
        使用Windows10的亚克力特效。设置为黑暗模式
        """
        return self.use_acrylic(True, hex_color, acrylic)

    def use_acrylic_mode_auto(self, hex_color: bool = False, acrylic: bool = False):
        """
        使用Windows10的亚克力特效。主题会变成和系统一样颜色的。
        """
        import darkdetect
        if darkdetect.isLight():
            self.use_acrylic_mode_light(hex_color, acrylic)
        elif darkdetect.isDark():
            self.use_acrylic_mode_dark(hex_color, acrylic)

    def update_window(self):
        """
        刷新窗口
        """
        return UpdateWindow(self._master)

    def enable_theming(self, bool: bool):
        return self.UXTheme.EnableTheming(bool)

    def find_window(self, Class, Name):
        return FindWindow(Class, Name)

    def set_master(self, master: tk.Tk):
        """
        设置组件的父组件。
        """
        SetParent(self._master, GetParent(master.winfo_id()))

    def set_window_text(self, text):
        return SetWindowText(self._master, text)

    def set_window_long(self, setting):
        """
        设置窗口样式
        """
        return SetWindowLong(self._master, GWL_STYLE, setting)

    def set_window_ex_long(self, setting):
        """
        设置窗口扩展样式
        """
        return SetWindowLong(self._master, GWL_EXSTYLE, setting)

    def set_window_pos(self, after, x, y, width, height, flags):
        SetWindowPos(self._master, after, x, y, width, height, flags)

    def set_window_pos_center(self):
        """
        将窗口放在屏幕中心。
        """
        x = self._master_tk.winfo_screenwidth() / 2 - self._master_tk.winfo_width() / 2
        y = self._master_tk.winfo_screenheight() / 2 - self._master_tk.winfo_height() / 2
        self._master_tk.geometry(
            f"{self._master_tk.winfo_width()}x{self._master_tk.winfo_height()}+{round(x)}+{round(y)}"
        )

    def set_window_pos_bottom_right(self, padx: int = 15, pady: int = 15):
        """
        将窗口放在右下位置，

        :param padx: 表示X间距
        :param pady: 表示Y间距
        """
        self._master_tk.after(1, lambda: self._master_tk.geometry(
            f"+{self._master_tk.winfo_screenwidth() - self._master_tk.winfo_width() - padx - 10}+"
            f"{self._master_tk.winfo_screenheight() - taskbar_height - self._master_tk.winfo_height() - pady - 35}"))

    def set_window_pos_bottom_left(self, padx: int = 15, pady: int = 15):
        """
        将窗口放在左下位置。

        :param padx: 表示X间距
        :param pady: 表示Y间距
        """
        self._master_tk.after(1, lambda: self._master_tk.geometry(
            f"+{padx}+{self._master_tk.winfo_screenheight() - taskbar_height - self._master_tk.winfo_height() - pady - 35}"))

    def set_window_pos_top_right(self, padx: int = 15, pady: int = 15):
        """
        将窗口放在右上位置。

        :param padx: 表示X间距
        :param pady: 表示Y间距
        """
        self._master_tk.after(1, lambda: self._master_tk.geometry(
            f"+{self._master_tk.winfo_screenwidth() - self._master_tk.winfo_width() - padx - 10}+{pady}"))

    def set_window_pos_top_left(self, padx: int = 15, pady: int = 15):
        """
        将窗口放在左上位置

        :param padx: 表示X间距
        :param pady: 表示Y间距
        """
        self._master_tk.after(1, lambda: self._master_tk.geometry(
            f"+{padx}+{pady}"))

    def get_window_long(self):
        return GetWindowLong(self._master, GWL_STYLE)

    def get_window_ex_long(self):
        return GetWindowLong(self._master, GWL_EXSTYLE)

    def add_window_popup(self):
        return self.add_window_long(WS_POPUP)

    def add_window_long(self, setting):
        return SetWindowLong(self._master, GWL_STYLE, self.get_window_long() & ~setting)

    def add_window_ex_long(self, setting):
        return SetWindowLong(self._master, GWL_EXSTYLE, self.get_window_ex_long() & ~setting)

    def add_window_popup_window(self):
        return self.add_window_long(WS_POPUPWINDOW)

    def add_window_init_minimize(self):
        return self.add_window_long(WS_MINIMIZE)

    def add_window_init_maximize(self):
        return self.add_window_long(WS_MAXIMIZE)

    def add_window_init_disable(self):
        return self.add_window_long(WS_DISABLED)

    def add_window_init_visible(self):
        return self.add_window_long(WS_VISIBLE)

    def add_window_sysmenu(self):
        return self.add_window_long(WS_SYSMENU)

    def add_window_toolwindow(self):
        return self.add_window_ex_long(WS_EX_TOOLWINDOW)

    def add_window_maximizebox(self):
        return self.add_window_long(WS_MAXIMIZEBOX)

    def add_window_minimizebox(self):
        return self.add_window_long(WS_MINIMIZEBOX)

    def add_window_caption(self):
        return self.add_window_long(WS_CAPTION)

    def add_window_titlebar(self):
        def titlebar():
            self.add_window_long(WS_CAPTION)
            self.set_window_pos(NULL, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE | SWP_NOZORDER | SWP_DRAWFRAME)
            self.update_window()

        self._master_tk.after(100, lambda: titlebar())

    def add_window_border(self):
        return self.add_window_long(WS_BORDER)

    def add_window_dlg_frame(self):
        return self.add_window_long(WS_DLGFRAME)

    def add_window_think_frame(self):
        return self.add_window_long(WS_THICKFRAME)

    def add_window_resize_border_frame(self):
        return self.add_window_long(WS_THICKFRAME)

    def add_window_child(self):
        return self.add_window_long(WS_CHILD)

    def release_capture(self):
        """
        使用ReleaseCapture释放并捕捉数据
        """
        return ReleaseCapture()

    def send_message(self, window, message, wParam, lParam):
        """
        使用SendMessage发送消息给Window，

        :param window: 接收消息的窗口
        :param message: 为要发送的消息
        :param wParam: 附加项
        :param lParam: 附加项
        """
        return SendMessage(GetParent(window.winfo_id()), message, wParam, lParam)

    def send_message_move_window(self, window):
        """
        拖动当前控件移动参数window。

        :param window: 被拖动的窗口
        """

        def move():
            self.release_capture()
            self.send_message(window, WM_SYSCOMMAND, SC_MOVE + HTCAPTION, 0)

        self._master_tk.bind("<B1-Motion>", lambda event: move())

    def show_window(self, state):
        return ShowWindow(self._master, state)

    def show_window_hide(self):
        return self.show_window(SW_HIDE)

    def show_window_maximize(self):
        return self.show_window(SW_MAXIMIZE)

    def show_window_minimize(self):
        return self.show_window(SW_MINIMIZE)

    def show_window_restore(self):
        return self.show_window(SW_RESTORE)

    def show_window_show(self):
        return self.show_window(SW_SHOW)

    def show_window_show_maximize(self):
        return self.show_window(SW_SHOWMAXIMIZED)

    def show_window_show_minimize(self):
        return self.show_window(SW_SHOWMINIMIZED)

    def show_window_show_minno_action(self):
        return self.show_window(SW_SHOWMINNOACTIVE)

    def show_window_show_na(self):
        return self.show_window(SW_SHOWNA)

    def show_window_show_normal(self):
        return self.show_window(SW_SHOWNORMAL)

    def close_window(self):
        return CloseWindow(self._master)

    def minimize_window(self):
        return CloseWindow(self._master)

    def enable_window(self, bool: bool):
        return EnableWindow(self._master, bool)

    def destroy_window(self):
        return DestroyWindow(self._master)

    def destroy_icon(self):
        return DestroyIcon(self._master)

    def drag_accept_files(self, bool: bool):
        return DragAcceptFiles(self._master, bool)

    def drag_finish(self):
        return DragFinish()

    def draw_menubar(self):
        return DrawMenuBar(self._master)

    def create_menu(self):
        return CreateMenu()

    def set_menu(self, menu):
        return SetMenu(self._master,
                       menu)


class DevAccumulatorButton(tk.Button):
    def __init__(self):
        super(DevAccumulatorButton, self).__init__()
        pass


class DevAppBar(tk.Frame):
    def __init__(self, master: tk.Widget = None, title: str = "", background="#ffffff", foreground="#000000"):
        """
        应用程序栏，
        """
        super(DevAppBar, self).__init__(master=master, relief=tk.FLAT, background=background)
        self.title = tk.Label(self, text=title, justify=tk.LEFT, background=background, foreground=foreground)
        self.title.pack(fill=tk.Y, side=tk.LEFT, padx=10, pady=5)

    def show(self):
        """
        显示组件在窗口的最上方
        """
        self.pack(fill=tk.X, ipadx=10, ipady=10)


class DevButton(tk.Button):
    def __init__(self, master, text: str = "", borderwidth: int = 0, image=None, font=("等线 Light", 10, "bold"),
                 command=None,
                 default_bg="#ffffff", default_fg="#000000",
                 active_bg="#177aff", active_fg="#d6eaff",
                 click_bg="#175bff", click_fg="#d6deff"):
        super(DevButton, self).__init__(master=master, relief=tk.FLAT, text=text, font=float, command=command,
                                        borderwidth=borderwidth, image=image,
                                        background=default_bg, foreground=default_fg)
        self.default_bg = default_bg
        self.default_fg = default_fg
        self.active_bg = active_bg
        self.active_fg = active_fg
        self.click_bg = click_bg
        self.click_fg = click_fg
        self.bind("<Leave>", self.nofocus)
        self.bind("<Enter>", self.focus)
        self.bind("<Button-1>", self.click)

    def nofocus(self, event=None):
        self.configure(background=self.default_bg, foreground=self.default_fg)

    def focus(self, event=None):
        self.configure(background=self.active_bg, foreground=self.active_fg)

    def click(self, event=None):
        self.configure(activebackground=self.click_bg, activeforeground=self.click_fg)


class DevDrag(object):
    def __init__(self, widget: tk.Widget, dragwidget: tk.Widget, iswindow: bool = False, x: bool = True, y: bool = True,
                 click_func=None, noclick_func=None, move_func=None):
        """
        这个组件能够拖动组件移动，实现更高级的功能。

        :param widget: 设为拖动命令的组件，你拖动这个组件，拖动的组件会移动。
        :param dragwidget: 设为被拖动的组件。
        :param iswindow: 是声明你要拖动的组件是窗口还是组件，是窗口填True，是组件填False。
        """
        self.widget = widget
        self.dragwidget = dragwidget
        self.iswindow = iswindow
        self.movex = tk.IntVar(self.widget, value=0)
        self.movey = tk.IntVar(self.widget, value=0)
        self.moved = tk.BooleanVar(self.widget, value=False)
        if click_func is None:
            self.widget.bind("<Button-1>", self.click)
        else:
            self.widget.bind("<Button-1>", click_func)
        if noclick_func is None:
            self.widget.bind("<ButtonRelease-1>", self.noclick)
        else:
            self.widget.bind("<ButtonRelease-1>", noclick_func)
        if move_func is None:
            self.widget.bind("<B1-Motion>", self.move)
        else:
            self.widget.bind("<B1-Motion>", move_func)
        self.x = x
        self.y = y

    def move(self, event=None):
        """
        内置函数，处理被拖动时移动
        """
        if not self.moved.get():
            return

        if self.x:
            newx = self.dragwidget.winfo_x() + (event.x - self.movex.get())
        else:
            newx = self.dragwidget.winfo_x()

        if self.y:
            newy = self.dragwidget.winfo_y() + (event.y - self.movey.get())
        else:
            newy = self.dragwidget.winfo_y()
        geometry = f"{self.dragwidget.winfo_width()}x{self.dragwidget.winfo_height()}+{newx}+{newy}"
        if self.iswindow:
            self.dragwidget.geometry(geometry)
        else:
            self.dragwidget.place(x=newx, y=newy, width=self.dragwidget.winfo_width(),
                                  height=self.dragwidget.winfo_height())
        self.widget.update()

    def click(self, event=None):
        """
        内置函数，处理被点击时记录按下时的位置信息
        """
        self.movex.set(event.x)
        self.movey.set(event.y)
        self.moved.set(True)

    def noclick(self, event=None):
        """
        内置函数，处理放开后设置是否按下为否
        """
        self.moved.set(False)


class DevHeaderBar(tk.Frame):
    def __init__(self, master: tk.Tk, border: bool = True, background="#ffffff", double_max: bool = True):
        """
        标题栏组件，能够自定义窗口标题栏。

        :param master: 为被设置窗口。
        :param border: 设置是否保留边框
        :param background: 设置标题栏背景
        :param double_max: 设置是否可以通过双击按钮最大化。
        """
        super(DevHeaderBar, self).__init__(master=master, background=background, height=35)
        self.master = master
        self.master.configure(background="#fdfdfd")
        self.hWnd = GetParent(self.master.winfo_id())
        Manage = DevManage(self)
        Window_Manage = DevManage(self.master)
        if border:
            Window_Manage.add_window_titlebar()
        elif not border:
            Window_Manage.add_window_long(WS_CAPTION)
        Manage.send_message_move_window(self.master)
        self.ismaximize = False
        if double_max:
            self.bind("<Double-Button-1>", lambda evt: self.maximize())

    def add_close_button(self, text: str = "🗙", font=("微软雅黑", 9),
                         background="#ffffff", foreground="#000000",
                         activebackground="#c42b1c", activeforeground="#ffffff"):
        """
        为标题栏添加关闭按钮。

        :param text: 为关闭按钮的文本
        :param font: 为关闭按钮的字体
        :param background: 为关闭按钮的背景颜色
        :param foreground: 为关闭按钮的前景颜色
        :param activebackground: 为关闭按钮触发时的背景颜色
        :param activeforeground: 为关闭按钮触发时的前景颜色
        """
        self.close_button = tk.Button(self, text=text, border=0, font=font,
                                      background=background, foreground=foreground,
                                      activebackground=activebackground, activeforeground=activeforeground,
                                      command=lambda: self.master.destroy())
        self.close_button.pack(side=tk.RIGHT, ipady=1, ipadx=10, fill=tk.Y)

    def add_maximize_button(self, text: str = "🗖", font=("微软雅黑", 9),
                            background="#ffffff", foreground="#000000",
                            activebackground="#e9e9e9", activeforeground="#b5b5b5"):
        """
        为标题栏添加最大化按钮，

        :param text: 为最大化按钮的文本
        :param font: 为最大化按钮的字体
        :param background: 为最大化按钮的背景颜色
        :param foreground: 为最大化按钮的前景颜色
        :param activebackground: 为最大化按钮触发时的背景颜色
        :param activeforeground: 为最大化按钮触发时的前景颜色
        """
        self.maxmize_button = tk.Button(self, text=text, border=0, font=font,
                                        background=background, foreground=foreground,
                                        activebackground=activebackground, activeforeground=activeforeground,
                                        command=self.maximize_event)
        self.maxmize_button.pack(side=tk.RIGHT, ipady=2, ipadx=12, fill=tk.Y)

    def add_minimize_button(self, text: str = "🗕", font=("微软雅黑", 9),
                            background="#ffffff", foreground="#000000",
                            activebackground="#e9e9e9", activeforeground="#b5b5b5"):
        """
        为标题栏添加最小化按钮，

        :param text: 为最小化按钮的文本
        :param font: 为最小化按钮的字体
        :param background: 为最小化按钮的背景颜色
        :param foreground: 为最小化按钮的前景颜色
        :param activebackground: 为最小化按钮触发时的背景颜色
        :param activeforeground: 为最小化按钮触发时的前景颜色
        """
        self.minimize_button = tk.Button(self, text=text, border=0, font=font,
                                         background=background, foreground=foreground,
                                         activebackground=activebackground, activeforeground=activeforeground,
                                         command=self.minimize)
        self.minimize_button.pack(side=tk.RIGHT, ipady=2, ipadx=12, fill=tk.Y)

    def add_icon(self, icon=Icon_TkinterDev, background="#ffffff", ):
        self.icon = tk.Label(self, image=tk.PhotoImage(icon), background=background)
        self.icon.pack(fill=tk.Y, side=tk.LEFT, padx=10)

    def add_title(self, text="", font=("微软雅黑", 9),
                  background="#ffffff", foreground="#000000"):
        """
        为标题栏添加最小化按钮，

        :param text: 为标题的文本
        :param font: 为标题的字体
        :param background: 为标题的背景颜色
        :param foreground: 为标题的前景颜色
        """
        self.title = tk.Label(self, text=text, font=font,
                              background=background, foreground=foreground)
        self.master.title(text)
        self.title.pack(fill=tk.Y, side=tk.LEFT, padx=10)

    def maximize_event(self):
        """
        内置函数，使窗口最大化
        """
        if self.ismaximize:
            self.master.state("normal")
            self.maxmize_button.configure(text="🗖")
            self.ismaximize = False
        elif not self.ismaximize:
            self.master.state("zoomed")
            self.maxmize_button.configure(text="🗗")
            self.ismaximize = True

    def minimize(self):
        """
        内置函数，使窗口最小化
        """
        self.master.state('icon')

    def maximize(self):
        """
        内置函数，使窗口最大化
        """
        if self.ismaximize:
            self.master.state("normal")
            self.ismaximize = False
        elif not self.ismaximize:
            self.master.state("zoomed")
            self.ismaximize = True


class DevImage(tk.Label):
    def __init__(self, master: tk.Widget, image: tk.PhotoImage = None, ):
        super(DevImage, self).__init__(master=master, image=image)


class DevNotifyIcon(object):
    def __init__(self, master: tk.Tk, tip: str = "托盘图标", icon=Icon_Folder):
        """
        正在开发，请不要使用
        """
        import os.path
        self._hWnd = GetParent(master.winfo_id())
        self._icon = icon
        self._icon_flags = LR_LOADFROMFILE | LR_DEFAULTSIZE
        self._hinst = GetModuleHandle(None)
        if os.path.isfile(self._icon):
            self._hicon = LoadImage(self._hinst,
                                    self._icon,
                                    IMAGE_ICON,
                                    0,
                                    0,
                                    self._icon_flags
                                    )
        else:
            Error("我们没有找到图标文件，将使用默认的图标")
            self._hicon = LoadIcon(0, IDI_APPLICATION)
        self._notify_id = (self.hWnd,
                           0,
                           NIF_ICON | NIF_MESSAGE | NIF_TIP,
                           WM_USER + 20,
                           self._hicon,
                           tip)

    @property
    def notify_id(self):
        return self.notify_id

    @notify_id.setter
    def notify_id(self, nid):
        self._notify_id = nid

    @property
    def hWnd(self):
        return self._hWnd

    @hWnd.setter
    def hWnd(self, hWnd):
        self._hWnd = hWnd

    def add(self):
        Shell_NotifyIcon(NIM_ADD, self._notify_id)

    def delete(self):
        Shell_NotifyIcon(NIM_DELETE, self._notify_id)

    def modify(self):
        Shell_NotifyIcon(NIM_MODIFY, self._notify_id)


class DevMenu(tk.Menubutton):
    def __init__(self, master=None, menu: tk.Menu = None, text: str = "", bg="#fafafa", fg="#000000",
                 active_bg="#3c7bfc", active_fg="#ffffff"):
        super(DevMenu, self).__init__(master=master, menu=menu, text=text, relief=tk.FLAT, background=bg, foreground=fg,
                                      activebackground=active_bg, activeforeground=active_fg)


class DevMenuBar(tk.Frame):
    def __init__(self, master: tk.Widget, bg="#fafafa"):
        super(DevMenuBar, self).__init__(master=master, background=bg)

    def add_menu(self, menu: DevMenu, side=tk.LEFT):
        menu.pack(side=side)

    def show(self):
        self.pack(fill=tk.X, side=tk.TOP)


class DevMessageBox(object):
    def __init__(self, master: tk.Tk):
        super(DevMessageBox, self).__init__()
        self._master = GetParent(master.winfo_id())

    def show(self):
        MessageBox(
            self._master,
        )


class DevObject(object):
    def __init__(self):
        """
        可以用于存储组件
        """
        self.obj = {}

    def add_widget(self, widget: tk.Widget, id: str):
        """
        添加组件

        :param widget: 为被存储的组件
        :param id: 为存储组件的ID
        """
        self.obj[id] = widget

    def set_widget(self, id: str, widget: tk.Widget):
        """
        设置组件

        :param widget: 为被存储的组件
        :param id: 为存储组件的ID
        """
        self.obj[id] = widget

    def get_widget(self, id: str) -> tk.Widget:
        """
        获取组件

        :param id: 为存储组件的ID
        """
        return self.obj[id]


class DevBorder(object):
    def __init__(self, widget: tk.Widget = None, iswindow: bool = True, border_color="#e1e1e1"):
        self.widget = widget
        self.iswindow = iswindow
        self.top = tk.Frame(widget, height=0, cursor="sb_v_double_arrow", background=border_color)
        self.top.pack(side=tk.TOP, ipady=1, fill=tk.X)
        self.bottom = tk.Frame(widget, height=0, cursor="sb_v_double_arrow", background=border_color)
        self.bottom.pack(side=tk.BOTTOM, ipady=1, fill=tk.X)
        self.left = tk.Frame(widget, height=0, cursor="sb_h_double_arrow", background=border_color)
        self.left.pack(side=tk.LEFT, ipadx=1, fill=tk.Y)
        self.right = tk.Frame(widget, height=0, cursor="sb_h_double_arrow", background=border_color)
        self.right.pack(side=tk.RIGHT, ipadx=1, fill=tk.Y)

    def top_click(self, evt=None):
        self._topx = self.top.winfo_x()
        self._topy = self.top.winfo_y()
        self._widgetx = self.widget.winfo_x()
        self._widgety = self.widget.winfo_y()
        self._widgetrootx = self.widget.winfo_rootx()
        self._widgetrooty = self.widget.winfo_rooty()

    def top_move(self, evt=None):
        widgetx = 0
        if self.iswindow:
            self.widget.geometry(f"")

    def bottom_move(self, evt=None):
        if self.iswindow:
            self.widget.geometry(f"{self.widget.winfo_width()}x{self.bottom.winfo_y()}")


class DevStack(tk.Frame):
    def __init__(self):
        """
        用于切换不同的界面
        """
        super(DevStack, self).__init__()
        self._pages = {}

    def add_page(self, page: tk.Widget, id: int = 0):
        """
        添加页面

        :param page: 页面组件
        :param id: 组件ID
        """
        self._pages[id] = page

    def show_page(self, id: int):
        """
        显示页面，会将其他页面隐藏

        :param id: 被显示的页面ID
        """
        self._pages[id].pack(fill=tk.BOTH, expand=tk.YES)
        for item in self._pages.keys():
            if not item == id:
                self.hide_page(item)

    def hide_page(self, id: int):
        """
        内置函数，最好不要使用，因为几乎没有什么用
        """
        self._pages[id].pack_forget()

    def get_page(self, id: int):
        """
        获取页面

        :param id: 所要获取的页面ID
        """
        return self._pages[id]

    def get_pages(self):
        """
        获取所有页面
        """
        return self._pages


class DevSideBar(tk.Frame):
    def __init__(self, master: tk.Widget, background="#ffffff", ):
        super(DevSideBar, self).__init__(master=master, background=background)

    def add_action(self, text: str = "", icon: str = None, commnad=None,
                   default_bg: str = "#ffffff", default_fg: str = "#000000",
                   font=("等线 Light", 10, "bold"), side=tk.TOP,
                   active_bg: str = "#177aff", active_fg: str = "#d6eaff",
                   click_bg: str = "#175bff", click_fg: str = "#d6deff"):
        if icon is None:
            button_icon = None
        else:
            button_icon = tk.PhotoImage(file=icon)
        return DevButton(self, text=text, image=button_icon, command=commnad,
                         default_bg=default_bg, default_fg=default_fg, font=font,
                         active_bg=active_bg, active_fg=active_fg,
                         click_bg=click_bg, click_fg=click_fg).pack(side=side)

    def show(self, side: str = tk.LEFT):
        self.pack(side=side, fill=tk.Y)


class DevStatusBar(tk.Frame):
    def __init__(self, master: tk.Widget = None, default_text: str = "", sizegrip: bool = True, background="#fcfcfc",
                 foreground="#000000"):
        """
        简单的状态栏，使用show可以将它显示出来，使用add_status在鼠标指针移动到组件上时，状态栏会显示状态文本。

        :param master: 父组件
        :param default_text: 默认文字
        :param background: 背景颜色
        """
        super(DevStatusBar, self).__init__(master=master, background=background, )
        self.widgetlist = []
        self.master = master
        self.default_text = default_text
        self.style = ttk.Style()
        self.style.configure("Dev.TSizegrip", background=background, foreground=foreground)
        self.status = tk.Label(self, text=default_text, background=background, foreground=foreground)
        self.status.pack(side=tk.LEFT, expand=tk.NO)
        self.sizegrip = ttk.Sizegrip(self, style="Dev.TSizegrip")
        if sizegrip:
            self.sizegrip.pack(side=tk.RIGHT, anchor=tk.SE, expand=tk.NO)

    def add_status(self, widget: tk.Widget, status: str = ""):
        self.widgetlist.append(widget)
        widget.bind("<Enter>", lambda event: self.status.configure(text=status))
        widget.bind("<Leave>", lambda event: self.status.configure(text=self.default_text))

    def set_sizegrip(self, sizegrip: ttk.Sizegrip):
        self.sizegrip = sizegrip

    def show(self):
        self.pack(fill=tk.X, side=tk.BOTTOM)


class DevToolbox(tk.Toplevel):
    def __init__(self, master: tk.Tk, title: str = "ToolBox"):
        """
        在测试窗口时可以使用工具箱来调整窗口。

        :param master: 组件的父组件
        :param title: 工具箱的标题
        """
        super(DevToolbox, self).__init__(master=master)
        from tkdev import window_move, window_border
        from tkinter import ttk
        self.configure(background="#fcfcfc")
        self.geometry("355x450")
        self.title = Label(self, text=title, background="#fcfcfc")
        self.title.pack(fill=X, side=TOP)

        window_move(self.title, self)
        window_border(self)
        self.Title_Button = ttk.Button(self, text="修改标题", command=self.set_title)
        self.Title_Button.pack(fill=X, side=TOP, padx=5, pady=5, ipady=5)
        self.Topmost_Button = ttk.Button(self, text="置顶", command=self.set_topmost)
        self.Topmost_Button.pack(fill=X, side=TOP, padx=5, pady=5, ipady=5)
        self.No_Topmost_Button = ttk.Button(self, text="取消置顶", command=self.set_no_topmost)
        self.No_Topmost_Button.pack(fill=X, side=TOP, padx=5, pady=5, ipady=5)
        self.Mica_Light_Button = ttk.Button(self, text="云母特效-浅色", command=self.mica_light)
        self.Mica_Light_Button.pack(fill=X, side=TOP, padx=5, pady=5, ipady=5)
        self.Mica_Dark_Button = ttk.Button(self, text="云母特效-深色", command=self.mica_dark)
        self.Mica_Dark_Button.pack(fill=X, side=TOP, padx=5, pady=5, ipady=5)
        self.Acrylic_Light_Button = ttk.Button(self, text="亚克力特效-浅色", command=self.acrylic_light)
        self.Acrylic_Light_Button.pack(fill=X, side=TOP, padx=5, pady=5, ipady=5)
        self.Acrylic_Dark_Button = ttk.Button(self, text="亚克力特效-深色", command=self.acrylic_dark)
        self.Acrylic_Dark_Button.pack(fill=X, side=TOP, padx=5, pady=5, ipady=5)
        self.Close_Me_Button = ttk.Button(self, text="关闭工具箱", command=self.destroy)
        self.Close_Me_Button.pack(fill=X, side=TOP, padx=5, pady=5, ipady=5)
        self.Close_Button = ttk.Button(self, text="关闭窗口", command=self.master.destroy)
        self.Close_Button.pack(fill=X, side=TOP, padx=5, pady=5, ipady=5)
        self.master = master

    def set_title(self):
        """
        内置函数，用于设置窗口标题
        """
        from tkinter import simpledialog
        title = simpledialog.askstring("输入标题", "请设置窗口的标题")
        self.master.title(title)

    def set_topmost(self):
        """
        内置函数，用于置顶窗口
        """
        self.master.attributes("-topmost", True)

    def set_no_topmost(self):
        """
        内置函数，用于取消窗口置顶
        """
        self.master.attributes("-topmost", False)

    def mica_light(self):
        """
        内置函数，用于设置云母特效明亮主题
        """
        DevManage(self.master).use_mica_mode_light()
        self.master.configure(background="#ffffff")

    def mica_dark(self):
        """
        内置函数，用于设置云母特效暗黑主题
        """
        DevManage(self.master).use_mica_mode_dark()
        self.master.configure(background="#000000")

    def acrylic_light(self):
        DevManage(self.master).use_acrylic_mode_light()
        self.master.configure(background="#ffffff")

    def acrylic_dark(self):
        DevManage(self.master).use_acrylic_mode_dark()
        self.master.configure(background="#000000")

    def show(self):
        """
        内置函数，用于显示窗口。
        """
        self.mainloop()


class DevTabbar(tk.Frame):
    def __init__(self, master: tk.Widget):
        """
        工具栏

        :param master: 父组件
        """
        super(DevTabbar, self).__init__(master=master)
        self.actions = {}
        self.actions_button = {}

    def add_action(self, name: str, action: DevAction, use_ttk: bool = False) -> tk.Widget:
        """
        添加DevAction组件
        """
        self.actions[name] = action
        if use_ttk:
            self.actions_button[name] = ttk.Button(self, text=action.text, image=action.icon, command=action.command)
        else:
            self.actions_button[name] = tk.Button(self, text=action.text, image=action.icon,
                                                  background=action.background, foreground=action.foreground,
                                                  activebackground=action.active_background,
                                                  activeforeground=action.active_foreground,
                                                  command=action.command)
        return self.actions_button[name]

    def show(self):
        """
        快速显示窗口
        """
        self.pack(fill=tk.X, side=tk.BOTTOM)

    def remove_action(self, name: str):
        """
        移除action

        :param name: 移除action的名称
        """
        self.actions_button[name].forget()

    def get_action(self, name: str):
        """
        获取action

        :param name: 获取action的名称
        """
        return self.actions[name]

    def get_action_button(self, name: str):
        """
        获取action生成的按钮

        :param name: 获取action的名称
        """
        return self.actions_button[name]


class DevWindow(tk.Tk):
    def __init__(self, title: str = "", size=(630, 300), icon=Icon_Empty):
        """
        快捷使用窗口，内置多种功能，快速使用
        """
        super(DevWindow, self).__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.iconbitmap(icon)
        self.configure(background="#ffffff")

    def wm_remove_titlebar(self):
        """
        移除标题栏与边框，保留着任务栏
        """
        self.after(0, lambda: window_custom_border_taskbar(self))

    remove_titlebar = wm_remove_titlebar

    def wm_remove_titlebar_none_border(self):
        """
        移除标题栏，无边框
        """
        window_custom_taskbar(self)

    remove_titlebar_none_border = wm_remove_titlebar_none_border

    def wm_statusbar(self, statusBar: tk.Widget = None):
        """
        设置状态栏，

        :param statusBar: 为被设置的状态栏
        """
        self._statusBar = statusBar
        self._statusBar.pack(fill=tk.X, side=tk.BOTTOM)
        return self._statusBar

    statusbar = wm_statusbar

    def wm_titlebar(self, titleBar: DevHeaderBar = None):
        """
        设置标题栏，

        :param titleBar: 为被设置的标题栏
        """
        self.minsize(100, 30)
        self._titlebar = titleBar
        self._titlebar.pack(fill=tk.X, side=tk.TOP)
        return self._titlebar

    titlebar = wm_titlebar

    def wm_menubar(self, menubar: DevMenuBar = None):
        menubar.show()

    menubar = wm_menubar

    def wm_centre(self):
        """
        居中窗口
        """
        DevManage(self).set_window_pos_center()

    centre = wm_centre

    def min_window(self):
        """
        最小化窗口
        """
        self.state("iconic")

    def create_tray(self, tooltip: str = "", install_winico: bool = True):
        """
        快速创建系统托盘图标，返回托盘组件

        :param tooltip: 设置托盘图标的提示文本
        :param install_winico: 如果未检测到winico安装，将会自动进行安装
        """
        return DevTray(self, text=tooltip, icon=ICON_APPLICATION, icon_mode=ICON_MODE_LOAD, auto_install=install_winico)

    def create_tray_with_show(self, tooltip: str = "", install_winico: bool = True):
        """
        快速创建系统托盘图标，并显示，返回托盘组件和托盘ID

        :param tooltip: 设置托盘图标的提示文本
        :param install_winico: 如果未检测到winico安装，将会自动进行安装
        """
        tray = self.create_tray(tooltip=tooltip, install_winico=install_winico)
        return tray, tray.show()

    def create_titlebar(self, title: str = "", border: bool = True, double_max: bool = True):
        """
        快速创建标题，返回标题栏组件

        :param title: 设置标题栏标题。
        :param border: 自定义窗口是否又边框。
        :param double_max: 设置是否可以通过双击放大窗口。
        """
        titlebar = DevHeaderBar(self, border=border, double_max=double_max)
        titlebar.add_title(title)
        titlebar.add_close_button()
        titlebar.add_maximize_button()
        titlebar.add_minimize_button()
        return titlebar

    def create_titlebar_with_show(self, title: str = "", border: bool = True, double_max: bool = True):
        """
        快速创建标题，并使用，返回标题栏组件

        :param title: 设置标题栏标题。
        :param border: 自定义窗口是否又边框。
        :param double_max: 设置是否可以通过双击放大窗口。
        """
        titlebar = self.create_titlebar(title=title, border=border, double_max=double_max)
        self.titlebar(titlebar)
        return titlebar

    def dpi(self):
        """
        设置dpi高清晰度
        """
        self.tk.call('tk', 'scaling', ScaleFactor / 75)

    def can_darg_file(self, func=Empty_Func):
        from windnd import hook_dropfiles
        hook_dropfiles(self, func=func)


class DevToplevel(tk.Toplevel, DevWindow):
    def __init__(self, master: tk.Tk, title: str = "", size=(630, 300), icon=Icon_Empty):
        super(DevToplevel, self).__init__(master=master)
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.iconbitmap(icon)


class DevPopup(DevToplevel):
    def __init__(self, master=None, border: bool = True):
        super(DevPopup, self).__init__(master=master)
        self.withdraw()
        if border:
            window_border(self)
        if not border:
            self.overrideredirect(True)

    def popup(self, x, y):
        self.deiconify()
        self.geometry(f"+{x}+{y}")
        self.bind("<FocusOut>", self.withdraw)


class DevTooltip(DevToplevel):
    def __init__(self, widget: tk.Widget, window: tk.Tk, message: str = "", after: int = 1000, border: bool = True,
                 padding: int = 3, side=tk.CENTER, height: int = 40, cursor: bool = False, width=None,
                 background="#ffffff", foreground="#000000"):

        """
        用于给组件设定工具提示

        :param widget: 表示设置工具提示的组件
        :param window: 表示设置组件的窗口
        :param message: 表示工具提示的文本
        :param after: 表示几秒之后显示
        :param border: 是否设定为窗口的边框
        """
        super(DevTooltip, self).__init__()
        self.configure(background=background, relief=tk.RAISED, border=1)
        from tkdev import window_border
        self._message = ttk.Label(self, background=background, foreground=foreground, text=message, anchor=tk.CENTER)
        self._message.pack(padx=padding, pady=padding, ipadx=padding, ipady=padding, fill=tk.BOTH, expand=tk.YES)
        if border:
            window_border(self)
        if not border:
            self.overrideredirect(True)
        self.withdraw()

        self.widget = widget
        self.window = window
        self._width = width
        self._height = height
        self._afterms = after
        self.side = side
        self.padding = padding
        self._curser = cursor

        self.ison = False
        self.border = border

        self.widget.bind("<Enter>", lambda evt: self.show(evt))
        self.widget.bind("<Leave>", lambda evt: self.hide(evt))

        self.geometry(f"{self.widget.winfo_width()}x{self._height}")

    @property
    def after_ms(self):
        """
        等待的毫秒
        """
        return self._afterms

    @after_ms.setter
    def after_ms(self, ms: int = 1000):
        self._afterms = ms

    @property
    def message(self):
        """
        工具提示的消息
        """
        return self.message

    @message.setter
    def message(self, text: str):
        self._message.configure(text=text)

    def hide(self, evt=None):
        """
        内置函数，用于隐藏窗口
        """
        self.ison = False
        self.window.deiconify()
        self.withdraw()

    def show(self, evt=None):
        """
        内置函数，用于显示窗口
        """
        self.ison = True

        def on():
            if self._width is None:
                self.geometry(f"{self.widget.winfo_width()}x{self._height}")
            elif self._width:
                self.geometry(f"{self._width}x{self._height}")
            if self.ison:
                if self._curser:
                    self.geometry(
                        f"+{round(evt.x) - round(self.winfo_width() / 2)}+{self.widget.winfo_rooty() + self.widget.winfo_height() + 5}")
                else:
                    if self.border:
                        self.geometry(
                            f"+{self.widget.winfo_rootx() - 7}+{self.widget.winfo_rooty() + self.widget.winfo_height() + 5}")
                    else:
                        self.geometry(
                            f"+{self.widget.winfo_rootx()}+{self.widget.winfo_rooty() + self.widget.winfo_height() + 5}")
                self.deiconify()

        self.after(self._afterms, on)


if __name__ == '__main__':
    Window = DevWindow()
    Manage = DevManage(Window)
    Manage.dwm_set_window_attribute_use_dark_mode()
    Window.after(100, lambda: print(Manage.dwm_get_window_attribute_use_dark_mode()))
    Window.mainloop()
