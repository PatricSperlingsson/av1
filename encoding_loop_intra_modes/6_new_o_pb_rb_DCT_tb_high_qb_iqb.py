import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dct, idct
from skimage.metrics import mean_squared_error, peak_signal_noise_ratio, structural_similarity
 
# Define the original image block (smooth gradient with only the bottom right corner as white)
original_block = np.array([
    [0,  64, 128, 192],
    [64, 85, 149, 213],
    [128, 149, 170, 234],
    [192, 213, 234, 255]
])
 
# Define the residual block (original image minus the DC prediction block)
dc_value = np.mean(original_block)  # Calculate the average value of the original image
predicted_block = np.full_like(original_block, dc_value)
residual_block = original_block - predicted_block
 
# Apply 2D DCT
transformed_block = dct(dct(residual_block.T, norm='ortho').T, norm='ortho')
 
# Define the Quantization matrix
#quantization_matrix = np.array([
#    [16, 11, 10, 16],
#    [12, 12, 14, 19],
#    [14, 13, 16, 24],
#    [14, 17, 22, 29]
#])

# Symmetric
quantization_matrix = np.array([
   [16, 12, 14, 14],
   [12, 16, 13, 17],
   [14, 13, 16, 22],
   [14, 17, 22, 29]
])

# Refined Quantization matrix
# Less compression for better MSE, SSIM and PSNR:
# quantization_matrix = np.array([
#     [8, 6, 7, 8],
#     [6, 7, 8, 10],
#     [7, 8, 10, 13],
#     [8, 10, 13, 16]
# ])

# Apply quantization
quantized_block = np.round(transformed_block / quantization_matrix)
 
# Dequantize the block
dequantized_block = quantized_block * quantization_matrix
 
# Apply inverse 2D DCT
inverse_transformed_block = idct(idct(dequantized_block.T, norm='ortho').T, norm='ortho')
 
# Reconstruct the block
reconstructed_block = predicted_block + inverse_transformed_block
 
# Calculate MSE, PSNR, and SSIM
mse = mean_squared_error(original_block, reconstructed_block)
psnr = peak_signal_noise_ratio(original_block, reconstructed_block, data_range=original_block.max() - original_block.min())
ssim = structural_similarity(original_block, reconstructed_block, data_range=original_block.max() - original_block.min(), win_size=3)
 
# Visualization
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(20, 4))
 
# Original Block Visualization
#im1 = axes[0, 0].imshow(original_block, cmap='gray', interpolation='nearest')
#axes[0, 0].set_title("Original Block")
#plt.colorbar(im1, ax=axes[0, 0], label='Pixel Value')
 
# Predicted Block Visualization
#im2 = axes[0, 1].imshow(predicted_block, cmap='gray', interpolation='nearest')
#axes[0, 1].set_title("Predicted Block (DC Prediction)")
#plt.colorbar(im2, ax=axes[0, 1], label='Predicted Value')
 
# Residual Block Visualization
im3 = ax1.imshow(residual_block, cmap='gray', interpolation='nearest')
ax1.set_title("Residual Block")
ax1.set_xticks(range(residual_block.shape[1]))
ax1.set_yticks(range(residual_block.shape[0]))
plt.colorbar(im3, ax=ax1, label='Residual Value')
 
# Transformed Block Visualization
im4 = ax2.imshow(transformed_block, cmap='hot', interpolation='nearest')
ax2.set_title("Transformed Block (DCT)")
ax2.set_xticks(range(transformed_block.shape[1]))
ax2.set_yticks(range(transformed_block.shape[0]))
plt.colorbar(im4, ax=ax2, label='Frequency Coefficients')
 
# Quantized Block Visualization
im5 = ax3.imshow(quantized_block, cmap='hot', interpolation='nearest')
ax3.set_title("Quantized Block")
ax3.set_xticks(range(quantized_block.shape[1]))
ax3.set_yticks(range(quantized_block.shape[0]))
plt.colorbar(im5, ax=ax3, label='Quantized Coefficients')

# Dequantized Block Visualization
im6 = ax4.imshow(dequantized_block, cmap='hot', interpolation='nearest')
ax4.set_title("Dequantized Block")
ax4.set_xticks(range(dequantized_block.shape[1]))
ax4.set_yticks(range(dequantized_block.shape[0]))
plt.colorbar(im6, ax=ax4, label='Dequantized Coefficients')

# # Inverse Transform Block Visualization
# im7 = ax5.imshow(inverse_transformed_block, cmap='gray', interpolation='nearest')
# ax5.set_title("Inverse Transform Block")
# ax5.set_xticks(range(inverse_transformed_block.shape[1]))
# ax5.set_yticks(range(inverse_transformed_block.shape[0]))
# plt.colorbar(im7, ax=ax5, label='Residual Value')
 
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
 
print("\nDequantized Block (Reconstructed Transformed Block):")
print(dequantized_block)
 
print("\nInverse Transformed Block (Reconstructed Residual Block):")
print(inverse_transformed_block)
 
print("\nReconstructed Block:")
print(reconstructed_block)
 
# Print MSE, PSNR and SSIM
print(f"\nMSE: {mse:.4f}")
print(f"PSNR: {psnr:.2f} dB")
print(f"SSIM: {ssim:.4f}")
