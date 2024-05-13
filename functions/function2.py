import cv2
import numpy as np

def adjust_brightness(image_path, addition_value):
    # Read the image
    image = cv2.imread(image_path)
    # Perform addition on each pixel value
    brightened_image = cv2.add(image, np.array([addition_value]))
    # save the image in the output folder
    cv2.imwrite('images/output.jpg', brightened_image)
    return

def adjust_brightness_subtract(image_path, subtraction_value):
    # Read the image
    image = cv2.imread(image_path)
    # Perform subtraction on each pixel value
    darkened_image = cv2.subtract(image, np.array([subtraction_value]))
    # save the image in the output folder
    cv2.imwrite('images/output.jpg', darkened_image)
    return


def adjust_contrast(image_path, multiplication_factor):
    # Read the image
    image = cv2.imread(image_path)
    # Perform multiplication on each pixel value
    high_contrast_image = cv2.multiply(image, np.array([multiplication_factor]))
    # save the image in the output folder
    cv2.imwrite('images/output.jpg', high_contrast_image)
    return