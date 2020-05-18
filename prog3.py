#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import numpy as np
from imageio import imread, imwrite
input1 = sys.argv[1]
input2 = sys.argv[2]
output = sys.argv[3]

im1 = imread(input1) # Открываем изображение
(h1, w1, d1) = im1.shape
im2 = imread(input2) # Открываем изображение
(h2, w2, d2) = im2.shape

print(f'width={w1}, height={h1}, size={im1.size}')
print(f'width={w2}, height={h2}, size={im2.size}')

# imwrite('copy.jpg', im, format='jpg') # пересохраняем исходное изображение
w0 = max(w1,w2)

im3 = np.zeros((h1+h2,w0,d1), dtype=np.uint8)

for ix in range(w1):
   for iy in range(h1):
        im3[iy][ix]=im1[iy][ix]
for ix in range(w2):
   for iy in range(h1):
        im3[iy+h1-1][ix]=im2[iy][ix]

imwrite(output, im3, format='jpg') # сохраняем транспонированное изображение 
