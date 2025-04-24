import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img1 = cv.imread("resources/lenna.png", cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
    
    
    img3 = img2[:,:,1]
    plt.imshow(img3, cmap='gray')
    plt.show()