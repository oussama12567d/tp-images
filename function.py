
import cv2
import numpy as np
import matplotlib.pyplot as plt


def rotate_image(image_path, angle):
    # Read the image
    image = cv2.imread(image_path)
    # Compute the rotation matrix
    center = (image.shape[1] // 2, image.shape[0] // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    # Apply the rotation
    rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
    # savae the image in the output folder
    cv2.imwrite('images/output.jpg', rotated_image)
    return 




#############################################################################""

def scale_image(image_path, scale_x, scale_y):
    # Read the image
    image = cv2.imread(image_path)
    # Compute the scaling matrix
    scaling_matrix = np.float32([[scale_x, 0, 0],
                                  [0, scale_y, 0]])
    # Apply the scaling
    scaled_image = cv2.warpAffine(image, scaling_matrix, 
                                   (int(image.shape[1] * scale_x), int(image.shape[0] * scale_y)))
    # save the image in the output folder
    cv2.imwrite('images/output.jpg', scaled_image)
    return

#############################################################################

def translate_image(image_path, tx, ty):
    # Read the image
    image = cv2.imread(image_path)
    # Define the translation matrix
    translation_matrix = np.float32([[1, 0, tx],
                                     [0, 1, ty]])
    # Apply the translation
    translated_image = cv2.warpAffine(image, translation_matrix,
                                      (image.shape[1], image.shape[0]))
    
    # save the image in the output folder
    cv2.imwrite('images/output.jpg', translated_image)
    return

##############################################################################


def horizontal_reflection(image_path):
    # Read the image
    image = cv2.imread(image_path)
    # Perform horizontal reflection (vertical flipping)
    reflected_image = cv2.flip(image, 0)
    # save the image in the output folder
    cv2.imwrite('images/output.jpg', reflected_image)
    return


#############################################################################

def affine_transform(image_path, scale_x, scale_y, shear_x, shear_y, translation_x, translation_y):
    # Read the image
    image = cv2.imread(image_path)
    # Compute the affine transformation matrix
    affine_matrix = np.float32([[scale_x, shear_x, translation_x],
                                [shear_y, scale_y, translation_y]])
    # Apply the affine transformation
    affine_image = cv2.warpAffine(image, affine_matrix, (image.shape[1], image.shape[0]))
    # save the image in the output folder
    cv2.imwrite('images/output.jpg', affine_image)
    return

#############################################################################


def adjust_brightness(image_path, addition_value):
    # Read the image
    image = cv2.imread(image_path)
    # Perform addition on each pixel value
    brightened_image = cv2.add(image, np.array([addition_value]))
    # save the image in the output folder
    cv2.imwrite('images/output.jpg', brightened_image)
    return


###############################################################################


def adjust_brightness_subtract(image_path, subtraction_value):
    # Read the image
    image = cv2.imread(image_path)
    # Perform subtraction on each pixel value
    darkened_image = cv2.subtract(image, np.array([subtraction_value]))
    # save the image in the output folder
    cv2.imwrite('images/output.jpg', darkened_image)
    return

#############################################################################


def adjust_contrast(image_path, multiplication_factor):
    # Read the image
    image = cv2.imread(image_path)
    # Perform multiplication on each pixel value
    high_contrast_image = cv2.multiply(image, np.array([multiplication_factor]))
    cv2.imwrite('images/output.jpg', high_contrast_image)
    return

#############################################################################


def bitwise_and_images(image_path1, image_path2):
    # Read the images
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    # Check if images are loaded successfully
    if image1 is None or image2 is None:
        print("Error: Unable to load images.")
        return None

    # Resize image2 to match the dimensions of image1
    image2_resized = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    # Perform bitwise AND operation
    bitwise_and_image = cv2.bitwise_and(image1, image2_resized)
    cv2.imwrite('images/output.jpg', bitwise_and_image)
    return



#############################################################################



def apply_thresholding(image_path, threshold_value):
    # Read the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Apply thresholding
    _, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    cv2.imwrite('images/output.jpg', thresholded_image)
    return


#############################################################################


def apply_gaussian_blur(image_path):
    kernel_size=(5, 5)
    # Read the image
    image = cv2.imread(image_path)
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
    cv2.imwrite('images/output.jpg', blurred_image)
    return


#############################################################################


def apply_laplacian_filter(image_path):
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


#############################################################################



def apply_sobel_filter(image_path):
    # Read the image
    image = cv2.imread(image_path)
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Sobel filter for horizontal edges
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    # Apply Sobel filter for vertical edges
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    # Combine the horizontal and vertical edge images
    sobel_image = cv2.magnitude(sobel_x, sobel_y)
    # Convert the result to 8-bit unsigned integers
    sobel_image = cv2.convertScaleAbs(sobel_image)
    cv2.imwrite('images/output.jpg', sobel_image)
    return



#############################################################################



def apply_bandpass_filter(image_path):
    kernel_size=(5, 5)
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


#############################################################################


def apply_custom_filter(image_path, custom_kernel):
    # Read the image
    image = cv2.imread(image_path)
    # Apply the custom filter using convolution
    filtered_image = cv2.filter2D(image, -1, custom_kernel)
    cv2.imwrite('images/output.jpg', filtered_image)
    return




#############################################################################

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


#############################################################################

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


#############################################################################

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


#############################################################################

def histogram_equalization_opencv(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Apply histogram equalization
    equalized_image = cv2.equalizeHist(image)
    #save the image
    cv2.imwrite('images/output.jpg', equalized_image)
    return

