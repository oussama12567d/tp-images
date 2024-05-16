import cv2
import numpy as np
from skimage.segmentation import active_contour
from skimage.segmentation import random_walker


def detect_and_draw_contours(image_path):
    # Load the image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Unable to load image.")
        return None

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray_image, threshold1=50, threshold2=150)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image
    image_with_contours = np.copy(image)
    cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)
    cv2.imwrite('images/output.jpg', image_with_contours)
    return


def segment_active_contour(image_path):
    image = cv2.imread(image_path)
    # Convert to grayscale if necessary
    if image.ndim == 3:
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        image_gray = image

    # Initialize a circle as the initial contour
    s = np.linspace(0, 2 * np.pi, 100)
    init = 50 * np.column_stack((np.cos(s), np.sin(s))) + np.array([image_gray.shape[1] // 2, image_gray.shape[0] // 2])

    # Perform active contour (snakes) segmentation
    snake = active_contour(image_gray, init, alpha=0.015, beta=10, gamma=0.001)
    cv2.imwrite('images/output.jpg', snake)
    return


def segment_random_walker(image_path):
    image = cv2.imread(image_path)
    # Choose seed points for the region growing
    seeds = np.zeros(image.shape, dtype=np.uint8)
    seeds[50, 50] = 1  # Object seed point
    seeds[100, 100] = 2  # Background seed point
    # Perform region growing using random walker algorithm
    labels = random_walker(image, seeds, mode='bf', beta=10)
    cv2.imwrite('images/output.jpg', labels)
    return



def detect_and_draw_circles(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image.")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray_image, (9, 9), 2)

    # Apply Hough Transform for circle detection
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=20,
                               param1=50, param2=30, minRadius=5, maxRadius=50)

    # Draw the circles on the original image
    image_with_circles = np.copy(image)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            center = (circle[0], circle[1])  # Circle center
            radius = circle[2]  # Circle radius
            # Draw the circle center
            cv2.circle(image_with_circles, center, 1, (0, 255, 0), 3)  # Green center
            # Draw the circle perimeter
            cv2.circle(image_with_circles, center, radius, (0, 0, 255), 3)  # Red perimeter

    cv2.imwrite('images/output.jpg', image_with_circles)
    return

