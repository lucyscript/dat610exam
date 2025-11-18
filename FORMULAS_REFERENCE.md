# DAT610 Wireless Communications - Quick Reference Formulas

## Essential Formulas to Memorize for Exam

### 1. Channel Capacity (Shannon's Theorem)
```
C = B × log₂(1 + SNR)
```
Where:
- C = Channel capacity (bits/second)
- B = Bandwidth (Hz)
- SNR = Signal-to-Noise Ratio (linear, not dB)

**Example:** If B = 1 MHz and SNRdB = 24 dB:
- First convert: SNR = 10^(24/10) = 251.19
- Then: C = 1×10^6 × log₂(1 + 251.19) ≈ 8 Mbps

### 2. Nyquist Formula (Noiseless Channel)
```
C = 2B × log₂(M)
```
Where:
- C = Data rate (bits/second)
- B = Bandwidth (Hz)
- M = Number of signaling levels

**Example:** To reach 8 Mbps with B = 1 MHz:
- 8×10^6 = 2×1×10^6 × log₂(M)
- log₂(M) = 4
- M = 2^4 = 16 signal levels

### 3. SNR Conversion
```
SNR(dB) = 10 × log₁₀(SNR)
```
Or inversely:
```
SNR = 10^(SNR(dB)/10)
```

**Common Values:**
- 3 dB = 2× power ratio
- 10 dB = 10× power ratio
- 20 dB = 100× power ratio
- 30 dB = 1000× power ratio

### 4. Free Space Path Loss (Friis Equation)
```
L(dB) = 20log₁₀(f) + 20log₁₀(d) - 147.56
```
Alternative form:
```
L(dB) = 20log₁₀(4πfd/c)
```

Where:
- f = Frequency (Hz)
- d = Distance (meters)
- c = Speed of light (3×10^8 m/s)
- γ = Path loss exponent (2 for free space)

**General Path Loss Model:**
```
L(dB) = γ × 10log₁₀(4πfd/c)
```
Where γ = 2 (free space), 3-4 (urban), 4-6 (indoors)

**Effect of frequency doubling:**
- If frequency doubles (450 MHz → 900 MHz): +6 dB loss
- Formula: 20log₁₀(2) ≈ 6 dB

### 5. Power and Energy

**Received Power:**
```
P_r(dBm) = P_t(dBm) + G_t(dB) + G_r(dB) - L(dB)
```

**dBm Conversion:**
```
P(dBm) = 10log₁₀(P(mW))
P(mW) = 10^(P(dBm)/10)
```

### 6. Hamming Code

**For (n, k) code:**
- n = total bits
- k = data bits
- r = parity bits = n - k

**Relationship:**
```
2^r ≥ n + 1
```

**Error Detection and Correction:**
- Minimum Hamming distance (dmin) = 3 for single error correction
- Can detect: dmin - 1 errors
- Can correct: ⌊(dmin - 1)/2⌋ errors

**Example:** For n=12 bits:
- 2^r ≥ 12 + 1 = 13
- r = 4 (since 2^4 = 16 ≥ 13)
- k = 12 - 4 = 8 data bits
- Can detect 2 errors, correct 1 error

**Parity bit positions:** Powers of 2 (1, 2, 4, 8, ...)

### 7. TCP Performance

**Throughput:**
```
Throughput = WindowSize / RTT
```

**Channel Utilization:**
```
Utilization = Throughput / Available_Bandwidth
```

**With Packet Loss:**
```
Throughput ≈ (MSS / RTT) × √(3/2p)
```
Where:
- MSS = Maximum Segment Size
- p = Packet loss probability

### 8. Cellular Network Capacity

**Frequency Reuse Factor:**
```
N = i² + ij + j²
```
Where i, j are cell shift parameters

**Common values:**
- N = 3: (i=1, j=1)
- N = 4: (i=2, j=0)
- N = 7: (i=2, j=1)
- N = 12: (i=2, j=2)

**Channels per Cell:**
```
k = S / N
```
Where:
- k = Channels per cell
- S = Total channels in system
- N = Reuse factor

### 9. CDMA Spreading

**Processing Gain:**
```
G_p = R_c / R_b = W / R_b
```
Where:
- R_c = Chip rate
- R_b = Bit rate
- W = Bandwidth

**Number of Users (for maximal length sequence):**
```
Maximum sequence length = 2^n - 1
```
Where n = number of bits in code generator

### 10. OFDM Parameters

**Number of Subcarriers:**
```
N = B / Δf
```
Where:
- B = Total bandwidth
- Δf = Subcarrier spacing

**Symbol Duration:**
```
T_s = 1 / Δf
```

**Guard Interval (to prevent ISI):**
```
T_g ≥ maximum delay spread
```

### 11. Modulation

**Bits per Symbol:**
```
b = log₂(M)
```
Where M = constellation size

**Examples:**
- BPSK: M=2, b=1 bit/symbol
- QPSK: M=4, b=2 bits/symbol
- 16-QAM: M=16, b=4 bits/symbol
- 64-QAM: M=64, b=6 bits/symbol

**Data Rate:**
```
R = (b × W) / T_s
```
Where:
- b = bits per symbol
- W = bandwidth
- T_s = symbol duration

### 12. Error Rates

**Bit Error Rate (BER) to Frame Error Rate (FER):**
```
FER ≈ 1 - (1 - BER)^n
```
For small BER:
```
FER ≈ n × BER
```
Where n = frame length in bits

### 13. ARQ Efficiency

**Stop-and-Wait:**
```
Efficiency = 1 / (1 + 2a)
```
Where a = (propagation delay) / (transmission time)

**Go-Back-N:**
```
Efficiency = (1 - P_e) / (1 + 2aP_e)
```
Where P_e = probability of frame error

**Selective Repeat:**
```
Efficiency = 1 - P_e
```

### 14. Antenna Gain

**Isotropic Antenna:**
```
G = 1 (0 dB)
```

**Directional Antenna:**
```
G(dB) = 10log₁₀(4π × A_e / λ²)
```
Where:
- A_e = Effective aperture area
- λ = Wavelength = c/f

### 15. Link Budget

**Total Link Budget:**
```
P_r = P_t + G_t + G_r - L_fs - L_misc
```

**Required SNR for Target BER:**
- BPSK: SNR ≈ 9.6 dB for BER = 10^-5
- QPSK: SNR ≈ 9.6 dB for BER = 10^-5
- 16-QAM: SNR ≈ 16.5 dB for BER = 10^-5
- 64-QAM: SNR ≈ 22.5 dB for BER = 10^-5

## Quick Conversion Tables

### dB to Linear Ratio
| dB | Ratio |
|----|-------|
| 0  | 1     |
| 3  | 2     |
| 6  | 4     |
| 10 | 10    |
| 20 | 100   |
| 30 | 1000  |

### Powers of 2 (for quick calculation)
| n | 2^n |
|---|-----|
| 10 | 1024 ≈ 10^3 |
| 20 | 1048576 ≈ 10^6 |
| 30 | ≈ 10^9 |

### Frequency Bands
| Band | Frequency | Wavelength |
|------|-----------|------------|
| 900 MHz | 900×10^6 Hz | 0.33 m |
| 2.4 GHz | 2.4×10^9 Hz | 0.125 m |
| 5 GHz | 5×10^9 Hz | 0.06 m |
| 28 GHz | 28×10^9 Hz | 0.011 m |

## Exam Tips for Calculations

1. **Always show your work** - partial credit available
2. **State your assumptions** clearly
3. **Convert dB properly** - most common mistake
4. **Check units** - Hz vs MHz, W vs mW vs dBm
5. **Use approximations** when exact calculation is complex:
   - log₂(10) ≈ 3.32
   - log₁₀(2) ≈ 0.301
   - π ≈ 3.14

## Common Exam Question Types

1. **Shannon/Nyquist problems:**
   - Given B and SNR, find C
   - Given C and B, find required M
   - Effect of frequency change on capacity

2. **Path loss problems:**
   - Calculate received power
   - Find maximum distance for given SNR
   - Compare different frequencies

3. **Hamming code:**
   - Given n, find k, r, error correction capability
   - Detect/correct errors in received codeword

4. **TCP performance:**
   - Calculate throughput given window size and RTT
   - Find channel utilization
   - Effect of packet loss

5. **Routing algorithms:**
   - Update routing tables (distance vector)
   - Count to infinity problem

6. **CDMA calculations:**
   - Find number of users given chip rate and max delay
   - Processing gain calculations

Remember: **Practice these formulas with past exam questions!**
