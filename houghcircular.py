import cv2
import numpy as np
import math
img = cv2.imread('great3.jpg',0)
im=cv2.imread('images.jpeg',0)
#img = cv2.medianBlur(img,7)
#blur = cv2.GaussianBlur(img,(17,17),0)
#kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
#im = cv2.filter2D(img, -1, kernel)
#cv2.imwrite('hc23.jpg',im)
cimg = cv2.cvtColor(im,cv2.COLOR_GRAY2BGR)
#edges = cv2.Canny(img,50,150,apertureSize = 3)
#cv2.imwrite('hc.jpg',blur)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=20,maxRadius=50)
if len(circles) == 1:
    x, y, r1 = circles[0][0]
    x1=math.floor(x)
    y1=math.floor(y)
    r5=math.floor(r1+6)	
    print(x,y)
    mask = np.zeros((179,281),dtype=np.uint8)
    cv2.circle(mask,(x,y),r1,(255,255,255),-1,8,0)
    #cv2.imwrite(argv[2],mask)
    out = im*mask
    white = 255-mask
    cv2.imwrite('bili.jpeg',~(out+white))

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=20,maxRadius=40)
im3=cv2.imread('bili.jpeg',0)
if len(circles) == 1:
    x, y, r2 = circles[0][0]
    print(r2)
    roi = im3[y1-r5:y1+r5, x1-r5:x1+r5]
    cv2.imwrite('r.jpg',roi)
    mask = np.zeros((92,92),dtype=np.uint8)
    cv2.circle(mask,(x,y),r2,(255,255,255),-1,8,0)
    mask=~mask
    #cv2.imwrite(argv[2],mask)
    out = roi*mask
    print(out);
    white = 255-mask
    cv2.imwrite('bili.jpeg',~(out+white))
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imwrite('bhu2.jpg',cimg)
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
