# Chatgpt implementation of rANS from this page:
# https://kedartatwawadi.github.io/post--ANS/
#
# I can run the test case on his page using the following input:
# Symbol Counts, F: 2, 1, 3, 1, 7, 2
# Input Symbol String: 3, 4, 4, 2, 4, 2, 4, 5, 4, 4, 1, 0, 2, 5, 0, 4
# => State: 17606003532
#
# Decoder gives back the Input Symbol String:
# Symbol Counts, F: 2, 1, 3, 1, 7, 2
# State: 17606003532
# Number of Encoded Symbols: 16
# => Input Symbol String that I encoded above
#
# It is working perfectly for my test case!

import numpy as np
from collections import Counter

# === Quantized Block (Example AV1 Coefficients) ===
quantized_block = np.array([
    [  0, -32,   3,  -2],
    [-32, -10,   0,   0],
    [  3,   0,  -2,   0],
    [ -2,   0,   0,  -1]
])

# === Step 1: Flatten the Block & Compute Symbol Frequencies ===
flat_block = quantized_block.flatten()
symbol_counts = Counter(flat_block)

# Convert to numpy array for calculations
symbols = sorted(symbol_counts.keys())
symbol_counts_np = np.array([symbol_counts[s] for s in symbols])
print(f"symbols: {symbols}, symbol_counts_np: {symbol_counts_np}")

# === Step 2: rANS Encoding Function ===
def C_rANS(s, state, symbol_counts):
    """
    rANS Encoding step: Compresses symbol `s` into `state`.
    """
    total_counts = np.sum(symbol_counts)  # M
    cumul_counts = np.insert(np.cumsum(symbol_counts), 0, 0)  # Cumulative frequencies

    s_count = symbol_counts[s]  # Symbol frequency
    next_state = (state // s_count) * total_counts + cumul_counts[s] + (state % s_count)
    print(f"IN: State: {state}, S: {s}, s_count: {s_count}, symbol_counts: {symbol_counts}, PARAM: cumul_counts: {cumul_counts}, OUT: next_state: {next_state}")
    return next_state

# === Step 3: rANS Decoding Function ===
def D_rANS(state, symbol_counts):
    """
    rANS Decoding step: Extracts a symbol from `state` and updates the state.
    """
    total_counts = np.sum(symbol_counts)  # M
    cumul_counts = np.insert(np.cumsum(symbol_counts), 0, 0)  # Cumulative frequencies

    # Cumulative frequency inverse function
    def cumul_inverse(y): 
        for i, _s in enumerate(cumul_counts): 
            if y < _s:
                return i - 1

    slot = state % total_counts  # Compute the slot     
    s = cumul_inverse(slot)  # Decode the symbol
    prev_state = (state // total_counts) * symbol_counts[s] + slot - cumul_counts[s]  # Update state
    print(f"IN: State: {state}, symbol_counts: {symbol_counts}, OUT: symbols[s]: {symbols[s]}, prev_state: {prev_state}")
    return symbols[s], prev_state

# === Step 4: Encode the Data ===
state = 0  # Initial state
encoded_data = []

for symbol in reversed(flat_block):  # Encode in reverse order
    print(f"IN: symbol: {symbol}, symbols.index(symbol): {symbols.index(symbol)}")
    state = C_rANS(symbols.index(symbol), state, symbol_counts_np)
    encoded_data.append(state)  # Store intermediate states

# Store final state
encoded_data = encoded_data[::-1]  # Reverse back

# === Step 5: Decode the Data ===
decoded_data = []
state = encoded_data.pop(0)  # Retrieve final state

for _ in range(len(flat_block)):
    symbol, state = D_rANS(state, symbol_counts_np)
    decoded_data.append(symbol)

decoded_block = np.array(decoded_data).reshape(quantized_block.shape)  # Restore shape

# === Output Results ===
print("\n=== Encoded Data ===")
print(encoded_data)

print("\n=== Decoded Block ===")
print(decoded_block)

# Verify correctness
assert np.array_equal(quantized_block, decoded_block), "❌ Decoding failed!"
print("\n✅ Successfully encoded and decoded using Multi-Symbol rANS!")

