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
*[TO BE COMPLETED]*

### Key Learning Questions:
- What are WiFi and 802.11?
- Physical and data link layer technologies for 802.11 versions?
- How does 802.11 architecture work?
- Different PAN technologies? Differences? Architectures?
- Different LPWAN technologies? Differences?

---

## Lecture 10: IoT Part 2 (Application Layer Protocols & Platforms)

### MQTT Protocol (Message Queuing Telemetry Transport)

**Architecture - Publish-Subscribe Mechanism**:
- **Publishers**: Produce data and send to broker
- **Subscribers**: Subscribe to topics of interest, receive notifications when new messages available
- **Broker**: Filters data based on topic and distributes to subscribers
  - Examples: Mosquitto, HiveMQ

**Key Characteristics**:
- **Publish/Subscribe paradigm** (vs Request/Response)
- **One-to-Many** communication pattern
- Clients don't know each other (decoupled)
- Every client can both publish AND subscribe
- **PUSH information paradigm** (broker pushes to subscribers)

**MQTT vs CoAP**:
- MQTT: PUSH-based, broker-centric, pub-sub model
- CoAP: PULL-based, request-response, no broker needed

---

### CoAP (Constrained Application Protocol)

**Purpose**: Enable web-based services in constrained wireless networks
- Designed for 8-bit microcontrollers
- Limited memory devices
- Low-power networks

**Key Characteristics**:
- **Request-Response interaction model** (similar to HTTP)
- Implements **REST** (Representational State Transfer)
- **PULL information paradigm** (client pulls from server)
- Resources identified by URIs
- Much lighter than HTTP for IoT devices

**CoAP Methods** (similar to HTTP):
- GET: Retrieve resource
- POST: Create resource
- PUT: Update resource
- DELETE: Remove resource

**CoAP Architecture Features**:
- **Proxying and Caching**: Cross-protocol proxy mechanisms enable HTTP-CoAP interactions
- Only supports limited subset of HTTP functionality
- Proxies provide data caching for efficiency

**CoAP vs HTTP**:
- CoAP: UDP-based, lightweight, designed for constrained devices
- HTTP: TCP-based, feature-rich, designed for traditional web

---

### IoT Platforms (Cloud-based)

**Basic Structure** (ISO/IEC JTC1):
1. **Things Layer**: Data gathering, discovery (Data → Information → Knowledge)
2. **Networking Layer**: Data transmission
3. **Platform Layer**: Computing, processing (Data → Information → Knowledge)
4. **User Layer**: Customer-facing, wisdom generation

**Four Essential Features**:

1. **Device Management**
   - Connect devices to the cloud
   - Configure devices remotely
   - Update firmware (OTA - Over-The-Air)
   - Monitor device health and status

2. **Data Management**
   - Store and retrieve data
   - Manage events
   - Visualize data
   - Share data across services

3. **Data Analysis/Automation**
   - Statistical analysis
   - Data mining
   - Machine learning
   - Event processing and rules engine

4. **Security**
   - Confidentiality (encryption)
   - Integrity (data and system protection)
   - Availability (system uptime)
   - Authenticity (identity verification)
   - Accountability (audit trails)

**Types of IoT Platforms**:

**Specialized Platforms**:
- Focus on one specific feature (e.g., device management)
- Device-specific functionality
- Strong security focus
- **Best for**: Connectivity management, device configuration, OTA firmware updates

**Generalized Platforms**:
- Many features implemented
- Two main approaches:
  - **Native IoT platforms**: Evolved from specialized platforms
  - **Cloud-based IoT platforms**: Traditional cloud solutions adapted for IoT
- Excellent data management
- Interface well with corporate IT solutions
- **Best for**: Data mining, machine learning, data fusion, event processing, rules engine

**Examples**:
- **Major Vendors**: IBM (Bluemix IoT), Microsoft (Azure IoT), Amazon (AWS IoT), Google (Cloud IoT), Intel
- **Specialized**: Thingspeak, The Things Network
- **Choice depends on application requirements**

---

### Exam-Relevant Comparisons

| Feature | MQTT | CoAP |
|---------|------|------|
| **Paradigm** | Publish-Subscribe | Request-Response |
| **Architecture** | Broker-based | Client-Server (no broker) |
| **Communication** | PUSH (broker to subscribers) | PULL (client requests) |
| **Pattern** | One-to-Many | One-to-One |
| **Coupling** | Clients decoupled | Direct client-server |
| **Use Case** | Event notification, telemetry | Resource access, device control |

**MQTT Advantages**:
- Efficient for event-driven data
- Scales well with many subscribers
- Clients don't need to know each other

**CoAP Advantages**:
- No broker needed (simpler architecture)
- RESTful (familiar web paradigm)
- Works with HTTP proxies
- Lightweight for constrained devices

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
