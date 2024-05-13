import cv2
import numpy as np

def contrast_stretching(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Compute the minimum and maximum intensity values
    min_intensity = np.min(image)
    max_intensity = np.max(image)
    # Perform contrast stretching
    stretched_image = ((image - min_intensity) / (max_intensity - min_intensity)) * 255
    # Convert the result to 8-bit unsigned integers
    stretched_image = stretched_image.astype(np.uint8)
    cv2.imwrite('images/output.jpg', stretched_image)
    return 


def perform_spatial_convolution(image_path, value):
    kernel =  np.ones((value, value), dtype=np.float32) / 9
    # Read the image
    image = cv2.imread(image_path)
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Perform spatial convolution
    convolved_image = cv2.filter2D(gray_image, -1, kernel)
    cv2.imwrite('images/output.jpg', convolved_image)
    return



def low_pass(image_path, value = 5):
    kernel_size = (value, value)
    # Read the image
    image = cv2.imread(image_path)
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
    cv2.imwrite('images/output.jpg', blurred_image)
    return



def high_pass(image_path):
    # Read the image
    image = cv2.imread(image_path)
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Laplacian filter
    laplacian_image = cv2.Laplacian(gray_image, cv2.CV_64F)
    # Convert the result to 8-bit unsigned integers
    laplacian_image = cv2.convertScaleAbs(laplacian_image)
    cv2.imwrite('images/output.jpg', laplacian_image)
    return


def Band_pass(image_path,value = 5):
    kernel_size = (value, value)
    # Read the image
    image = cv2.imread(image_path)
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur (low-pass filter)
    blurred_image = cv2.GaussianBlur(gray_image, kernel_size, 0)
    # Apply Laplacian filter (high-pass filter)
    laplacian_image = cv2.Laplacian(blurred_image, cv2.CV_64F)
    # Combine the low-pass and high-pass filtered images
    bandpass_image = gray_image - laplacian_image
    cv2.imwrite('images/output.jpg', bandpass_image)
    return



def apply_custom_filter(image_path, value):
    custom_kernel =np.array(value)
    # Read the image
    image = cv2.imread(image_path)
    # Apply the custom filter using convolution
    filtered_image = cv2.filter2D(image, -1, custom_kernel)
    cv2.imwrite('images/output.jpg', filtered_image)
    return


def histogram_equalization(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Compute the histogram
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    # Compute the cumulative sum of the histogram values
    cdf = np.cumsum(histogram)
    # Normalize the CDF to range [0, 1]
    cdf_normalized = cdf / float(cdf.max())
    # Map pixel intensities to the normalized CDF
    mapped_image = np.interp(image.flatten(), range(256), cdf_normalized).reshape(image.shape)
    # Convert the result to 8-bit unsigned integers
    mapped_image = (mapped_image * 255).astype(np.uint8)
    cv2.imwrite('images/output.jpg', mapped_image)
    return



def equalized_image(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Compute the histogram
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    # Compute the cumulative sum of the histogram values
    cdf = np.cumsum(histogram)
    # Normalize the CDF to range [0, 1]
    cdf_normalized = cdf / float(cdf.max())
    # Map pixel intensities to the normalized CDF
    equalized_image = np.interp(image.flatten(), range(256), cdf_normalized).reshape(image.shape)
    # Convert the result to 8-bit unsigned integers
    equalized_image = (equalized_image * 255).astype(np.uint8)
    cv2.imwrite('images/output.jpg', equalized_image)
    return



def apply_gaussian_blur(image_path, value = 5):
    kernel_size = (value, value)
    # Read the image
    image = cv2.imread(image_path)
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
    cv2.imwrite('images/output.jpg', blurred_image)
    return
