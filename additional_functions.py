import os
import shutil
from PIL import Image


def rgba2rgb(image):
    '''
    Convert to RGBA to make sure it's a supported alpha channel
    '''
    convert_image = image.convert('RGBA')
    new_img = Image.new("RGB", convert_image.size, (255, 255, 255))
    new_img.paste(convert_image, mask=convert_image.split()[3])
    # 3 is the alpha channel

    return new_img


def flip_image(image):
    new_img = image.transpose(Image.FLIP_LEFT_RIGHT)
    return new_img


def rotate_image(image, degree):
    # convert to RGBA to get transparent background
    new_img = image.convert('RGBA')
    new_img = new_img.rotate(degree)
    background = Image.new("RGB", new_img.size, (255, 255, 255))
    background.paste(new_img, mask=new_img.split()[3])
    # 3 is the alpha channel
    return background


def resize_image(image, width, height):
    new_img = image.resize((width,height))
    return new_img


def move_image(srs_dir, dst_dir):
    for each in os.listdir(srs_dir):
        shutil.move(srs_dir + '/' + each, dst_dir + '/' + each)
