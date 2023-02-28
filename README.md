# You Get GUI 使用文档

## 1 为什么开发

前段时间，我发现了一款优秀的命令行视频下载工具：**you-get**。这么好的工具，因为上手困难就被雪藏实在可惜

正巧，我有着多视频网站的下载需求。于是——我们一拍即合，做出了一款这样优秀的下载工具

## 2 界面演示

### 2.1 明 / 暗色演示截图

<img src="./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/%E6%98%8E%E6%9A%97%E8%89%B2.png" alt="明暗色" style="zoom: 33%;" />

### 2.2 主题设计

得益于 **sv-ttk** 的帮助，我做出来了一个 winUI3 式的界面，极度 win11 化，与 win11 相匹配

另外，我们使用了 winapi，可以自动识别系统当前主题模式，为您自动切换

同时得益于 winapi，我们得以更改窗口标题栏（win11 目前测试效果最好，win10 会出现要重新聚焦才会更改颜色的问题）的颜色，让整个窗口观感更好

我们的窗口多次改进，不断优化用户使用体验。提供更具有逻辑性，方便的页面设计



## 3 使用教程

### 3.1 下载选项区域

设置一些初始参数

<img src="./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/image-20230227215827320.png" alt="image-20230227215827320" style="zoom:150%;" />

- **Using m3u8 URL：**使用 m3u8 的下载方式。主要用于下载 m3u8 格式的网络视频

- **Auto Rename：**自动重命名，如果您下载了两个标题相同的文件，将会依照先后顺序，更改最后下载的标题，避免重复

- **Overwrite Files：**覆写文件。我为您开启了此选项（开启此选项将会覆盖自动重命名），我认为覆写是比重命名更好的选择。当然，您也可以自行关闭

- **Skip Check File Size：**跳过文件大小检查，默认关闭此项。因为部分网站的视频资源嗅探有问题，所以推荐关闭此选项，避免下载文件不全的问题

- **Download Captions：**下载字幕。部分视频网站将会提供字幕文件。我们的爬虫能嗅探到这一点，所以会自动下载它。当然，字幕文件也有可能是弹幕（比如 bilibili ）

- **Merge Video Parts：**自动合并视频。有些网站将会把视频和音频分开推流（不是一个完整的视频文件）。开启此选项后，如果识别到是音视频分开的将会自动合并成一个文件

  > 注意：如果您未下载 ffmpeg 软件并配置好环境，此选项无效果（详见 **程序配置-ffmpeg 依赖安装** ）

  

### 3.2 调试选项区域

给一些高级用户使用，请确保您知道您或得到的信息或者使用的选项是干什么的

<img src="./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/image-20230227221308532.png" alt="image-20230227221308532" style="zoom:150%;" />

- **Show Debug Info：**显示调试信息。开启该选项后，运行结束后软件虚拟的终端将会输出爬虫嗅探过程，方便您分析下载失败的原因
- **Ignore SSL Errors：**忽略 SSL 错误。您有可能使用了一些特殊的上网方式导致了 SSL 错误，最终导致软件无法继续下载。启用该选项可以让您正常下载
- **Show Download Link：**显示下载链接。爬虫将会向您返回它嗅探到的资源下载链接，您可以根据需求自行获取（需要填写视频链接）
- **Show Extracted Info：**显示下载信息。此选项将会告诉您所有的清晰度以及链接还有视频信息
- **Show Extracted Json：**返回解析出来的视频信息 Json。此选项将会返回爬虫解析出来的信息并以 Json 的方式存储。您可以选择保存它自行分析
- **Show Version：**显示版本。这将为您提供我们软件的内核版本



### 3.3 代理选项区域

这块区域主要是填写代理信息，您也可以禁用它们（默认不开启）

<img src="./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/image-20230227221831731.png" alt="image-20230227221831731" style="zoom:150%;" />

- **Disabled Proxy：**禁用代理。开启该选项则不会使用任何形式的代理下载视频和视屏信息

- **Only For Extracting：**仅将代理用于解析视频信息。此选项仅支持 HTTP 代理，不支持 SOCKS

- **Use HTTP Proxy：**使用 HTTP 代理

- **HTTP Proxy（HOST）：**填入 HTTP 代理的主机名（host）

- **HTTP Proxy（PORT）：**填入 HTTP 代理的端口（port）

- **Use SOCKS Proxy：**使用 SOCKS 代理

- **SOCKS Proxy（HOST）：**填入 SOCKS 代理的主机名（host）

- **SOCKS Proxy（PORT）：**填入 SOCKS 代理的端口（port）

- **SOCKS Proxy（USERNAME）：**填入 SOCKS 代理的用户名（username）

- **SOCKS Proxy（PASSWORD）：**填入 SOCKS 代理的密码（password）

  > **注意：**
  >
  > 1. 受限于中国国家法律法规，本文档不细讲代理。请依照您所在国家的法律法规使用
  > 2. 如果代理没有用户名密码，可以不填



### 3.4 保存选项区域

<img src="./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/image-20230228132558639.png" alt="image-20230228132558639" style="zoom:150%;" />

**Set Output Filename：**设置文件输出名称。默认为获取到的网页视频标题

**Set Output Path：**设置输出路径。不填默认下载到用户文件夹

**Open Save Path：**打开输出路径。更方便填写

### 3.5 开始选项区域

提供其他选项的依赖信息以及发出启动操作

<img src="./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/image-20230228132614562.png" alt="image-20230228132614562" style="zoom:150%;" />

- **Video URL(Required)：**视频链接（必填）。给爬虫提供要嗅探的资源地址

- **Firefox Cookies：**火狐浏览器数据。Cookies 是保存用户信息的文件，我们需要它模拟登陆网站以获得更高的清晰度

  > 有时候会报 431 错误，详见 **程序配置-程序问题解决**

- **Get Cookies(Auto)：**自动获取 Cookies。此选项大部分情况下能获取正确。部分用户可能无法正确识别。如果使用 自动获取 Cookies 后无法正常启动下载，请手动导入
- **Import Cookies(Manual)：**手动导入 Cookies。选择 cookies.sqlite3 即可导入
- **Complete：**完成。您已经确认信息提交无误，可以开始下载了。程序将会审查您的信息是否正确
- **Build The Command：**命令显示。我们将会把生成出来的命令显示在这里，您可以随意改动。反正······发送的指令也不是从这获取的
- **清晰度下拉框：**清晰度下拉框。解析完成后您可以自行选择清晰度，默认使用可以下载的最高清晰度
- **Download：**下载。按下该按钮将会启动下载操作，请==不要关闭终端和主窗口==
- **结果输出框：**输出程序运行结果。如果有报错或者下载完成都会在这里显示内容

### 3.6 关于程序区域

严格意义上来说，这是一片实验性功能。目前 Open Options 以及 View Help 均不会在稳定版本中开放（不会添加这部分的函数代码）

<img src="./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/image-20230228132639972.png" alt="image-20230228132639972" style="zoom:150%;" />

- **Dark Theme：**开启 / 关闭暗黑模式。默认会自动识别系统当前使用主题，并自动切换

  > **注意：**由于 winapi 的原因，Win10 22H2 已知需要重新聚焦窗口才能使窗口标题栏黑化。Win11 22H2 可以完美运行。

- **Open Options：**打开配置文件。预览版中可以为用户保存上一次下载的设置，以方便您的使用。但是目前该方法仍有问题需要解决，所以稳定版本没有该项功能（仅为按钮）
- **View Help：**查看帮助。该方法同样在测试，所以稳定版本没有该项功能（仅为按钮）



## 4 程序配置

### 4.1 ffmpeg 依赖安装

需要注意的是，程序仅仅集成了 you-get，并未集成 ffmpeg 。如果您不安装 ffmpeg 可能会出现：

- 音视频分离
- 下载速度缓慢

所以我们强烈推荐您安装 ffmpeg，ffmpeg 应该在源码中的 depend 文件夹。由于我们不确定这样做是否符合开源协议，所以请手动安装：

1. 找到 ffmpeg.exe：

![image-20230228133734051](./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/image-20230228133734051.png)

2. 按下 Ctrl + X 剪切该文件

![image-20230228133900392](./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/image-20230228133900392.png)

3. 粘贴到 C:\Windows

![image-20230228133920082](./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/image-20230228133920082.png)

> **注意：**安装到其他同样在系统环境变量中的 path 中的路径也可以正常使用

4. 打开终端，发送 ffmpeg，如果安装成功应该会输出如下信息：

   ![image-20230228134057433](./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/image-20230228134057433.png)

### 4.2 程序问题解决

目前已知问题：

- 有些用户提交火狐 Cookies 之后会产生 431 错误：

  - 原因：疑似解析火狐 Cookies 的库无法解析大量的 Cookies 数据

  - 解决方法：

    1. 打开火狐浏览器

       <img src="./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/image-20230228191226037.png" alt="image-20230228191226037" style="zoom: 67%;" />

    2. 打开设置

       <img src="./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/image-20230228191301656.png" alt="image-20230228191301656" style="zoom: 67%;" />

    3. 找到 **隐私与安全**，下滑找到 **Cookies 和网站数据**，并点击 **清除数据**

       <img src="./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/image-20230228191447933.png" alt="image-20230228191447933" style="zoom:67%;" />

    4. 再次尝试下载

  

## 5 特别鸣谢

**感谢所有参与测试用户：**

- A量子广告-「量子」
- 大叔学 Python
- 会飞的鱼
- 是一只憨猪猪啊
- 当代大学牲
- 椎名みかん
- fish4terrisa

**感谢以下库的作者：**

- [soimort/you-get](https://github.com/soimort/you-get)

  <img src="./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/d1dd1d744c155d4986a74bc2c149b684a04cceca.png" alt="GitHub - soimort/you-get: Dumb downloader that scrapes the web" style="zoom:50%;" />

- [rdbende/Sun-Valley-ttk-theme](https://github.com/rdbende/Sun-Valley-ttk-theme)

<img src="./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/e2fb8460fcfb2d115be9214e037d2c1d813bc786.png" alt="GitHub - rdbende/Sun-Valley-ttk-theme: A gorgeous theme for ttk, based on Microsoft's Sun Valley visual styles ✨" style="zoom:50%;" />

- [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg)

  <img src="./You%20Get%20Preview%20%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.assets/e3ec0517a99a9129a850678a14e2d905960a4133.png" alt="GitHub - FFmpeg/FFmpeg: Mirror of https://git.ffmpeg.org/ffmpeg.git" style="zoom:50%;" />
