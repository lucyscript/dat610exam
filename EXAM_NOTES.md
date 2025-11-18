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

### Part 2: 5G Networks (EXAM CRITICAL)

#### 5G Core Network Architecture
**Two Representations:**
- **Service-based**: Shows how services are exposed by NFs through network interfaces
- **Reference point**: Shows direct interactions between NFs

**Key Network Functions (NFs):**
- **AMF** (Access & Mobility Management): UE authentication, authorization, mobility management
- **SMF** (Session Management): PDU session establishment, management, release between UE and DN
- **UPF** (User Plane Function): Packet routing/forwarding, QoS handling, IP mobility anchoring
- **AUSF** (Authentication Server): Data storage for UE authentication
- **UDM** (Unified Data Management): UE subscription data storage
- **PCF** (Policy Control): QoS policy rules control and management
- **NRF** (Network Repository): Registration and discovery of NF services
- **NSSF** (Network Slice Selection): Selects network slice instances for UE requests
- **NEF** (Network Exposure): Interface for external applications
- **AF** (Application Function): Provides session-related info to PCF

**Control Plane vs User Plane Separation** - Key 5G feature for flexibility

#### 5G RAN Architecture
**Components:**
- **gNodeB (gNB)**: 5G base station - terminates UP and CP protocols
- **ng-eNB**: 4G base station connected to 5GC
- **NG-RAN**: 5G Radio Access Network
- **Interfaces**: NG (to 5GC), Xn (inter-gNB)

**Functional Split:**
- **Central Unit (CU)**: Non-real-time protocols and services
- **Distributed Units (DUs)**: Physical layer and real-time services
- One DU connects to one CU (can have secondary CU for reliability)

#### 5G NR Air Interface (CRITICAL FOR EXAM)

**Frequency Ranges:**
- **FR1**: 410 MHz – 7,125 MHz (sub-6 GHz)
- **FR2**: 24,250 MHz – 71,000 MHz (mmWave)

**Modulation Schemes (Adaptive Modulation and Coding - AMC):**
- **Uplink**: π/2-BPSK, QPSK, 16-QAM, 64-QAM, 256-QAM
- **Downlink**: QPSK, 16-QAM, 64-QAM, 256-QAM
- **π/2-BPSK**: BPSK variant with low peak-to-average power ratio

**Key Technologies:**
- **Massive MIMO and Beamforming**: Multiple antennas for increased capacity
- **FDD/TDD**:
  - FDD: Symmetric traffic, less interference, rural/suburban areas, <10 GHz
  - TDD: Asymmetric traffic, better for MIMO/beamforming, urban areas, >10 GHz
- **Waveforms**:
  - **CP-OFDM**: Both UL/DL, cyclic prefix, good for multi-antenna, high spectral efficiency
  - **DFT-S-OFDM**: UL only, lower peak-to-average power ratio, robust to fading
- **Numerology**: Flexible subcarrier spacing (15, 30, 60, 120, 240 kHz) - higher frequencies use larger spacing

**Error Control:**
- **LDPC Codes**: For data plane (PDSCH, PUSCH) - quasi-cyclic structure, hardware-friendly
- **Polar Codes with CRC**: For control plane (PDCCH, PUCCH, PBCH) - lower complexity/latency
- **HARQ**: Hybrid ARQ with incremental redundancy

#### Enabling Technologies of 5G (VERY IMPORTANT)

**1. Software-Defined Networking (SDN):**
- **Separates control plane from data plane**
- Control plane logically centralized in software-based controller
- **Benefits**: Simplified algorithms, commodity hardware, programmability, multi-vendor support
- **Southbound Interface**: e.g., OpenFlow (controller to switches)
- **Northbound Interface**: REST APIs (applications to controller)

**2. Network Function Virtualization (NFV):**
- **Decouples network functions from proprietary hardware**
- **VNF** (Virtual Network Function): Software implementation of network function
- **NFVI** (NFV Infrastructure): Provides virtualized resources (compute, storage, network)
- **MANO** (Management and Orchestration):
  - **NFVO**: NS lifecycle, resource orchestration
  - **VNFM**: VNF lifecycle management
  - **VIM**: Manages virtualized resources
- **Benefits**: Reduced CapEx/OpEx, faster service deployment, flexibility, scalability

**3. Network Slicing:**
- **Multiple logical networks on shared infrastructure**
- Enabled by SDN + NFV
- Supports different service requirements:
  - **eMBB** (enhanced Mobile Broadband): High data rates
  - **mMTC** (massive Machine Type Communications): Many low-power devices
  - **URLLC** (Ultra-Reliable Low-Latency): <1ms latency, 99.999% reliability
- **Components**: VNF Forwarding Graph (VNFFG), NFVI-PoP

**4. Multi-access Edge Computing (MEC):**
- **Computing resources at network edge** (close to users/data sources)
- **Benefits**: Reduced latency, context awareness, cloud offloading, reduced backhaul traffic
- **Architecture**:
  - **MEC Host**: Contains MEP (platform) and virtualization infrastructure
  - **MEP** (MEC Platform): Provides environment for MEC apps, hosts services, traffic routing
  - **MEC Apps**: Discover/consume MEC services
  - **System-level**: MEO (orchestrator), OSS, User app LCM proxy
  - **Host-level**: MEPM (platform manager), VIM
- **MEC-in-NFV**: MEP and MEC Apps are VNFs; MEO = MEAO + NFVO
- **5G-MEC Deployment**: Can place MEC hosts at various points (with UPF, at NAP, in CN, distributed)

#### 5G Deployment Options (EXAM RELEVANT)
**Migration Strategy from 4G to 5G:**
- **Option 3**: NSA (Non-Standalone) - LTE master + NR secondary, connected to EPC (initial deployment)
- **Option 2**: SA (Standalone) - NR connected to 5GC
- **Option 4**: NSA - NR master + LTE secondary, connected to 5GC
- **Option 5**: SA - LTE connected to 5GC
- **Option 7**: NSA - LTE master + NR secondary, connected to 5GC

**Typical Migration Path**: Option 3 → Option 4/5/7 → Full 5G SA

**5G Core Benefits:**
- Native network slicing support
- Native MEC support
- Native URLLC support
- Service-based architecture

#### Virtualized RAN (vRAN)
- **Decouples RAN hardware and software**
- RAN functions run as VNFs on COTS or custom hardware
- **Full virtualization**: All units (RU, DU, CU) on cloud platforms
- **Partial virtualization**: Some units on bare metal
- **Benefits**: Flexibility, vendor independence, cost reduction

#### Network Disaggregation & Decomposition
- **Disaggregation**: Separates hardware and software vendors → eliminates vendor lock-in
- **Decomposition**: Splits gNB into CU and DU with standard interfaces
- **Enables**: Multi-vendor deployment, virtualization, use of COTS servers

### Key Learning Questions (Part 2):
- Architecture of 5G and new features? ✓
- Principles and characteristics of 5G Core Network and RAN? ✓
- Technologies used in 5G NR Air Interface? ✓
- Enabling technologies of 5G? ✓
- How can 5G be deployed? ✓
- New challenges in 5G? ✓

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
