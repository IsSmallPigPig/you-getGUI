## you-get Download Tools

------

## 1 项目简介

此项目基于 you-get 开发，调用终端向 you-get 发送命令以达到下载的效果。是为了帮助不使用 python 工具的人更方便的使用 you-get 这一下载神器
如果对项目有任何疑问或者建议，欢迎加入QQ群：473542615

![image-20230114132520545](README.assets/you-get-tools群二维码.png)



## 2 项目界面

![image-20230114132520545](README.assets/image-20230114132520545.png)



## 3 项目使用方法

#### 3.1 基础设置

------

##### 1.1 视频下载链接

视频下载链接为必填项，如果不填写该项则在确认信息时拦截

##### 1.2 输出文件名称

此项为非必填项目，若不填此项则默认为视频标题

##### 1.3 文件保存路径

此项为非必填项目，若不填此项则默认为用户主目录

##### 1.4 cookies 路径

此项为非必填项目，若不填此项则无法下载高清视频及会员视频

**提交其他 cookies：**指在非火狐浏览器保存 cookies 的位置提交 cookies，比如你的 cookies 是从网上获取的，则可以使用此项

**自动获得火狐 cookies：**此项将为安装了火狐浏览器的用户自动获得 cookies。使用时只要点一下则自动获得 cookies 存储路径



#### 3.2 确认信息

------

如果您确认您填写的信息已经填写完毕，则可以点击此按钮。程序将会对您提供的信息转换为指令并指出您填写信息的问题



#### 3.3 下载属性

------

##### 3.1 清晰度下拉框

此项暂时未完成，完成时将可以自行选择下载清晰度

##### 3.2 生成指令

此项会将生成出来的命令在这里显示

##### 3.3 开始下载

若查看生成指令后没有疑问，点击此项就会开始下载



#### 3.4 终端

------

终端是为了那些需要查看下载信息的用户提供的，在这里你可以看到操作完成后的输出（暂时未实现实时更新）



> **注意：**高级设置和其他设置不做说明，自行查阅 you-get 作者的说明



## 4 项目结构

------

![image-20230114133902501](README.assets/image-20230114133902501.png)

正如您所见，项目总体分为5个部分，分别为：

- Core
- Date
- Download
- Tool
- 运行区（main.py)

我将会向您介绍各个分区的用处



### 4.1 Core

------

Core 是我为 you-get 写的 API，该文件夹可以复制出来单独使用

Core 文件夹涵盖了 you-get 大部分的指令，每一个指令都写了详尽的注释以便开发者使用



### 4.2 Date

------

Date 是用于存储必要的运行信息的（例如后续开发要解析的 json 文件就会暂存于该目录）



### 4.3 Download

------

Download 是为电脑小白准备的一键安装 you-get 库。



### 4.5 Tool

------

Tool 是本项目的主体

- menu.py：GUI实现文件
- tools.py ：执行函数
- constants.py：执行函数



### 4.6 运行目录

------

运行目录中有环境配置文件以及 main.py 启动文件



## 5 一些问题

------

- 本项目目前并不支持 linux 

- 本项目不支持多语言
- 本项目未解决实时显示终端信息
- 半成品状态



## 6 基于项目

------

**ttk 渲染引擎：**[rdbende/Sun-Valley-ttk-theme: A gorgeous theme for ttk, based on Microsoft's Sun Valley visual styles ✨ (github.com)](https://github.com/rdbende/Sun-Valley-ttk-theme)

**you-get：**[soimort/you-get: Dumb downloader that scrapes the web (github.com)](https://github.com/soimort/you-get)

**一键部署 you-get 支持：**[twlz0ne/you-get_install: 一键安装 you-get 到 windows (github.com)](https://github.com/twlz0ne/you-get_install)

由衷的感谢以上作者



## 7 开源许可证

------

此项目基于 MIT license 开源，我十分希望有优秀的作者能帮助我完成这个作品，此项目永不收费且永久开源
