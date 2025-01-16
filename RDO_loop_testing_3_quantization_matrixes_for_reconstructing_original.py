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

# Define the predicted block (DC Prediction)
dc_value = 150  # Ensuring the predicted block matches the residuals
predicted_block = np.full_like(residual_block, dc_value)

# Original block (before compression)
original_block = predicted_block + residual_block

# Define a simple quantization matrix for testing (e.g., different quantization matrices for RDO)
quantization_matrices = [
    np.array([
        [16, 11, 10, 16],
        [12, 12, 14, 19],
        [14, 13, 16, 24],
        [14, 17, 22, 29]
    ]),
    np.array([
        [10, 7, 6, 10],
        [8, 8, 9, 13],
        [9, 8, 10, 16],
        [9, 11, 14, 19]
    ]),
    np.array([
        [20, 14, 12, 20],
        [16, 16, 18, 25],
        [18, 16, 20, 30],
        [18, 22, 28, 38]
    ])
]

# Initialize variables for the best RDO cost
best_rd_cost = float('inf')
best_quantization_matrix = None
best_quantized_block = None
best_reconstructed_block = None

# Lambda factor for controlling the balance between rate and distortion
lambda_factor = 0.1

# Try each quantization matrix and calculate its RDO cost
for q_matrix in quantization_matrices:
    # Apply DCT on residual block
    transformed_block = dct(dct(residual_block.T, norm='ortho').T, norm='ortho')

    # Quantize the transformed block
    quantized_block = np.round(transformed_block / q_matrix)

    # Dequantize the block
    dequantized_block = quantized_block * q_matrix

    # Apply inverse DCT
    inverse_transformed_block = idct(idct(dequantized_block.T, norm='ortho').T, norm='ortho')

    # Reconstruct the block
    reconstructed_block = predicted_block + inverse_transformed_block

    # Calculate the distortion (MSE)
    distortion = np.mean((original_block - reconstructed_block) ** 2)

    # Calculate the rate (count the non-zero quantized coefficients)
    rate = np.count_nonzero(quantized_block)

    # Calculate the RDO cost
    rd_cost = distortion + lambda_factor * rate

    # Update the best RDO if the current one is better
    if rd_cost < best_rd_cost:
        best_rd_cost = rd_cost
        best_quantization_matrix = q_matrix
        best_quantized_block = quantized_block
        best_reconstructed_block = reconstructed_block

# Visualize the best RDO outcome
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Best Quantized Block Visualization
im1 = axes[0].imshow(best_quantized_block, cmap='hot', interpolation='nearest')
axes[0].set_title("Best Quantized Block")
plt.colorbar(im1, ax=axes[0], label='Quantized Coefficients')

# Best Reconstructed Block Visualization
im2 = axes[1].imshow(best_reconstructed_block, cmap='gray', interpolation='nearest')
axes[1].set_title("Best Reconstructed Block")
plt.colorbar(im2, ax=axes[1], label='Pixel Value')

# Original Block Visualization
im3 = axes[2].imshow(original_block, cmap='gray', interpolation='nearest')
axes[2].set_title("Original Block")
plt.colorbar(im3, ax=axes[2], label='Pixel Value')

plt.tight_layout()
plt.show()

# Print the best RDO cost and the best quantization matrix
print(f"Best RDO Cost: {best_rd_cost}")
print(f"Best Quantization Matrix:")
print(best_quantization_matrix)
