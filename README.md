# 通过Telegram bot来查看和控制你的Mac锁屏状态



## 功能

1. 通过Telegram bot锁定屏幕/进入屏保/查看锁定状态。
2. 每隔一分钟发送当前锁屏状态，并自动删除上一条状态，防止刷屏。

## 说明

​	记得在`maclock_push.py`里把chat_id和token换成你自己的。

​	***所有人***都可以通过bot来查看和控制你的Mac，所以记得使用私人的bot，***不要轻易透露bot给别人***。~~权限控制还没搞清楚怎么做。~~

## 使用方法

​	安装python-telegram-bot 库，版本是13.13，注意不要安装20版本。然后运行`maclock_push.py`就可以在bot上查看效果了。

​	`/status`	`/lock` `/screen`分别是查看状态、进入锁屏和进入屏幕保护。

​	还加入了一个定时器，每隔一分钟发送一次锁屏状态，并且自动删除上一次发送的状态，防止刷屏。

## 效果图

![2022-12-05 _ 09.15.20_Telegram.gif](2022-12-05 _ 09.15.20_Telegram.gif)

## 更好的使用方法

​	通过pyinstaller `pyinstaller --noconsole maclock_push.py`打包成app，然后在设置-用户与群组里把app设置为开机启动。

​	如果不想在dock栏里看到图标，可以在终端输入`sudo lsappinfo setinfo -app maclock_push ApplicationType=UIElement`来隐藏app图标。