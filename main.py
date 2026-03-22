import sys
import PIL.Image
import cv2
import PIL
import numpy as np
import matplotlib.pyplot as plt
import time

# This algorithm works by adding the weighted position (Ortsvector)
# of all mass points (here pixels).
# Then dividing those by the total area (or weight in 3d).
# This algorithm is rather slow for large images

start = time.time()

infile = sys.argv[1]

img = PIL.Image.open(infile)
mono_image = img.convert("L")
img_array = np.asarray(mono_image)

# Accumulator for positions x.
xS = 0 
yS = 0

# Accumulator for the area.
a = 0

# Loop through all pixels
for iy, ix in np.ndindex(img_array.shape):
    v = img_array[iy, ix] / 255 # Density 0-1, white is 100% dense, black 0%.
    a += v # Mass point weight is added to total
    
    # Add the weighted position
    xS += ix*v 
    yS += iy*v

# Divide position sum by area
x = float(xS / a)
y = float(yS / a)


COM_txt = f'COM is at [{round(x, 3)}, {round(y, 3)}] \n ({round(x/img_array.shape[1]*100,1)}%, {round(y/img_array.shape[0] * 100,1)}%)'
print(COM_txt)

plt.imshow(img)
plt.plot(x,y, "ro")
plt.annotate(COM_txt, (x+15,y), color="#ff0000")

plt.savefig(f'{infile}_COM.png')

print("Found COM in", time.time() - start, "seconds!")
plt.show()