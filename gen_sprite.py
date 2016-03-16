import sys
from PIL import Image
from os import walk
import re
import fnmatch
import time
import os

image_files = []

ext_filter = ['*.png']
regex_filter = r'|'.join([fnmatch.translate(x) for x in ext_filter])

for (dirpath, dirnames, filenames) in walk("."):
	filenames[:] = [fname for fname in filenames if re.match(regex_filter, fname)]
	image_files.extend(filenames)

#print(image_files)

images = map(Image.open, image_files)
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]


curr_time = int(round(time.time() * 1000))
sprite_dir = "sprite_%s" % (curr_time)
sprite_filepath = "%s/sprite.jpg" % (sprite_dir)

os.mkdir(sprite_dir)
new_im.save(sprite_filepath)

print("Done, sprite stored at %s" % (sprite_filepath))
