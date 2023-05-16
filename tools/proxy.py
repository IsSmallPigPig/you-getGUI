# 导入requests库和re模块
# 好用的
import requests

# 定义一个函数，接受一个代理地址作为参数，返回True或False表示是否有效
def check_proxy(proxy, port):
    # 设置请求头和超时时间
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    timeout = 5

    # 尝试用代理访问一个测试网站，比如百度
    try:
        response = requests.get("https://www.global.bing.com", headers=headers, proxies={"https": f"{proxy}:{port}"},
                                timeout=timeout)
        # 如果状态码是200，并且响应内容包含百度的关键字，说明代理有效
        if response.status_code == 200:
            return True
        else:
            return False
    # 如果发生异常，说明代理无效
    except Exception as e:
        return False


# 定义一个函数，接受一个代理地址，端口号，用户名和密码作为参数，返回True或False表示是否有效
# 定义一个函数，接受一个代理地址，端口号，可选的用户名和密码作为参数，返回True或False表示是否有效
def check_proxy(proxy, port, username=None, password=None):
    # 设置请求头和超时时间
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    timeout = 5

    # 如果有用户名和密码，需要构造一个带有认证信息的代理字符串
    if username and password:
        proxy = f"{username}:{password}@{proxy}:{port}"
    else:
        proxy = f"{proxy}:{port}"

    # 尝试用代理访问一个测试网站，比如谷歌
    try:
        response = requests.get("https://www.global.bing.com", headers=headers, proxies={"http": f"socks5://{proxy}", "https": f"socks5://{proxy}"}, timeout=timeout)
        # 如果状态码是200，并且响应内容包含谷歌的关键字，说明代理有效
        if response.status_code == 200:
            return True
        else:
            return False
    # 如果发生异常，说明代理无效
    except Exception as e:
        return False
