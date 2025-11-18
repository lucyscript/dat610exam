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
*[TO BE COMPLETED]*

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

### WLAN (IEEE 802.11 / WiFi)

#### Key 802.11 Standards
**Standard** | **Freq** | **Year** | **Max Speed** | **Key Features**
802.11a | 5 GHz | 1999 | 54 Mbps | OFDM, not compatible with b/g
802.11b | 2.4 GHz | 1999 | 11 Mbps | DSSS, longer range than 802.11a
802.11g | 2.4 GHz | 2003 | 54 Mbps | Backward compatible with 802.11b
802.11n | 2.4/5 GHz | 2009 | 150-600 Mbps | MIMO-OFDM (multiple antennas)
802.11ac | 5 GHz | 2014 | Up to 6.93 Gbps | Up to 8 spatial streams, 256-QAM
802.11ax (Wi-Fi 6) | 2.4/5/6 GHz | 2021 | Up to 9.6 Gbps | OFDMA, 1024-QAM, 6 GHz band
802.11be (Wi-Fi 7) | 2.4/5/6 GHz | 2025 | Up to 46 Gbps | 16 spatial streams, 4096-QAM, MLO

#### 802.11 Architecture
- **IEEE 802 Stack**: LLC (Logical Link Control) + MAC + PLCP + PMD
  - LLC: Interface to higher layers, addressing, error control
  - MAC: Media Access Control (CSMA/CA)
  - PLCP: Physical Layer Convergence - maps MAC frames, synchronization, signaling
  - PMD: Physical Medium Dependent - transmitting/receiving data

- **Network Topologies**:
  - **BSS (Basic Service Set)**: Single AP interconnecting wireless clients
  - **ESS (Extended Service Set)**: Multiple BSSs interconnected via distribution system
  - **BSSID**: MAC address of AP's NIC
  - **SSID**: Network name (e.g., "eduroam")

#### 802.11 PHY Layer
**PHY data rate determined by**:
- **Channel Width**: 20, 40, 80, 160, 320 MHz
- **Modulation and Coding Scheme (MCS)**: BPSK, QPSK, 16-QAM, 64-QAM, 256-QAM, 1024-QAM, 4096-QAM
- **Number of Spatial Streams (SS)**: 1-16 (via MIMO)
- **Guard Interval (GI)**: Prevents inter-symbol interference

**Transmission Schemes**: DSSS, OFDM, MIMO-OFDM, OFDMA

#### 802.11 MAC Layer - CSMA/CA with RTS/CTS
**Why CA instead of CD?**
- WLANs are half-duplex (cannot listen while sending)
- Impossible to detect collisions during transmission

**CSMA/CA Process**:
1. **Carrier Sense**: Listen if channel is idle
2. **RTS** (Ready to Send) - optional: Request dedicated channel access
3. **CTS** (Clear to Send) - optional: AP grants channel access
4. **Random backoff** if channel busy (Collision Avoidance)
5. **Transmit data**
6. **ACK**: All transmissions acknowledged; no ACK = assumed collision, restart

**Solves**: Hidden and exposed terminal problems

#### 802.11 Security
**Authentication Methods**:
- **WEP** (Wired Equivalent Privacy): RC4 encryption, NEVER USE - broken
- **WPA** (Wi-Fi Protected Access): TKIP encryption, Message Integrity Check (MIC)
- **WPA2**: AES encryption with CCMP (Counter Cipher Mode with Block Chaining Message Authentication Code)
  - **Personal**: Pre-Shared Key (PSK) for home networks
  - **Enterprise**: 802.1X/EAP authentication via RADIUS server
- **WPA3**: Latest, strongest security
  - **Personal**: SAE (Simultaneous Authentication of Equals) - prevents brute force
  - **Enterprise**: 192-bit cryptographic suite, 802.1X/EAP
  - **Open Networks**: OWE (Opportunistic Wireless Encryption)
  - **IoT**: DPP (Device Provisioning Protocol) replaces WPS

**Encryption Protocols**:
- **TKIP**: WPA, changes key per packet
- **AES-CCMP**: WPA2, strongest current standard

---

### WPAN (Wireless Personal Area Networks)

#### Bluetooth (IEEE 802.15.1)
**Characteristics**:
- 2.4 GHz ISM band
- Range: ~10 meters
- Low power, low cost
- Managed by Bluetooth Special Interest Group

**Network Topology**:
- **Piconet**: 1 Master + up to 7 active slaves, shared frequency hopping
- **Scatternet**: Multiple interconnected piconets via bridge devices
- **Master**: Determines channel access, frequency hopping, timing (TDD)
- **Slaves**: Communicate only with master

**Bluetooth Profiles** (Usage Models):
- **HSP/HFP**: Headset/Hands-free calling
- **A2DP**: Stereo audio streaming
- **AVRCP**: Audio/video remote control
- **SPP**: Serial port emulation
- **HID**: Keyboards, mice

**Specifications**:
- **PHY**: GFSK modulation, 2.4 GHz ISM band, 1 MHz carrier spacing
- **Baseband**: FH-TDD-TDMA for piconet, FH-CDMA for scatternet
- **Data Rate**: 1 Mbps (BR), 2-3 Mbps (EDR)
- **Versions**:
  - 2.0 (EDR), 3.0 (High Speed + 802.11)
  - 4.0 (Low Energy), 5.0 (4x range, 2x speed, IoT)

#### ZigBee (IEEE 802.15.4)
**Characteristics**:
- Sub-GHz ISM bands: 868 MHz, 915 MHz, 2.4 GHz
- Low data rate, long battery life
- Maintained by Zigbee Alliance

**Architecture**:
- **IEEE 802.15.4**: Defines PHY and MAC
- **ZigBee**: Adds NWK, APS, ZDO, Application layers
  - **NWK**: Addressing, routing, network formation
  - **APS**: Reliable delivery, binding, group management
  - **ZDO**: Device role, network management, security
  - **ZCL**: Standard clusters for interoperability

**Network Topologies**:
- **Star**: Coordinator + end devices
- **Mesh**: AODV-like routing (AODVjr) for low power
- **Cluster Tree**: Hierarchical tree-based routing

**Device Types**:
- **Coordinator**: Manages network, assigns addresses
- **Routers**: Relay messages
- **End Devices**: Send/receive data

**Network Types**:
- **Non-beacon**: No time sync, routers always on, mesh topology
- **Beacon-based**: Periodic beacons, star or tree topology

#### 6LoWPAN (IPv6 over Low-Power WPAN)
**Purpose**: Enable IPv6 on resource-constrained IoT devices

**Key Features**:
- Based on IEEE 802.15.4 PHY/MAC
- IETF specification: RFC 4944
- **Adaptation Layer**: Header compression and fragmentation (RFC 6282)
  - MTU: 1280 bytes → 127 bytes
  - Address: 128 bits → 64/16 bit MAC addresses
- Enables IP connectivity for small, low-power devices

---

### LPWAN (Low-Power Wide Area Networks)

**Characteristics**: Long-range, low data rate, high connectivity, low power, low cost

#### LoRa / LoRaWAN
**LoRa (Physical Layer)**:
- **Proprietary**: Developed by Semtech, maintained by LoRa Alliance
- **Range**: 2-5 km urban, 15 km rural
- **Modulation**: CSS (Chirp Spread Spectrum) - sweeping frequency
  - Cheaper than DSSS (no accurate sync)
  - FEC codes for resilience
- **Bands**: Sub-GHz ISM (868, 915, 433 MHz)
- **Data Rate**: 0.3 - 27 Kbps
- **Battery**: Years on small batteries

**LoRaWAN (MAC/Network Layer)**:
- Cloud-based MAC, centralized control via network server
- Devices transmit asynchronously to multiple gateways
- **Device Classes**:
  - **Class A**: Uplink first, downlink only after uplink (most energy-efficient)
  - **Class B**: Scheduled downlink windows
  - **Class C**: Almost always listening
- **Network Server**: Message consolidation, routing, control, supervision

#### NB-IoT (NarrowBand IoT)
**Characteristics**:
- **3GPP**: Release 13 (2016), Release 14 (2017)
- Based on LTE standard subset
- **Licensed** LTE bandwidth
- **Narrowband**: Single 180 kHz channel
- **MAC**:
  - Downlink: OFDMA (multi-user OFDM)
  - Uplink: SC-FDMA (single carrier, lower power)
- **Data Rate**:
  - Downlink: 26-127 Kbps
  - Uplink: 17-159 Kbps
- **Best for**: Stationary, energy-efficient applications

#### LTE-M (LTE Cat-M1)
**Characteristics**:
- **3GPP**: Release 12 (2015), 13 (2016), 14 (2017)
- Based on LTE standard
- **Licensed** LTE bandwidth (1.4 MHz)
- **Data Rate**: 1 Mbps (DL and UL)

**Differences from NB-IoT**:
- **Higher data rate**: 1 Mbps vs 26-159 Kbps
- **Higher mobility**: Full mobility with handovers
- **Higher bandwidth**: >1 MHz vs 180 kHz
- **Voice support**: VoLTE capable
- **Higher cost**
- **Use cases**: Wearables, trackers, VoLTE devices

**Comparison Summary**:
- **LoRa**: Unlicensed, longest range, lowest cost, proprietary
- **NB-IoT**: Licensed, best battery life, stationary devices
- **LTE-M**: Licensed, mobility support, voice capable, higher data rate

---

### Key Exam Points

**WLAN**:
- Know 802.11 standard evolution and key features
- Understand CSMA/CA mechanism and why CD doesn't work
- BSS vs ESS architecture
- Security progression: WEP → WPA → WPA2 → WPA3
- PHY parameters: channel width, MCS, spatial streams

**WPAN**:
- Bluetooth: piconet/scatternet structure, master-slave
- ZigBee: coordinator/router/device roles, topologies (star/mesh/tree)
- 6LoWPAN: IPv6 over constrained devices, header compression

**LPWAN**:
- LoRa/LoRaWAN: Proprietary, CSS modulation, unlicensed, device classes
- NB-IoT: 3GPP, licensed, narrowband (180 kHz), stationary
- LTE-M: 3GPP, licensed, wider bandwidth, mobility, voice

**Compare technologies**: Know trade-offs between range, data rate, power, cost, mobility

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
