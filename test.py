import asyncio
from bilibili_api import video
from av2bv import *

async def getinfo(BV):
    # 实例化 Video 类
    v = video.Video(bvid=BV)
    # 获取信息
    info = await v.get_info()
    # 打印信息
    return info

if __name__ == '__main__':
    # asyncio.get_event_loop().run_until_complete(main())
    BV = av_to_bv("AV840692187")
    info = asyncio.get_event_loop().run_until_complete(getinfo(BV))
    print(info)