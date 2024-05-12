
import cv2
import numpy as np

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

# Example usage
if __name__ == "__main__":
    image_path = 'th.jpg'
    scale_x = 2
    scale_y = 1.5
    scaled_image = scale_image(image_path, scale_x, scale_y)
    # Display the original and scaled images
    cv2.imshow('Original Image', cv2.imread(image_path))
    cv2.imshow('Scaled Image', scaled_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()