import os
import shutil
from PIL import Image

from additional_functions import rgba2rgb, resize_image, \
    rotate_image, move_image, flip_image

pokemon_dataset_dir = 'data'
processed_dataset = 'data_preprocessed'

white_background = processed_dataset + '/white_background'
flip = processed_dataset + '/flip'
rotate = processed_dataset + '/rotate'
resize = processed_dataset + '/resize'
train = processed_dataset + '/train'

if os.path.basename(os.getcwd()) != 'pokemon_GAN':
    os.chdir('pokemon_GAN')
current_dir = os.getcwd()
pokemon_dir = os.path.join(current_dir, pokemon_dataset_dir)
white_background_dir = os.path.join(current_dir, white_background)
flip_dir = os.path.join(current_dir, flip)
rotate_dir = os.path.join(current_dir, rotate)
resize_dir = os.path.join(current_dir, resize)
train_dir = os.path.join(current_dir, train)

if not os.path.exists(white_background_dir):
                os.makedirs(white_background_dir)
if not os.path.exists(flip_dir):
                os.makedirs(flip_dir)
if not os.path.exists(rotate_dir):
                os.makedirs(rotate_dir)
if not os.path.exists(resize_dir):
                os.makedirs(resize_dir)
if not os.path.exists(train_dir):
                os.makedirs(train_dir)


# Convert from RGBA to RGB
for each in os.listdir(pokemon_dir):
    img = Image.open(pokemon_dir + '/' + each, 'r')
    img.load()
    rgb_img = rgba2rgb(img)
    rgb_img.save(white_background + '/' + each[:-3] + 'jpg', 'JPEG',
                 quality=100)

# Resize image
for each in os.listdir(white_background_dir):
    img = Image.open(white_background + '/' + each, 'r')
    img.load()
    resize_img = resize_image(img, 64, 64)
    resize_img.save(resize + '/' + each[:-4] + '.jpg', 'JPEG', quality=100)

# Flip image horizontally
for each in os.listdir(resize_dir):
    img = Image.open(resize + '/' + each, 'r')
    img.load()
    flip_img = flip_image(img)
    flip_img.save(flip + '/' + each[:-4] + '-f.jpg', 'JPEG', quality=100)

for each in os.listdir(resize_dir):
    img = Image.open(resize + '/' + each, 'r')
    img.load()
    rotate3deg = rotate_image(img, 3)
    rotate3deg.save(rotate + '/' + each[:-4] + '_ccwr3.jpg', 'JPEG',
                    quality=100)
    rotate5deg = rotate_image(img, 5)
    rotate5deg.save(rotate + '/' + each[:-4] + '_ccwr5.jpg', 'JPEG',
                    quality=100)
    rotate7deg = rotate_image(img, 7)
    rotate7deg.save(rotate + '/' + each[:-4] + '_ccwr7.jpg', 'JPEG',
                    quality=100)
    rotate3degcw = rotate_image(img, -3)
    rotate3degcw.save(rotate + '/' + each[:-4] + '_cwr3.jpg', 'JPEG',
                      quality=100)
    rotate5degcw = rotate_image(img, -5)
    rotate5degcw.save(rotate + '/' + each[:-4] + '_cwr5.jpg', 'JPEG',
                      quality=100)
    rotate7degcw = rotate_image(img, -7)
    rotate7degcw.save(rotate + '/' + each[:-4] + '_cwr7.jpg', 'JPEG',
                      quality=100)

for each in os.listdir(flip_dir):
    img = Image.open(flip + '/' + each, 'r')
    img.load()
    rotate3deg = rotate_image(img, 3)
    rotate3deg.save(rotate + '/' + each[:-4] + '_ccwr3.jpg', 'JPEG',
                    quality=100)
    rotate5deg = rotate_image(img, 5)
    rotate5deg.save(rotate + '/' + each[:-4] + '_ccwr5.jpg', 'JPEG',
                    quality=100)
    rotate7deg = rotate_image(img, 7)
    rotate7deg.save(rotate + '/' + each[:-4] + '_ccwr7.jpg', 'JPEG',
                    quality=100)
    rotate3degcw = rotate_image(img, -3)
    rotate3degcw.save(rotate + '/' + each[:-4] + '_cwr3.jpg', 'JPEG',
                      quality=100)
    rotate5degcw = rotate_image(img, -5)
    rotate5degcw.save(rotate + '/' + each[:-4] + '_cwr5.jpg', 'JPEG',
                      quality=100)
    rotate7degcw = rotate_image(img, -7)
    rotate7degcw.save(rotate + '/' + each[:-4] + '_cwr7.jpg', 'JPEG',
                      quality=100)

for dirr in flip_dir, resize_dir, rotate_dir:
    move_image(dirr, train_dir)
    shutil.rmtree(dirr, ignore_errors=True)

shutil.rmtree(white_background_dir, ignore_errors=True)
