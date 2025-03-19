import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dct, idct
from sklearn.metrics import mean_squared_error
from collections import Counter
import heapq

# Define the residual block (smooth gradient)
residual_block = np.array([
    [0, 50, 100, 150],
    [50, 100, 150, 200],
    [100, 150, 200, 250],
    [150, 200, 250, 300],
])

# Define a simple DC prediction block (average of all values in the original image)
dc_value = 150
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

# Huffman Encoding (for entropy coding)
def huffman_encoding(data):
    frequency = Counter(data.flatten())
    heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return dict(heap[0][1:])

huffman_codes = huffman_encoding(quantized_block)

# Dequantize the block
dequantized_block = quantized_block * quantization_matrix

# Apply inverse 2D DCT
inverse_transformed_block = idct(idct(dequantized_block.T, norm='ortho').T, norm='ortho')

# Reconstruct the block
reconstructed_block = predicted_block + inverse_transformed_block

# Calculate error metrics
mse = mean_squared_error(original_block.flatten(), reconstructed_block.flatten())
max_pixel_value = 255
psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))

# Visualization
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

axes[0, 0].imshow(original_block, cmap='gray', interpolation='nearest')
axes[0, 0].set_title("Original Block")

axes[0, 1].imshow(predicted_block, cmap='gray', interpolation='nearest')
axes[0, 1].set_title("Predicted Block (DC Prediction)")

axes[0, 2].imshow(residual_block, cmap='gray', interpolation='nearest')
axes[0, 2].set_title("Residual Block")

axes[1, 0].imshow(transformed_block, cmap='hot', interpolation='nearest')
axes[1, 0].set_title("Transformed Block (DCT)")

axes[1, 1].imshow(quantized_block, cmap='hot', interpolation='nearest')
axes[1, 1].set_title("Quantized Block")

axes[1, 2].imshow(reconstructed_block, cmap='gray', interpolation='nearest')
axes[1, 2].set_title("Reconstructed Block")

plt.tight_layout()
plt.show()

# Print Huffman codes
print("Huffman Codes for Quantized Block:")
for symbol, code in huffman_codes.items():
    print(f"Value: {symbol}, Code: {code}")

# Print error metrics
print(f"\nMean Squared Error (MSE): {mse}")
print(f"Peak Signal-to-Noise Ratio (PSNR): {psnr:.2f} dB")

