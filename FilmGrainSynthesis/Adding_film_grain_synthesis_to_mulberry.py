import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'mulberry.jpg'
image = cv2.imread(image_path)

# Check if the image was successfully loaded
if image is None:
    print(f"Error: Unable to load image from {image_path}")
else:
    # Convert the image from BGR (OpenCV default) to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Apply Non-Local Means Denoising
    denoised_image = cv2.fastNlMeansDenoisingColored(image_rgb, None, h=10, templateWindowSize=7, searchWindowSize=21)

    # # Function to add synthetic film grain
    # def add_film_grain(image, intensity=0.05):
    #     row, col, ch = image.shape
    #     mean = 0
    #     sigma = intensity * 255  # Standard deviation scaled by intensity
    #     gauss = np.random.normal(mean, sigma, (row, col, 1)).astype('uint8')
    #     gauss = np.repeat(gauss, ch, axis=2)  # Repeat the noise across all color channels
    #     noisy_image = cv2.addWeighted(image, 1.0, gauss, 0.2, 0)
    #     return noisy_image

    def add_film_grain(image, intensity):
        row, col, ch = image.shape
        mean = 0
        sigma = intensity * 9  # Standard deviation scaled by intensity
        gauss = np.random.normal(mean, sigma, (row, col, 1)).astype('uint8')
        gauss = np.repeat(gauss, ch, axis=2)  # Repeat the noise across all color channels
        noisy_image = cv2.addWeighted(image, 1.0, gauss, 0.2, 0)
        return noisy_image

    # Add synthetic film grain to the denoised image
    synthesized_grain_image = add_film_grain(denoised_image, intensity=0.1)

    # Display the original, denoised, and synthesized grain images side by side
    plt.figure(figsize=(18, 6))

    # Original image
    plt.subplot(1, 3, 1)
    plt.title('Original Image with Film Grain')
    plt.imshow(image_rgb)
    plt.axis('off')

    # Denoised image
    plt.subplot(1, 3, 2)
    plt.title('Denoised Image')
    plt.imshow(denoised_image)
    plt.axis('off')

    # Synthesized grain image
    plt.subplot(1, 3, 3)
    plt.title('Reconstructed Image with Synthesized Grain')
    plt.imshow(synthesized_grain_image)
    plt.axis('off')

    plt.show()
