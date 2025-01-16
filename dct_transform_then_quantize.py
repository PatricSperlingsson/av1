import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dct
 
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
 
# Visualize the residual block, transformed block, and quantized block
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))
 
# Residual Block Visualization
im1 = ax1.imshow(residual_block, cmap='gray', interpolation='nearest')
ax1.set_title("ResidualBlock")
ax1.set_xlabel("ColumnIndex")
ax1.set_ylabel("Row Index")
ax1.set_xticks(range(residual_block.shape[1]))
ax1.set_yticks(range(residual_block.shape[0]))
plt.colorbar(im1, ax=ax1, label='Residual Value')  # Useplt.colorbar and link to the specific axis
 
#Transformed Block Visualization
im2 = ax2.imshow(transformed_block, cmap='hot', interpolation='nearest')
ax2.set_title("Transformed Block (DCT)")
ax2.set_xlabel("ColumnIndex")
ax2.set_ylabel("Row Index")
ax2.set_xticks(range(transformed_block.shape[1]))
ax2.set_yticks(range(transformed_block.shape[0]))
plt.colorbar(im2, ax=ax2, label='Frequency Coefficients')
 
#Quantized Block Visualization
im3 = ax3.imshow(quantized_block, cmap='hot', interpolation='nearest')
ax3.set_title("QuantizedBlock")
ax3.set_xlabel("ColumnIndex")
ax3.set_ylabel("Row Index")
ax3.set_xticks(range(quantized_block.shape[1]))
ax3.set_yticks(range(quantized_block.shape[0]))
plt.colorbar(im3, ax=ax3, label='Quantized Coefficients')
 
plt.tight_layout()
plt.show()
 
# Print the numerical values of the transformed and quantized blocks
print("Transformed Block (DCT):")
print(transformed_block)
 
print("\nQuantized Block:")
print(quantized_block)