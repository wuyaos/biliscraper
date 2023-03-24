from PIL import Image
from pathlib import Path

def crop_image(input_file, output_file, ratio):
    with Image.open(input_file) as img:
        width, height = img.size
        
        target_width = int(height * ratio)
        target_height = height
        
        left = int((width - target_width) / 2)
        upper = 0
        right = int((width + target_width) / 2)
        lower = target_height
        
        try:
            cropped_img = img.crop((left, upper, right, lower))
            cropped_img.save(output_file)
        except:
            img = img.convert('RGB')
            cropped_img = img.crop((left, upper, right, lower))
            cropped_img.save(output_file)

if __name__ == '__main__':
    poster_path = Path("X:/bilibili/movie")
    for poster in poster_path.rglob("poster*"):
        print(poster)
        crop_image(poster, poster, 0.75)