import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dct, idct
from sklearn.metrics import mean_squared_error

# Define the residual block (smooth gradient)
residual_block = np.array([
    [0, 50, 100, 150],
    [50, 100, 150, 200],
    [100, 150, 200, 250],
    [150, 200, 250, 300],
])

# Define a simple DC prediction block (average of all values in the original image)
dc_value = 150  # This ensures that the prediction block + residuals match the original
predicted_block = np.full_like(residual_block, dc_value)

# Calculate the original block for verification
original_block = predicted_block + residual_block

# Apply 2D DCT
transformed_block = dct(dct(residual_block.T, norm='ortho').T, norm='ortho')

# Define a quantization matrix (example)
quantization_matrix = np.array([
    [16, 11, 10, 16],
    [12, 12, 14, 19],
    [14, 13, 16, 24],
    [14, 17, 22, 29]
])

# Apply quantization
quantized_block = np.round(transformed_block / quantization_matrix)

# Dequantize the block
dequantized_block = quantized_block * quantization_matrix

# Apply inverse 2D DCT
inverse_transformed_block = idct(idct(dequantized_block.T, norm='ortho').T, norm='ortho')

# Reconstruct the block
reconstructed_block = predicted_block + inverse_transformed_block

# Calculate error metrics
mse = mean_squared_error(original_block.flatten(), reconstructed_block.flatten())
max_pixel_value = 255  # Assuming 8-bit depth
psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))

# Visualization
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Original Block Visualization
im1 = axes[0, 0].imshow(original_block, cmap='gray', interpolation='nearest')
axes[0, 0].set_title("Original Block")
plt.colorbar(im1, ax=axes[0, 0], label='Pixel Value')

# Predicted Block Visualization
im2 = axes[0, 1].imshow(predicted_block, cmap='gray', interpolation='nearest')
axes[0, 1].set_title("Predicted Block (DC Prediction)")
plt.colorbar(im2, ax=axes[0, 1], label='Predicted Value')

# Residual Block Visualization
im3 = axes[0, 2].imshow(residual_block, cmap='gray', interpolation='nearest')
axes[0, 2].set_title("Residual Block")
plt.colorbar(im3, ax=axes[0, 2], label='Residual Value')

# Transformed Block Visualization
im4 = axes[1, 0].imshow(transformed_block, cmap='hot', interpolation='nearest')
axes[1, 0].set_title("Transformed Block (DCT)")
plt.colorbar(im4, ax=axes[1, 0], label='Frequency Coefficients')

# Quantized Block Visualization
im5 = axes[1, 1].imshow(quantized_block, cmap='hot', interpolation='nearest')
axes[1, 1].set_title("Quantized Block")
plt.colorbar(im5, ax=axes[1, 1], label='Quantized Coefficients')

# Reconstructed Block Visualization
im6 = axes[1, 2].imshow(reconstructed_block, cmap='gray', interpolation='nearest')
axes[1, 2].set_title("Reconstructed Block")
plt.colorbar(im6, ax=axes[1, 2], label='Pixel Value')

plt.tight_layout()
plt.show()

# Print numerical values for debugging and verification
print("Original Block:")
print(original_block)

print("\nPredicted Block:")
print(predicted_block)

print("\nResidual Block:")
print(residual_block)

print("\nTransformed Block (DCT):")
print(transformed_block)

print("\nQuantized Block:")
print(quantized_block)

print("\nDequantized Block:")
print(dequantized_block)

print("\nInverse Transformed Block (Reconstructed Residuals):")
print(inverse_transformed_block)

print("\nReconstructed Block:")
print(reconstructed_block)

# Print error metrics
print(f"\nMean Squared Error (MSE): {mse}")
print(f"Peak Signal-to-Noise Ratio (PSNR): {psnr:.2f} dB")
