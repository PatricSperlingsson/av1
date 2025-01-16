import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dct, idct

# Define the residual block (smooth gradient)
residual_block = np.array([
    [0, 50, 100, 150],
    [50, 100, 150, 200],
    [100, 150, 200, 250],
    [150, 200, 250, 300],
])
  
# Apply 2D DCT
transformed_block = dct(dct(residual_block.T, norm='ortho').T, norm='ortho')

# Define a quantization matrix (for demonstration, we can use a simple one)
quantization_matrix = np.array([
    [16, 11, 10, 16],
    [12, 12, 14, 19],
    [14, 13, 16, 24],
    [14, 17, 22, 29]
])

# Apply quantization (divide transformed coefficients by quantization matrix values)
quantized_block = np.round(transformed_block / quantization_matrix)

# Dequantization step (multiply quantized coefficients by quantization matrix values)
dequantized_block = quantized_block * quantization_matrix

# Apply inverse 2D DCT to reconstruct the residual block
inverse_transformed_block = idct(idct(dequantized_block.T, norm='ortho').T, norm='ortho')

# Visualize all steps: residual block, transformed block, quantized block, dequantized block, and reconstructed block
fig, axs = plt.subplots(1, 5, figsize=(30, 6))

# Residual Block Visualization
im1 = axs[0].imshow(residual_block, cmap='gray', interpolation='nearest')
axs[0].set_title("Residual Block")
axs[0].set_xlabel("Column Index")
axs[0].set_ylabel("Row Index")
axs[0].set_xticks(range(residual_block.shape[1]))
axs[0].set_yticks(range(residual_block.shape[0]))
plt.colorbar(im1, ax=axs[0], label='Residual Value')

# Transformed Block Visualization
im2 = axs[1].imshow(transformed_block, cmap='hot', interpolation='nearest')
axs[1].set_title("Transformed Block (DCT)")
axs[1].set_xlabel("Column Index")
axs[1].set_ylabel("Row Index")
axs[1].set_xticks(range(transformed_block.shape[1]))
axs[1].set_yticks(range(transformed_block.shape[0]))
plt.colorbar(im2, ax=axs[1], label='Frequency Coefficients')

# Quantized Block Visualization
im3 = axs[2].imshow(quantized_block, cmap='hot', interpolation='nearest')
axs[2].set_title("Quantized Block")
axs[2].set_xlabel("Column Index")
axs[2].set_ylabel("Row Index")
axs[2].set_xticks(range(quantized_block.shape[1]))
axs[2].set_yticks(range(quantized_block.shape[0]))
plt.colorbar(im3, ax=axs[2], label='Quantized Coefficients')

# Dequantized Block Visualization
im4 = axs[3].imshow(dequantized_block, cmap='hot', interpolation='nearest')
axs[3].set_title("Dequantized Block")
axs[3].set_xlabel("Column Index")
axs[3].set_ylabel("Row Index")
axs[3].set_xticks(range(dequantized_block.shape[1]))
axs[3].set_yticks(range(dequantized_block.shape[0]))
plt.colorbar(im4, ax=axs[3], label='Dequantized Coefficients')

# Reconstructed Block Visualization
im5 = axs[4].imshow(inverse_transformed_block, cmap='gray', interpolation='nearest')
axs[4].set_title("Reconstructed Block")
axs[4].set_xlabel("Column Index")
axs[4].set_ylabel("Row Index")
axs[4].set_xticks(range(inverse_transformed_block.shape[1]))
axs[4].set_yticks(range(inverse_transformed_block.shape[0]))
plt.colorbar(im5, ax=axs[4], label='Reconstructed Value')

plt.tight_layout()
plt.show()

# Print the numerical values of each step
print("Residual Block:")
print(residual_block)

print("\nTransformed Block (DCT):")
print(transformed_block)

print("\nQuantized Block:")
print(quantized_block)

print("\nDequantized Block:")
print(dequantized_block)

print("\nInverse Transformed Block (Reconstructed Residuals):")
print(inverse_transformed_block)
