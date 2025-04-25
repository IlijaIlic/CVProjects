import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img1 = cv.imread("resources/lenna.png")
    img1_rgb = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
    
    img2 = cv.imread("resources/peppers.tiff")
    img2_rgb = cv.cvtColor(img2, cv.COLOR_BGR2RGB)
    
    plt.subplot(1,2,1)
    plt.title("Original picture 1")
    plt.imshow(img1_rgb)
    
    plt.subplot(1,2,2)
    plt.title("Original picture 2")
    plt.imshow(img2_rgb)
    
    plt.show()
    
    
    img3 =  np.zeros((512, 512, 3), dtype=np.uint8)
    
    for x in range(512):
        for y in range(512):
            if img1_rgb[x,y,1] >= img2_rgb[x,y,1]:
                img3[x,y] = img1_rgb[x,y]
            else:
                img3[x,y] = img2_rgb[x,y]

    
    plt.title("Image created by combining first two images based on green values")
    plt.imshow(img3)
    plt.show()