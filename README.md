==New:
1. Enabled console_qr=True to enable it run on server 
2. Add function for reply to specific my_friend only. (robot.py)
3. Add new API key from tuling robot. 


==Original source
# wxrobot

## 一、启动步骤
1.下载wxpy库 `pip3 install -U wxpy -i "https://pypi.doubanio.com/simple/"`，使用的是国内源，如果使用anaconda直接在pycharm里面下载，注意项目环境问题！

2.启动`robot.py`，弹出登录二维码，手机微信扫一扫登录

4.在robot.py中修改了bot = Bot(cache_path=True, console_qr=True)，console_qr=True表示在控制台打印二维码显示，方便部署到服务器，如果你不需要部署服务器可去掉这个入参

## 二、功能介绍

### 好友功能

针对微信好友的一些功能，如自动通过好友申请，与使用机器人好友聊天等

#### 1.自动通过好友申请
可匹配好友申请时的消息中关键字，例如：请求添加好友说明中包含"加群"，则通过申请，其他则不做处理！

#### 2.机器人聊天
目前聊天仅支持文字

wxpy库已经深度整合图灵机器人与小i机器人，目前暂时只接入图灵机器人，后面可实现管理员口令自动切换

管理员可远程控制开关。

### 群功能

#### 1.机器人群聊
群聊中回复好友，默认开启并且需要@机器人，可在`config.py`修改默认配置！
如果配置了机器人管理员则可以用关键字远程控制相关配置。

#### 2.监控群分享
群中如果有谁发分享文章，机器人则会转发至机器人管理员，方便管理员第一时间监控是否有人发广告！
默认关闭，开启需要`config.py`中配置监控群。
管理员可远程控制开关。

#### 3.监听某人
监听某人（如老板）在群聊中的消息，只要他在某群中发布了消息则将消息转发至管理员！
默认关闭，开启需要config.py中配置监听群。
管理员可远程控制开关。

#### 4.转发至群
如果开启转发模式，管理员发送消息给机器人后，机器人将消息转发至指定群，如转发至：Python交流1群...Python交流n群。
默认关闭，开启需要`config.py`中配置转发群。
管理员可远程控制开关。

### 公众号功能
pass

### 管理员功能

如果你使用的是你的小号，那么你可以配置一个管理员，可以远程来控制此机器人，添加方式：
在`config.pyz`中修改配置项`bot_master_name=管理员名称`（最好使用备注名称）即可！

如果没有添加管理员，则无法使用远程控制功能，机器人日志消息将发送至机器人的文件助手中！

设置好机器人的管理员后，可以向机器人发送以下命令来远程控制机器人：

`查看状态`：查看机器人配置状态
<br/><br/>`开启转发模式`：开启之后管理员给机器人发什么他都会转发到指定群，可以发送：关闭转发模式 来关闭换发模式，慎用！<br/>`关闭转发模式`
<br/><br/>`休眠`：所有功能关闭，只允许管理员发指令<br/>`开启`：恢复功能<br/>`退出`：退出登录
<br/><br/>`开启好友回复`：自动聊天回复，默认开启<br/>`关闭好友回复`
<br/><br/>`开启群聊回复`：开启群聊回复，默认开启<br/>`关闭群聊回复`
<br/><br/>`开启群聊艾特回复`：群聊中是否需要@机器人才会回复，默认是需要<br/>`关闭群聊艾特回复`：关闭后则不需要@机器人就会自动回复，慎用！
<br/><br/>`开启转发群艾特模式`：当群聊中有人@你，则会将消息转发至机器管理员，默认开启<br/>`关闭转发群艾特模式`：
<br/><br/>`开启监听模式`：监听某些群中的某些人的群聊，默认关闭，开启前需要配置在哪些群中监听哪些人<br/>`关闭监听模式`
<br/><br/>`开启监控模式`：指定群中有人推分享则会转发到机器人管理员中（监控广告），默认关闭，开启前需要配置监控群<br/>`关闭监控模式`
<br/><br/>`开启防撤回模式`：当有好友或群聊中有人撤回消息，将会把被撤回的消息发送至管理员，默认开启<br/>`关闭防撤回模式`
<br/><br/>

## 三、文档说明

1.[wxpy官方文档](https://wxpy.readthedocs.io/zh/latest/)

