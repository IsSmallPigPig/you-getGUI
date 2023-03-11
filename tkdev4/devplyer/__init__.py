auto_install_plyer = True


def set_auto_install_plyer(auto: bool):
    global auto_install_plyer
    auto_install_plyer = auto


def install_plyer():
    if auto_install_plyer:
        try:
            import plyer
        except ImportError:
            import os
            import sys
            os.system(f"{sys.executable} -m pip install plyer -i https://pypi.tuna.tsinghua.edu.cn/simple/")


class DevEmail(object):
    def __init__(self):
        install_plyer()

    def send(self, recipient=None, subject=None, text=None):
        from plyer.utils import platform
        from plyer import email

        email.send(recipient=recipient, subject=subject, text=text)


class DevNotification(object):
    def __init__(self, title: str = "Title", message: str = "Message", app_name: str = "Python", app_icon="",
                 timeout: int = 0):
        """
        用于发送消息通知，但是需要安装plyer库。

        :param title: 设置通知的标题。
        :param message: 设置通知的消息。
        :param app_name: 设置通知的应用名称。
        :param app_icon: 设置通知的标题。
        :param timeout: 显示通知的时间。
        """
        install_plyer()
        self._title = title
        self._message = message
        self._app_name = app_name
        self._app_icon = app_icon
        self._timeout = timeout

    def show(self):
        """
        显示消息
        """
        from plyer.utils import platform
        from plyer import notification

        notification.notify(
            title=self._title,
            message=self._message,
            app_name=self._app_name,
            app_icon=self._app_icon,
            timeout=self._timeout,
        )


if __name__ == '__main__':
    DevNotification().show()