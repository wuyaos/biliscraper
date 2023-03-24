from file_parsing import file_parsing
from gen_nfo import gen_nfo
from pathlib import Path
import time
from rename_file import format_filename
import re
from resize_pic import crop_image
from rename_file import format_name
from modify import replace_gif

input_file = Path("C:/Users/wff19/Downloads/Compressed/DownKyi-1.5.7/Media/link/")
# 重命名文件夹
format_name(input_file)
print("生成nfo文件")
for video_dir in input_file.glob("*"):
    # 获取视频列表
    video_num = len([video for video in video_dir.glob("*.mp4")])
    flag = False
    if video_num > 1:
        flag = True
    # 判断是否存在poster.jpg 以及 存在gif文件
    if not (video_dir / "poster.jpg").exists() :
        print(video_dir.name)
        format_filename(video_dir)
        video_list = [video for video in video_dir.glob("*.mp4")]
        # 产生nfo文件
        time.sleep(0.1)
        # 获取视频文件，并循环些nfo
        for video in video_list:
            file_name = video.name.split(".mp4")[0]
            nfo_file = video_dir / (file_name + ".nfo")
            if not nfo_file.exists():
                print(f"{nfo_file}生成成功")
                bilivideo_info = file_parsing(video, flag)
                nfo_content = gen_nfo(bilivideo_info)
                with open(nfo_file, "w", encoding="utf-8") as f:
                    f.write(nfo_content)
            else:
                print("nfo文件已存在")
