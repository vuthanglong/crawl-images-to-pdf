import os
from PIL import Image

lst = os.listdir('./imgs') # your directory path
number_of_files = len(lst)

image_1 = Image.open('imgs/%s.jpg' % 1)
im_1 = image_1.convert('RGB')
img_list = []

for i in range(2, number_of_files + 1):
  image = Image.open('imgs/%s.jpg' % i)
  im_rgb = image.convert('RGB')
  img_list.append(im_rgb)
im_1.save(r'pdf/antrom.pdf', save_all=True, append_images=img_list)
