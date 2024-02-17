```
██╗   ██╗██╗   ██╗ ██████╗ ██╗   ██╗███████╗    ███████╗██╗  ██╗██████╗  ██████╗ ██████╗ ████████╗
╚██╗ ██╔╝██║   ██║██╔═══██╗██║   ██║██╔════╝    ██╔════╝╚██╗██╔╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
 ╚████╔╝ ██║   ██║██║   ██║██║   ██║█████╗█████╗█████╗   ╚███╔╝ ██████╔╝██║   ██║██████╔╝   ██║
  ╚██╔╝  ██║   ██║██║▄▄ ██║██║   ██║██╔══╝╚════╝██╔══╝   ██╔██╗ ██╔═══╝ ██║   ██║██╔══██╗   ██║
   ██║   ╚██████╔╝╚██████╔╝╚██████╔╝███████╗    ███████╗██╔╝ ██╗██║     ╚██████╔╝██║  ██║   ██║
   ╚═╝    ╚═════╝  ╚══▀▀═╝  ╚═════╝ ╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝
                                                                            by Natro92
```
> 这几天在搞Obsidian，想把内容本地化一下，但是一个一个导出太费劲了，就简单写了一个demo。

本项目无需使用语雀的Token。但是需要使用Cookie来进行登录。
# 使用方法

- 安装依赖
```
pip install -r requirements.txt
```

- 获取Cookie

登录 [语雀](https://www.yuque.com) 后，在主页 `F12` 打开开发者工具。切换至`网络`栏，刷新页面，复制框选内容粘贴至程序根目录的`cookie.txt`中。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/34866087/1708189907504-5986da5f-cfde-4433-8f70-b6c1e85ff005.png#averageHue=%232b2828&clientId=u9501d254-fc5c-4&from=paste&height=779&id=u8af822f1&originHeight=974&originWidth=1860&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=174494&status=done&style=none&taskId=ucb17ef3f-3e9a-4e36-bbab-a09cbb1ec70&title=&width=1488)

- 到程序根目录下运行
```
python yuque-export.py
```

- 运行截图

![image.png](https://cdn.nlark.com/yuque/0/2024/png/34866087/1708190078999-f09542ef-cf07-485e-8fdd-a87d1ddb4962.png#averageHue=%231b1a16&clientId=u9501d254-fc5c-4&from=paste&height=734&id=ub73f7616&originHeight=918&originWidth=1571&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=265840&status=done&style=none&taskId=u1d014313-e52b-46ea-a6a2-d68a72ab9d0&title=&width=1256.8)
结果保存在程序根目录下`output`文件夹中，保存速度可能与网速有关，我测试时设置0.5-0.8s延迟时约1.5s一个md文件。
你可以在`config/settings.py`中修改参数配置：
```
# * 文件导出路径 默认为项目文件夹下的output文件夹 或者修改为绝对路径
save_place = "output"

# * 是否显示详细信息 1 为显示 0 为不显示
show_detailed = 0

# * 每次导出休眠时间，随机为 wait_time 到 wait_time + wait_time_delta 之间的数
# * 比如 wait_time = 0.2, wait_time_delta = 0.1, 则每次导出的等待时间为 0.2 到 0.3 秒之间
is_wait = 1  # * 是否开启等待 1 为开启 0 为关闭，目前关闭有Bug，待修 如果出现cannot access local variable 'text_data' where it is not associated with a value 可能就需要调大点了
wait_time = 0.5
wait_time_delta = 0.3

# * 导出设置
attachment = "true"  # * 导出 LaTeX 公式图片
latexcode = "false"  # * 导出 LaTeX 公式为 Markdown 语法
anchor = "false"  # * 导出保持语雀的锚点
linebreak = "false"  # * 导出保持语雀的换行
```
修改这部分可能会有点小bug，注意事项我都卸载里面了。
注意：本版本未支持导出图片至本地，原因是Obsidian的一些插件似乎支持这个功能，另一个原因是本来用来使用的Hexo，是可以通过不传referrer来绕过防盗链检测的，详情可以看：

- [将语雀作为静态博客图床](https://natro92.fun/posts/d18ef46e/)
