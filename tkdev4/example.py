from src.tkdev4.devpre import *
from sv_ttk import *
from random import choice, randint

Word = ("厕所🚾", "老八👴", "冰块🧊", "岩浆🔥",
        "雷霆🌩", "可乐🍹", "雪碧🍸", "作业📗",
        "大树🌳", "大叔👴", "老鼠🐀", "猫咪🐱",
        "飞机✈", "火车🚆", "蜜汁🍷", "汉堡🍔",
        "大便超人", "枕头🪅", "床🛏", "垃圾",
        "麦克风🎤", "班主任👩", "手机📱", "智障👨‍🦯",
        "剑🗡", "箭🏹", "弓箭🏹", "孔雀🦚",
        "鸟🐦", "鸵鸟🦅", "鲨鱼🐟", "鲸鱼🐋",
        "小丑🤡", "恐龙🦖", "电脑💻", "水💧",
        "火🔥", "农药", "死亡💀", "游戏👾",
        "太阳☀", "月亮🌙", "狗🐕", "猴子🐒",
        "凹凸曼", "超人", "森林🌳", "老六")
List = []
ONE_VAR = ""
TWO_VAR = ""
THREE_VAR = ""
FOUR_VAR = ""


def Open_Toolbox():
    ToolBox = DevPreToolbox(Window)
    ToolBox.title.configure(background="#000000")
    ToolBox.mica(Dark)


def Open_View():
    View = DevToplevel()
    window_border(View)
    window_move(View, View)
    View.mica()
    Message_Text = ""
    for list in Word:
        Message_Text = Message_Text + str(list) + "                "
    Message = tk.Message(View, text=Message_Text, background="#000000")
    Message.pack(fill=tk.BOTH, expand=tk.YES)


def Choice_ONE():
    global ONE_VAR, List, HEAR
    YES = choice(Word)
    NO = "卧底😈"
    if NUMBER_VAR.get() == 3:
        List = [YES, YES]
        List.insert(randint(0, 2), NO)
    elif NUMBER_VAR.get() == 4:
        List = [YES, YES, YES]
        List.insert(randint(0, 3), NO)

    ONE_VAR = List[0]
    ONE.configure(state=tk.DISABLED)
    WORD.configure(text=f"你的单词是 {ONE_VAR} (此单词将在4秒内消失，请记好！)")
    HEAR = 2

    def AFTER():
        WORD.configure(text="请2号玩家抽取单词")
        TWO.configure(state=tk.NORMAL)

    WORD.after(4000, AFTER)


def Choice_TWO():
    global TWO_VAR, HEAR
    TWO_VAR = List[1]
    TWO.configure(state=tk.DISABLED)

    WORD.configure(text=f"你的单词是 {TWO_VAR} (此单词将在4秒内消失，请记好！)")
    HEAR = 3

    def AFTER():
        WORD.configure(text="请3号玩家抽取单词")
        THREE.configure(state=tk.NORMAL)

    WORD.after(4000, AFTER)


def Choice_THREE():
    global THREE_VAR, HEAR
    HOME = (ONE_VAR, TWO_VAR)
    THREE_VAR = List[2]
    THREE.configure(state=tk.DISABLED)

    WORD.configure(text=f"你的单词是 {THREE_VAR} (此单词将在4秒内消失，请记好！)")

    if NUMBER_VAR.get() == 3:
        HEAR = 1
    elif NUMBER_VAR.get() == 4:
        HEAR = 4

    def AFTER():
        if NUMBER_VAR.get() == 3:
            NUMBER_RESULT.configure(state=tk.NORMAL)
            WORD.configure(text="请开始游戏！如果你们已经结束游戏了，请点右上角查看结果按钮，看看所有人的真实身份吧！")
        else:
            FOUR.configure(state=tk.NORMAL)
            WORD.configure(text="请4号玩家抽取单词")

    WORD.after(4000, AFTER)


def Choice_FOUR():
    global FOUR_VAR, HEAR
    FOUR_VAR = List[3]
    FOUR.configure(state=tk.DISABLED)

    WORD.configure(text=f"你的单词是 {FOUR_VAR} (此单词将在4秒内消失，请记好！)")

    def AFTER():
        WORD.configure(text="请开始游戏！如果你们已经结束游戏了，请点右上角查看结果按钮，看看所有人的真实身份吧！")
        NUMBER_RESULT.configure(state=tk.NORMAL)

    WORD.after(4000, AFTER)


def TOGGLE_THREE():
    NUMBER_THREE.configure(style="Accent.TButton")
    NUMBER_FOUR.configure(style="TButton")


def TOGGLE_FOUR():
    NUMBER_FOUR.configure(style="Accent.TButton")
    NUMBER_THREE.configure(style="TButton")


Window = DevWindow()
Window.configure(background="#000000")
HEAR = 1
Window.geometry("830x440")


def Space():
    print(HEAR)
    WORD.configure(text="正在进行远程电脑操控，请稍等，3秒后显示抽取结果")
    if HEAR == 1:
        Window.after(3000, Choice_ONE)
    elif HEAR == 2:
        Window.after(3000, Choice_TWO)
    elif HEAR == 3:
        Window.after(3000, Choice_THREE)
    elif HEAR == 4:
        Window.after(3000, Choice_FOUR)


Window.bind("<Double-space>", lambda evt: Space())
Window.title("谁是卧底")
Window.iconbitmap(Icon_Folder)
use_dark_theme()
NUMBER = ttk.Frame(Window)
NUMBER_VAR = IntVar(value=3)
NUMBER_THREE = ttk.Radiobutton(NUMBER, text="三人", variable=NUMBER_VAR, value=3, style="Accent.TButton",
                               command=TOGGLE_THREE)
NUMBER_THREE.pack(fill=tk.X, side=tk.LEFT, ipady=5, pady=5, padx=5)
NUMBER_FOUR = ttk.Radiobutton(NUMBER, text="四人", variable=NUMBER_VAR, value=4, style="TButton", command=TOGGLE_FOUR)
NUMBER_FOUR.pack(fill=tk.X, side=tk.LEFT, ipady=5, pady=5, padx=5)


def RESULT():
    if NUMBER_VAR.get() == 3:
        WORD.configure(text=f"1 {ONE_VAR}  2 {TWO_VAR}  3 {THREE_VAR}")
    else:
        WORD.configure(text=f"1 {ONE_VAR}  2 {TWO_VAR}  3 {THREE_VAR}  4 {FOUR_VAR}")
    WORD.after(5000, lambda: WORD.configure(text="谁是卧底？找出其中隐藏在多数人之间不同单词的人"))
    ONE.configure(state=tk.NORMAL)
    NUMBER_RESULT.configure(state=tk.DISABLED)


NUMBER_RESULT = ttk.Button(NUMBER, text="游戏结束", style="Accent.TButton", command=RESULT, state=tk.DISABLED)
NUMBER_RESULT.pack(fill=tk.X, side=tk.RIGHT, ipady=5, pady=5, padx=5)
NUMBER_VIEW = ttk.Button(NUMBER, text="预览单词", style="TButton", command=Open_View)
NUMBER_VIEW.pack(fill=tk.X, side=tk.RIGHT, ipady=5, pady=5, padx=5)
NUMBER_TOOLBOX = ttk.Button(NUMBER, text="工具箱", style="TButton", command=Open_Toolbox)
NUMBER_TOOLBOX.pack(fill=tk.X, side=tk.RIGHT, ipady=5, pady=5, padx=5)
NUMBER.pack(fill=tk.X, side=tk.TOP, ipady=3, pady=5, padx=5)
ONE = ttk.Button(Window, text="1 请抽取你的单词", command=Choice_ONE, state=tk.NORMAL, style="Accent.TButton")
ONE.pack(fill=tk.X, side=tk.TOP, ipady=5, pady=5, padx=5)
TWO = ttk.Button(Window, text="2 请抽取你的单词", command=Choice_TWO, state=tk.DISABLED, style="Accent.TButton")
TWO.pack(fill=tk.X, side=tk.TOP, ipady=5, pady=5, padx=5)
THREE = ttk.Button(Window, text="3 请抽取你的单词", command=Choice_THREE, state=tk.DISABLED, style="Accent.TButton")
THREE.pack(fill=tk.X, side=tk.TOP, ipady=5, pady=5, padx=5)
FOUR = ttk.Button(Window, text="4 请抽取你的单词", command=Choice_FOUR, state=tk.DISABLED, style="Accent.TButton")
FOUR.pack(fill=tk.X, side=tk.TOP, ipady=5, pady=5, padx=5)
WORD = ttk.Label(Window, text="谁是卧底？找出其中隐藏在多数人之间不同单词的人", anchor=tk.CENTER, background="#000000", font=("微软雅黑", 15))
WORD.pack(fill=tk.BOTH, ipady=5, pady=5, padx=5, expand=tk.YES)
Manage = DevManage(Window)
Manage.use_mica_mode_auto()
Window.mainloop()
