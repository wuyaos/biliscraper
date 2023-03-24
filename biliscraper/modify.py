from pathlib import Path
import subprocess
from PIL import Image
from biliscraper.resize_pic import crop_image

ffmpeg_path = "C:/app/ffmpeg/bin/ffmpeg.exe"
ffmprobe_path = "C:/app/ffmpeg/bin/ffprobe.exe"

def replace_gif(input_path:Path):
    """
    将gif文件替换为封面
    """
    print(input_path)
    # 获取视频列表
    video = [video for video in input_path.glob("*.mp4")][0]
    # 获取视频时长
    result = subprocess.run([ffmprobe_path, '-i', video, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    duration = float(result.stdout)

    # 截取视频的10%时长的截图
    start_time = duration * 0.2
    image_file = input_path / "poster.jpg"
    subprocess.run([ffmpeg_path, '-i', video, '-ss', str(start_time), '-vframes', '1', "-y",str(image_file)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # 若为竖向图，则直接改名为poster.jpg
    image_obj = Image.open(image_file)
    if image_obj.height < image_obj.width:
        crop_image(image_file, image_file, 0.65)
        image_obj.close()
    # 删除gif文件
    for gif in input_path.glob("*.gif"):
        gif.unlink()
