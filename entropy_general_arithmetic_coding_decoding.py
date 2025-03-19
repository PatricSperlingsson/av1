import numpy as np
import arithmeticcoding

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

# Create a frequency table (required for arithmetic coding)
def create_frequencies(symbol_counts):
    freq_table = arithmeticcoding.SimpleFrequencyTable([1] * 256)  # Initialize with uniform frequencies
    for symbol, count in symbol_counts.items():
        freq_table.set(symbol & 0xFF, count)
    return freq_table

freq_table = create_frequencies(symbol_counts)

# Perform Arithmetic coding (encoding)
bitout = arithmeticcoding.BitOutputStream(open("encoded.bin", "wb"))
encoder = arithmeticcoding.ArithmeticEncoder(32, bitout)

# Encode symbols
for symbol in flat_block:
    encoder.write(freq_table, symbol & 0xFF)

encoder.finish()
bitout.close()

print("\nEntropy encoding complete. Encoded data saved to 'encoded.bin':")
with open('encoded.bin', 'rb') as f:
    print(f.read())

# Perform Arithmetic decoding (decoding)
bitin = arithmeticcoding.BitInputStream(open("encoded.bin", "rb"))
decoder = arithmeticcoding.ArithmeticDecoder(32, bitin)

# Decode symbols
decoded_block = []
for _ in range(flat_block.size):
    symbol = decoder.read(freq_table)
    decoded_block.append(symbol if symbol < 128 else symbol - 256)  # Handle negative values

bitin.close()

# Reshape decoded block to the original shape
decoded_block = np.array(decoded_block).reshape(quantized_block.shape)

print(f"\nDecoded block:\n{decoded_block}")

# Verify if the decoded block matches the original block
if np.array_equal(quantized_block, decoded_block):
    print("Decoding successful! The decoded block matches the original block.")
else:
    print("Decoding failed! The decoded block does not match the original block.")

