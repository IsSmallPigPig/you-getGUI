from re import I
from tkdev4 import DevManage, DevWindow, DevTray, Icon_Folder
from tkinter import *
from tkfontawesome import icon_to_image
from platform import system
from sys import getwindowsversion
from sv_ttk import use_dark_theme, use_light_theme


class Window(DevWindow):
    def __init__(self, title: str = "熊出没", size=(380,600)):
        super().__init__(title=title, size=size)
        self.menubar = Menu(self, background="#000000")
        self.configure(menu=self.menubar)
        self.iconbitmap(default="C:\\tkinterDev\\src\\tkdev4\\logo.ico")
        self.manage = DevManage(self)
        self.manage.set_window_pos_bottom_right()
        self.manage.add_window_resize_border_frame()
        self.manage.add_window_maximizebox()
        self.manage.add_window_minimizebox()
        self.bind("<FocusOut>", lambda event: self.manage.close_window)
        self.set_systray()
        self.set_theme()

    def set_systray(self):

        def func():
            pass

        self.systray = DevTray(self, text="熊出没", icon="application", icon_mode="load", menu_func=func)
        self.systray.show()

    def set_theme(self, mode="auto"):
        if system() == "Windows":
            if getwindowsversion().build >= 22621:
                self.manage.dwm_set_window_attribute_systembackdrop_type_tabbed_window()
        if mode == "auto":
            if system() == "Windows":
                if getwindowsversion().build >= 22000:
                    from darkdetect import isDark
                    if isDark() == True:
                        self.configure(background="#000000")
                        self.manage.dwm_set_window_attribute_use_dark_mode()
                    else:
                        self.configure(background="#ffffff")
                        self.manage.dwm_set_window_attribute_use_light_mode()
    

if __name__ == "__main__":
    root = Window()
    root.mainloop()