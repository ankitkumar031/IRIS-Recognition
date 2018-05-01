import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('images.jpeg',0)

edges = cv.Canny(img,40,220)
cv.imwrite('great3.jpg',edges)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

