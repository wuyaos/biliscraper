from biliscraper.file_parsing import file_parsing
from biliscraper.gen_nfo import gen_nfo
from pathlib import Path
import time
from biliscraper.rename_file import format_filename, format_name
import argparse

# todo: 1.日志文件；2.srt文件没重命名成功；3.TV类型刮削

def main():
    parser = argparse.ArgumentParser(description='BiliBili视频刮削工具')
    parser.add_argument('-i', '--inputdir', type=str, default="./", help="刮削的文件夹路径")
    parser.add_argument('-s', '--style', type=str, default="movie", help="刮削样式：movie/tv")
    input_file = Path(parser.parse_args().inputdir).absolute()
    style = parser.parse_args().style

    # 重命名文件夹
    print("==========重命名文件夹==========")
    format_name(input_file)
    print("==========生成nfo文件==========")
    for video_dir in input_file.glob("*"):
        print("**********************************")
        print(f"开始处理文件夹：{video_dir.name}")
        # 获取视频列表
        video_num = len([video for video in video_dir.glob("*.mp4")])
        flag = False
        if video_num > 1:
            flag = True
            print("该视频为多P视频")
        else:
            print("该视频为单P视频")
        # 判断是否存在poster.jpg 以及 存在gif文件
        if not (video_dir / "poster.jpg").exists():
            print("开始整理文件...")
            format_filename(video_dir)
            video_list = [video for video in video_dir.glob("*.mp4")]
            # 产生nfo文件
            time.sleep(0.3)
            # 获取视频文件，并循环些nfo
            print("开始产生nfo文件...")
            for video in video_list:
                file_name = video.name.split(".mp4")[0]
                nfo_file = video_dir / (file_name + ".nfo")
                if not nfo_file.exists():
                    bilivideo_info = file_parsing(video, flag)
                    nfo_content = gen_nfo(bilivideo_info)
                    with open(nfo_file, "w", encoding="utf-8") as f:
                        f.write(nfo_content)
                    print(f"{nfo_file.name}生成成功")
                else:
                    print("nfo文件已存在")
        print("**************完成*************")
