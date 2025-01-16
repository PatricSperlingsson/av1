import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dct

# Define the identity transform (the output will be the same as the input)
def identity_transform(block):
    """Returns the same block (identity transform)."""
    return block

# Define the input block (uniform block)
input_block = np.array([
    [100, 100, 100, 100],
    [100, 100, 100, 100],
    [100, 100, 100, 100],
    [100, 100, 100, 100],
])

# Apply identity transform
output_block = identity_transform(input_block)

# Print the numerical values of the input and output block
print("Transformed Block (Identity Transform):")
print(output_block)

# Visualize the input and output block
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Input Block Visualization
im1 = ax1.imshow(input_block, cmap='gray', interpolation='nearest')
ax1.set_title("Input Block")
ax1.set_xlabel("Column Index")
ax1.set_ylabel("Row Index")
ax1.set_xticks(range(input_block.shape[1]))
ax1.set_yticks(range(input_block.shape[0]))
plt.colorbar(im1, ax=ax1, label='Block Value')  # Use plt.colorbar and link to the specific axis

# Output Block Visualization
im2 = ax2.imshow(output_block, cmap='gray', interpolation='nearest')
ax2.set_title("Output Block (Identity Transform)")
ax2.set_xlabel("Column Index")
ax2.set_ylabel("Row Index")
ax2.set_xticks(range(output_block.shape[1]))
ax2.set_yticks(range(output_block.shape[0]))
plt.colorbar(im2, ax=ax2, label='Block Value')

plt.tight_layout()
plt.show()
