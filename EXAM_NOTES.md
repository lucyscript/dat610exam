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
A **computer network** is an interconnected collection of autonomous computers connected through:
- **Networking devices**: Gateways, routers, switches, bridges, hubs, repeaters
- **Communication links**: Wired (fiber optic, twisted pair, coax) or wireless
- **Purpose**: Resource sharing, communication, data exchange

---

## Network Types by Geographic Scope

| Type | Range | Characteristics |
|------|-------|----------------|
| **BAN** (Body Area Network) | On/around body | Wearable devices, medical sensors |
| **PAN** (Personal Area Network) | ~1-10m | Bluetooth, NFC |
| **LAN** (Local Area Network) | ~100m | WiFi, Ethernet in buildings |
| **MAN** (Metropolitan Area Network) | ~10km | City-wide networks |
| **WAN** (Wide Area Network) | >10km | Internet, cellular networks |

---

## Network Topologies ⭐ EXAM TOPIC

### Common Topologies

1. **BUS Topology**
   - Single shared communication line
   - All devices connected to the bus
   - Simple but single point of failure

2. **STAR Topology**
   - Central switch/hub
   - All devices connect to center
   - Centralized control, hub is critical point

3. **RING Topology**
   - Circular connection
   - Data flows in one direction
   - Token passing mechanism

4. **HIERARCHICAL/TREE Topology**
   - Multiple levels of switches/bridges
   - Scalable structure
   - Used in enterprise networks

5. **MESH Topology**
   - Multiple interconnections
   - High redundancy and fault tolerance
   - Complex but robust

### Topology Comparison

| Aspect | Centralized (Star) | Decentralized | Distributed (Mesh) |
|--------|-------------------|---------------|-------------------|
| **Points of Failure** | Few (central node) | Multiple | Many alternative paths |
| **Fault Tolerance** | Low | Medium | High |
| **Scalability** | Limited by center | Good | Excellent |
| **Ease of Development** | Easy | Medium | Complex |
| **Evolution/Diversity** | Limited | Good | Excellent |

---

## Switching Techniques ⭐ IMPORTANT

### Circuit Switching
- **Dedicated communication path** between source and destination
- **Three phases**:
  1. Circuit establishment
  2. Information transfer
  3. Circuit disconnect
- **Characteristics**:
  - Constant resource allocation
  - Predictable delay and jitter
  - Transparent but inefficient bandwidth use
- **Example**: PSTN (Public Switched Telephone Network)

### Packet Switching
- **No dedicated path** - packets routed independently
- **Datagram approach** (connectionless):
  - No call setup required
  - Each packet independent
  - Packets may take different routes
- **Characteristics**:
  - Efficient bandwidth utilization
  - Variable delay
  - Better for bursty traffic
- **Example**: Internet (IP)

**Key Difference**: Circuit switching reserves resources; packet switching shares resources dynamically

---

## Protocol Layering & OSI Model ⭐ EXAM TOPIC

### OSI 7-Layer Model

| Layer | Function | Protocols/Examples |
|-------|----------|-------------------|
| **7. Application** | User applications | HTTP, FTP, SMTP, POP |
| **6. Presentation** | Data format translation | Encryption, compression |
| **5. Session** | Session management | Connection establishment |
| **4. Transport** | End-to-end reliability, flow control | TCP, UDP |
| **3. Network** | Addressing, routing | IP, ICMP, IGMP |
| **2. Data Link** | MAC, error control, framing | Ethernet (802.3), WiFi (802.11) |
| **1. Physical** | Bit transmission on medium | Wireless, Fiber, Coax, TP |

### Challenges Addressed by Each Layer

**Link-Based Connection (Data Link)**:
- Representing 1s and 0s on medium (encoding)
- Fragmentation into frames
- Error detection and correction
- Flow control
- Medium Access Control (MAC)

**Network-Based Connection**:
- **Routing**: Finding paths through network
- **End-to-end reliability**: Ensuring data arrives
- **End-to-end flow control**: Preventing overflow
- **Congestion control**: Managing network load

### Protocol Encapsulation

```
Application:     [Data]
Transport:       [TH][Data]
Network:         [NH][TH][Data]
Data Link:       [MH][NH][TH][Data][MT]
```
- **Headers (H)** added at each layer
- **Trailer (T)** added at Data Link (e.g., CRC)

---

## Internet Protocol Suite ⭐ IMPORTANT

### Hourglass Architecture
```
Application Layer (many protocols)
    ↓
Transport Layer (TCP/UDP)
    ↓
Network Layer (IP) ← Waist of hourglass
    ↓
Data Link Layer (many technologies)
    ↓
Physical Layer (many media)
```

**Key Point**: IP is the unifying protocol that enables internetworking

### Protocol Stack Mapping

| OSI Layer | Internet Suite | Examples |
|-----------|---------------|----------|
| Application | Application | FTP, HTTP, SMTP, POP |
| Transport | Transport | TCP, UDP |
| Network | Internet | IP, ICMP, IGMP, ARP, RARP |
| Data Link | Network Access | IEEE 802.11, IEEE 802.3 |
| Physical | Physical | Wireless, F/O, TP, Coax |

---

## Networking Equipment ⭐ EXAM TOPIC

| Device | OSI Layer | Function |
|--------|-----------|----------|
| **Hub/Repeater** | Physical (1) | Signal amplification |
| **Bridge/Switch** | Data Link (2) | MAC-based forwarding |
| **Router** | Network (3) | IP-based routing between networks |

**Key Concept**: Higher-layer devices include lower-layer functionality

---

## Internetworking

### Definition
**Interconnection of networks** maintaining individual network identities
- Hierarchical: LAN → MAN → WAN
- Uses routers to connect networks
- IP provides unified addressing

### The Internet
- Global network of networks
- Uses Internet Protocol Suite (TCP/IP)
- Packet-switched, best-effort delivery

---

## Standardization Organizations

| Organization | Focus Area |
|--------------|-----------|
| **IETF** | Internet protocols (TCP/IP, HTTP) |
| **IEEE** | Wired & wireless communication (802.11, 802.3) |
| **ITU** | Telecommunication standards, PSTN |
| **ETSI** | European telecom standards |
| **ISO** | International standards (OSI model) |
| **3GPP** | 3G/4G/5G cellular standards |
| **5GPPP** | 5G research and development |

---

## Wireless Network Challenges ⭐ EXAM CRITICAL

### Additional Challenges Beyond Wired Networks

1. **Wireless Channel Issues**:
   - **High interference**: Co-channel, adjacent channel
   - **Limited coverage**: Path loss, obstacles
   - **Error prone**: Higher BER than wired
   - **User mobility**: Handoff, location tracking
   - **Variability**: Fading, multipath

2. **Impact on Protocol Layers**:
   - **Physical**: Signal propagation, modulation
   - **Data Link (MAC)**: Hidden/exposed terminal, CSMA/CA
   - **Data Link (LLC)**: Higher error rates need robust FEC/ARQ
   - **Network**: Routing in mobile/ad-hoc networks
   - **Transport**: TCP performance degradation

---

## Wireless Network Taxonomy ⭐ EXAM TOPIC

### By Range and Data Rate

| Category | Range | Technologies | Data Rate |
|----------|-------|-------------|-----------|
| **Short Range** | 1-10m | Bluetooth, NFC, ZigBee | 1 Kbps - 1 Mbps |
| **Medium Range** | ~100m | WiFi/802.11, Z-Wave | 10 Mbps - 1 Gbps |
| **Long Range** | 1-10+ km | Cellular (2G-5G), LoRa, NB-IoT, WiMax | 100 Kbps - 10 Gbps |

### By Infrastructure

#### Infrastructureless Networks
- **Ad Hoc Networks**: Temporary, self-organizing
- **Sensor Networks**: Data collection, monitoring
- **Mesh Networks**: Multi-hop, self-healing

#### Infrastructured Networks
- **Wireless LAN**: WiFi with access points
- **Wireless WAN**: Cellular networks (2G/3G/4G/5G)

### By Tier (Mobility Support)

| Type | Characteristics | Examples |
|------|----------------|----------|
| **High Tier** | Pedestrian + vehicular speeds, large coverage | Cellular networks |
| **Low Tier** | Pedestrian speeds only, short range | WiFi, Bluetooth |

### By Spectrum

| Type | Characteristics | Examples |
|------|----------------|----------|
| **Licensed** | Exclusive use, regulated | Cellular networks |
| **Shared** | Shared exclusive use (ASA) | Private 5G |
| **Unlicensed** | Open access, multiple technologies | WiFi, Bluetooth, ZigBee |

---

## Wireless Paradigms Comparison ⭐ EXAM IMPORTANT

### Ad Hoc vs Cellular Networks

| Aspect | Ad Hoc | Cellular |
|--------|--------|----------|
| **Infrastructure** | None | Fixed infrastructure (base stations) |
| **Topology** | Dynamic, may change often | Fixed infrastructure, mobile terminals |
| **Nodes** | Terminals relay traffic | Infrastructure nodes relay, terminals don't |
| **Links** | Multi-hop wireless | Single wireless hop to infrastructure |
| **Mobility** | Nodes fully mobile | Terminals mobile, infrastructure fixed |
| **Routing** | Dynamic routing required | Fixed routing in infrastructure |

### Ad Hoc Networking

**Characteristics**:
- Infrastructureless, multi-hop
- Self-forming and self-healing
- Dynamic topology

**Applications**:
- Disaster relief operations
- Temporary network deployment
- Military communications
- Smart buildings
- Cooperative objects

**Challenges**:
- Wireless medium issues
- Hidden/exposed terminal problems
- Mobility and node failures
- Self-configuration and topology maintenance
- Distributed routing
- Node localization and time synchronization
- End-to-end reliability in multi-hop

### Cellular Networking

**Characteristics**:
- Infrastructured, single-hop to base station
- Fixed base stations, mobile terminals
- Hierarchical architecture

**Architecture**:
- **Cell**: Geographic coverage area
- **Base Station Transceiver/Radio Port**: Wireless interface
- **Base Station Controller/Radio Port Controller**: Manages multiple base stations
- **Mobile Switching Center**: Core network connection

---

## Sensor & Actuator Networks

### Network Components
- **Sensor nodes (snodes)**: Collect data
- **Actuator nodes (anodes)**: Perform actions
- **Collector nodes (cnodes)**: Aggregate data
- **Gateway nodes (gnodes)**: Connect to external networks

### Design Factors

| Factor | Importance |
|--------|-----------|
| **Environment** | Often hostile, harsh, unreachable |
| **Fault Tolerance** | High - critical points of failure common |
| **Scalability** | Order of thousands of nodes |
| **Production Cost** | Must be cost-effective |
| **Hardware Constraints** | Tiny, low processing/memory capacity |
| **Power Consumption** | **VERY CRITICAL** - often battery-powered |
| **Topology** | Generally fixed, network mobility possible |

### Traffic Patterns
- One-to-many (task distribution)
- Many-to-one (data collection)
- Many-to-many (collaboration)
- Temporally and spatially correlated data

---

## Mesh Networks

### Architecture
- **Mesh Routers**: Form backbone, relay traffic
- **Mesh Clients**: End-user devices
- **Backbone Mesh**: Router-to-router connections
- **Access Mesh**: Client access to routers

### Integration
- Can integrate with cellular, WiFi, Internet
- Provides redundant paths
- Self-healing capabilities

### Applications
- Broadband home networking
- Community and neighborhood networking
- Enterprise networking
- Transportation systems
- Building automation

---

## Paradigm Comparison Table ⭐ EXAM TOPIC

| Factor | Ad Hoc | Mesh | Sensor & Actuator |
|--------|--------|------|-------------------|
| **Wireless Medium** | ISM | ISM | ISM, acoustic, low antenna |
| **Networking Regime** | Random 1-to-1 | Random 1-to-1, gateway | Many-to-1, many-to-many |
| **Traffic** | Random, multimedia | Random, multimedia | Correlated data |
| **QoS Requirements** | Bandwidth, delay, jitter | Bandwidth, delay, jitter | **Power**, delay, reliability |
| **Mobility** | Mobile | Typically fixed | Generally fixed |
| **Fault Tolerance** | No critical points | Critical points exist | High requirements |
| **Environment** | Day-to-day | Day-to-day | **Hostile, harsh** |
| **Power Efficiency** | Not very critical | Not critical | **VERY CRITICAL** |
| **Scalability** | Hundreds | Tens | **Thousands** |
| **Hardware** | Laptops, PDAs | No constraint | **Tiny, limited** |
| **Cost** | No constraint | No constraint | **Must be cheap** |

---

## Key Exam Topics Summary

1. **Network types** by geographic scope (BAN, PAN, LAN, MAN, WAN)
2. **Network topologies** (Bus, Star, Ring, Mesh, Tree) and trade-offs
3. **Circuit vs Packet switching** differences
4. **OSI 7-layer model** functions and protocols at each layer
5. **Protocol encapsulation** (headers/trailers)
6. **Internet Protocol Suite** hourglass architecture
7. **Networking equipment** operating at different layers
8. **Wireless challenges**: interference, mobility, error rates
9. **Wireless taxonomy**: by range, infrastructure, tier, spectrum
10. **Ad hoc vs Cellular** comparison
11. **Sensor network** design factors (especially power)
12. **Mesh network** architecture
13. **Standardization organizations** and their roles

---

### Key Learning Questions (Answered):

✓ **What is a computer network?**: Interconnected autonomous computers sharing resources through networking devices and links

✓ **Types of networks?**: BAN, PAN, LAN, MAN, WAN (by scope); Ad-hoc, Cellular, Sensor, Mesh (by paradigm)

✓ **How does communication work?**: Through protocol layering (OSI model) with encapsulation at each layer

✓ **Network challenges?**: Encoding, fragmentation, error control, flow control, MAC, routing, reliability, congestion control

✓ **How are challenges addressed?**: Protocol layering - each layer addresses specific challenges (protocols implement solutions)

✓ **Additional wireless challenges?**: High interference, limited coverage, error-prone channel, mobility, variability - impact ALL layers

✓ **Wireless network taxonomy?**: By range (short/medium/long), infrastructure (yes/no), tier (high/low), spectrum (licensed/unlicensed); Paradigms: ad-hoc, cellular, sensor, mesh

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

### Why Error Control is Critical in Wireless
**Problem**: High bit error rates in wireless due to interference, fading, multipath
- Frame error probability: P₂ = 1 - (1 - Pᵦ)^F
- Example: Pᵦ=10⁻⁵, F=2046 bits → P₂=0.02 (2% frame error rate!)
- **Need**: Both detection AND correction mechanisms

### Error Control Approaches
1. **FEC (Forward Error Correction)**: Add redundancy to correct errors at receiver
2. **BEC (Backward Error Correction)**: Detect errors + ARQ (retransmission)
3. **Hybrid ARQ**: Combine FEC + ARQ for optimal performance

---

## Error Detection Methods

### 1. Parity Check
- Single parity bit: detects odd number of bit errors
- **Limitation**: Cannot detect even number of errors (e.g., 2-bit errors)

### 2. Cyclic Redundancy Check (CRC) ⭐ IMPORTANT
**Process**:
- Data block D (k bits) + Pattern P (m bits) → Frame of n bits
- FCS (Frame Check Sequence) = n-k redundant bits
- Compute: Append (n-k) zeros to D, divide by P using XOR (modulo-2), remainder = FCS

**Example Calculation**:
```
D = 1101011011 (10 bits), P = 10011 (5 bits)
Append 4 zeros: 11010110110000
Divide by P using XOR → Remainder = 1110
Transmitted: 1101011011|1110
```

**Key Property**: Detects any number of bit errors with properly chosen P

---

## Automatic Repeat Request (ARQ)

### ARQ Components ⭐ EXAM TOPIC
1. **ACK/NAK**: Receiver sends acknowledgment (ACK) or negative ACK (NAK)
2. **Timeout**: Sender waits RTT (Round-Trip Time) before retransmitting
3. **Sequence Numbers**: Track frames (modulo K)
4. **Windows**: Buffer size at sender/receiver

### 1. Stop-and-Wait ARQ
- **Window**: Tx=1, Rx=1
- Send one frame → Wait for ACK → Send next
- **Sequence numbers**: K=2 (modulo 2)
- **Problem**: Poor utilization (waits full RTT between frames)

### 2. Go-Back-N ARQ ⭐ IMPORTANT
- **Window**: Tx=W, Rx=1
- Send W frames without waiting for ACK
- **Cumulative ACK**: ACK confirms all frames up to that sequence
- **Error handling**: NAK triggers retransmission from error point
- **Sequence numbers**: K = W+1
- **Problem**: Discards out-of-order frames (inefficient)

### 3. Selective Repeat ARQ ⭐ IMPORTANT
- **Window**: Tx=W, Rx>1
- Accepts out-of-order frames
- **Selective NAK**: Only retransmit specific errored frame
- **Sequence numbers**: K = 2W+1
- **Advantage**: Most efficient (only retransmits lost frames)

### Piggybacking
- Embed ACK in data frames for bidirectional traffic
- Reduces overhead

---

## Error Correction: Block Codes

### Key Concepts
- **(n, k) code**: k data bits → n codeword bits
- **Redundancy**: (n-k)/k
- **Code rate**: k/n (higher = less redundancy)
- **Hamming distance dₘᵢₙ**: Minimum bit differences between valid codewords

**Error Capabilities** ⭐ FORMULA
- **Detectable errors**: dₘᵢₙ - 1
- **Correctable errors**: t = ⌊(dₘᵢₙ - 1)/2⌋

### 1. Hamming Code
**Parameters**:
- n = 2^m - 1 (block length)
- k = 2^m - m - 1 (data bits)
- m = n - k (check bits)
- dₘᵢₙ = 3 (correct 1 bit, detect 2 bits)

**Key Features**:
- Check bits at positions: 1, 2, 4, 8, ... (powers of 2)
- **Syndrome word**: XOR of error positions → indicates error location
- **Rarely used** in practice (limited error correction)

**Example**: n=12 bits → m=4 check bits, k=8 data bits

### 2. Cyclic Codes (BCH, Reed-Solomon)
- **Reed-Solomon**: Most powerful cyclic code
- Well-suited for **burst error correction**
- Widely used in wireless systems

### 3. Low-Density Parity-Check (LDPC) Codes ⭐ EXAM TOPIC

**Definition**: Parity-check matrix H with very few 1s (low density)

**Regular LDPC Properties**:
1. Each code bit in wc parity constraints
2. Each row has wr 1s (constant)
3. Each column has wc 1s (constant)
4. wr << n and wc << m (low density)

**Decoding**: Iterative message-passing algorithm using **Tanner graph**
- Bit nodes (columns) ↔ Check nodes (rows)
- Exchange messages until constraints satisfied
- **Advantage**: Near Shannon-limit performance
- **Used in**: 4G LTE, 5G NR, WiFi

### 4. Polar Codes ⭐ 5G STANDARD
- **Recursive FEC**: Repeated XOR operations
- Codeword length = power of 2
- K data bits + (N-K) frozen bits (set to 0)
- **Encoding**: Simple XOR structure (G₂ blocks)
- **Decoding**: Successive cancellation algorithm
- **Advantage**: Efficient implementation
- **Performance**: Slightly worse than LDPC but simpler
- **Used in**: 5G NR control channels

---

## Error Correction: Convolutional Codes

### Parameters: (n, k, K)
- **k**: Input data bits processed at a time
- **n**: Output bits generated from k inputs
- **K**: Constraint length (memory = K-1 previous blocks)
- **Code rate**: k/n

### Encoding
- **Shift register** with XOR operations
- Output depends on current + (K-1) previous inputs
- **State**: K-1 past values

**Example (2,1,3)**:
- Input: 1 bit at a time
- Output: 2 bits
- Memory: 2 previous bits
- States: 2² = 4 states (00, 01, 10, 11)

### State Diagram & Trellis
- **State diagram**: Shows all possible state transitions
- **Trellis diagram**: State diagram unfolded over time
- Used for Viterbi decoding

### Viterbi Algorithm ⭐ IMPORTANT
- Finds **most likely input** that produced received output
- **Metric**: Hamming distance
- Traces through trellis to find minimum-distance path
- **Decoding window**: Process b bits at a time

---

## Turbo Codes ⭐ 3G/4G STANDARD

### Architecture
- **Two parallel RSC encoders** (Recursive Systematic Convolutional)
- **Interleaver**: Permutes input between encoders
- Original data preserved (systematic)
- Each encoder produces 1 check bit

### Features
- **Puncturing**: Remove bits to adjust code rate (1/3 → 1/2)
- **Iterative decoding**: Multiple passes for high confidence
- **Performance**: Very close to Shannon limit
- **Used in**: 3G, 4G LTE

**Drawback**: Decoding delay due to iterations

---

## Block Interleaving

**Purpose**: Spread burst errors across multiple blocks

**Process**:
- Write data by rows into m×n matrix
- Read out by columns
- Burst error of length B → distributed across B different blocks
- Combined with FEC: better burst error tolerance

---

## Hybrid ARQ (HARQ) ⭐ EXAM TOPIC

### Why HARQ?
- **FEC alone**: Wastes bandwidth in good channel conditions
- **ARQ alone**: Excessive delay in bad channel conditions
- **Solution**: Adaptive combination

### Type-I HARQ
- Use FEC to correct common errors
- ARQ retransmission when FEC fails
- Same codeword retransmitted

### Type-II HARQ (Incremental Redundancy)
- First transmission: Low redundancy (error detection only)
- Retransmissions: Incrementally add FEC redundancy
- **Chase combining**: Keep previous errored frames, combine with retransmissions
- **Puncturing**: Remove bits instead of changing code

**Advantages**:
- Adapts to channel quality
- Efficient bandwidth usage
- Used in LTE and 5G

---

## ARQ vs FEC Trade-offs

### ARQ Advantages ✓
- Simple implementation
- No bandwidth overhead in good conditions
- Adapts to channel quality

### ARQ Disadvantages ✗
- High delay in poor conditions
- Inefficient for high BER
- Not suitable for real-time (voice, video)

### FEC Advantages ✓
- No retransmission delay
- Good for broadcast/multicast
- Suitable for real-time applications

### FEC Disadvantages ✗
- Always adds overhead (even when not needed)
- Complex encoding/decoding
- Limited error correction capability

### HARQ Solution ⭐
- Combines benefits of both
- Adapts redundancy to channel conditions
- Industry standard (LTE, 5G)

---

## Exam-Critical Formulas

### Shannon's Capacity (Theoretical Limit)
```
C = B log₂(1 + SNR)
```

### Frame Error Probability
```
P₂ = 1 - (1 - Pᵦ)^F
```

### Hamming Code Parameters
```
n = 2^m - 1
k = 2^m - m - 1
dₘᵢₙ = 3
```

### Error Capabilities
```
Detectable errors: dₘᵢₙ - 1
Correctable errors: ⌊(dₘᵢₙ - 1)/2⌋
```

### ARQ Sequence Numbers
```
Stop-and-wait: K = 2
Go-back-N: K = W + 1
Selective repeat: K = 2W + 1
```

---

## Coding Schemes in Wireless Standards

| Standard | Error Detection | FEC | ARQ |
|----------|----------------|-----|-----|
| **3G** | CRC | Turbo Codes | HARQ Type-II |
| **4G LTE** | CRC | Turbo Codes, LDPC | HARQ Type-II |
| **5G NR** | CRC | LDPC (data), Polar (control) | HARQ Type-II |
| **WiFi 6** | CRC | LDPC | MAC-level retransmission |

---

## Key Exam Topics Summary

1. **CRC calculation** (modulo-2 division with XOR)
2. **ARQ types** (Stop-and-wait, Go-back-N, Selective Repeat)
3. **Hamming code** calculation and syndrome
4. **LDPC vs Hamming** comparison
5. **Polar codes** structure (5G relevance)
6. **Convolutional encoding** (shift registers, state diagrams)
7. **Viterbi algorithm** concept
8. **Turbo codes** architecture (two encoders + interleaver)
9. **HARQ types** and advantages
10. **ARQ vs FEC trade-offs**

---

### Key Learning Questions (Answered):
✓ **Importance of error detection/correction in wireless**: High BER requires robust error control
✓ **Different approaches**: FEC (proactive), ARQ (reactive), HARQ (hybrid)
✓ **Error detection methods**: Parity (simple), CRC (robust)
✓ **ARQ versions**: Stop-and-wait (simple), Go-back-N (efficient), Selective Repeat (optimal)
✓ **Error correction methods**: Block codes (Hamming, LDPC, Polar), Convolutional, Turbo
✓ **ARQ vs FEC**: ARQ=low overhead but delay; FEC=no delay but overhead; HARQ=best of both

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
