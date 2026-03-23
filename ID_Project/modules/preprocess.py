import cv2
import numpy as np   

def preprocess_image(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.convertScaleAbs(gray, alpha=1.5, beta=0)

    blur = cv2.GaussianBlur(gray, (3,3), 0)

    sharpen_kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    sharpen = cv2.filter2D(blur, -1, sharpen_kernel)

    return sharpen