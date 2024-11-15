import PIL.Image
import cv2
import PIL
import numpy as np
import matplotlib.pyplot as plt

img = PIL.Image.open("./test_01.psd")
mono_image = img.convert("L")
img_array = np.asarray(mono_image)

pixel_count = img_array.shape[0] * img_array.shape[1]

xS = 0
yS = 0

a = 0

for iy, ix in np.ndindex(img_array.shape):
    v = img_array[iy, ix] / 255 # Density 0-1
    # v = 1
    a += v
    xS += ix*v
    yS += iy*v

x = xS / a
y = yS / a


plt.imshow(img)
plt.plot(x,y, "ro")

plt.show()
