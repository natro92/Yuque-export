#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Project ：yuque-export 
@File    ：yuque-export.py
@desc    ：
@Author  ：@Natro92
@Date    ：2024/2/17 17:26 
@Blog    : natro92.github.io
@Contact : 2997453446@qq.com
"""
import asyncio
import aiohttp
import os
from os.path import exists
from datetime import datetime
from yuque.api import get_book_stacks, test_session_status, get_docs, get_info, generate_markdown_tasks
import re
import config.settings as settings
from yuque.utils import print_colored_text, start_program

yuque_session = ''
login_name = ''


def read_cookie():
    """
    读取cookie文件
    :return: yuque的session
    """
    untidy_cookie = ''
    yuque_session = ''
    if not exists('cookie.txt'):
        # 生成cookie.txt文件
        with open('cookie.txt', 'w') as f:
            f.write('将cookie内容放在这里！')
        raise Exception(
            'Cookie 文件不存在，已自动为您生成，请按照 README.md 中的说明获取 Cookie 并保存到 cookie.txt 文件中')

    with open('cookie.txt', 'r') as f:
        untidy_cookie = f.read()
    # * 正则读取session
    yuque_session = re.findall(r'_yuque_session=(.*?);', untidy_cookie)
    if not yuque_session:
        raise Exception('Cookie 文件格式不正确，请按照 README.md 中的说明获取 Cookie 并保存到 cookie.txt 文件中')
    return yuque_session[0]


if __name__ == '__main__':
    start_program()
    # 判断config文件是否存在已经解析的session，如果存在则进行测试是否可以继续使用。
    # 这里不方便切换用户
    if not exists('config/session'):
        with open('config/session', 'w') as f:
            f.write(read_cookie())
    else:
        with open('config/session', 'r') as f:
            yuque_session = f.read()
        os.remove('config/session')
    # * 拉取目录
    # * 判断Cookie是否有效
    try:
        book_stacks_json = asyncio.run(get_book_stacks(yuque_session))
    except Exception as e:
        print_colored_text(31, f"[*] {e}")
        print_colored_text(31, "[*] 请检查cookie是否过期，或者未修改cookie.txt文件中的内容")
        # 删除session缓存
        if exists('config/session'):
            os.remove('config/session')
        exit(1)
    books = book_stacks_json['data'][0]['books']
    book_list = []
    print_colored_text(33, f"[*] 获取目录列表信息")

    for index, book in enumerate(books):
        book_list.append({"index": index, "name": book['name'], "slug": book['slug'], "id": book['id'],
                          "items_count": book['items_count']})
        if settings.show_detailed:
            print(index, book['name'], book['slug'], book['id'], book['items_count'])
    # * 选择目录
    # book_index = int(input('请输入要导出的目录序号：-1为全部使用空格隔开 eg: 1 2 3\n'))
    # 拉取全部
    # * 拉取文章
    doc_list = []
    for book in book_list:
        # * 生成目录
        get_docs_json = asyncio.run(get_docs(yuque_session, str(book['id'])))
        # * 解析文章参数
        docs = get_docs_json['data']
        print_colored_text(33, f"[*] 获取 {book['name']} 列表信息")
        for index, doc in enumerate(docs):
            created_at = datetime.strptime(doc["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S")
            doc_list.append(
                {"index": index, "title": doc['title'], "slug": doc['slug'], "id": doc['id'], "type": doc['type'],
                 "created_at": doc['created_at'], "word_count": doc['word_count'], "name": book['name'],
                 "book_id": book['id'], "book_slug": book['slug']})
            if settings.show_detailed:
                print(index, doc['title'], doc['slug'], doc['id'], created_at, doc["word_count"])
            # TODO 删除这里
        # print(f"[*] 获取{book['name']}文章列表信息完成")
    # * 获取个人login
    info_json = asyncio.run(get_info(yuque_session))
    # /data/login
    login_name = info_json['data']['login']
    # TODO 这里可以加个自定义导出的功能，方便拓展比如导出到hexo等
    # * 导出文章
    asyncio.run(generate_markdown_tasks(yuque_session, login_name, doc_list))
