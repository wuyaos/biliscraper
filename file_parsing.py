import asyncio
import datetime
import json
from pathlib import Path
import re
import jsbeautifier
import requests
from bilibili_api import video, video_tag


async def getinfo(BV):
    # 实例化 Video 类
    v = video.Video(bvid=BV)
    # 获取信息
    info = await v.get_info()
    # 打印信息
    return info

# 解析文件名
def file_parsing(file:Path, flag=False):
    # flag为True时,存在多P视频
    parent_dir = file.parent
    # 匹配title
    bilivideo_name = re.search(r'^(.+)\(', parent_dir.name).group(1)
    # 匹配Id
    bilivideo_id = re.search(r'\((\w+)\)$', parent_dir.name).group(1)
    if flag:
        # 解析pname,pid,名称格式<title - pid#pname.mp4>
        pname = re.search(r'(.*) - (\d+)#(.*)\.mp4', file.name).group(3)
        pid = re.search(r'(.*) - (\d+)#(.*)\.mp4', file.name).group(2)
        pname = f"{pid}.{pname}"
    else:
        pname = None
    url = 'https://api.bilibili.com/x/tag/archive/tags'
    params = {'bvid': bilivideo_id}
    response = requests.get(url, params=params).json()
    info = asyncio.get_event_loop().run_until_complete(getinfo(bilivideo_id))
    actorlist = []
    if "staff" in info.keys():
        staff_list = info["staff"]
        for staff in staff_list:
            if staff["title"]=="UP主" or staff["title"]=="参演":
                actorlist.append({"name": staff["name"], "thumb": staff["face"], "role": staff["title"],"profile":f"https://space.bilibili.com/{staff['mid']}"})
    else:
        actorlist.append({"name": info["owner"]["name"], "thumb": info["owner"]["face"], "role": "UP主","profile":f"https://space.bilibili.com/{info['owner']['mid']}"})
    tag_list = []

    for tag in response['data']:
        tag_list.append(tag['tag_name'])
    bilivideo_info = {
        "title": bilivideo_name,
        "originaltitle": bilivideo_name,
        "sorttitle": bilivideo_name,
        "year": datetime.datetime.fromtimestamp(info["pubdate"]).strftime('%Y'),
        "releasedate": datetime.datetime.fromtimestamp(info["pubdate"]).strftime('%Y-%m-%d'),
        "country": "中国",
        "countrycode": "CN",
        "pname": pname,
        "bvid": bilivideo_id,
        "plot": info["desc"],
        "genre": ['Bilibili', info["tname"]],
        "actor": actorlist,
        "poster": info["pic"],
        "tag": tag_list,
        "original_filename": file.name,
    }
    return bilivideo_info

if __name__ == '__main__':
    info = asyncio.get_event_loop().run_until_complete(getinfo("BV1dx411F7jC"))
    print(info)