import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img_bgr = cv.imread("resources/lenna.png")
    img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
    
    
    img_red = img_rgb[:,:,0]
    
    plt.subplot(1,2,1)
    plt.title("Original picture")
    plt.imshow(img_rgb)
    
    plt.subplot(1,2,2)
    plt.title("Red values of the picture")
    plt.imshow(img_red, cmap='gray')
    plt.show()
    
    