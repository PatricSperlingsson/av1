import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dct
 
#Define the residual block (smooth gradient)
residual_block = np.array([
    [0, 50, 100, 150],
    [50, 100, 150, 200],
    [100, 150, 200, 250],
    [150, 200, 250, 300],
])
 
#Apply2D DCT
transformed_block = dct(dct(residual_block.T, norm='ortho').T, norm='ortho')
 
#Visualize the residual block and transformed block
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
 
#Residual Block Visualization
im1 = ax1.imshow(residual_block, cmap='gray', interpolation='nearest')
ax1.set_title("ResidualBlock")
ax1.set_xlabel("ColumnIndex")
ax1.set_ylabel("Row Index")
ax1.set_xticks(range(residual_block.shape[1]))
ax1.set_yticks(range(residual_block.shape[0]))
plt.colorbar(im1, ax=ax1, label='Residual Value')  # Useplt.colorbar and link to the specific axis
 
# Print the numerical values of the transformed block
print("Transformed Block (DCT):")
print(transformed_block)
 
#Transformed Block Visualization
im2 = ax2.imshow(transformed_block, cmap='hot', interpolation='nearest')
ax2.set_title("Transformed Block (DCT)")
ax2.set_xlabel("ColumnIndex")
ax2.set_ylabel("Row Index")
ax2.set_xticks(range(transformed_block.shape[1]))
ax2.set_yticks(range(transformed_block.shape[0]))
plt.colorbar(im2, ax=ax2, label='Frequency Coefficients')  # Useplt.colorbar here as well
 
plt.tight_layout()
plt.show()