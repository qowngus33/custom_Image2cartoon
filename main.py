import cv2 as cv
import numpy as np

morph_operations = [
    {'name': 'Erode',     'operation': cv.MORPH_ERODE},  # Alternative) cv.erode()
    {'name': 'Dilate',    'operation': cv.MORPH_DILATE}, # Alternative) cv.dilate()
    {'name': 'Open',      'operation': cv.MORPH_OPEN},
    {'name': 'Close',     'operation': cv.MORPH_CLOSE},
]

kernel_tables = [
    {'name': '3x3 Box',   'kenerl': np.ones((3, 3), dtype=np.uint8)},
    {'name': '5x5 Box',   'kenerl': np.ones((5, 5), dtype=np.uint8)},
    {'name': '5x1 Bar',   'kernel': np.ones((10, 1), dtype=np.uint8)},
    {'name': '1x5 Bar',   'kernel': np.ones((1, 10), dtype=np.uint8)},
    {'name': '5x5 Cross', 'kernel': np.array([[0,0,1,0,0], [0,0,1,0,0], [1,1,1,1,1], [0,0,1,0,0], [0,0,1,0,0]], dtype=np.uint8)},
]

def cartoonize_image(image):
    # Convert image to grayscale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Apply median blur to reduce noise
    # gray = cv.medianBlur(gray, 5)

    # Detect edges using adaptive thresholding
    # edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)
    # edges = cv.Laplacian(gray, cv.CV_8U, ksize=5)
    edges = cv.Canny(gray, 500, 700, apertureSize=5)

    edges = ~edges
    k_name, kernel = kernel_tables[2].values()
    m_name, operation = morph_operations[2].values()
    edges = cv.morphologyEx(edges, operation, kernel, iterations=1)
    # edges = cv.bilateralFilter(edges, 9, 300, 300)

    # Apply bilateral filter to smoothen the image while preserving edges
    # for i in range(5):
    #     image = cv.bilateralFilter(image, 9, 300, 300)

    # Combine edges and color image using bitwise_and
    cartoon = cv.bitwise_and(image, image, mask=edges)

    return cartoon


# Load the image
# image = cv.imread('image/IMG_4303.JPG')
image = cv.imread('image/new_world2.png')

# Apply cartoonize function
cartoon_image = cartoonize_image(image)

# Concatenate original and cartoonized images horizontally
output_image = cv.hconcat([image, cartoon_image])

# Display the concatenated image
cv.imshow('Original vs Cartoonized', output_image)

cv.waitKey(0)
cv.destroyAllWindows()
