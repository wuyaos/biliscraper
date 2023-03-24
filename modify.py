# 寻找对应的BVxx替换gif文件
import requests
from pathlib import Path

def gen_cover(bvid, cover_path):
    """
    根据视频BV号的视频截图作为封面
    """
    # 生成封面
    cover_url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
    cover_json = requests.get(cover_url).json()
    cover_url = cover_json["data"]["pic"]
    # 下载封面
    cover = requests.get(cover_url)
    with open(cover_path, "wb") as f:
        f.write(cover.content)
    
def replace_gif(input_path:Path):
    """
    将gif文件替换为封面
    """
    # 寻找对应的BVxx替换gif文件
    for file in input_path.rglob("*.gif"):
        # 获取父目录名，解析bvid
        bvid = file.parent.name.split('(')[1].split(')')[0]
        # 生成封面
        cover_path = file.parent / f"poster.jpg"
        gen_cover(bvid, cover_path)
        # 删除gif文件
        file.unlink()
