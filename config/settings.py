#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Project ：yuque-export 
@File    ：settings.py
@desc    ：
@Author  ：@Natro92
@Date    ：2024/2/17 17:26 
@Blog    : natro92.github.io
@Contact : 2997453446@qq.com
"""

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
