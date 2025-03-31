import numpy as np

# Define the quantized block
quantized_block = np.array([
    [  0, -32,   3,  -2],
    [-32, -10,   0,   0],
    [  3,   0,  -2,   0],
    [ -2,   0,   0,  -1]
])

print(f"\nOriginal block:\n{quantized_block}")

# Flatten the block and count symbol frequencies
flat_block = quantized_block.flatten()
unique, counts = np.unique(flat_block, return_counts=True)
symbol_counts = dict(zip(unique, counts))




# ---- CDF Probability Table ----
# Create a CDF table with probability ranges
def create_cdf(symbol_counts):
    """Creates a real CDF table with [low, high) probability ranges."""
    sorted_symbols = sorted(symbol_counts.keys(), key=lambda s: symbol_counts[s])  # Sort by frequency
    total = sum(symbol_counts.values())  # Total occurrences
    
    cdf_table = {}
    lower_bounds = []
    upper_bounds = []
    cumulative = 0

    print("\nCDF Table (Symbol -> Range):")
    for symbol in sorted_symbols:
        lower = cumulative / total
        cumulative += symbol_counts[symbol]
        upper = cumulative / total
        
        cdf_table[symbol] = (lower, upper)
        lower_bounds.append(lower)
        upper_bounds.append(upper)

        print(f"  Symbol: {symbol:3}  |  Range: [{lower:.6f}, {upper:.6f})")

    return cdf_table, sorted_symbols, lower_bounds, upper_bounds

# Generate the CDF table
cdf_table, sorted_symbols, lower_bounds, upper_bounds = create_cdf(symbol_counts)





# ---- CDF ENCODING ----
# Start encoding using range multiplication
low, high = 0.0, 1.0  # Initial range

for symbol in flat_block:
    symbol_low, symbol_high = cdf_table[symbol]  # Get symbol's range
    range_size = high - low  # Current range size

    # Apply range multiplication
    high = low + range_size * symbol_high
    low = low + range_size * symbol_low

# Store the final encoded value (a number between [low, high))
encoded_value = (low + high) / 2  # Midpoint of the range

print(f"\nFinal encoded range: [{low:.12f}, {high:.12f})")
print(f"\nEncoded value: {encoded_value:.12f}")

# ---- CDF DECODING ----
decoded_block = []
decoded_value = encoded_value  # Start decoding with encoded value
low, high = 0.0, 1.0  # Reset initial range

for _ in range(flat_block.size):
    # Find which symbol corresponds to the current state
    range_size = high - low
    target = (decoded_value - low) / range_size  # Normalize within [0,1)

    symbol_index = None
    for i, (l, h) in enumerate(zip(lower_bounds, upper_bounds)):
        if l <= target < h:
            symbol_index = i
            break

    if symbol_index is None:
        raise ValueError(f"Decoding error: No symbol found for target {target}")

    # Get the actual symbol
    symbol = sorted_symbols[symbol_index]
    decoded_block.append(symbol)

    # Update range based on the symbol's CDF
    low = low + range_size * lower_bounds[symbol_index]
    high = low + range_size * (upper_bounds[symbol_index] - lower_bounds[symbol_index])

# Reshape decoded block to match the original shape
decoded_block = np.array(decoded_block).reshape(quantized_block.shape)

print(f"\nDecoded block:\n{decoded_block}")

# Verify if the decoded block matches the original block
if np.array_equal(quantized_block, decoded_block):
    print("Decoding successful! The decoded block matches the original block.")
else:
    print("Decoding failed! The decoded block does not match the original block.")
