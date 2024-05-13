import cv2
import matplotlib.pyplot as plt
import numpy as np

def apply_clahe(image_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Check if the image is loaded successfully
    if image is None:
        print("Error: Unable to load the image.")
        return None
    
    # Create a CLAHE object
    # clipLimit specifies the contrast limit, typically a value of 2.0 is good.
    # tileGridSize specifies the size of the region to perform the equalization, typically (8, 8).
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    
    # Apply CLAHE to the grayscale image
    enhanced_image = clahe.apply(image)
    cv2.imwrite('images/output.jpg', enhanced_image)
    return

def linear_contrast_stretching(image_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Check if the image is loaded successfully
    if image is None:
        print("Error: Unable to load the image.")
        return None
    
    # Get the minimum and maximum intensity values from the image
    min_intensity = np.min(image)
    max_intensity = np.max(image)
    
    # Perform linear contrast stretching
    # Map the original intensity range [min_intensity, max_intensity] to [0, 255]
    stretched_image = (image - min_intensity) * (255 / (max_intensity - min_intensity))
    stretched_image = np.clip(stretched_image, 0, 255).astype(np.uint8)
    cv2.imwrite('images/output.jpg', stretched_image)    
    return



def mean_filter(image_path, value):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    kernel_size = (value, value)
    # Apply the mean (averaging) filter using cv2.blur function
    mean_filtered_image = cv2.blur(image, kernel_size)
    cv2.imwrite('images/output.jpg', mean_filtered_image)
    return


def median_filter(image_path, kernel_size):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Apply the median filter using cv2.medianBlur function
    median_filtered_image = cv2.medianBlur(image, kernel_size)
    cv2.imwrite('images/output.jpg', median_filtered_image)
    return


def bilateral_filter(image_path, d, sigmaColor, sigmaSpace):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Apply the bilateral filter using cv2.bilateralFilter function
    bilateral_filtered_image = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
    cv2.imwrite('images/output.jpg', bilateral_filtered_image)
    return


def unsharp_masking(image_path, amount=1.5, radius=5):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Create a Gaussian blurred version of the image
    blurred_image = cv2.GaussianBlur(image, (0, 0), radius)
    # Calculate the mask by subtracting the blurred image from the original image
    mask = cv2.subtract(image, blurred_image)
    # Multiply the mask by the amount
    mask = cv2.multiply(mask, np.array([amount]))
    # Add the mask back to the original image
    sharpened_image = cv2.add(image, mask)
    cv2.imwrite('images/output.jpg', sharpened_image)
    return


# White balance adjustment (Gray world algorithm)
def adjust_white_balance(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    result = image.copy()
    avg_bgr = cv2.mean(result)[:3]
    avg_gray = np.mean(avg_bgr)
    scale_factors = avg_gray / np.array(avg_bgr)
    for i in range(3):
        result[:, :, i] = np.clip(result[:, :, i] * scale_factors[i], 0, 255)
    cv2.imwrite('images/output.jpg', result)
    return





def add_gaussian_noise(image_path, mean=0, stddev=20):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    noise = np.random.normal(mean, stddev, image.shape)
    noisy_image = image + noise
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    cv2.imwrite('images/output.jpg', noisy_image)
    return


def apply_gaussian_blur(image_path, ksize=5):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred_image = cv2.GaussianBlur(img, (ksize, ksize), 0)
    cv2.imwrite('images/output.jpg', blurred_image)
    return


def downsample(image_path, scale=2):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    downscaled_image = cv2.resize(img, None, fx=1/scale, fy=1/scale, interpolation=cv2.INTER_LINEAR)
    cv2.imwrite('images/output.jpg', downscaled_image)
    return