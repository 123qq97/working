import os

# 直接下载DEFAULT默认品质的格式视频: you-get + 视频地址
# os.system('you-get https://www.bilibili.com/video/BV1Px41167GF?from=search&seid=13390240613390403617')

#下载到指定路径: you-get -o 本地路径 + 视频地址
# os.system('you-get -o C:/Users/JF/Desktop/视频/ https://www.bilibili.com/video/BV1h7411L7VV?from=search&seid=13390240613390403617')

# 获取视频下所有品质和格式的信息: you-get -i + 视频地址
# os.system('you-get -i https://www.bilibili.com/video/BV1E7411k7Qy?from=search&seid=14467929794535435809')

#获取指定品质/格式的视频: you-get --format=xx +视频地址   ，(format品质格式用 you-get -i 获取)
# os.system('you-get --format=flv720 -o C:/Users/JF/Desktop/视频/ https://www.bilibili.com/video/BV1E7411k7Qy?from=search&seid=14467929794535435809')

#解析视频真实地址: you-get -u +视频地址
# os.system('you-get -u https://www.bilibili.com/video/BV1E7411k7Qy?from=search&seid=14467929794535435809')

#获取视频的json信息: you-get --json +视频地址
# os.system('you-get --json https://www.bilibili.com/video/BV1St411w72P?from=search&seid=8389839597474901756')

#修改编码格式，默认GBK为936，utf-8为65001
# os.system('chcp 65001')

#修复标题栏文字乱码
# os.system('Lucida Console')