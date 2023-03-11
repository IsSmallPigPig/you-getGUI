from tkdev4 import DevStack, DevWindow, DevManage, Icon_Folder
from darkdetect import isDark, isLight
from tkinter import *
from tkinter import ttk
from sv_ttk import use_light_theme, use_dark_theme


Window = DevWindow()
Window.iconbitmap(Icon_Folder)
Window.title("MainWindow")
Manage = DevManage(Window)
Manage.dwm_set_window_attribute_systembackdrop_type_mainwindow()


def auto():
    if isLight():
        Manage.dwm_set_window_attribute_use_light_mode()
        use_light_theme()
    elif isDark():
        Manage.dwm_set_window_attribute_use_dark_mode()
        use_dark_theme()


def light():
    Manage.dwm_set_window_attribute_use_light_mode()
    use_light_theme()


def dark():
    Manage.dwm_set_window_attribute_use_dark_mode()
    use_dark_theme()


def round():
    Manage.dwm_set_window_round_round()


def round_small():
    Manage.dwm_set_window_round_round_small()


def round_donot():
    Manage.dwm_set_window_round_donot_round()


def basic_false():
    Manage.dwm_set_window_attribute_ncrendering_policy(0)


def basic_true():
    Manage.dwm_set_window_attribute_ncrendering_policy(1)


def settings():
    Stack.show_page(2)


def back():
    Stack.show_page(1)


auto()
Stack = DevStack()

StartPage = ttk.Frame(Stack)
StartLogo = ttk.Label(StartPage, text="MainWindow Demo", font=("微软雅黑", 14), anchor="center")
StartLogo.pack(fill="both", expand="yes")
Stack.after(2000, lambda: Stack.show_page(1))

MainPage = ttk.Frame(Stack)
MainPage_Label = ttk.Label(MainPage, text="主页面", font=("微软雅黑", 10), anchor="center")
MainPage_Label.pack(fill="both", expand="yes")
Setting = ttk.Button(MainPage, text="设置", command=settings)
Setting.pack(fill="x", expand="yes", side="left")
Quit = ttk.Button(MainPage, text="退出", command=Window.quit)
Quit.pack(fill="x", expand="yes", side="left")

SettingPage = ttk.Frame(Stack)

SettingTheme = ttk.Labelframe(SettingPage, text="主题")
ThemeVar = StringVar()
ThemeVar.set("Auto")
AutoTheme = ttk.Radiobutton(SettingTheme, text="自动", variable=ThemeVar, value="Auto", command=auto)
AutoTheme.pack(side="left", padx=10, pady=10)
LightTheme = ttk.Radiobutton(SettingTheme, text="明亮", variable=ThemeVar, value="Light", command=light)
LightTheme.pack(side="left", padx=10, pady=10)
DarkTheme = ttk.Radiobutton(SettingTheme, text="黑暗", variable=ThemeVar, value="Dark", command=dark)
DarkTheme.pack(side="left", padx=10, pady=10)
BackButton = ttk.Button(SettingTheme, text="返回", command=back)
BackButton.pack(side="right", anchor="e", padx=10, pady=10, ipadx=10)
SettingTheme.pack(fill="x", side="top", padx=10, pady=10)

SettingRound = ttk.Labelframe(SettingPage, text="圆角")
RoundVar = StringVar()
RoundVar.set("Round")
Round = ttk.Radiobutton(SettingRound, text="圆角", variable=RoundVar, value="Round", command=round)
Round.pack(side="left", padx=10, pady=10)
RoundSmall = ttk.Radiobutton(SettingRound, text="小圆角", variable=RoundVar, value="Round Small", command=round_small)
RoundSmall.pack(side="left", padx=10, pady=10)
DonotRound = ttk.Radiobutton(SettingRound, text="不要圆角", variable=RoundVar, value="Donot Round", command=round_donot)
DonotRound.pack(side="left", padx=10, pady=10)
BackButton2 = ttk.Button(SettingRound, text="返回", command=back)
BackButton2.pack(side="right", anchor="e", padx=10, pady=10, ipadx=10)
SettingRound.pack(fill="x", side="top", padx=10, pady=10)

SettingBasic = ttk.Labelframe(SettingPage, text="Basic")
BasicVar = StringVar()
BasicVar.set("False")
BasicFalse = ttk.Radiobutton(SettingBasic, text="否", variable=BasicVar, value="False", command=basic_false)
BasicFalse.pack(side="left", padx=10, pady=10)
BasicTrue = ttk.Radiobutton(SettingBasic, text="是", variable=BasicVar, value="True", command=basic_true)
BasicTrue.pack(side="left", padx=10, pady=10)

BackButton3 = ttk.Button(SettingBasic, text="返回", command=back)
BackButton3.pack(side="right", anchor="e", padx=10, pady=10, ipadx=10)

SettingBasic.pack(fill="x", side="top", padx=10, pady=10)


Stack.add_page(StartPage, 0)
Stack.add_page(MainPage, 1)
Stack.add_page(SettingPage, 2)
Stack.show_page(0)
Stack.pack(fill="both", expand="yes")
Window.mainloop()