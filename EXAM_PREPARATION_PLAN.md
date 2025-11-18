# DAT610 Wireless Communications - Comprehensive Exam Preparation Plan

## Exam Details
- **Date:** December 9th, 2025 (To be confirmed)
- **Duration:** 4 hours
- **Format:** Open-ended questions (usually 8 questions with sub-questions)
- **Materials:** No printed/written materials allowed, basic calculator permitted
- **Weight:** 70% of final grade (Project: 30%, Assignments: pass/fail)
- **Language:** Answer in English
- **Computer:** Bring your own computer to the exam

## Key Exam Strategies
1. **Study everything** - slides, notes, and textbooks
2. **Be concise and to the point** - not too long, not too short
3. **Stay on topic** - off-topic content won't count toward grade
4. **Read all questions first** - note down doubts before starting
5. **Make assumptions** - if parameters are missing, state your assumptions clearly
6. **Guest lectures are included** - expect questions on guest lecture topics

## Common Question Patterns from Past Exams

### 1. Calculation Questions (15-20 points each)
- **Shannon's Formula:** C = B×log₂(1+SNR)
- **Nyquist Formula:** C = 2B×log₂M
- **Path Loss Formula:** LdB = 20log(4πfd/c) = 20log(f) + 20log(d) - 147.56 dB
- **SNR Conversion:** SNRdB = 10log₁₀(SNR)
- Topics: Channel capacity, frequency effects, signaling levels, path loss

### 2. Protocol Implementation (15 points)
- Write pseudocode for CSMA/CA or similar MAC protocols
- Must understand: medium sensing, backoff, collision avoidance
- Use provided function calls correctly

### 3. Error Control (10-15 points)
- Hamming codes: calculate check bits, detect/correct errors
- Compare: Block codes vs Convolutional codes vs Turbo codes
- FEC vs BEC (ARQ) trade-offs
- LDPC (Low Density Parity Check) vs Hamming code

### 4. Network Layer (10-15 points)
- Routing table updates (distance vector algorithms)
- Count to infinity problem
- AODV vs DSR comparison for sensor networks
- Mobile IP and mobility management

### 5. Comparison Questions (10-15 points)
- CDMA vs OFDMA pros/cons
- CSMA/CA vs CSMA/CD vs SMAC
- TCP variants for wireless networks
- Different wireless network types (WLAN, PAN, LPWAN)
- IEEE 802.11 versions (a, g, n, p, ac, ax)

### 6. Cellular Networks (10-15 points)
- Evolution: 1G → 2G → 3G → 4G → 5G → 6G vision
- Architecture differences between generations
- 4G LTE architecture and features
- 5G Core Network, RAN, NR Air Interface
- Enabling technologies: massive MIMO, network slicing, edge computing
- Deployment strategies
- Handoff mechanisms (hysteresis, threshold, ping-pong avoidance)
- Location registration schemes (time-based, distance-based, dynamic)
- Paging strategies (blanket vs selective)

### 7. LPWAN Technologies (10 points)
- LoRa, NB-IoT, LTE-M comparisons
- Use cases and trade-offs
- Private 5G concepts

### 8. WLAN/PAN (10-15 points)
- IEEE 802.11 architecture and operation
- Hidden terminal and exposed terminal problems
- RTS/CTS mechanism
- PAN technologies: Bluetooth, ZigBee, 6LoWPAN
- Physical and MAC layer technologies enabling different standards

### 9. Transport Layer (9-15 points)
- Why conventional TCP doesn't fit wireless networks
- TCP slow start, congestion avoidance
- Window size calculations, throughput estimation
- Channel utilization problems
- Solutions: Split TCP, Indirect TCP, Snoop TCP

### 10. Security (10 points)
- Wireless security challenges
- Attack types: sink hole, black hole, selective forwarding
- Authentication and encryption in wireless networks

### 11. IoT (varies)
- IoT architecture and protocols
- Sensor network routing (DSR, AODV suitability)
- Energy efficiency considerations
- Localization techniques (multilateration, time difference of arrival)

### 12. Multiplexing & Multiple Access (10-15 points)
- TDMA, FDMA, CDMA, OFDMA, SC-OFDMA
- OFDM and ISI (Inter-Symbol Interference)
- Pseudonoise sequences for CDMA
- Maximal length sequence generators

## Topic-by-Topic Study Guide

### Lecture 0: Course Information
- Course structure and objectives
- Wireless communication overview

### Lecture 1: Technological Background
**Key Questions:**
- What is a computer network?
- Types of networks (LAN, WAN, MAN, PAN)
- How communication works (OSI model, protocols)
- Network challenges: reliability, routing, addressing, flow control
- Additional wireless challenges: mobility, power, interference, security
- Wireless network taxonomy: Ad-hoc, Cellular, Sensor, Mesh

**Study Focus:**
- Protocol stack layers
- Differences between wired and wireless networks
- Network paradigms and architectures

### Lecture 2: Physical Layer
**Key Questions:**
- What is a signal? (analog vs digital, time vs frequency domain)
- Antenna characteristics (gain, radiation pattern, polarization)
- Propagation mechanisms (reflection, diffraction, scattering)
- Interference types (co-channel, adjacent channel, ISI, multipath)
- Encoding vs Modulation (ASK, FSK, PSK, QAM)
- Multiplexing (TDMA, FDMA, CDMA) vs Duplexing (FDD, TDD)
- Channel correction (equalization, diversity, spread spectrum)

**Study Focus:**
- Shannon and Nyquist formulas (memorize!)
- Path loss calculations
- Friis transmission equation
- Modulation techniques and constellation diagrams
- Fading types (fast/slow, flat/frequency-selective)

### Lecture 3: Data Link Layer MAC
**Key Questions:**
- Issues of shared medium access (collisions, fairness, efficiency)
- Multiple access categorization (contention-based, scheduled, random)
- CSMA variants (non-persistent, 1-persistent, p-persistent, CSMA/CA)
- Hidden and exposed terminal problems + solutions (RTS/CTS)
- CDMA principles (spreading codes, orthogonality)
- OFDM, OFDMA, SC-OFDMA differences
- Pros/cons of CDMA vs OFDMA

**Study Focus:**
- CSMA/CA algorithm (can you write pseudocode?)
- Why CSMA/CD doesn't work in wireless
- CDMA code properties (autocorrelation, cross-correlation)
- OFDM benefits for multipath/ISI
- Maximal length sequences

### Lecture 4: Data Link Layer Coding
**Key Questions:**
- Why error detection/correction is critical in wireless
- Error control approaches (ARQ, FEC, Hybrid ARQ)
- Error detection methods (parity, CRC, checksum)
- ARQ versions (Stop-and-Wait, Go-Back-N, Selective Repeat)
- Error correction methods (Block codes, Convolutional codes, Turbo codes, LDPC)
- ARQ vs FEC pros/cons and when to use each

**Study Focus:**
- Hamming code calculations (given n, find k, dmin, error detection/correction capability)
- CRC polynomial division
- Block codes (7,4 Hamming) vs Convolutional codes
- BER impact on FEC vs ARQ choice
- Turbo codes and LDPC concepts

### Lecture 5: Network & Transport Layers
**Network Layer Key Questions:**
- What is IP? IPv4 vs IPv6 differences
- Packet structure and addressing
- Routing tables and algorithms (Distance Vector, Link State)
- Routing protocols (RIP, OSPF, AODV, DSR)
- Why mobile IP is needed (triangle routing, home agent, foreign agent)
- QoS mechanisms (DiffServ, IntServ)

**Transport Layer Key Questions:**
- Transport protocol goals (reliability, flow control, congestion control)
- TCP vs UDP differences
- Why TCP doesn't suit wireless (assumes congestion, not errors)
- TCP slow start and congestion avoidance
- Solutions: Indirect TCP, Snoop TCP, Mobile TCP
- Acknowledgment schemes (positive, negative, selective)

**Study Focus:**
- Routing table update calculations
- Count to infinity problem
- AODV vs DSR for different network types
- TCP throughput and utilization calculations
- Congestion window vs receive window

### Lecture 6: Cellular Networks (MOST IMPORTANT TOPIC)
**Key Questions Part 1:**
- Cellular network principles (frequency reuse, handoff, cell splitting)
- Cellular operations (registration, paging, handoff, location management)
- Evolution: 1G (analog) → 2G (digital, GSM) → 3G (WCDMA, CDMA2000) → 4G (LTE, all-IP) → 5G (eMBB, URLLC, mMTC)
- 4G LTE architecture (EPC: MME, SGW, PGW; eNodeB)
- 6G vision (THz, AI/ML, holographic communications)
- LPWAN technologies (LoRa, NB-IoT, LTE-M) differences
- Private 5G use cases

**Key Questions Part 2:**
- 5G architecture and new features (network slicing, MEC, service-based architecture)
- 5G Core Network characteristics (AMF, SMF, UPF, control/user plane separation)
- Radio Access Network (gNB, CU-DU split)
- 5G NR Air Interface technologies (massive MIMO, beamforming, millimeter wave)
- Enabling technologies (SDN, NFV, cloud-native, network slicing)
- 5G deployment options (NSA, SA, spectrum strategies)
- New challenges (security, complexity, energy, cost)

**Study Focus:**
- Draw and label 4G LTE architecture
- Draw and label 5G architecture
- Understand service-based architecture
- Frequency reuse factor calculations
- Handoff mechanisms and parameters
- Location registration cost-benefit analysis
- Key differences between each generation
- 5G use case categories: eMBB, URLLC, mMTC

### Lecture 7: WLAN-PAN-LPWAN
**Key Questions:**
- WiFi vs 802.11 (WiFi is certification, 802.11 is standard)
- Physical layer differences across 802.11 versions (FHSS, DSSS, OFDM, MIMO, MU-MIMO)
- MAC layer (CSMA/CA, DCF, PCF)
- 802.11 architecture (BSS, ESS, IBSS, AP, distribution system)
- PAN technologies differences:
  - Bluetooth (piconets, scatternets, frequency hopping)
  - ZigBee (mesh, low power, IEEE 802.15.4)
  - 6LoWPAN (IPv6 over low power networks)
- LPWAN comparisons (range, data rate, power consumption)

**Study Focus:**
- 802.11 a/b/g/n/ac/ax/ax specifications (frequency, speed, range)
- Hidden/exposed terminal in 802.11 context
- Bluetooth architecture and protocol stack
- When to use which technology (WLAN vs PAN vs LPWAN)

### Lecture 8: Tools
- Likely about measurement tools, simulation tools, or practical tools
- **Note:** Check lecture content specifically for this

### Lecture 9: Wireless Security
**Key Questions:**
- Wireless security challenges (eavesdropping, man-in-the-middle, DoS)
- Attack types:
  - Sink hole attack (attract all traffic)
  - Black hole attack (drop all packets)
  - Selective forwarding (drop some packets)
  - Wormhole, Sybil attacks
- Security mechanisms:
  - WEP, WPA, WPA2, WPA3
  - Authentication protocols
  - Encryption (AES, etc.)

**Study Focus:**
- Compare attack types
- Security protocol evolution in WiFi
- Authentication vs encryption
- Security in different wireless technologies

### Lecture 10: IoT
**Key Questions:**
- IoT architecture layers (perception, network, application)
- IoT protocols (MQTT, CoAP, AMQP)
- Sensor network characteristics
- Energy-efficient routing
- Localization techniques:
  - Time of Arrival (ToA)
  - Time Difference of Arrival (TDoA)
  - Received Signal Strength (RSS)
  - Angle of Arrival (AoA)
- Multilateration methods

**Study Focus:**
- IoT protocol stack
- Sensor network routing suitability (AODV, DSR)
- Localization accuracy and complexity trade-offs
- Power efficiency in sensor networks

## Formulas to Memorize

### Capacity and SNR
```
Shannon: C = B × log₂(1 + SNR) [bits/sec]
Nyquist: C = 2B × log₂(M) [bits/sec]
SNR (dB): SNRdB = 10 × log₁₀(SNR)
```

### Path Loss
```
Free Space: LdB = 20log(f) + 20log(d) - 147.56 dB
General: LdB = γ × 10log(4πfd/c)
where γ = path loss exponent (2 for free space, 4 for urban)
```

### Hamming Code
```
For (n, k) code:
n = total bits
k = data bits
r = check bits = n - k
Relationship: 2^r ≥ n + 1
Minimum distance: dmin = 3 for single error correction
Can detect: dmin - 1 errors
Can correct: ⌊(dmin - 1)/2⌋ errors
```

### TCP Performance
```
Throughput = WindowSize / RTT
Utilization = Throughput / Bandwidth
```

### Frequency Reuse
```
Reuse factor = N = i² + ij + j²
where i, j are cell shift parameters
```

## Study Schedule Recommendation

### Week 1: Foundation
- Day 1-2: Lecture 1 (Technological Background)
- Day 3-4: Lecture 2 (Physical Layer) + practice calculations
- Day 5-6: Lecture 3 (MAC Layer) + write CSMA/CA pseudocode
- Day 7: Review and practice problems

### Week 2: Core Protocols
- Day 1-2: Lecture 4 (Error Coding) + practice Hamming codes
- Day 3-4: Lecture 5a (Network Layer) + routing exercises
- Day 5-6: Lecture 5b (Transport Layer) + TCP calculations
- Day 7: Review and practice problems

### Week 3: Wireless Technologies
- Day 1-3: Lecture 6 (Cellular Networks) - CRITICAL TOPIC
- Day 4-5: Lecture 7 (WLAN-PAN-LPWAN)
- Day 6: Lecture 8 (Tools)
- Day 7: Review cellular architecture drawings

### Week 4: Final Topics & Review
- Day 1-2: Lecture 9 (Wireless Security)
- Day 3-4: Lecture 10 (IoT)
- Day 5-6: Work through past exam questions
- Day 7: Full review of all topics

### Final Days Before Exam
- Review all formulas
- Practice drawing architectures (4G, 5G, 802.11)
- Review comparison topics (AODV vs DSR, CDMA vs OFDMA, etc.)
- Quick review of learning questions for each lecture

## Practice Problems to Complete

1. **Calculate channel capacity** with various SNR and bandwidth values
2. **Hamming code problems:** Find errors, correct them, calculate parameters
3. **Path loss calculations:** Effect of frequency and distance changes
4. **CSMA/CA pseudocode:** Write from scratch
5. **Routing table updates:** Practice distance vector algorithm
6. **TCP throughput:** Calculate utilization with packet loss
7. **Cellular frequency reuse:** Calculate interference, capacity
8. **Draw architectures:** 4G LTE, 5G, 802.11, Bluetooth
9. **Compare protocols:** Make comparison tables for major topics
10. **Work through all past exam questions**

## Key Comparison Tables to Create

1. **Cellular Generations:** 1G vs 2G vs 3G vs 4G vs 5G
2. **Multiple Access:** TDMA vs FDMA vs CDMA vs OFDMA
3. **Error Control:** ARQ vs FEC vs Hybrid ARQ
4. **Routing Protocols:** AODV vs DSR vs others
5. **TCP Variants:** Traditional vs Indirect vs Snoop vs Mobile
6. **802.11 Standards:** a vs b vs g vs n vs ac vs ax
7. **PAN Technologies:** Bluetooth vs ZigBee vs 6LoWPAN
8. **LPWAN Technologies:** LoRa vs NB-IoT vs LTE-M
9. **Security Attacks:** Sink hole vs Black hole vs Selective forwarding
10. **Localization Methods:** ToA vs TDoA vs RSS vs AoA

## Resources Checklist

- [ ] All lecture slides (0-10)
- [ ] Textbooks (Wireless Communication Networks and Systems, 5G Wireless)
- [ ] Past exam questions
- [ ] Learning questions for each lecture
- [ ] Your own notes from lectures
- [ ] Guest lecture materials
- [ ] Practice problems with solutions
- [ ] Comparison tables
- [ ] Architecture diagrams
- [ ] Formula sheet (for memorization, not for exam)

## Final Checklist Before Exam

- [ ] Memorized all key formulas
- [ ] Can draw 4G and 5G architectures from memory
- [ ] Can explain differences between cellular generations
- [ ] Can write CSMA/CA pseudocode
- [ ] Understand all comparison topics
- [ ] Practiced Hamming code problems
- [ ] Reviewed all past exam questions
- [ ] Comfortable with capacity and path loss calculations
- [ ] Know TCP performance issues in wireless
- [ ] Understand all error control mechanisms
- [ ] Can explain all wireless technologies (WLAN, PAN, LPWAN)
- [ ] Know security attacks and countermeasures
- [ ] Understand IoT architecture and protocols

## Exam Day Reminders

1. Bring your own computer
2. Bring a basic calculator
3. Read ALL questions first before starting
4. Note doubts and potential assumptions
5. Allocate time per question (4 hours / 8 questions ≈ 30 min each)
6. Answer what is asked - be concise and on-topic
7. If missing parameters, state your assumptions clearly
8. Show your work for calculations
9. Leave time for review at the end

## High-Priority Topics (Focus if short on time)

1. **Cellular Networks (Lecture 6)** - Largest topic, always multiple questions
2. **Physical Layer calculations** - Shannon, Nyquist, path loss
3. **Error coding** - Hamming codes, ARQ vs FEC
4. **CSMA/CA** - Implementation and hidden terminal problem
5. **5G architecture and features** - Very current and important
6. **TCP in wireless networks** - Common question
7. **Routing protocols** - AODV vs DSR
8. **802.11 standards** - Differences and features

Good luck with your exam preparation!
