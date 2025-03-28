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
symbols = unique.tolist()
symbol_counts = dict(zip(unique, counts))

# Convert frequency table into CDF table
def create_cdf(symbol_counts):
    """Create CDF table sorted by probability (most frequent symbol last)."""
    sorted_symbols = sorted(symbol_counts.keys(), key=lambda s: symbol_counts[s])  # Sort by frequency
    total = sum(symbol_counts.values())  # Total occurrences
    
    cdf_table = {}
    cumulative = 0
    frequencies = []

    print("\nCDF Table (Symbol -> CDF Value):")
    
    for symbol in sorted_symbols:
        cumulative += symbol_counts[symbol]
        cdf_table[symbol] = cumulative  # Store cumulative frequency
        frequencies.append(cumulative)
        print(f"  Symbol: {symbol:3}  |  CDF: {cumulative:3}/{total}")  # Print CDF table

    return cdf_table, sorted_symbols, frequencies, total

cdf_table, sorted_symbols, frequencies, total_count = create_cdf(symbol_counts)

# Create a frequency table from CDF
freq_table = arithmeticcoding.SimpleFrequencyTable(frequencies)

# Perform Arithmetic coding (encoding)
bitout = arithmeticcoding.BitOutputStream(open("encoded.bin", "wb"))
encoder = arithmeticcoding.ArithmeticEncoder(32, bitout)

# Encode symbols using the CDF-derived frequency table
for symbol in flat_block:
    encoder.write(freq_table, sorted_symbols.index(symbol))  # Encode by symbol index

encoder.finish()
bitout.close()

def print_bitstream(filename):
    """Reads the encoded file and prints its bitstream."""
    with open(filename, 'rb') as f:
        byte_data = f.read()
        bitstream = ''.join(format(byte, '08b') for byte in byte_data)  # Convert to binary string
        print(f"\nBitstream ({len(bitstream)} bits):\n{bitstream}")

print("\nEntropy encoding complete. Encoded data saved to 'encoded.bin':")
with open('encoded.bin', 'rb') as f:
    print(f.read())
# Call print_bitstream after encoding
print_bitstream("encoded.bin")

# Perform Arithmetic decoding (decoding)
bitin = arithmeticcoding.BitInputStream(open("encoded.bin", "rb"))
decoder = arithmeticcoding.ArithmeticDecoder(32, bitin)

# Decode symbols using the CDF-derived frequency table
decoded_block = []
for _ in range(flat_block.size):
    symbol_index = decoder.read(freq_table)  # Read index
    decoded_block.append(sorted_symbols[symbol_index])  # Convert index back to symbol

bitin.close()

# Reshape decoded block to the original shape
decoded_block = np.array(decoded_block).reshape(quantized_block.shape)

print(f"\nDecoded block:\n{decoded_block}")

# Verify if the decoded block matches the original block
if np.array_equal(quantized_block, decoded_block):
    print("Decoding successful! The decoded block matches the original block.")
else:
    print("Decoding failed! The decoded block does not match the original block.")

