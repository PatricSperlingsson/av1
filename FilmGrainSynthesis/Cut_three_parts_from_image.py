import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'film_grain_synthesis.png'
image = cv2.imread(image_path)

# Check if the image was successfully loaded
if image is None:
    print(f"Error: Unable to load image from {image_path}")
else:
    # Convert the image from BGR (OpenCV default) to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the positions and size for the sections to be extracted
    positions = [(500, 190), (1209, 190), (1918, 190)]
    section_size_x = 50
    section_size_y = 30

    # Extract the sections
    sections = []
    for (x, y) in positions:
        section = image_rgb[y:y+section_size_y, x:x+section_size_x]
        sections.append(section)

    # Display the sections side by side
    plt.figure(figsize=(15, 5))

    for i, section in enumerate(sections):
        plt.subplot(1, 3, i+1)
        plt.imshow(section)
        plt.axis('off')

    plt.show()
