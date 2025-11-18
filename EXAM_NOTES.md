# DAT610 - Wireless Communications
## Exam Preparation Notes

---

## Table of Contents
1. [Lecture 0: Course Information](#lecture-0-course-information)
2. [Lecture 1: Technological Background](#lecture-1-technological-background)
3. [Lecture 2: Physical Layer](#lecture-2-physical-layer)
4. [Lecture 3: Data Link Layer (MAC)](#lecture-3-data-link-layer-mac)
5. [Lecture 4: Data Link Layer (LLC)](#lecture-4-data-link-layer-llc)
6. [Lecture 5: Network and Transport Layers](#lecture-5-network-and-transport-layers)
7. [Lecture 6: Cellular Networks](#lecture-6-cellular-networks)
8. [Lecture 7: WPAN, WLAN, LPWAN](#lecture-7-wpan-wlan-lpwan)
9. [Guest Lectures](#guest-lectures)
10. [Important Formulas](#important-formulas)

---

## Lecture 0: Course Information

### Exam Format (CRITICAL)
- **Duration**: 4 hours
- **Format**: ~8 open-ended questions with sub-questions
- **Materials**: NO printed or written materials allowed
- **Calculator**: Basic calculator permitted
- **Computer**: Bring your own computer to exam

### Examination Structure
- **Assignments**: 3 individual assignments (pass/not pass) - Must pass ALL
- **Project**: 30% of final grade
- **Final Exam**: 70% of final grade
- **IMPORTANT**: Must pass all three components to pass the course

### Course Coverage Scope
**Bottom-up OSI Layer Approach**:
1. **Physical Layer**: Signals, antennas, wireless channels, modulation, multiplexing
2. **Data Link Layer (MAC)**: CSMA, CDMA, OFDMA
3. **Data Link Layer (LLC)**: Error detection, ARQ, FEC (Block & Convolutional codes)
4. **Network Layer**: IP, routing, mobility, QoS
5. **Transport Layer**: TCP, UDP, wireless adaptations
6. **Application Networks**:
   - WPAN: Bluetooth, ZigBee, 6LoWPAN
   - WLAN: IEEE 802.11 (WiFi)
   - LP-WAN: LoRa, NB-IoT, LTE-M
   - Cellular: 2G, 3G, 4G, 5G
7. **Security**: Wireless security mechanisms

### Wireless Technology Classification
**By Range and Data Rate**:
- **Short Range (~1-10m)**: NFC/RFID, Bluetooth (1 Mbps)
- **Medium Range (~100m)**: WiFi/802.11 (10 Mbps - 1 Gbps), ZigBee
- **Long Range (~1-10+ km)**: Cellular (2G-5G), LPWAN (NB-IoT, LoRa, SigFox), LTE-M

### Key Exam Preparation Tips
1. **Study ALL material**: slides, notes, books, standards
2. **Guest lectures ARE included** in exam topics
3. **Answer style**: Be to the point - not too long, not too short
4. **Avoid off-topic content** - it will not count for grades
5. **Read all questions first** and note down doubts
6. Past exam questions available but content may differ

### Learning Questions Per Lecture
Each lecture has specific learning questions that guide exam preparation:
- **Lecture 1**: Networks, protocols, wireless challenges, network taxonomy
- **Lecture 2**: Signals, antennas, propagation, modulation, encoding
- **Lecture 3**: MAC protocols, CSMA, CDMA, OFDMA, hidden/exposed terminals
- **Lecture 4**: Error detection/correction, ARQ types, FEC methods
- **Lecture 5**: IP, routing, mobility, QoS, TCP/UDP, wireless transport
- **Lecture 6**: Cellular principles, 2G-5G evolution, LPWAN technologies
- **Lecture 7**: WiFi 802.11, Bluetooth, ZigBee, LoRa

### Course Context and Motivation
- **Smart Cities**: IoT integration, 5G connectivity
- **Industry 4.0**: Wireless industrial automation, IIoT
- **5G Applications**: Ultra-reliable low-latency communications (URLLC)
- **Private 5G Networks**: Campus networks, enterprise deployments

---

## Lecture 1: Technological Background
*[TO BE COMPLETED]*

### Key Learning Questions:
- What is a computer network?
- Which are the types of networks?
- How is communication in a network working?
- What are the challenges in networks?
- Additional challenges of wireless networks?
- Characteristics of different wireless networks (taxonomy)?

---

## Lecture 2: Physical Layer

### 1. Signal Fundamentals

#### Signal Representation
- **Time Domain**: Amplitude vs time (periodic/aperiodic, analog/digital)
- **Frequency Domain**: Amplitude vs frequency (Fourier analysis)
- **Bandwidth**:
  - **Absolute bandwidth**: All frequencies with non-zero power
  - **Effective bandwidth**: Contains most of the signal energy (more practical)
  - Higher bandwidth → higher data rate (but requires higher frequency)

#### Electromagnetic Spectrum
- **Wavelength**: λ = c/f (c = 3×10⁸ m/s)
- **Frequency ranges**: ELF (3-30 Hz) to THz (> 300 GHz)
- **5G Frequency Ranges**:
  - FR1: 410 MHz - 7.125 GHz (sub-6 GHz)
  - FR2: 24.25 GHz - 71.0 GHz (mmWave)

### 2. Propagation Mechanisms

#### Propagation Modes
- **Ground wave** (f < 2 MHz): Follows Earth's contour
- **Sky wave** (2-30 MHz): Ionospheric reflection
- **Line of Sight** (f > 30 MHz): Direct transmission
  - LOS distance: d₁ = 3.57√(kh₁) where k = 4/3
  - Radio horizon: r = 3.57(√(kh₁) + √(kh₂))

#### Path Loss Formulas (CRITICAL for exam)
```
Free-space path loss:
LdB = 20log₁₀(f) + 20log₁₀(d) - 147.56 dB
  f in MHz, d in meters

Indoor path loss (ITU-R model):
LdB = 20log₁₀(f) + 10n·log₁₀(d) + Lf(nfloors) - 28 dB
  n = path loss exponent
  Lf = floor penetration loss
```

### 3. Transmission Impairments

#### Attenuation
- Signal strength decreases with distance
- Stronger at higher frequencies
- **Atmospheric absorption**: peaks at 22 GHz (H₂O, O₂)

#### Multipath Effects
- **Causes**: Reflection, scattering, diffraction
- **Result**: Multiple signal copies arrive at different times
- **Intersymbol Interference (ISI)**: Unwanted effect when symbols overlap

#### Fading Types
- **Time-based**:
  - Fast fading: Channel changes rapidly (coherence time Tc < symbol time Ts)
  - Slow fading: Channel changes slowly (Tc > Ts)
- **Frequency-based**:
  - Flat fading: Bandwidth < coherence bandwidth (all frequencies affected equally)
  - Frequency-selective fading: Bandwidth > coherence bandwidth (different frequencies affected differently)
- **Channel Models**:
  - **AWGN**: Additive White Gaussian Noise only
  - **Rayleigh fading**: No line of sight (NLOS)
  - **Rician fading**: With line of sight (LOS)

#### Noise and SNR
```
Thermal noise:
  N₀ = kT (W/Hz) where k = 1.38×10⁻²³ J/K
  N = kTB (total noise power)
  NdBW = -228.6 dBW + 10log₁₀(T) + 10log₁₀(B)

SNR:
  SNRdB = 10log₁₀(S/N)

Energy per bit to noise ratio:
  Eb/N₀ = (S/R)/(N₀) = S/(kTR)
  Higher Eb/N₀ → Lower BER
```

### 4. Channel Capacity (CRITICAL for exam)

```
Shannon's Formula (with noise):
  C = B log₂(1 + SNR) bps
  - Accounts for noise
  - Upper bound on capacity

Nyquist Formula (noiseless):
  C = 2B log₂(M) bps
  - M = number of signal levels
  - Practical limit without noise

Feasible signal levels:
  M = √(1 + SNR)

Spectral efficiency:
  η = C/B (bps/Hz)
```

### 5. Antennas

#### Antenna Types
- **Isotropic**: Radiates equally in all directions (theoretical reference)
- **Directional**: Concentrates energy in specific direction
  - Half-wave dipole (λ/2 Hertz antenna)
  - Quarter-wave dipole (λ/4 Marconi antenna)
  - Parabolic reflective antenna

#### Antenna Characteristics
- **Radiation pattern**: 3D representation of power distribution
- **Beam width**: Angle where power ≥ half of maximum
- **Antenna gain**: Ratio of radiation intensity vs isotropic antenna
  - Higher gain → more directional → smaller coverage area

#### Smart Antennas
- **Switched beam**: Select best beam from predefined set
- **Adaptive array**: Track and adapt to mobile target movement
- **Benefits**: Better signal quality, interference reduction

### 6. MIMO (Multiple Input Multiple Output)

#### MIMO Fundamentals
- **n×m MIMO**: n transmit antennas, m receive antennas
- **Transmission schemes**:
  - **Spatial diversity**: Same data on multiple antennas (reliability)
  - **Spatial multiplexing**: Different data on different antennas (capacity)

#### Types of MIMO
- **SU-MIMO**: Single user
- **MU-MIMO**:
  - Uplink (multiple access): Multiple users transmit to base station
  - Downlink (broadcast): Base station transmits to multiple users
- **Massive MIMO**: Base station with tens/hundreds of antennas

#### Beamforming
- **Definition**: Track and direct narrow antenna beam to mobile target
- **Benefits**:
  - Higher SNR at receiver
  - Interference prevention
  - Higher network efficiency
- **Beam management**: Beam sweep → measurement → determination → report
- **FD-MIMO (3D-MIMO)**: Vary beam in azimuth AND elevation

#### Massive MIMO Challenges
- High computational complexity
- Complex channel estimation
- Pilot contamination

### 7. Modulation (Digital Data → Analog Signals)

#### Basic Modulation Techniques
| Technique | Varies | Example |
|-----------|--------|---------|
| **ASK** | Amplitude | 0: low amplitude, 1: high amplitude |
| **FSK** | Frequency | 0: frequency f₁, 1: frequency f₂ |
| **PSK** | Phase | 0: phase 0°, 1: phase 180° |

#### Multilevel Modulation
- **Purpose**: Increase data rate without increasing bandwidth
- **MASK**: Multiple amplitude levels
- **MFSK**: Multiple frequency levels
- **MPSK**: Multiple phase shifts
  - BPSK (2 levels): 1 bit/symbol
  - QPSK (4 levels): 2 bits/symbol
  - 8-PSK (8 levels): 3 bits/symbol
  - 16-PSK (16 levels): 4 bits/symbol
- **QAM**: Combines ASK and PSK (varies amplitude AND phase)
  - 16-QAM, 64-QAM, 256-QAM, 1024-QAM

#### Key Concepts
```
Symbol rate vs data rate:
  Data rate (bps) = Symbol rate (baud) × log₂(M)
  where M = number of signal levels

Constellation diagram:
  - Plots I(t) vs Q(t) (in-phase vs quadrature)
  - Shows all possible signal states
  - Distance between points affects error probability
```

#### Modulation Trade-offs
- **Higher M** (more levels):
  - ✓ Higher data rate
  - ✗ More susceptible to noise
  - ✗ Requires higher SNR
- **Lower M** (fewer levels):
  - ✓ More robust to noise
  - ✗ Lower data rate

### 8. Encoding

#### Analog → Digital (Digitization)
**Pulse Code Modulation (PCM)**:
1. **Sampling**: Sample at rate fs > 2fm (Nyquist theorem)
2. **Quantization**: Map samples to discrete levels
3. **Encoding**: Convert to binary

**Delta Modulation**:
- Approximates signal with staircase function
- Step size δ determines accuracy
- Simpler than PCM but less accurate

#### Digital → Digital (Line Coding)
**Manchester Encoding** (used in Ethernet):
- Transition in middle of each bit period
- 0: high-to-low transition
- 1: low-to-high transition
- Requires 2× bandwidth (disadvantage)
- Self-clocking (advantage)

**Differential Manchester**:
- Transition for 0, no transition for 1
- Used in Token Ring

### 9. Duplexing (IMPORTANT for comparisons)

| Aspect | FDD | TDD |
|--------|-----|-----|
| **Full name** | Frequency Division Duplexing | Time Division Duplexing |
| **Separation** | Different frequency bands | Different time slots |
| **Spectrum** | Paired (UL and DL bands) | Unpaired (same band) |
| **Guard** | Guard band between UL/DL | Guard time between UL/DL |
| **Flexibility** | Fixed UL/DL ratio | Dynamic UL/DL ratio |
| **Best for** | Symmetric traffic | Asymmetric traffic |
| **MIMO** | Complex channel reciprocity | Better channel reciprocity |
| **Interference** | Less interference | Potential UL/DL interference |
| **Cost** | Higher (needs duplexer) | Lower (simpler RF) |

**When to use**:
- **FDD**: Continuous traffic, symmetric data, wider coverage
- **TDD**: Bursty traffic, asymmetric data, better for massive MIMO

### 10. Channel Correction Mechanisms

#### Forward Error Correction (FEC)
- Receiver detects AND corrects errors
- Adds redundancy at transmitter
- Examples: Hamming codes, convolutional codes, turbo codes, LDPC

#### Adaptive Equalization
- Linear equalizer circuit with adjustable taps
- Combats ISI from multipath
- Adapts to time-varying channel

#### Adaptive Modulation and Coding (AMC)
- Switch modulation scheme based on channel conditions
- Good channel → higher order modulation (64-QAM, 256-QAM)
- Poor channel → lower order modulation (QPSK, 16-QAM)
- Maximizes throughput while maintaining quality

#### Diversity Techniques
- Exploit independent fading on different channels
- **Space diversity**: Multiple antennas at different locations
- **Frequency diversity**: Transmit on multiple frequencies
- **Time diversity**: Transmit at different times (with interleaving)

### 11. Coverage vs Data Rate Trade-off

```
Frequency ↑ → Coverage ↓ (higher path loss)
Bandwidth ↑ → Frequency ↑ (need more spectrum at higher bands)
Data Rate ↑ → Bandwidth ↑ (Shannon/Nyquist)

Therefore: Higher data rates → Higher frequencies → Lower coverage
```

### 12. mmWave Challenges (5G FR2)

**Frequency range**: 30-300 GHz (wavelength 1-10 mm)

**Challenges**:
- Limited coverage (high path loss)
- NLOS difficulties (blockage by obstacles)
- Mobility problems (beam tracking)
- High power consumption
- Susceptible to atmospheric absorption

**Solutions**:
- Beamforming and beam tracking
- Small cell deployment
- Carrier aggregation
- Dual connectivity (combine with sub-6 GHz)

### Key Learning Questions:
- What is a signal?
- What is an antenna and how is it characterized?
- Basic propagation mechanisms?
- Main interference types?
- What are encoding and modulation? Techniques?
- Multiplexing and duplexing definitions?
- Main channel correction mechanisms?

---

## Lecture 3: Data Link Layer (MAC)
*[TO BE COMPLETED]*

### Key Learning Questions:
- Issues of accessing shared medium?
- How are multiple access schemes categorized?
- What is CSMA? Why multiple versions?
- Hidden and exposed terminal problems? Solutions?
- What is CDMA?
- What are OFDM, OFDMA, SC-OFDMA?
- Pros and cons of CDMA vs OFDMA?

---

## Lecture 4: Data Link Layer (LLC)
*[TO BE COMPLETED]*

### Key Learning Questions:
- Importance of error detection/correction in wireless?
- Different approaches for error control?
- Methods for error detection? How do they work?
- Different versions of ARQ?
- Methods for error correction?
- Pros and cons of ARQ vs FEC? How to overcome cons?

---

## Lecture 5: Network and Transport Layers
*[TO BE COMPLETED]*

### Key Learning Questions:
- What is IP? Challenges it addresses?
- Differences between IPv4 and IPv6? Why IPv6?
- What is a routing table?
- Possible routing algorithms and protocols?
- Why is mobile IP needed? How does it work?
- What is QoS? How can it be provided?
- Target of transport protocol?
- Difference between TCP and UDP?
- Is TCP suitable for wireless?
- Transport-layer solutions for wireless?

---

## Lecture 6: Cellular Networks
*[TO BE COMPLETED]*

### Key Learning Questions (Part 1):
- Principles of cellular networks?
- Operations of cellular networks?
- Evolution of cellular networks?
- Architecture of 4G and new features?
- Current vision of 6G?
- Different LPWAN technologies? Differences?
- What is private 5G?

### Key Learning Questions (Part 2):
- Architecture of 5G and new features?
- Principles and characteristics of 5G Core Network and RAN?
- Technologies used in 5G NR Air Interface?
- Enabling technologies of 5G?
- How can 5G be deployed?
- New challenges in 5G?

---

## Lecture 7: WPAN, WLAN, LPWAN
*[TO BE COMPLETED]*

### Key Learning Questions:
- What are WiFi and 802.11?
- Physical and data link layer technologies for 802.11 versions?
- How does 802.11 architecture work?
- Different PAN technologies? Differences? Architectures?
- Different LPWAN technologies? Differences?

---

## Guest Lectures

### IIoT and Applications
*[TO BE COMPLETED]*

### Wireless Security
*[TO BE COMPLETED]*

---

## Important Formulas

### Shannon's Formula (Channel Capacity)
```
C = B log₂(1 + SNR)
```
- C = Channel capacity (bps)
- B = Bandwidth (Hz)
- SNR = Signal-to-Noise Ratio (linear)

### Nyquist Formula (Maximum Data Rate)
```
C = 2B log₂(M)
```
- C = Channel capacity (bps)
- B = Bandwidth (Hz)
- M = Number of signaling levels

### SNR Conversion
```
SNRdB = 10 log₁₀(SNR)
```

### Path Loss (Free Space)
```
LdB = 10 log₁₀(Pt/Pr) = 20 log₁₀(4πfd/c) = 20 log₁₀(f) + 20 log₁₀(d) - 147.56
```
- Pt = Transmitted power
- Pr = Received power
- f = Frequency
- d = Distance
- c = Speed of light

### Path Loss (with exponent)
```
LdB = 10 log₁₀(Pt/Pr) = γ·10 log₁₀(4πfd/c)
```
- γ = Path loss exponent (typically 2-4)

---

## Exam Strategy Checklist

- [ ] Review all learning questions for each lecture
- [ ] Practice past exam questions
- [ ] Understand formulas and when to apply them
- [ ] Study wireless protocol mechanisms (CSMA/CA, ARQ, etc.)
- [ ] Know differences between wireless technologies
- [ ] Understand cellular evolution (2G→5G)
- [ ] Review error correction codes (Hamming, convolutional, turbo, LDPC)
- [ ] Understand TCP issues in wireless and solutions
- [ ] Know routing protocols (AODV, DSR) characteristics
- [ ] Review guest lecture topics (IIoT, Security)

---

**Last Updated**: [Current Date]
**Status**: Lecture 0 Complete - Remaining lectures to be added
