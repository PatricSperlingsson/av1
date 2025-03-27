import cv2

# Load the combined image
combined_image_path = "original_and_quantized_image.png"
combined_image = cv2.imread(combined_image_path, cv2.IMREAD_GRAYSCALE)

# Get the dimensions of the image
height, width = combined_image.shape

# Adjust the boundaries for accurate splitting
midpoint = width // 2
left_margin = 3
right_margin = 9
split_width = midpoint - left_margin - right_margin

# Split the image into left (original) and right (quantized) parts
original_image = combined_image[:, left_margin:midpoint - right_margin]
quantized_image = combined_image[:, midpoint + right_margin:midpoint + right_margin + split_width]

# Save the split images
original_image_path = "original_image.png"
quantized_image_path = "quantized_image.png"
cv2.imwrite(original_image_path, original_image)
cv2.imwrite(quantized_image_path, quantized_image)

# Display the paths to the saved images
original_image_path, quantized_image_path
