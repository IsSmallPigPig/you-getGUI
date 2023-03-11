from tkinter import *


def Empty():
    pass


class DrawButton(Canvas):
    def __init__(self, master: Widget = None, round: bool = True,
                 background="#ffffff", activebackground="#fafafa",
                 foreground="#131313", activeforeground="#fafafa",
                 border_color="#005fb8", active_border_color="#005fb8",
                 borderradius: int = 20, command=Empty, font=("微软雅黑", 11),
                 text: str = ""):
        super(DrawButton, self).__init__(master=master, background=master.cget("background"))
        self.pack()
        self.radius = borderradius
        self.background = background
        self.activebackground = activebackground
        self.foreground = foreground
        self.activeforeground = activeforeground
        self.border_color = border_color
        self.active_border_color = active_border_color
        self.text = text
        self.command = command
        self.font = font
        self.round = round
        self.bind("<Configure>", lambda evt: self.upload())
        self.bind("<Enter>", self.enter)
        self.bind("<Leave>", self.leave)
        self.bind("<ButtonRelease-1>", self.ifcommand)

    def enter(self, evt):
        self.In = True

    def leave(self, evt):
        self.In = False

    def ifcommand(self, evt):
        if self.In:
            self.command()

    def set_background(self, background):
        self.background = background
        self.upload()

    def upload(self, ):
        self.delete(ALL)

        def round_button(x1, y1, x2, y2, radius=25, **kwargs):
            points = [x1 + radius, y1,
                      x1 + radius, y1,
                      x2 - radius, y1,
                      x2 - radius, y1,
                      x2, y1,
                      x2, y1 + radius,
                      x2, y1 + radius,
                      x2, y2 - radius,
                      x2, y2 - radius,
                      x2, y2,
                      x2 - radius, y2,
                      x2 - radius, y2,
                      x1 + radius, y2,
                      x1 + radius, y2,
                      x1, y2,
                      x1, y2 - radius,
                      x1, y2 - radius,
                      x1, y1 + radius,
                      x1, y1 + radius,
                      x1, y1]

            return self.create_polygon(points, **kwargs, activefill=self.activebackground, smooth=self.round,
                                       activeoutline=self.active_border_color, outline=self.border_color)

        button = round_button(self.winfo_x(), self.winfo_y(), self.winfo_width(), self.winfo_height(),
                              radius=self.radius, fill=self.background)

        def text(x1, y1, text: str, foreground, font):
            return self.create_text(x1, y1, text=text, fill=foreground, font=font)

        button_text = text(self.winfo_width() / 2, self.winfo_height() / 2, self.text, foreground=self.foreground, font=self.font)

        return button, button_text


if __name__ == '__main__':
    Root = Tk()
    Button = DrawButton(Root, borderradius=25, text="Hello", round=True,
                        background="#186ebf", activebackground="#307dc5", foreground="#e5e9eb",
                        command=lambda: print("SN"))
    Button.pack(fill=BOTH, expand=YES, padx=10, pady=10)
    Root.mainloop()
