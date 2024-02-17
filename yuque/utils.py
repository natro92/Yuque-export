#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Project ：yuque-export 
@File    ：utils.py
@desc    ：
@Author  ：@Natro92
@Date    ：2024/2/17 17:26 
@Blog    : natro92.github.io
@Contact : 2997453446@qq.com
"""


def print_colored_text(color_code, text):
    """
    打印彩色文字
    :param color_code:
    :param text:
    :return:
    """
    print(f"\033[{color_code}m{text}\033[0m")


def get_colored_text(color_code, text):
    return f"\033[{color_code}m{text}\033[0m"


def start_program():
    ascii_art = """  
██╗   ██╗██╗   ██╗ ██████╗ ██╗   ██╗███████╗    ███████╗██╗  ██╗██████╗  ██████╗ ██████╗ ████████╗
╚██╗ ██╔╝██║   ██║██╔═══██╗██║   ██║██╔════╝    ██╔════╝╚██╗██╔╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
 ╚████╔╝ ██║   ██║██║   ██║██║   ██║█████╗█████╗█████╗   ╚███╔╝ ██████╔╝██║   ██║██████╔╝   ██║   
  ╚██╔╝  ██║   ██║██║▄▄ ██║██║   ██║██╔══╝╚════╝██╔══╝   ██╔██╗ ██╔═══╝ ██║   ██║██╔══██╗   ██║   
   ██║   ╚██████╔╝╚██████╔╝╚██████╔╝███████╗    ███████╗██╔╝ ██╗██║     ╚██████╔╝██║  ██║   ██║   
   ╚═╝    ╚═════╝  ╚══▀▀═╝  ╚═════╝ ╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                                                            by Natro92 
    Github https://github.com/natro92
    Blog https://natro92.fun"""
    print(ascii_art)
