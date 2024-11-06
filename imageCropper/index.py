from PIL import Image
import os

target = "Attack1"
path = "OriginalImages/Atack1/"
files = os.listdir(path)
for file in files:
  image=Image.open(f'{path}{file}')

  imageBox = image.getbbox()
  cropped = image.crop(imageBox)
  cropped.save(f'Cropped/{target}/{file}')