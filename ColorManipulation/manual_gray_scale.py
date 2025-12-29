import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

if __name__ == "__main__":
    img = cv.imread("../resources/lenna.png")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    img_cv_grayscale = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    imgH, imgW, channels = img.shape
    print(imgH)
    print(imgW)

    img_manual_grayscale = np.zeros((imgH, imgW, 1), dtype=np.uint8)
 
    grayscale_formula = [0.299, 0.587, 0.144]
    img_manual_grayscale = np.dot(img, grayscale_formula)

    plt.subplot(1,3,1)
    plt.title("Original image")
    plt.imshow(img)

    plt.subplot(1,3,2)
    plt.title("OpenCV GrayScale image")
    plt.imshow(img_cv_grayscale, cmap="gray")

    plt.subplot(1,3,3)
    plt.title("Manual GrayScale image")
    plt.imshow(img_manual_grayscale, cmap="gray")

    plt.show()