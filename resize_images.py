import os
from glob import glob

from PIL import Image


def resize_images(images_dir, image_save_dir, image_size):

    os.makedirs(image_save_dir, exist_ok=True)

    image_paths = glob(os.path.join(images_dir, '*'))

    for img_path in image_paths:
        image = Image.open(img_path)
        image = image.convert('RGB')

        resize_image = image.resize((image_size, image_size))
        save_path = os.path.join(image_save_dir, os.path.basename(img_path))
        resize_image.save(save_path)


def _main():
    images_dir = '../images/'  # 適宜変更
    image_save_dir = '../resize_images/'  # 適宜変更
    image_size = 128  # 適宜変更

    resize_images(images_dir=images_dir, image_save_dir=image_save_dir, image_size=image_size)


if __name__ == '__main__':
    _main()