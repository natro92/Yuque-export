#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Project ：yuque-export 
@File    ：api.py
@desc    ：
@Author  ：@Natro92
@Date    ：2024/2/17 17:25 
@Blog    : natro92.github.io
@Contact : 2997453446@qq.com
"""
import random

import aiohttp
import asyncio
import aiofiles
import json

from tqdm import trange, tqdm
import config.settings as settings
from pathlib import Path

from yuque.utils import print_colored_text, get_colored_text


async def write_text_to_markdown(filename, text):
    # 使用aiofiles打开文件以进行异步写操作
    # * 确定文件夹均存在，不存在则创建
    file_path = Path(settings.save_place + '/' + filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    async with aiofiles.open(file_path, 'w', encoding='utf-8') as file:
        await file.write(text)
    # 用tqdm的write来代替print可以不让输出被打断
    tqdm.write(get_colored_text(32, f" {filename} 保存成功"))


async def test_session_status(_session_key, session):
    """
    判断session是否过期
    TODO 再说吧
    :return: bool
    """
    pass


async def _get_book_stacks(_session_key, session):
    """
    获取知识库列表，返回JSON数据
    :return: json_data
    """
    url = 'https://www.yuque.com/api/mine/book_stacks'
    headers = {
        'Host': 'www.yuque.com',
        'Cookie': '_yuque_session=' + _session_key,
    }
    async with session.get(url, headers=headers) as response:
        # 确保返回状态是200 OK
        response.raise_for_status()
        # 解析返回的JSON数据
        json_data = await response.json()
        return json_data


async def get_book_stacks(_session_key):
    """
    获取知识库列表
    :param _session_key:
    :return:
    """
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        json_response = await _get_book_stacks(_session_key, session)
        # print(json_response)
        return json_response


async def _get_docs(_session_key, session, book_id):
    """
    导出markdown格式doc，保存到本地
    :return: json_data
    """
    url = 'https://www.yuque.com/api/docs?book_id=' + book_id
    headers = {
        'Host': 'www.yuque.com',
        'Cookie': '_yuque_session=' + _session_key,
    }
    async with session.get(url, headers=headers) as response:
        # 确保返回状态是200 OK
        response.raise_for_status()
        # 解析返回的JSON数据
        json_data = await response.json()
        return json_data


async def get_docs(_session_key, book_id):
    async with aiohttp.ClientSession() as session:
        json_response = await _get_docs(_session_key, session, book_id)
        # print(json_response)
        return json_response


async def _get_info(_session_key, session):
    """
    获取个人信息来拼接yrl，返回JSON数据
    :return: json_data
    """
    url = 'https://www.yuque.com/api/mine'
    headers = {
        'Host': 'www.yuque.com',
        'Cookie': '_yuque_session=' + _session_key,
    }
    async with session.get(url, headers=headers) as response:
        # 确保返回状态是200 OK
        response.raise_for_status()
        # 解析返回的JSON数据
        json_data = await response.json()
        return json_data


async def get_info(_session_key):
    async with aiohttp.ClientSession() as session:
        json_response = await _get_info(_session_key, session)
        # print(json_response)
        return json_response


async def _get_markdown(_session_key, session, login, book_slug, doc_slug):
    """
    获取文章列表，返回markdown内容
    :return: text_data
    """
    url = 'https://www.yuque.com/' + login + '/' + book_slug + '/' + doc_slug + f'/markdown?attachment={settings.attachment}&latexcode={settings.latexcode}&anchor={settings.anchor}&linebreak={settings.linebreak}'
    headers = {
        'Host': 'www.yuque.com',
        'Cookie': '_yuque_session=' + _session_key,
    }
    async with session.get(url, headers=headers) as response:
        # 确保返回状态是200 OK
        response.raise_for_status()
        text_data = await response.text()
        return text_data


async def yuque_export(_session_key, login, book_slug, doc_slug, book_name, doc_title, doc_type):
    async with aiohttp.ClientSession() as session:
        if doc_type == 'Doc':
            text_data = await _get_markdown(_session_key, session, login, book_slug, doc_slug)
        else:
            # TODO 如果是其他种类导出，暂时不处理
            pass
        await write_text_to_markdown(book_name + '/' + doc_title + '.md', text_data)


async def generate_markdown_tasks(yuque_session, login, doc_list):
    """
    异步排序任务
    :param yuque_session: session文本
    :param login: login name参数
    :param doc_list: doc列表
    :return:
    """
    tasks = []
    for doc in tqdm(doc_list):
        # * 随机休眠
        if settings.is_wait:
            await asyncio.sleep(random.uniform(settings.wait_time, settings.wait_time + settings.wait_time_delta))
        task = asyncio.create_task(
            yuque_export(yuque_session, login, doc['book_slug'], doc['slug'], doc['name'], doc['title'], doc['type']))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print_colored_text(32, f" [*] 导出完成")
