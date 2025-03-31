import numpy as np
import matplotlib.pyplot as plt
 
#Define the ADST for 1D
def adst_1d(vector):
    """Applies the 1D Asymmetric Discrete SineTransform."""
    N = len(vector)
    result = np.zeros(N)
    for k in range(N):
        result[k] = sum(vector[n] * np.sin((np.pi * (n + 1) * (k + 1)) / (N + 1)) for n in range(N))
    return result
 
#Define the 2D ADST
def adst_2d(block):
    """Applies the 2D Asymmetric Discrete SineTransform."""
    # Apply ADST to rows
    transformed = np.apply_along_axis(adst_1d, axis=1, arr=block)
    # Apply ADST to columns
    transformed = np.apply_along_axis(adst_1d, axis=0, arr=transformed)
    return transformed
 
#Define the residual block (sharpedge)
residual_block = np.array([
    [30, 30, 30, 30],
    [10, 10, 10, 10],
    [10, 10, 10, 10],
    [10, 10, 10, 10]
])
 
#Apply2D ADST
transformed_block_adst = adst_2d(residual_block)
 
# Print the numerical values of the transformed block
print("Transformed Block (ADST):")
print(transformed_block_adst)
 
#Visualize the Residual Block and Transformed Block (ADST)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
 
#Residual Block Visualization
im1 = ax1.imshow(residual_block, cmap='gray', interpolation='nearest')
ax1.set_title("Residual Block (Input)")
ax1.set_xlabel("ColumnIndex")
ax1.set_ylabel("Row Index")
ax1.set_xticks(range(residual_block.shape[1]))
ax1.set_yticks(range(residual_block.shape[0]))
plt.colorbar(im1, ax=ax1, label='Residual Value')
 
#Transformed Block Visualization (ADST)
im2 = ax2.imshow(transformed_block_adst, cmap='hot', interpolation='nearest')
ax2.set_title("Transformed Block (ADST)")
ax2.set_xlabel("ColumnIndex")
ax2.set_ylabel("Row Index")
ax2.set_xticks(range(transformed_block_adst.shape[1]))
ax2.set_yticks(range(transformed_block_adst.shape[0]))
plt.colorbar(im2, ax=ax2, label='Frequency Coefficients')
 
plt.tight_layout()
plt.show()