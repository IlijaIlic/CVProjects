import numpy as np
import cv2 as cv   
import matplotlib.pyplot as plt

if __name__ == "__main__":
    img = cv.imread("./resources/lenna.png")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)


    countsR, bins = np.histogram(img[:,:,0],bins = 256, range = (0,256))
    countsG, bins = np.histogram(img[:,:,1],bins = 256, range = (0,256))
    countsB, bins = np.histogram(img[:,:,2],bins = 256, range = (0,256))

    plt.subplot(2,1,1)
    plt.title("Analyzed image")
    plt.imshow(img)

    plt.subplot(2,3,4)
    plt.title("Histogram Red")
    plt.stairs(countsR,bins, color="red", fill=True)

    plt.subplot(2,3,5)
    plt.title("Histogram Green")
    plt.stairs(countsG,bins, color="green", fill=True)

    plt.subplot(2,3,6)
    plt.title("Histogram Blue")
    plt.stairs(countsB,bins, color="blue", fill=True)
   

    plt.show()