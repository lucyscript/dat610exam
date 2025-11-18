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

### Part 3: 5G RAN Deployment and Orchestration (EXAM CRITICAL)

#### RAN Architecture Components
**Key Terminology**:
- **RU (Radio Unit)**: Handles radio frequency transmission/reception
- **DU (Distributed Unit)**: Processes lower-layer protocols (real-time)
- **CU (Central Unit)**: Processes higher-layer protocols (non-real-time)
- **BBU (BaseBand Unit)**: Unit that processes baseband signals
- **RRU (Remote Radio Unit)**: Remote radio unit separated from BBU

**Network Segments**:
- **Fronthaul**: Connection between RU and DU
- **Midhaul**: Connection between DU and CU (F1 interface)
- **Backhaul**: Connection between CU and 5G Core (NG interface)

#### 5G RAN Deployment Scenarios (VERY IMPORTANT)

1. **Independent RRU, CU, and DU locations**
   - All components separated
   - Maximum flexibility but complex connectivity
   - Fronthaul → DU → Midhaul → CU → Backhaul → 5GC

2. **RU and DU Integration**
   - RU and DU co-located
   - Simplifies fronthaul
   - Midhaul → CU → Backhaul → 5GC

3. **Co-located CU and DU**
   - BBU contains both CU and DU
   - Remote RU (RRU)
   - Fronthaul → BBU → Backhaul → 5GC

4. **RRU, DU, and CU Integration**
   - Fully integrated basestation
   - Simplest deployment
   - Direct Backhaul → 5GC
   - Similar to traditional architecture

**Common Arrangement**: BBU containing both CU and DU functionality, with one or more RUs (collocated or remote RRUs)

#### Key Challenges in 5G (EXAM TOPIC)

**Primary Challenge**: Need for **intelligence to manage and orchestrate complexity**
- 5G networks are highly complex with many components
- Dynamic resource allocation required
- AI/ML needed for automation and optimization

#### Resource Orchestration (CRITICAL CONCEPT)

**Three Resource Categories**:

1. **Data Resources**:
   - Computing resources (processing power)
   - Storage resources (data storage capacity)

2. **Network Resources**:
   - Interconnectivity (transport network capacity)
   - Access (radio access network resources)

3. **User Mobility**:
   - Handoff management
   - Service continuity across cells

**Three Key Requirements** (Know these well):

1. **Security** 🔒
   - Protect against unauthorized access
   - Secure data and network resources
   - Critical for multi-tenant environments

2. **Dependability** 💎
   - Reliability (correct operation)
   - Availability (service uptime)
   - Resilience to failures

3. **Performance** 🚀
   - Low latency
   - High throughput
   - Efficient resource utilization

#### How 5G Can Be Deployed (Answer to Learning Question)

Based on deployment scenarios:
- **Centralized deployment**: CU/DU at central location, RRUs distributed
- **Distributed deployment**: Independent RU, DU, CU locations for flexibility
- **Integrated deployment**: Full integration at cell sites
- **Hybrid deployment**: Mix of above based on requirements

**Trade-offs**:
- Centralized: Better resource sharing, more complex transport
- Distributed: Maximum flexibility, higher complexity
- Integrated: Simpler, less flexible for optimization

#### New Challenges in 5G (Answer to Learning Question)

1. **Complexity Management**
   - Multiple deployment options
   - Dynamic network topologies
   - Heterogeneous technologies

2. **Orchestration and Automation**
   - Need AI/ML for intelligent resource allocation
   - Dynamic service placement
   - Multi-access edge computing (MEC)

3. **Meeting Requirements Simultaneously**
   - Security AND performance
   - Dependability AND flexibility
   - Cost efficiency AND quality

4. **Network Slicing**
   - Isolation between slices
   - Resource allocation per slice
   - Security per slice

5. **Edge Computing Integration**
   - Placing compute at network edge
   - Service migration
   - Latency requirements

---

### Exam Preparation Notes for Lecture 6 Part 3:

**High-Probability Exam Questions**:
1. Explain the different 5G RAN deployment scenarios and their trade-offs
2. What are the three key requirements for resource orchestration in 5G?
3. Describe the main challenges in 5G networks
4. Explain the difference between fronthaul, midhaul, and backhaul
5. What resources need to be orchestrated in 5G? (data, network, user mobility)

**Key Points to Remember**:
- RU/DU/CU architecture provides flexibility in 5G deployment
- Four main deployment scenarios from fully distributed to fully integrated
- Orchestration requires balancing security, dependability, and performance
- Intelligence (AI/ML) needed to manage 5G complexity
- Resources span computing, storage, connectivity, and mobility

**Terminology to Master**:
- RU, DU, CU, BBU, RRU
- Fronthaul, Midhaul, Backhaul
- Orchestration, MEC (Multi-access Edge Computing)
- Network slicing

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
