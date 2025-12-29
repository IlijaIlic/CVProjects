import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt 
 
if __name__ == "__main__":
    img = cv.imread("./resources/baboon.png")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img_gray = cv.GaussianBlur(img_gray,(7,7),0)

    horizontal_edges = cv.Sobel(img_gray, cv.CV_64F, 1, 0, ksize=3)
    vertical_edges = cv.Sobel(img_gray, cv.CV_64F, 0, 1, ksize=3)

    horizontal_edges = cv.convertScaleAbs(horizontal_edges)
    vertical_edges = cv.convertScaleAbs(vertical_edges)

    edge_threshold = 70

    magnitude = np.sqrt(vertical_edges.astype(np.float32)**2 + horizontal_edges.astype(np.float32)**2)
    magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)

    combined_edges_img = np.where(magnitude>edge_threshold, 255,0).astype(np.uint8)
    
    plt.subplot(1,3,1)
    plt.title("Original image")
    plt.imshow(img)

    plt.subplot(1,3,2)
    plt.title("Horizontal edges detected")
    plt.imshow(horizontal_edges, cmap="gray")

    plt.subplot(1,3,3)
    plt.title("Vertical edges detected")
    plt.imshow(vertical_edges, cmap="gray")

    # FIRST WINDOW SHOW
    plt.show()
    # --------------
    
    plt.subplot(1,2,1)
    plt.title("Gradient Magnitude")
    plt.imshow(magnitude, cmap="gray")

    plt.subplot(1,2,2)
    plt.title("Combined edges - Binary")
    plt.imshow(combined_edges_img, cmap="gray")

    # SECOND WINDOW SHOW
    plt.show()