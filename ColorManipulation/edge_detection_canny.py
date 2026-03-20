import cv2 as cv
import matplotlib.pylab as plt
import numpy as np

if __name__ == '__main__':
    img = cv.imread("resources/lenna.png")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    edges = cv.Canny(img, 100, 200)

    plt.title("Original image:")
    plt.imshow(img)
    plt.show()

    plt.title("Edges detected with Canny:")
    plt.imshow(edges, cmap="gray")
    plt.show()