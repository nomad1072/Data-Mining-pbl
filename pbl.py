import os, os.path, time
from scipy import misc
from scipy.ndimage import gaussian_filter1d
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageFilter


for file in os.listdir("/Users/siddharthlanka/Desktop/Data-Mining-pbl"):
	if file.endswith(".jpg"):
		img = misc.imread(str(file))
		print img.dtype, img.shape
		img_tinted = img * [1, 0.95, 0.9]
		img_tinted = misc.imresize(img_tinted, (200,255))
		path = str(file)
		l = path.split(".")
		l.insert(1,"_tinted.")
		path = ''.join(l)
		quality_val = 90
		misc.imsave(path, img_tinted)


for file in os.listdir("/Users/siddharthlanka/Desktop/Data-Mining-pbl"):
	if file.endswith("tinted.jpg"):
		img = misc.imread(str(file))
		img1 = gaussian_filter1d(img, 2)
		plt.imshow(img)
		plt.show()



