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

### What is a Computer Network?
- **Definition**: Collection of interconnected devices (end systems) connected via network equipment (routers, switches, bridges, hubs, repeaters)
- **Purpose**: Enable communication and resource sharing between devices

### Network Types by Coverage
- **BAN (Body Area Network)**: Personal devices on/around body
- **PAN (Personal Area Network)**: ~1-10m range
- **LAN (Local Area Network)**: ~100m range
- **MAN (Metropolitan Area Network)**: City-wide coverage
- **WAN (Wide Area Network)**: Large geographical areas (1-10+ km)

### Network Topologies
**Physical Arrangements**:
- **Bus**: Single shared cable, hub/bus connection
- **Star**: Central switch, point-to-point connections
- **Ring**: Circular connection pattern
- **Hierarchical/Tree**: Layered structure with switches/bridges
- **Mesh**: Multiple interconnected paths (routers)

**Topology Characteristics**:
- **Centralized**: Single point of failure, easy development
- **Decentralized**: Multiple control points, better fault tolerance
- **Distributed**: No central control, maximum fault tolerance, high diversity

### Communication in Networks

**Circuit Switching** (PSTN):
- Dedicated communication path
- Three phases: Circuit establishment → Information transfer → Circuit disconnect
- Constant resource allocation (low delay/jitter)
- Transparent but inefficient

**Packet Switching** (Internet):
- No dedicated path/resource
- Data sent as packets (header + payload)
- **Datagram approach** (connectionless): No call setup, each packet independent
- More efficient resource utilization

### Network Challenges & Solutions

**Link-Based Challenges**:
- Representing 1s and 0s on medium → Physical layer
- Fragmentation → Data Link layer
- Error detection and correction → LLC sublayer
- Flow control → Data Link/Transport layer
- Medium Access Control (MAC) → MAC sublayer

**Network-Wide Challenges**:
- Routing → Network layer
- End-to-end reliability → Transport layer
- End-to-end flow control → Transport layer
- Congestion control → Transport layer

### Protocol Layering

**OSI Model (7 Layers)**:
1. **Physical**: Representing bits on medium
2. **Data Link**: MAC, synchronization, error control, flow control
3. **Network**: Addressing, routing
4. **Transport**: Reliability, flow and congestion control
5. **Session**: Establishing, managing, terminating sessions
6. **Presentation**: Syntax differences
7. **Application**: Applications

**Internet Protocol Suite (5 Layers)**:
1. **Physical**: Medium-specific transmission
2. **Data Link**: IEEE 802.11 (wireless), IEEE 802.3 (Ethernet)
3. **Network**: IP (hour glass model - single protocol)
4. **Transport**: TCP (reliable), UDP (unreliable)
5. **Application**: FTP, HTTP, SMTP, POP

**Key Concepts**:
- **Encapsulation**: Adding headers at each layer (sender side)
- **Decapsulation**: Removing headers at each layer (receiver side)
- **Hour Glass Model**: IP as the narrow waist - enables interoperability

### Networking Equipment by Layer
- **Physical**: Repeater, Hub
- **Data Link (MAC)**: Bridge, Switch
- **Network**: Router

### Wireless Network Challenges
**Beyond wired network challenges**:
- **High Interference**: Shared medium, electromagnetic interference
- **Limited Coverage**: Signal attenuation with distance
- **Error Prone**: Higher bit error rates than wired
- **User Mobility**: Changing topology, handoffs
- **Variability**: Channel conditions change over time/location

**Impact on Protocols**:
- Physical layer: Signal propagation, modulation
- MAC layer: Shared medium access, hidden/exposed terminals
- LLC: Higher error rates require robust error control
- Network layer: Mobility support, routing in dynamic topology
- Transport layer: TCP performance issues

### Wireless Network Taxonomy

**By Range and Technology**:
- **Long Range**: Cellular (2G-5G), WiMax, LPWAN
- **Medium Range**: Wi-Fi (802.11), Z-Wave
- **Short Range**: Bluetooth, NFC, ZigBee

**By Infrastructure**:
- **Infrastructureless**: Ad-hoc, Sensor, Mesh networks
- **Infrastructured**: Wireless LAN, Cellular WAN

**By Tier**:
- **High Tier**: Pedestrian + vehicular speeds, large coverage (cellular)
- **Low Tier**: Pedestrian speeds only, short range (WiFi, Bluetooth)

**By Spectrum**:
- **Licensed**: Exclusive use (cellular networks)
- **Shared**: Authorized Shared Access (ASA)
- **Unlicensed**: ISM bands (WiFi, Bluetooth, ZigBee)

### Ad-hoc Networks
**Characteristics**:
- Infrastructureless, multihop communication
- Mobile nodes can relay traffic
- Dynamic topology
- All links wireless

**Applications**:
- Temporary network deployment
- Disaster relief operations
- Smart buildings
- Cooperative objects
- Healthcare

**Challenges**:
- Wireless medium issues
- Interference, Hidden/Exposed terminal problems
- Mobility and node failures
- Self-forming, self-configuration, self-healing
- Topology maintenance and routing
- Node localization and time synchronization

### Cellular Networks
**Characteristics**:
- Fixed infrastructure, single hop
- Terminal nodes don't relay traffic
- Wireless access link, wired/wireless backbone

**Architecture**:
- **Cell**: Coverage area
- **Base Station Transceiver/Radio Port**: Wireless interface
- **Base Station Controller/Radio Port Controller**: Cell management
- **Mobile Switching Center**: Network coordination

### Sensor & Actuator Networks
**Characteristics**:
- One-to-many, many-to-one, many-to-many communication
- Temporally and spatially correlated data
- Generally fixed nodes (network mobility possible)
- Very critical power efficiency
- Order of thousands of nodes
- Tiny, low processing/memory capacity
- Must be cost effective
- Often operate in hostile/harsh environments

**Design Factors** (CRITICAL):
- Environment and operating conditions
- Fault tolerance requirements
- Scalability (thousands of nodes)
- Production cost constraints
- Hardware constraints
- Power consumption (most critical)
- Topology changes

### Mesh Networks
**Components**:
- **Mesh Routers**: Form backbone mesh
- **Mesh Clients**: Connect to access mesh
- **Gateway Nodes**: Connect to Internet/other networks

**Types**:
- **Backbone Mesh**: Router-to-router infrastructure
- **Access Mesh**: Client access to infrastructure

**Applications**:
- Broadband home networking
- Community/neighborhood networking
- Enterprise networking
- Transportation systems
- Building automation

### Comparison: Ad-hoc vs Mesh vs Sensor

| Factor | Ad-hoc | Mesh | Sensor |
|--------|--------|------|---------|
| **Infrastructure** | None | Gateway nodes | Collector/gateway nodes |
| **Mobility** | Mobile | Typically fixed | Fixed (network mobility) |
| **Scalability** | Hundreds | Tens | Thousands |
| **Power** | Not critical | Not critical | **Very critical** |
| **Hardware** | Laptops, PDAs | No constraints | Tiny, limited resources |
| **QoS Focus** | Bandwidth, delay, jitter | Bandwidth, delay, jitter | **Power, delay, reliability** |
| **Traffic** | Random, multimedia | Random, multimedia | Correlated data |
| **Cost** | No constraints | No constraints | **Must be cost effective** |

### Ad-hoc vs Cellular

| Aspect | Ad-hoc | Cellular |
|--------|--------|----------|
| **Infrastructure** | None | Fixed infrastructure |
| **Topology** | May change often | Infrastructure rarely changes |
| **Node Function** | Terminals relay traffic | Infrastructure nodes relay, terminals don't |
| **Links** | Mostly wireless, multihop | Wireless access + wired/wireless backbone |

### EXAM-CRITICAL Formulas & Concepts
- **Protocol layers**: Know which layer handles what function
- **Encapsulation/Decapsulation**: Header addition/removal at each layer
- **Packet vs Circuit switching**: Key differences and applications
- **Wireless challenges**: Know what makes wireless different from wired
- **Network taxonomy**: Classification by range, infrastructure, tier, spectrum
- **Design factors**: Environment, fault tolerance, scalability, power, cost

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
