import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dct, idct
from sklearn.metrics import mean_squared_error
import heapq
import collections

# ------------------------- Huffman Coding -------------------------

class HuffmanNode:
    """Node for Huffman Tree."""
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    """Builds the Huffman tree given symbol frequencies."""
    heap = [HuffmanNode(sym, freq) for sym, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = HuffmanNode(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(heap, new_node)

    return heap[0]

def generate_huffman_codes(node, prefix="", codebook={}):
    """Generates the Huffman encoding table."""
    if node is not None:
        if node.symbol is not None:
            codebook[node.symbol] = prefix
        generate_huffman_codes(node.left, prefix + "0", codebook)
        generate_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encode(data, codebook):
    """Encodes data using Huffman coding."""
    return ''.join(codebook[sym] for sym in data.flatten())

def huffman_decode(encoded_str, root):
    """Decodes a Huffman-encoded string."""
    decoded_data = []
    node = root
    for bit in encoded_str:
        node = node.left if bit == '0' else node.right
        if node.symbol is not None:
            decoded_data.append(node.symbol)
            node = root
    return np.array(decoded_data)

# ------------------------- Block Processing -------------------------

# Define the residual block (smooth gradient)
residual_block = np.array([
    [0, 50, 100, 150],
    [50, 100, 150, 200],
    [100, 150, 200, 250],
    [150, 200, 250, 300],
])

# Define a simple DC prediction block (average value)
dc_value = 150
predicted_block = np.full_like(residual_block, dc_value)

# Calculate original block
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
quantized_block = np.round(transformed_block / quantization_matrix).astype(int)

# Huffman Encoding of Quantized Block
flat_quantized = quantized_block.flatten()
frequencies = collections.Counter(flat_quantized)
huffman_root = build_huffman_tree(frequencies)
huffman_codebook = generate_huffman_codes(huffman_root)
encoded_data = huffman_encode(quantized_block, huffman_codebook)

# Huffman Decoding
decoded_data = huffman_decode(encoded_data, huffman_root)
decoded_block = decoded_data.reshape(quantized_block.shape)

# Dequantize the block
dequantized_block = decoded_block * quantization_matrix

# Apply inverse 2D DCT
inverse_transformed_block = idct(idct(dequantized_block.T, norm='ortho').T, norm='ortho')

# Reconstruct the block
reconstructed_block = predicted_block + inverse_transformed_block

# Compute Error Metrics
mse = mean_squared_error(original_block.flatten(), reconstructed_block.flatten())
max_pixel_value = 255  # Assuming 8-bit depth
psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))

# ------------------------- Visualization -------------------------

fig, axes = plt.subplots(2, 4, figsize=(18, 10))

def show_image(ax, data, title, cmap='gray'):
    im = ax.imshow(data, cmap=cmap, interpolation='nearest')
    ax.set_title(title)
    plt.colorbar(im, ax=ax)

# Display different stages of processing
show_image(axes[0, 0], original_block, "Original Block")
show_image(axes[0, 1], predicted_block, "Predicted Block (DC Prediction)")
show_image(axes[0, 2], residual_block, "Residual Block")
show_image(axes[0, 3], transformed_block, "Transformed Block (DCT)", cmap='hot')
show_image(axes[1, 0], quantized_block, "Quantized Block", cmap='hot')
show_image(axes[1, 1], decoded_block, "Huffman Decoded Block", cmap='hot')
show_image(axes[1, 2], dequantized_block, "Dequantized Block", cmap='hot')
show_image(axes[1, 3], reconstructed_block, "Reconstructed Block")

plt.tight_layout()
plt.show()

# ------------------------- Print Results -------------------------

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

print("\nHuffman Codes for Quantized Block:")
for symbol, code in huffman_codebook.items():
    print(f"Value: {symbol}, Code: {code}")
print("Huffman Encoded Data:")
print(encoded_data)

print("\nHuffman Decoded Block:")
print(decoded_block)

print("\nDequantized Block:")
print(dequantized_block)

print("\nReconstructed Block:")
print(reconstructed_block)

print(f"\nMean Squared Error (MSE): {mse}")
print(f"Peak Signal-to-Noise Ratio (PSNR): {psnr:.2f} dB")

