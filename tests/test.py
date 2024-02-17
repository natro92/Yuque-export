#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Project ：yuque-export 
@File    ：test.py
@desc    ：
@Author  ：@Natro92
@Date    ：2024/2/17 19:25 
@Blog    : natro92.github.io
@Contact : 2997453446@qq.com
"""
import asyncio

import aiohttp

from yuque.api import get_book_stacks

if __name__ == '__main__':
    print(asyncio.run(get_markdown("GjmDSBKgdOqFpJrwqFMTeWrwHi8Q23nTwneAzobQi2kdKSqn69ZpSHkWxFnQAwmGhbpHvifdpTp6hNQ2uCFoew==",
                             "natro92", "ono5a2", "age44awabi4dqy74", 'MyCTF', '测试test123')))


