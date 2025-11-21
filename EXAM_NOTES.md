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

### 1. Shared Medium Access Problem

**The Problem**: Multiple users sharing same wireless channel need coordination to avoid collisions
- Wireless is a **broadcast medium** - all nodes can hear each other (in range)
- **Collisions** occur when two transmissions overlap → data lost
- Need **Medium Access Control (MAC)** protocols to coordinate access

---

### 2. Multiple Access Schemes Classification ⭐ EXAM IMPORTANT

| Category | Approach | Examples |
|----------|----------|----------|
| **Contention-based** | Compete for channel, handle collisions | ALOHA, CSMA, CSMA/CD, CSMA/CA |
| **Conflict-free** | Pre-allocate resources, no collisions | FDMA, TDMA, CDMA, OFDMA |
| **Hybrid** | Combine both approaches | PRMA, D-TDMA, RAMA |

**Fixed vs Random Access**:
- **Fixed assignment**: Deterministic, guaranteed access, may waste capacity
- **Random access**: Dynamic, efficient for bursty traffic, risk of collisions

---

### 3. ALOHA Protocols

**Pure ALOHA**:
- Transmit whenever data available
- If collision → wait random time, retransmit
- **Throughput**: S = G·e^(-2G), max ~18.4% at G=0.5

**Slotted ALOHA**:
- Time divided into slots; transmit only at slot boundaries
- **Throughput**: S = G·e^(-G), max ~36.8% at G=1
- Double the efficiency of pure ALOHA

---

### 4. CSMA (Carrier Sense Multiple Access) ⭐ EXAM CRITICAL

**Key Principle**: "Listen before talk" - sense channel before transmitting

#### CSMA Variants:

| Version | Behavior when Channel Busy | Behavior when Channel Idle | Efficiency |
|---------|---------------------------|---------------------------|------------|
| **1-persistent** | Wait until idle, transmit immediately | Transmit with probability 1 | High collision risk |
| **Non-persistent** | Wait random time, then sense again | Transmit immediately | Lower collision, higher delay |
| **p-persistent** | Wait until idle | Transmit with probability p; defer with (1-p) | Balanced approach |

**Why multiple versions?** Trade-off between:
- **Delay** (how long to wait)
- **Collision probability** (risk of simultaneous transmission)

---

### 5. CSMA/CD (Collision Detection) ⭐ EXAM TOPIC

**Used in**: Wired Ethernet (802.3)

**Key Concept**: Detect collision while transmitting, abort immediately

**Algorithm**:
1. Sense channel (carrier sense)
2. If idle → transmit
3. **While transmitting, monitor for collision**
4. If collision detected → abort, send jam signal
5. Wait random backoff time, retry

**Minimum Frame Size**: Must be large enough to detect collision
- **t = 2τ** (round-trip propagation delay)
- Frame transmission time must be ≥ 2τ

**Binary Exponential Backoff**:
- After collision k: wait random time in [0, 2^k - 1] × slot_time
- Maximum k = 10, then give up after 16 attempts

**Why NOT used in wireless?**
- Cannot detect collision while transmitting (transmitter overwhelms receiver)
- Hidden terminal problem makes detection unreliable

---

### 6. CSMA/CA (Collision Avoidance) ⭐⭐ VERY EXAM IMPORTANT

**Used in**: WiFi (802.11), wireless networks

**Key Concept**: Avoid collisions rather than detect them

#### Basic DCF (Distributed Coordination Function):

```
DIFS → Data → SIFS → ACK
```

- **DIFS** (DCF InterFrame Space): Wait period before transmitting
- **SIFS** (Short InterFrame Space): Short wait for ACK (higher priority)
- **NAV** (Network Allocation Vector): Virtual carrier sensing timer

#### RTS/CTS Mechanism (Solves Hidden Terminal):

```
Sender: DIFS → RTS → [wait]
Receiver:        SIFS → CTS → [wait]
Sender:                 SIFS → Data → [wait]
Receiver:                      SIFS → ACK
```

- **RTS** (Request to Send): Sender requests channel
- **CTS** (Clear to Send): Receiver grants permission
- All nodes hearing RTS/CTS set NAV → defer transmission

---

### 7. Hidden and Exposed Terminal Problems ⭐⭐ EXAM CRITICAL

#### Hidden Terminal Problem:

```
    A ←→ B ←→ C
    (A and C cannot hear each other)
```

- **Problem**: A transmits to B; C cannot sense A's transmission
- C thinks channel is idle, transmits → **collision at B**
- **Solution**: RTS/CTS handshake
  - C hears CTS from B → knows to wait

#### Exposed Terminal Problem:

```
    A ← B → C → D
    (B transmitting to A; C wants to transmit to D)
```

- **Problem**: C senses B's transmission to A
- C defers even though transmitting to D would NOT cause collision
- **Result**: Unnecessary waiting, reduced throughput
- **Note**: RTS/CTS does NOT fully solve this

---

### 8. CDMA (Code Division Multiple Access) ⭐ EXAM TOPIC

**Key Concept**: All users transmit simultaneously on same frequency using unique codes

#### Spread Spectrum Techniques:

**FHSS (Frequency Hopping Spread Spectrum)**:
- Transmitter/receiver hop between frequencies in synchronized pattern
- Pattern determined by **pseudonoise (PN) sequence**

**DSSS (Direct Sequence Spread Spectrum)**:
- Each bit multiplied by spreading code (chips)
- Signal spread across wider bandwidth
- **Processing Gain**: PG = chip rate / data rate

#### PN Sequence Properties (EXAM IMPORTANT):

1. **Balance**: Equal number of 1s and 0s (differ by at most 1)
2. **Run property**: Half of runs length 1, quarter length 2, etc.
3. **Autocorrelation**: High peak at zero shift, low elsewhere

**Maximum Length Sequence (m-sequence)**:
- Generated by Linear Feedback Shift Register (LFSR)
- Period: **p = 2^n - 1** (n = number of registers)

#### Orthogonal Codes (Walsh-Hadamard):

- **Orthogonality**: Cross-correlation = 0
- Each user assigned unique code
- Receiver can separate users by correlation with known code

**Walsh-Hadamard Matrix Construction**:
```
H₁ = [1]
H₂ₙ = | Hₙ   Hₙ  |
      | Hₙ  -Hₙ  |
```

---

### 9. OFDM (Orthogonal Frequency Division Multiplexing) ⭐ EXAM IMPORTANT

**Key Concept**: Divide wideband channel into many narrow orthogonal subcarriers

**Orthogonality**:
- Subcarriers spaced at 1/Ts (Ts = symbol duration)
- Peak of one subcarrier aligns with nulls of others
- Allows overlap without interference

**Implementation**:
- **Transmitter**: IFFT (converts frequency domain → time domain)
- **Receiver**: FFT (converts time domain → frequency domain)

**Cyclic Prefix (Guard Interval)**:
- Copy end of symbol to beginning
- **Eliminates ISI** (Inter-Symbol Interference) from multipath
- Trade-off: Reduces spectral efficiency

**PAPR (Peak-to-Average Power Ratio) Problem**:
- OFDM has high PAPR due to multiple subcarrier summation
- Requires linear amplifiers (less power efficient)

---

### 10. OFDMA (Orthogonal Frequency Division Multiple Access)

**Key Concept**: OFDM + multi-user access via subcarrier allocation

- Divide subcarriers into **subchannels**
- Assign different subchannels to different users
- Users can be allocated based on channel conditions

**Advantages**:
- Flexible resource allocation
- Multi-user diversity gain
- Efficient for varying traffic patterns

---

### 11. SC-FDMA (Single Carrier FDMA) ⭐ EXAM TOPIC

**Used in**: LTE uplink, 5G NR uplink

**Key Difference from OFDMA**:
- Adds **DFT precoding** before IFFT
- Results in **lower PAPR** than OFDMA
- More power efficient for mobile devices (important for battery)

**Why used in uplink?**
- Mobile devices have limited battery/power
- Lower PAPR = more efficient power amplifier usage

---

### 12. CDMA vs OFDMA Comparison ⭐ EXAM TOPIC

| Aspect | CDMA | OFDMA |
|--------|------|-------|
| **Multiplexing** | Code domain | Frequency domain |
| **Interference** | All users interfere (managed by codes) | Orthogonal subcarriers (no interference) |
| **Near-far problem** | Significant (needs power control) | Less severe |
| **Flexibility** | Fixed spreading factor | Dynamic subcarrier allocation |
| **Spectral efficiency** | Good with RAKE receiver | Very high |
| **Complexity** | Moderate | Higher (FFT/IFFT) |
| **Multipath** | RAKE receiver exploits | Cyclic prefix handles |

---

### 13. NOMA (Non-Orthogonal Multiple Access)

**5G Technology**: Allow more users than orthogonal resources

**Key Techniques**:
- **Superposition coding**: Transmit multiple users on same resource
- **SIC (Successive Interference Cancellation)**: Receiver decodes strongest signal first, subtracts, then decodes weaker signals

---

### Key Exam Formulas & Concepts:

```
CSMA/CD minimum frame size:
  Transmission time ≥ 2τ (round-trip delay)

ALOHA throughput:
  Pure: S = G·e^(-2G), max 18.4%
  Slotted: S = G·e^(-G), max 36.8%

m-sequence period:
  p = 2^n - 1 (n = shift register length)

OFDM subcarrier spacing:
  Δf = 1/Ts (Ts = symbol duration)

Processing Gain (DSSS):
  PG = Chip rate / Data rate = Bandwidth expansion
```

---

### Key Learning Questions (Answered):

✓ **Issues of accessing shared medium?** Collisions when multiple users transmit simultaneously; need MAC protocols

✓ **How are multiple access schemes categorized?** Contention-based (ALOHA, CSMA), Conflict-free (TDMA, FDMA, CDMA, OFDMA), Hybrid

✓ **What is CSMA? Why multiple versions?** Carrier sensing before transmit; versions trade off delay vs collision probability

✓ **Hidden and exposed terminal problems? Solutions?** Hidden: nodes can't hear each other, collision at receiver (solved by RTS/CTS); Exposed: unnecessary deferral (harder to solve)

✓ **What is CDMA?** Code-based multiplexing where all users transmit on same frequency with unique spreading codes

✓ **What are OFDM, OFDMA, SC-OFDMA?** OFDM: orthogonal subcarriers via FFT; OFDMA: multi-user subcarrier allocation; SC-FDMA: lower PAPR for uplink

✓ **Pros and cons of CDMA vs OFDMA?** CDMA: simpler, near-far problem; OFDMA: higher spectral efficiency, more complex, flexible allocation

---

## Lecture 4: Data Link Layer (LLC)

### Why Error Control is Critical in Wireless
**Problem**: High bit error rates in wireless due to interference, fading, multipath
- Frame error probability: P₂ = 1 - (1 - Pᵦ)^F
- Example: Pᵦ=10⁻⁵, F=2046 bits → P₂ ≈ 0.02 (2% frame error rate!)
- **Need**: Both detection AND correction mechanisms

### Error Control Approaches
1. **FEC (Forward Error Correction)**: Add redundancy to correct errors at receiver - no retransmission needed
2. **BEC (Backward Error Correction)**: Detect errors + ARQ (retransmission requests)
3. **Hybrid ARQ (HARQ)**: Combine FEC + ARQ for optimal performance

**When to use FEC vs BEC?**
- **High BER (bad channel)**: FEC preferred - retransmissions too costly
- **Low BER (good channel)**: BEC preferred - less overhead
- **Variable conditions**: Hybrid ARQ adapts to channel quality

---

### Error Detection Methods

**Parity Check**
- Add single parity bit to make total 1s even (even parity) or odd (odd parity)
- Detects odd number of bit errors; misses even number of errors
- Simple but weak protection

**CRC (Cyclic Redundancy Check)**
- Based on polynomial division in GF(2)
- Frame Check Sequence (FCS) appended to data
- Receiver divides received frame by generator polynomial
- **Remainder = 0**: No error detected; **Remainder ≠ 0**: Error detected
- Much stronger than parity; detects burst errors effectively

---

### ARQ (Automatic Repeat Request)

**Stop-and-Wait ARQ**
- Send one frame, wait for ACK before sending next
- Timeout triggers retransmission
- **Simple but inefficient** - low throughput, especially with high RTT

**Go-Back-N ARQ**
- Sender can have up to N frames outstanding (sliding window)
- Receiver only accepts frames in order
- **NAK or timeout**: Retransmit ALL frames from error point onwards
- Wasteful if only one frame corrupted
- Window size N ≤ 2^k - 1 (k = sequence number bits)

**Selective Repeat ARQ**
- Both sender and receiver have windows
- Receiver buffers out-of-order frames
- **Only retransmit specific corrupted frames**
- More efficient but requires more receiver buffer
- Window size N ≤ 2^(k-1)

**ARQ Acknowledgement Types**
- **Positive ACK**: Confirm correct receipt
- **Negative ACK (NAK)**: Request specific retransmission
- **Cumulative ACK**: Acknowledges all frames up to sequence number

---

### Block Codes (n, k)

**Terminology**
- **(n, k) code**: k data bits encoded to n total bits
- **r = n - k**: Redundancy bits (parity/check bits)
- **Code rate R = k/n**: Efficiency (higher = less overhead)
- **Hamming distance d(a,b)**: Number of bit positions that differ
- **Minimum distance dmin**: Smallest distance between any two codewords

**Error Detection/Correction Capability**
- **Detect up to (dmin - 1) errors**
- **Correct up to t = ⌊(dmin - 1)/2⌋ errors**
- Example: dmin = 5 → detect 4 errors OR correct 2 errors

---

### Hamming Code ⭐ (EXAM FAVORITE)

**Structure of (n, k) Hamming Code**
- Check bits placed at positions 2^i (positions 1, 2, 4, 8, 16...)
- Data bits fill remaining positions
- Each check bit covers specific positions based on binary representation
- **n = 2^r - 1, k = n - r** (for standard Hamming code)

**Check Bit Coverage** (position has 1 in binary representation at that power of 2)
- **Position 1 (p₁)**: covers positions 1,3,5,7,9,11,13,15... (odd positions)
- **Position 2 (p₂)**: covers positions 2,3,6,7,10,11,14,15...
- **Position 4 (p₄)**: covers positions 4,5,6,7,12,13,14,15...
- **Position 8 (p₈)**: covers positions 8,9,10,11,12,13,14,15...

**Syndrome Word Calculation**
1. Calculate parity for each check bit group (including the check bit)
2. Syndrome = [c₄c₃c₂c₁] in binary
3. **Syndrome = 0**: No error detected
4. **Syndrome ≠ 0**: Syndrome value = position of error bit

**Example Calculation** (typical exam question):
- Received: 1011010 (7-bit Hamming)
- Check p₁: positions 1,3,5,7 → XOR = 1⊕1⊕0⊕0 = 0
- Check p₂: positions 2,3,6,7 → XOR = 0⊕1⊕1⊕0 = 0
- Check p₄: positions 4,5,6,7 → XOR = 1⊕0⊕1⊕0 = 0
- Syndrome = 000 → No error

**Hamming Code Properties**
- dmin = 3 → corrects 1 error OR detects 2 errors
- Cannot do both simultaneously
- Extended Hamming (add overall parity) → dmin = 4, can detect 2 + correct 1

---

### LDPC Codes (Low-Density Parity-Check)

**Key Characteristics**
- Sparse parity-check matrix H (mostly zeros)
- Represented by **Tanner graph** (bipartite: variable nodes ↔ check nodes)
- **Iterative decoding**: Message passing between nodes
- Near Shannon limit performance

**LDPC vs Hamming Code** (exam question)
| Feature | Hamming | LDPC |
|---------|---------|------|
| Complexity | Simple | Complex |
| Performance | Moderate | Near Shannon limit |
| Decoding | Algebraic | Iterative |
| Block length | Short | Long (thousands of bits) |
| Applications | Memory ECC | 5G, WiFi, DVB |

---

### Polar Codes

- Based on **channel polarization** concept
- Recursive structure using "reverse shuffle"
- Channels become either very reliable or very unreliable
- Put data bits on reliable channels, frozen bits on unreliable
- Used in **5G control channels**
- **Successive cancellation decoding**

---

### Convolutional Codes (n, k, K)

**Parameters**
- **n**: Output bits per input
- **k**: Input bits per step (usually 1)
- **K**: Constraint length (memory + 1)
- **Code rate R = k/n**

**Key Concepts**
- Encoder has **memory** (shift registers)
- Output depends on current AND previous inputs
- Represented by **state diagram** or **trellis diagram**

**Viterbi Decoding**
- Maximum likelihood decoding
- Traces through trellis finding most probable path
- Computes **Hamming distance** between received and expected
- Keeps **survivor path** with minimum cumulative distance

---

### Turbo Codes

**Structure**
- Two **RSC (Recursive Systematic Convolutional)** encoders in parallel
- **Interleaver** between encoders (scrambles bit order)
- **Puncturing**: Remove some parity bits to increase rate

**Decoding**
- **Iterative decoding** between two decoders
- Exchange **soft information** (LLR - Log Likelihood Ratios)
- Multiple iterations improve performance
- Near Shannon limit at reasonable complexity

**Convolutional vs Turbo Codes** (exam comparison)
| Feature | Convolutional | Turbo |
|---------|---------------|-------|
| Decoding | Viterbi (optimal) | Iterative (sub-optimal) |
| Complexity | Moderate | Higher |
| Performance | Good | Near Shannon limit |
| Latency | Lower | Higher (iterations) |
| Applications | Voice, older systems | 3G/4G data |

---

### Hybrid ARQ (HARQ)

**Type-I HARQ**
- FEC code always transmitted
- If decoding fails → request retransmission
- Retransmitted frame is identical
- Simple but less efficient

**Type-II HARQ (Incremental Redundancy)**
- First transmission: Systematic bits + some parity
- If fails: Send **additional parity bits** (not identical copy)
- Receiver **combines** all received bits
- **Chase combining**: Same bits, soft combining
- **Incremental redundancy**: Different parity bits each time
- More efficient, used in LTE/5G

---

### Key Exam Formulas Summary

| Formula | Meaning |
|---------|---------|
| P₂ = 1 - (1 - Pᵦ)^F | Frame error probability |
| dmin - 1 | Max detectable errors |
| t = ⌊(dmin-1)/2⌋ | Max correctable errors |
| n = 2^r - 1 | Hamming code length |
| R = k/n | Code rate |

---

### Practice Questions (Lecture 4)

✓ **How do you calculate the syndrome word for Hamming code?** Calculate XOR of each parity group; syndrome gives error position in binary

✓ **What is the difference between LDPC and Hamming codes?** LDPC: iterative decoding, long blocks, near Shannon limit; Hamming: algebraic, short blocks, simpler

✓ **Compare convolutional codes vs turbo codes** Convolutional: Viterbi decoding, moderate complexity; Turbo: iterative decoding, near Shannon limit, higher latency

✓ **When is FEC preferred over BEC?** High BER channels where retransmissions are costly (real-time, satellite, poor wireless)

✓ **Explain Go-Back-N vs Selective Repeat** GBN: retransmit all from error; SR: only retransmit specific frame; SR more efficient but needs receiver buffering

✓ **What is HARQ Type-II?** Combines FEC with ARQ; sends incremental redundancy on retransmission; receiver combines all for better decoding

---

## Lecture 5: Network and Transport Layers

### Network Layer Fundamentals

**What is the Network Layer (L3)?**
- Provides **end-to-end communication** between source and destination (NOT per-link like DLL)
- Basic operations: **addressing, encapsulation, decapsulation, routing**
- IP encapsulates transport layer PDU (TCP segment or UDP datagram)
- IP addressing does NOT change along the path (except with NAT)

---

### Internet Protocol (IP)

**Key IP Characteristics:**
- **Connectionless**: No control info, sync, or ack packets
- **Best-effort (BE)**: No delivery guarantee, unreliable, no retries
- **Media-independent**: Works over fiber, copper, wireless, etc.
- **IP packets can arrive:**
  - Out-of-sequence
  - With errors/corrupted
  - Lost (no guarantee)
  - Relies on Layer 4 (TCP/UDP) to handle these issues

---

### IPv4 vs IPv6 Comparison

| Feature | IPv4 | IPv6 |
|---------|------|------|
| **Address Length** | 32 bits (2³²) | 128 bits (2¹²⁸) |
| **Address Space** | ~4 billion addresses | 340 trillion trillion trillion |
| **Header Size** | Variable (20+ bytes) | Fixed (40 bytes) |
| **Address Format** | Dotted decimal (192.168.1.1) | Hexadecimal (2001:db8::1) |
| **Fragmentation** | Routers can fragment | Only source fragments |
| **Header Checksum** | Yes | No (removed) |
| **NAT Required?** | Yes (due to depletion) | No (enough addresses) |
| **Key Fields** | TTL, Protocol, Checksum | Hop Limit, Next Header, Flow Label |

**Why IPv6?**
1. **IPv4 address depletion** - running out of addresses
2. **Eliminates NAT** - restores end-to-end connectivity
3. **Simpler header** - faster router processing
4. **Better QoS support** - Flow Label field for traffic classes
5. **Built-in security** - IPsec mandatory

---

### IPv4 Addressing

**IPv4 Packet Header Key Fields:**
- **Version**: 4 bits = 0100 (for IPv4)
- **Differentiated Services (DS)**: QoS marking
- **TTL (Time to Live)**: Hop count limit (decremented at each router)
- **Protocol**: Next layer protocol (6=TCP, 17=UDP, 1=ICMP)
- **Source/Destination Address**: 32-bit addresses
- **Header Checksum**: Detects corruption

**Addressing Methods:**
1. **Classful** (obsolete): Fixed blocks (Class A, B, C)
2. **CIDR (Classless InterDomain Routing)**: Arbitrary prefix length
   - Format: `network/prefix-length` (e.g., 200.23.16.0/23)
   - Network portion can be any length
3. **Subnetting**: Dividing IP prefix internally for management
4. **Private Addresses (RFC1918):**
   - Class A: 10.0.0.0/8
   - Class B: 172.16.0.0/12
   - Class C: 192.168.0.0/16

**NAT (Network Address Translation):**
- Maps one external IP to many internal IPs
- Uses TCP/UDP ports to distinguish connections (PAT)
- **Limitations**: Violates layering, breaks end-to-end connectivity

---

### IPv6 Addressing

**IPv6 Packet Header Key Fields:**
- **Version**: 4 bits = 0110 (for IPv6)
- **Traffic Class**: QoS (equivalent to DS field)
- **Flow Label**: 20-bit field for specialized traffic handling
- **Payload Length**: Length of data portion
- **Next Header**: Next protocol (improved options mechanism)
- **Hop Limit**: Replaces TTL
- **Source/Destination Address**: 128-bit addresses

**IPv6 Address Format:**
- Written as 8 hextets: `x:x:x:x:x:x:x:x` (x = 4 hex digits)
- **Rule #1**: Omit leading zeros (01ab → 1ab)
- **Rule #2**: Double colon (::) replaces contiguous zeros (only ONCE!)
  - Example: `2001:db8:0:1111:0:0:0:200` → `2001:db8:0:1111::200`

**IPv6 Address Types:**
- **Unicast**: Unique identifier for one interface
  - **Global Unicast Address (GUA)**: Public, routable (like public IPv4)
  - **Link-Local Address (LLA)**: Required, local link only (fe80::/10)
- **Multicast**: One-to-many (replaces broadcast)
- **Anycast**: Assigned to multiple devices, routed to nearest

**Prefix Length**: Recommended /64 for LANs (required for SLAAC)

---

### IP Routing

**Routing Table Contents:**
- **Network ID**: Destination subnet
- **Metric**: Cost to each route
- **Next Hop**: Gateway address (next router)
- **Interface**: Outgoing interface to use

**Route Types:**
1. **Directly Connected (C)**: Router's own interfaces
2. **Remote Routes**:
   - **Static (S)**: Manually configured by admin
   - **Dynamic**: Learned via routing protocols (OSPF, EIGRP)
3. **Default Route**: Catch-all route (0.0.0.0/0 or ::/0)

**Static vs Dynamic Routing:**
- **Static**: Manual config, good for small networks, doesn't adapt to changes
- **Dynamic**: Auto-discovery, maintains up-to-date info, finds best path, adapts to failures

---

### Routing Algorithms

**Distance Vector (DV):**
- Router knows only **distance and direction** to destinations
- Shares routing table with **immediate neighbors**
- Examples: RIPv2, EIGRP
- **Problem**: Count-to-infinity (slow convergence on failures)
  - Solution: Define "infinity" as max hops + 1

**Link State (LS):**
- Router learns **full network topology**
- Shares **own link state** with **all routers** (flooding)
- Each router computes best path (e.g., Dijkstra's SPF)
- Examples: OSPF, IS-IS
- **Advantage**: Faster convergence, no count-to-infinity

**Algorithm Types:**
- **Interior Gateway Protocols (IGP)**: Within autonomous system (OSPF, EIGRP, RIP)
- **Exterior Gateway Protocols (EGP)**: Between autonomous systems (BGP - Path Vector)

---

### Mobile IP

**Problem**: Standard IP assumes devices stay in one location

**Solution Components:**
1. **Home Network**: Original network of mobile node
2. **Foreign Network**: Network where mobile node currently resides
3. **Home Agent (HA)**: Router in home network
4. **Foreign Agent (FA)**: Router in foreign network
5. **Care-of-Address (CoA)**: Temporary address in foreign network
6. **Home Address**: Permanent address

**Three Basic Capabilities:**
1. **Discovery**:
   - Agents broadcast advertisements
   - Mobile Node (MN) can send solicitation
   - MN learns CoA
2. **Registration**:
   - MN sends registration request to HA
   - Informs HA of current CoA
3. **Tunneling**:
   - HA encapsulates packets
   - Forwards from home address to CoA via tunnel
   - FA decapsulates and delivers to MN

**Standards:**
- RFC 5944: IP Mobility Support for IPv4
- RFC 6275: Mobility Support in IPv6

---

### Quality of Service (QoS)

**What is QoS?**
- Mechanisms to provide **different priority** to different applications/users/flows
- Manages: **bandwidth, delay, jitter, packet loss**

**Application Requirements (Exam Important!):**

| Application | Reliability | Delay | Jitter | Bandwidth |
|-------------|------------|-------|--------|-----------|
| **E-mail** | High | Low | Low | Low |
| **File transfer** | High | Low | Low | Medium |
| **Web access** | High | Medium | Low | Medium |
| **Remote login** | High | Medium | Medium | Low |
| **Audio on demand** | Low | Low | **High** | Medium |
| **Video on demand** | Low | Low | **High** | **High** |
| **Telephony** | Low | **High** | **High** | Low |
| **Videoconferencing** | Low | **High** | **High** | **High** |

**QoS Techniques:**
- **Overprovisioning**: Add more capacity
- **Buffering**: Store packets temporarily
- **Traffic Shaping**:
  - Leaky bucket (constant rate)
  - Token bucket (bursty allowed)
- **Resource Reservation**: RSVP
- **Admission Control**: Accept/reject new flows
- **Packet Scheduling**: Prioritize queues

**QoS Models:**
1. **Best Effort (BE)**: No QoS guarantees
2. **Integrated Services (IntServ)**:
   - Per-flow resource reservation
   - Uses RSVP protocol
   - End-to-end cooperation required
   - **Scalability issues**
3. **Differentiated Services (DiffServ)**:
   - Class-based treatment
   - Uses **DSCP** field in IP header (6 bits)
   - Packets marked at edge, treated per-hop
   - More scalable than IntServ

**Traffic Marking:**
- **Ethernet**: CoS (Class of Service) - 3 bits
- **WiFi (802.11)**: TID (Traffic Identifier) - 3 bits
- **IPv4/IPv6**: DSCP (Differentiated Services Code Point) - 6 bits

---

### Exam Focus Points

**Most Likely Exam Topics:**
1. ✓ **IPv4 vs IPv6 differences** (header, addressing, why needed)
2. ✓ **Routing table structure** and how routes are added
3. ✓ **Distance Vector vs Link State** algorithms (differences, pros/cons)
4. ✓ **Mobile IP operation** (HA, FA, CoA, tunneling)
5. ✓ **QoS requirements** per application type
6. ✓ **QoS models** (BE, IntServ, DiffServ) - differences
7. ✓ **NAT operation** and limitations
8. ✓ **IPv6 address compression** rules
9. ✓ **Static vs Dynamic routing** - when to use each
10. ✓ **Count-to-infinity problem** in DV algorithms

**Common Exam Question Patterns:**
- Compare IPv4 and IPv6 headers
- Explain Mobile IP registration and tunneling process
- Match applications to QoS requirements
- Explain routing algorithm operation (DV or LS)
- Calculate routing table updates
- Describe NAT operation and issues
- Compress/decompress IPv6 addresses

---

### Key Formulas & Concepts

**IPv4 Subnetting:**
- Subnet mask determines network vs host portion
- CIDR notation: `network/prefix-length`
- Number of hosts = 2^(32-prefix) - 2

**IPv6 Addressing:**
- Recommended prefix: /64 for LANs
- Link-local: fe80::/10
- Global unicast: 2000::/3

**Routing Metrics:**
- Hop count (RIP)
- Bandwidth (EIGRP)
- Cost (OSPF) = Reference BW / Interface BW

---

**Note**: Transport layer (TCP/UDP) will be covered separately but remember TCP is **NOT optimal** for wireless due to:
- Interpreting wireless losses as congestion
- Unnecessary retransmissions
- Solutions: Split TCP, Snoop Protocol, Explicit notifications
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

## Lecture 6: Cellular Networks

### Principles of Cellular Networks

**Core Concept**: Low-power (<100W) systems with shorter radius (<20km) using numerous transmitters/receivers to increase capacity for mobile radio telephone services.

**Advantages**:
- **Frequency reuse**: Better utilization of wireless resources and higher capacity
- **Lower power requirements**: Smaller devices and longer-lasting batteries
- Single-hop, infrastructured architecture

**Cell Organization**:
- **Hexagonal cells** provide equidistant antennas (ideal pattern)
- **Square cells** are simpler but geometry not ideal
- In practice: variations due to antenna design, topographical limitations, local signal propagation

**Frequency Reuse**:
- **No same frequency in adjacent cells** (to avoid interference)
- **Reuse factor N**: Number of cells in a cluster (e.g., N=7)
- Minimum separation required between cells using same frequency

**Increasing Capacity Methods**:
1. **Adding new channels** (given unused channels)
2. **Frequency borrowing** (from adjacent cells)
3. **Cell Splitting** (splitting into smaller cells in high-traffic areas)
4. **Cell Sectoring** (dividing cell into sectors - see triangular antennas)
5. **Network Densification** (Femtocell → Picocell → Macrocell, self-organizing networks)
6. **Inter-Cell Interference Coordination (ICIC)** and Coordinated Multipoint Transmission

---

### Operation of Cellular Systems

**Key Elements**:
- **Base Station (BS)**: Radio Tx/Rx to/from User Equipment (UE)
- **Air interface**: Wireless interface between BS and UE
- **MTSO** (Mobile Telecommunication Switching Office): Call origination/termination
- **RAN** (Radio Access Network): Network between BSs and core network
- **Core Network**: Provides networking services

**Channel Types**:
- **Control channels**: Information exchange to set up and manage connections
- **Traffic channels**: Transport voice or data between users

**Call Procedure** (6 steps):
1. **Mobile unit initialization**: Scan/select strongest control channel, handshake with MTSO
2. **Mobile-originated call**: Send called number on control channel to BS → MTSO
3. **Paging**: MTSO sends paging message to certain BSs based on last known location
4. **Call accepted**: Called unit responds, MTSO sets up circuit and selects traffic channels
5. **Ongoing call**: Connection maintained
6. **Handoff**: Seamless traffic channel change when moving to new BS coverage area

**Other Functions**: Call termination, call drop, fixed/remote calls, emergency prioritization

---

### Evolution of Cellular Networks

**Technology Timeline**:
| Generation | Deployment | Download Speed | Latency | Air Interface | Core Network | Primary Service |
|------------|-----------|----------------|---------|---------------|--------------|-----------------|
| **1G** | 1980s | 2 kbit/s | N/A | Analog | Circuit switching | Analog voice calls |
| **2G** | 1990s | 384 kbit/s | 629 ms | Digital, TDMA, CDMA | Circuit switching, packet switching | Digital calls, SMS, basic Internet |
| **3G** | 2000s | 2 Mbit/s | 212 ms | WCDMA, CDMA2000 | Packet switching, IP | Mobile broadband, smartphones |
| **4G** | 2010s | 1 Gbit/s | 60-98 ms | OFDM, OFDMA, MIMO | IP | Fast mobile broadband, high-speed Internet, IoT |
| **5G** | 2020s | >1 Gbps | <1 ms | AAS, FD-MIMO | IP | eMBB, mMTC, URLLC |

**Intermediate Generations**:
- **2G+**: GPRS (171.2 kbps), EDGE (600-750 kbps)
- **3G+**: HSDPA (1.8-14.4 Mbps), HSUPA (5.76 Mbps), HSPA+ (21-336 Mbps)
- **4G**: LTE (Release 8-9), LTE-Advanced (Release 10-12), LTE-Advanced Pro (Release 13+)

**3GPP Release Timeline**:
- **3G**: Release 99, Releases 4-7
- **4G**: Releases 8-14
- **5G**: Releases 15+ (Release 15: 2018, Release 16: 2020, Release 17: 2022, Release 18-19: ongoing)

---

### 4G/LTE Architecture

**LTE Architecture Components**:

**E-UTRAN (Evolved UTRAN)**:
- Consists of several **eNodeBs** (Evolved NodeB)
- eNodeBs embed their own control functionality
- Direct communication between eNodeBs (unlike UMTS)
- Use of Relay Nodes

**EPC (Evolved Packet Core)**:
- **MME** (Mobility Management Entity): Authentication, SGSN selection at 2G/3G handovers, resource allocation, mobility management
- **S-GW** (Serving Gateway): Interconnection between E-UTRAN and EPC, packet routing/forwarding, mobility anchor
- **P-GW** (PDN Gateway): Routing point to external Packet Data Network
- **HSS** (Home Subscriber Server): Subscriber information

**UE (User Equipment)**:
- ME (Mobile Equipment) + USIM (Universal SIM)

**Key Features**:
- **Air Interface**: OFDM/MIMO, DL: OFDMA, UL: SC-FDMA, both FDD and TDD
- **Carrier Aggregation**: Intra-band contiguous, intra-band non-contiguous, inter-band non-contiguous
- **Resource Management**: Bearer-based (GBR/Non-GBR), QoS Class Identifiers (QCI)
- **Radio Resource Allocation**: Resource Grid → Resource Elements → Resource Blocks

**LTE Evolution**:
| Version | 3GPP Release | LTE Category | Max Download | Carrier Aggregation | Carrier BW | Latency | MIMO | QAM |
|---------|--------------|--------------|--------------|---------------------|------------|---------|------|-----|
| **LTE** | Rel.8-9 | CAT1-5 | 150Mbps | 0 | 10MHz | 100ms | 2 | 64 |
| **LTE-A** | Rel.10-12 | CAT6-16 | 1Gbps | Up to 5 | 100MHz | 10ms | 8 | 64 |
| **LTE-A Pro** | Rel.13+ | CAT17-19 | 3Gbps | Up to 32 (LAA, LWA) | 640MHz | 2ms | 32 | 256 |

---

### 5G Use Scenarios

**Three Main Scenarios** (ITU IMT-2020):

**1. eMBB (Enhanced Mobile Broadband)**:
- **Focus**: Peak data rate, user experienced data rate
- **Requirements**: High data rates, area traffic capacity
- **Use Cases**: 3D video, UHD screens, work/play in cloud, AR/VR, gigabytes in a second

**2. mMTC (Massive Machine-Type Communication)**:
- **Focus**: Connection density, network energy efficiency
- **Requirements**: Support for massive number of devices
- **Use Cases**: Smart city, smart home/building, massive IoT sensors

**3. URLLC (Ultra-Reliable Low-Latency Communication)**:
- **Focus**: Latency, reliability, mobility
- **Requirements**: <1ms latency, 1-10^-8 reliability
- **Use Cases**: Industry automation, mission-critical applications, self-driving cars, remote surgery

**Key Performance Improvements vs 4G**:
- **Peak data rate**: 20 Gbps (100x improvement)
- **User experienced data rate**: 100 Mbps - 1 Gbps
- **Latency**: <1 ms (10x improvement)
- **Mobility**: Up to 500 km/h
- **Connection density**: 10^6 devices/km²
- **Energy efficiency**: 100x improvement
- **Area traffic capacity**: 10 Mbps/m²
- **Spectrum efficiency**: 3x improvement

---

### 6G Vision (IMT-2030)

**Framework Recommendation**: ITU-R M.2160 (November 2023)

**Six Usage Scenarios**:
1. **Immersive Communication** (extension of eMBB)
2. **Massive Communication** (extension of mMTC)
3. **HRLLLC** - Hyper Reliable & Low-Latency Communication (extension of URLLC)
4. **Ubiquitous Connectivity** (NEW)
5. **AI and Communication** (NEW)
6. **Integrated Sensing and Communication** (NEW)

**Four Overarching Aspects** (design principles for all scenarios):
- Sustainability
- Connecting the unconnected
- Ubiquitous intelligence
- Security and resilience

**Key Capabilities (Palette Diagram)**:
- **Enhanced from 5G**: Peak data rate, user experienced data rate, spectrum efficiency, area traffic capacity, mobility (500-1000 km/h), latency (0.1-1 ms), reliability (1-10^-5 to 1-10^-9), connection density (10^6-10^8 devices/km²)
- **New capabilities**: Sensing-related, AI-related, sustainability, interoperability, positioning (1-10 cm), coverage, security and resilience

**Timeline**:
- Requirements: 2025-2026
- Standards Development: 2026-2028
- Standards Enhancement: 2028-2030
- Systems deployment: Around 2030

**3GPP Timeline**:
- 6G requirements: Rel-20* (2026)
- 6G studies: Rel-20* (2026-2027)
- 6G specification: Rel-21* (2027-2028)

---

### LPWAN Technologies (Brief Overview)

**Key LPWAN Options**:
- **LoRa**: Long range, low power, unlicensed spectrum
- **NB-IoT**: Narrowband IoT, licensed spectrum, cellular-based
- **LTE-M**: LTE for Machines, licensed spectrum, cellular-based

**Comparison Point**: All designed for massive IoT, differ in range, power consumption, data rates, spectrum licensing, and cost

---

### Private 5G

**Definition**: Dedicated 5G network for specific organization/enterprise use

**Spectrum Options**:
- **Dedicated spectrum**: Very wide-range coverage (mainly outdoor)
- **Dedicated/shared spectrum**: Wide-range (indoor/outdoor), high-capacity/throughput
- **Shared spectrum**: Short-range (mainly indoor), high-capacity/throughput (like Wi-Fi 6/6E)

**Use Cases**:
- Industrial automation/Industry 4.0
- Smart buildings/campuses
- Transportation and logistics
- Public safety
- Healthcare facilities

**Comparison with Public 5G and Wi-Fi 6**:

| Feature | Public 5G | Private 5G | Wi-Fi 6 |
|---------|-----------|------------|---------|
| Coverage | Outdoor (long range) | Indoor/Outdoor (wide range) | Indoor (short range) |
| Ownership | Carrier managed | Enterprise owned | Enterprise owned |
| Target Apps | Mobile broadband, AR/VR, outdoor wireless | Massive IoT, industry automation | Indoor enterprise, retail |
| Security | eSIM/SIM authentication | eSIM/SIM authentication | WPA3 |
| Cost | Higher operation cost | Medium cost | Lower operation cost |
| Modulation | 256QAM | 256QAM | 1024QAM |

---

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

---

## Lecture 6 Part 2: 5G Architecture and Enabling Technologies

### 5G Core Network Architecture

**Key Innovation**: Service-Based Architecture (SBA) with Network Functions (NFs)

**Two Architectural Representations**:
1. **Service-based representation**: Shows how services are provided/exposed by NFs
2. **Reference point representation**: Shows interactions between NFs

**Separation of Planes**:
- **Control Plane**: Signaling and network control
- **User Plane**: Actual user data transmission

**Major 5G Core Network Functions**:

| Function | Acronym | Primary Responsibility |
|----------|---------|------------------------|
| Authentication Server Function | AUSF | Data storage for UE authentication |
| Access & Mobility Management Function | AMF | UE authentication, authorization, and mobility management |
| Network Exposure Function | NEF | Interface for outside applications to access network services |
| Network Repository Function | NRF | Registration and discovery of services offered by NFs |
| Network Slice Selection Function | NSSF | Selection of network slice instances to accommodate UE requests |
| Network Slice Authentication & Authorization | NSSAAF | Slice authentication and authorization |
| Policy Control Function | PCF | Control and management of policy rules for QoS |
| Session Management Function | SMF | PDU session establishment, management, and release (between UE and DN) |
| Unified Data Management | UDM | Data storage for UE subscription information |
| User Plane Function | UPF | Handling of user plane path of PDU sessions |
| Application Function | AF | Provision of session-related information to PCF for dynamic policy control |
| Service Communication Proxy | SCP | Enabling direct or indirect communication of NFs |

**UPF (User Plane Function) - Critical Component**:
- **UE IP mobility anchoring**: Transit nodes forward PDUs without data loss during handover
- **PDU handling**: Packet routing, forwarding, QoS handling
- **Other functions**: Traffic usage reporting, packet inspection, transport level packet marking

**PDU Session Establishment** (Simplified flow):
1. UE → RAN → AMF: Session establishment request
2. AMF: SMF selection
3. SMF → UDM: Validation/information retrieval
4. SMF: PDU session authentication/authorization
5. SMF: PCF selection, UPF selection
6. First uplink data transmission
7. Final session establishment
8. First downlink data transmission

---

### 5G RAN Architecture

**NG-RAN Components**:
- **gNodeB (gNB)**: 5G User Plane (UP) and Control Plane (CP) protocol terminations
- **ng-eNB**: 4G UP and CP protocol terminations (for 4G/5G interworking)
- **5GC**: 5G Core Network
- **NG interface**: Connection between gNB/ng-eNB and 5GC
- **Xn interface**: Interconnection between gNBs and ng-eNBs

**Functional Split of gNodeB**:
- **Central Unit (CU)**: Processes non-real-time protocols and services
- **Distributed Unit (DU)**: Processes physical layer protocol and real-time services
- **F1 interface**: Connection between CU and DU
- One DU connects to one CU (primary), optionally to secondary CU for redundancy

---

### 5G NR Air Interface Technologies

**Frequency Ranges** (3GPP TS 38.101-1 and 38.101-2):
- **FR1 (Sub-6 GHz)**: 410 MHz – 7,125 MHz
- **FR2 (mmWave)**: 24,250 MHz – 71,000 MHz

**Adaptive Modulation and Coding (AMC)**:
- **Uplink (UL)**: π/2-BPSK, QPSK, 16-QAM, 64-QAM, 256-QAM
- **Downlink (DL)**: QPSK, 16-QAM, 64-QAM, 256-QAM

**π/2-BPSK** (Uplink only):
- Variation of BPSK with 180° phase shift
- Low peak-to-average power ratio (PAPR)
- Energy efficient for UE

**Duplexing**: FDD and TDD

| Feature | 5G FDD | 5G TDD |
|---------|---------|---------|
| Application | Symmetric UL/DL traffic | Asymmetric UL/DL traffic |
| Interference | Less | More |
| Deployment | Best for rural/suburban areas | Best for urban areas with low-power nodes |
| Beamforming | Explicit beamforming only | Explicit beamforming only |
| Frequency bands | Low frequency (<10 GHz) | High frequency (>10 GHz) |
| Channel response | DL/UL use different channels | Same channel for DL/UL - better for MIMO/beamforming |

**Waveforms** (3GPP TR 38.802):
1. **CP-OFDM** (Cyclic Prefix OFDM):
   - Both uplink and downlink
   - Mandatory cyclic prefix
   - Best for multi-antenna tech, high spectral efficiency, low complexity
   - Well localized in time domain (good for latency-critical apps and TDD)
   - More robust to phase noise (critical at high frequencies)

2. **DFT-S-OFDM** (DFT Spread OFDM):
   - Uplink only
   - Similar to SC-FDMA
   - Allows non-continuous (clustered) groups of subcarriers
   - More robust to selective fading
   - Lower PAPR than CP-OFDM

**Numerologies** (Subcarrier Spacing):
- **Flexibility**: Higher spacing at higher frequencies
- **μ** values: 0, 1, 2, 3, 4
- **Subcarrier spacing (Δf)**: 15, 30, 60, 120, 240 kHz (Δf = 2^μ × 15 kHz)
- **OFDM symbol duration**: Decreases with higher μ (66.67 μs for μ=0, down to 4.17 μs for μ=4)

**Error Control in 5G** (3GPP TS 38.212):

| Channel | Description | Coding |
|---------|-------------|--------|
| **Uplink** | | |
| PUCCH (Physical Uplink Control Channel) | UCI: scheduling requests, CQI, HARQ info | Polar code |
| PUSCH (Physical Uplink Shared Channel) | Application data + RRC signaling | LDPC for data, Polar for UCI |
| **Downlink** | | |
| PDCCH (Physical Downlink Control Channel) | DCI: scheduling decisions, transmission grants | Polar code |
| PDSCH (Physical Downlink Shared Channel) | Application data and paging | LDPC |
| PBCH (Physical Broadcast Channel) | System information for UE to connect to gNodeB | Polar code |

**LDPC Codes** (Low-Density Parity-Check):
- **Quasi-Cyclic LDPC**: Defined by 3GPP
- Benefits hardware implementations of encoding/decoding
- Used for data plane (high throughput)
- Base matrix approach to compute parity-check matrix H

**Polar Codes**:
- Used for control plane
- Reduce complexity and latency of decoding process
- CRC (Cyclic Redundancy Check) attached for error detection

**HARQ** (Hybrid Automatic Repeat Request):
- Combines ARQ with FEC
- Fast retransmission at physical layer

**Massive MIMO and Beamforming**:
- Large antenna arrays
- Spatial multiplexing
- Beam steering for improved coverage and capacity

---

### 5G NR Evolution (3GPP Releases)

| Release | Year | Key Features |
|---------|------|--------------|
| **Release 15** | 2018 | Foundation: Sub-6 GHz with massive MIMO, mmWave, 5G core, eMBB, LTE integration, flexible OFDM, advanced channel coding |
| **Release 16** | 2020 | Expansion: URLLC/IIoT, 5G NR V2X, positioning, unlicensed spectrum (NR-U), IAB, better coverage, in-band eMTC/NB-IoT |
| **Release 17** | 2022 | Continued expansion: NR-Light (RedCap) for IoT, spectrum >52.6 GHz, enhanced IIoT, improved IAB, non-terrestrial networks, cm-accuracy positioning |
| **Release 18+** | Ongoing | 5G Advanced: AI/ML, full-duplex MIMO, XR (Extended Reality), smart repeaters, broadcast enhancements, sidelink in unlicensed spectrum |

---

### Enabling Technologies of 5G

#### 1. Software-Defined Networking (SDN)

**Core Concept**: Separation of control plane and data plane

**Key Characteristics**:
- **Logical centralization**: Control plane in software-based controller
- **Data plane**: Network devices forward packets based on controller instructions
- **Off-the-shelf computing platforms**: COTS hardware

**SDN Architecture Components**:
- **Network Devices** (Data Plane): Forward packets
- **Southbound Interface** (e.g., OpenFlow): Controller ↔ Network devices
- **SDN Controllers** (Control Plane): Network intelligence and control
- **Northbound Interface** (e.g., REST API): Applications ↔ Controller
- **East/Westbound Interface**: Controller ↔ Controller communication
- **Network Applications**: Business logic

**Advantages of SDN**:
- **Simplified algorithms**: Centralized algorithms easier than distributed
- **Commodity network hardware**: COTS instead of expensive proprietary hardware
- **Layered architecture**: Open interfaces enable multi-vendor environments
- **Eliminating middle-boxes**: Functions become network applications
- **Third-party applications**: Easy development on top of controller
- **Programmability**: Configure → Program network for flexibility

---

#### 2. Network Function Virtualization (NFV)

**Core Concept**: Decouple network functions from proprietary hardware appliances

**ETSI NFV Architecture Components**:

| Component | Description |
|-----------|-------------|
| **VNF** (Virtual Network Function) | Software implementation of network function decoupled from hardware |
| **EMS** (Element Management System) | Local VNF management |
| **NFVI** (NFV Infrastructure) | Virtualized resources (compute, storage, network) from hardware via virtualization layer |
| **VIM** (Virtualization Infrastructure Manager) | Manages allocation/monitoring of virtual resources, reports to VNFM |
| **VNFM** (VNF Manager) | VNF lifecycle management, fault/performance/security management |
| **NFVO** (NFV Orchestrator) | Orchestrates Network Services (NS), manages VNFFGs, selects resources |
| **OSS/BSS** | Operation/Business Support Systems |
| **VNFFG** (VNF Forwarding Graph) | Graph of logical links connecting VNFs |
| **NFVI-PoP** | NFVI Point of Presence where VNFs can be deployed |

**NFV MANO (Management and Orchestration)**:
- **VIM**: Manages NFVI resources
- **VNFM**: Manages VNF lifecycle
- **NFVO**: Orchestrates Network Services and VNFs

**Advantages of NFV**:
- **Reduced CapEx/OpEx**: Lower capital and operational expenditures
- **Rapid innovation**: Quick service rollout
- **Ease of interoperability**: Multi-vendor environment
- **Single platform**: Different applications, users, tenants
- **Agility and flexibility**: Dynamic resource allocation
- **Openness**: Wide variety of ecosystems

---

#### 3. Network Slicing

**Definition**: Multiple logical networks on top of shared infrastructure

**Key Features**:
- **Heterogeneous services**: Different slices for different use cases
- **Multi-domain infrastructure**: Spans RAN, transport, core
- **Enabled by**: SDN + NFV + Orchestration

**Enables 5G Usage Scenarios**:
- **eMBB slice**: High bandwidth, moderate latency
- **mMTC slice**: Massive connections, low power
- **URLLC slice**: Ultra-low latency, high reliability

**Network Slice Components**:
- **Service graph/VNFFG**: Chain of VNFs for the slice
- **Slice-specific resources**: Dedicated or shared
- **Slice isolation**: Performance and security isolation

---

#### 4. Multi-Access Edge Computing (MEC)

**Definition**: Computing capabilities at the edge of the network close to users

**ETSI MEC Architecture** (System-level and Host-level):

**MEC Host (MEH)**:
- **MEC Platform (MEP)**: Environment for MEC applications, hosts MEC services
- **Virtualization Infrastructure**: Compute, storage, network resources
- **MEC Applications**: Run on MEP, consume/offer MEC services
- **Data Plane**: Routes traffic among apps, services, DNS, access networks

**MEC Host-level Management**:
- **MEPM** (MEC Platform Manager): Manages application lifecycle, rules, requirements, prepares VI, element management
- **VIM**: Manages/monitors virtual resources, prepares VI, reports to MEPM

**MEC System-level Management**:
- **MEO** (MEC Orchestrator): Overview of MEC system, on-boards apps, selects MEH, triggers app instantiation/termination/relocation
- **OSS**: Decides on granting requests
- **User app LCM proxy**: Permits device apps to request on-boarding/instantiation/termination

**MEC in 5G Networks**:
- MEC system integrated with 5G Core
- MEP and MEC App are VNFs
- MEO = MEAO + NFVO
- MEPM = MEPM-V + 2 VNFMs

**Benefits of MEC**:
- **Reduced latency**: Processing close to users
- **Contextual information**: Real-time awareness of local environment
- **Cloud offloading**: Reduce load on central cloud
- **Traffic congestion reduction**: Local data processing

**5G-MEC Deployment Scenarios**:
1. UPF and MEH co-located at edge
2. UPF at edge, MEH centralized
3. UPF and MEH at aggregation point
4. UPF and MEH in core network

---

### 5G Deployment Options and Migration Strategy

**Deployment Options** (3GPP):
- **Features that distinguish each option**:
  - Use of Dual Connectivity
  - Radio Access Technology acting as master node (LTE or NR)
  - Core Network used (EPC or 5GC)

**Key Deployment Options**:

| Option | Configuration | Core Network | Description |
|--------|---------------|--------------|-------------|
| **Option 1** | SA (Standalone) LTE | EPC | LTE connected to EPC |
| **Option 2** | SA NR | 5GC | NR connected to 5GC |
| **Option 3** | NSA (Non-Standalone) | EPC | LTE master, NR assistant (EN-DC) |
| **Option 4** | NSA | 5GC | NR master, LTE assistant (NE-DC) |
| **Option 5** | SA LTE | 5GC | LTE connected to 5GC |
| **Option 7** | NSA | 5GC | LTE master, NR assistant (NGEN-DC) |

**Migration Strategy**:
- **Early deployment**: Option 3 (NSA with EPC) - Re-use existing 4G EPC
- **Transition**: Options 2, 4, 5, 7 with 5GC for full 5G capabilities

**5G Core Advantages over EPC**:
- Native support for Network Slicing
- Native support for MEC
- Native support for URLLC
- Service-Based Architecture

---

### Disaggregation and Virtualization

**Network Disaggregation**:
- **Eliminates vendor lock-in**: Multi-vendor environment
- **Best-of-breed selection**: Choose optimal hardware and software separately

**RAN Decomposition**:
- **gNodeB** split into:
  - **Central Unit (CU)**: Non-real-time protocols, higher layers
  - **Distributed Unit (DU)**: Real-time protocols, physical layer
  - **F1 interface**: CU ↔ DU connection

**Virtualized RAN (vRAN)**:
- **Decouples hardware and software**: RAN functions as VNFs
- **COTS servers**: Commodity or custom hardware with merchant silicon
- **Deployment flexibility**:
  - **Full virtualization**: RU (radio transceiver) + vDU + vCU
  - **Partial virtualization**: RU + bare metal DU + vCU
  - **Traditional RAN**: All bare metal

**Virtualization Technologies**:
- **Type-1 Hypervisor**: Runs directly on hardware (bare metal)
- **Type-2 Hypervisor**: Runs on host OS
- **Containers**: OS-level virtualization, lighter weight

---

### New Challenges in 5G

**Technical Challenges**:
1. **Ultra-low latency**: <1 ms for URLLC applications
2. **Massive connectivity**: 10^6 devices/km² for mMTC
3. **High reliability**: 99.999999% for mission-critical apps
4. **Complex network management**: Orchestration of slices, VNFs, MEC
5. **Security**: Increased attack surface with virtualization and openness
6. **Interoperability**: Multi-vendor, multi-domain integration

**Operational Challenges**:
1. **Migration complexity**: From 4G to 5G, NSA to SA
2. **Spectrum management**: Coordination of FR1 and FR2
3. **Energy efficiency**: Increased computational demands
4. **Cost**: High deployment costs for new infrastructure

**Research Directions**:
1. **AI/ML integration**: Intelligent network management (Release 18+)
2. **Non-terrestrial networks**: Satellite integration
3. **Sensing and communication**: Integrated systems
4. **Terahertz communications**: Beyond mmWave (6G)

---

### Key Learning Questions (Part 2):
- Architecture of 5G and new features? ✓
- Principles and characteristics of 5G Core Network and RAN? ✓
- Technologies used in 5G NR Air Interface? ✓
- Enabling technologies of 5G? ✓
- How can 5G be deployed? ✓
- New challenges in 5G? ✓
- Architecture of 5G and new features?
- Principles and characteristics of 5G Core Network and RAN?
- Technologies used in 5G NR Air Interface?
- Enabling technologies of 5G?
- How can be 5G deployed?
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

## Lecture 10: IoT - Part 1 (Guest Lecture)

### IoT Four-Layer Architecture
**Critical for Understanding IoT Systems**:

1. **Device Layer (The Things)**:
   - Smart sensors (temperature, light, motion)
   - Smart actuators (displays, sound, motors)
   - Computation capability (can run programs)
   - Communication interfaces (wired/wireless)

2. **Network Layer**:
   - WPAN, WLAN, WMAN (short/medium range)
   - Cellular networks (long range)
   - Internet backbone

3. **Data Analytics Layer**:
   - ML/AI algorithms
   - Historical data analytics
   - Streaming data analytics
   - Cloud storage

4. **Application Layer**:
   - Decision making
   - Dashboards, web services
   - Augmented reality

### IoT Hardware Components

**IoT Boards**:
- **Microcontroller Boards** (e.g., Arduino):
  - System on Chip (SoC) with processing cores, RAM, EPROM
  - Executes custom programs on microcontroller

- **Single Board Computers** (e.g., Raspberry Pi):
  - Complete computer on single circuit board
  - Fan-less, low-power, low-profile architecture

**Sensor Node (Mote) Architecture**:
- **Key Components**:
  - Microcontroller (processing/sampling)
  - Data SRAM (critical limiting resource)
  - Flash storage (program images, data logs)
  - Sensor Interface (ADC for analog, digital sensors)
  - Wireless/Wired Network Interface
  - Low-power standby & wakeup capability

### Power Consumption (EXAM CRITICAL)

**Power Consumption Model**:
- Sleep – Active [Wakeup / Work] cycle
- **Average Power**: P_ave = f_sleep × P_sleep + f_wakeup × P_wakeup + f_work × P_work
- **Lifetime**: EnergyStore / (P_ave - P_generated)

**General Design Guideline**:
- Switch off Radio (TX/RX/IDLE) "as soon as possible"
- Radio power consumption roughly same for TX, RX, or IDLE listening
- **Total energy dominated by idle listening**

**Power Spending Factors**:
1. **Duty Cycle**: How often devices are on
2. **Protocol Efficiency**: What they do when on
3. **TX Power**: How much power they transmit (and amplifier efficiency)
4. **Transmission Duration**: Data rate affects energy per bit
5. **Signal Processing**: DSP or RF dominated

**Example Power Values (802.11 PSM)**:
- TX: 700-1100 mW
- RX: 170-350 mW
- Idle: 66-92 mW
- Sleep: 13-142 μW

### Wireless Technologies for IoT

**Communications Criteria**:
1. **Range**: Signal propagation distance
2. **Frequency Bands**: Licensed vs unlicensed, sub-GHz
3. **Power Consumption**: Stable power vs battery
4. **Topology**: Network layouts for connecting objects
5. **Constrained Devices**: Connectivity limitations
6. **Constrained-Node Networks**: Network challenges

**Network Architectures**:
- **Mobile Radio Networks** (Cellular: 2G-5G)
- **Capillary Multi-hop Networks** (Short/medium range + backhauling)
- **Low Power Wide Area Networks (LPWAN)**

**Technology Comparison (Key Parameters)**:

| Technology | Range | Data Rate | Power | Spectrum | Latency |
|------------|-------|-----------|-------|----------|---------|
| **Wi-Fi** | ~100m | 100+ Mbps | High | Unlicensed 2.4/5 GHz | Low |
| **Wi-Fi HaLow** | ~1km | Few kbps | Low | Unlicensed sub-1 GHz | 1.6-10s |
| **Bluetooth LE** | ~100m | 1-10 Mbps | Low | Unlicensed 2.4 GHz | Low |
| **ZigBee** | ~100m | 250 kbps | Low | Unlicensed 2.4 GHz | Low |
| **LoRaWAN** | 2-5km urban, 15km rural | 50-290 bps | Very Low | Unlicensed sub-1 GHz | High |
| **NB-IoT** | 10-15km | 20-200 kbps | Low | Licensed | 1.6-10s |
| **LTE-M** | 7-10km | <1 Mbps | Low | Licensed in-band | 10-15ms |
| **EC-GSM** | <25km | 240 kbps | Low | Licensed GSM | 700ms-2s |

### Wi-Fi Power Saving Modes

**Active Mode**: Radio always on (high power)

**Legacy PS Mode (PS-Poll)**:
- Station sleeps between beacons
- Wakes up to receive beacon
- Sends PS-Poll if data buffered at AP
- Significant power savings with increased latency

**Tradeoff**: Latency vs. Power Saving

### Interference at 2.4 GHz (Important)

**Wi-Fi vs ZigBee**:
- Operate on same band
- Wi-Fi typically 100x more power (100 mW vs 1 mW)
- Some ZigBee channels avoid Wi-Fi spectrum (channels 25, 26)

**BLE vs Wi-Fi**:
- BLE advertising channels (37, 38, 39) avoid 802.11 channels 1, 6, 11
- 9 data channels still available for BLE

### Energy Calculations (Practice This!)

**Energy Definition**: Current (A) × Voltage (V) × Time (s) = Power (W) × Time (s)

**Example Calculation**:
- Battery: 180 mAh, 1.5V → Energy = 180×10⁻³ × 3600 × 1.5 = 972 J
- TX Power: 15 mW, Duration: 3 ms → Energy per TX = 15×10⁻³ × 3×10⁻³ = 45 μJ
- Number of transmissions: 972 / (45×10⁻⁶) = 21.6 million
- Lifetime (1 TX/min): 21.6×10⁶ minutes ≈ 15,000 days ≈ 40 years

### IoT Protocol Stack

**Messaging Protocols** (Application Layer):
- MQTT (publish-subscribe, TCP-based)
- CoAP (request-response, UDP-based, lightweight)
- AMQP (message queuing)
- HTTP (web-based, heavier)

**Transport**: TCP (reliable) / UDP (lightweight)
**Network**: IPv4, IPv6, 6LoWPAN (IPv6 over Low-Power networks)
**PHY/MAC**: IEEE 802.3, 802.11, 802.15.4, 802.15.1 (BLE), others

**Why New Stack Needed**:
- Traditional HTTP/FTP/SNMP too heavy for constrained devices
- TCP/UDP overhead undesirable for low-power
- Need tight coupling with PHY for energy efficiency
- Routing needed for tiny disconnected devices

### Key Exam Topics
- Understand 4-layer IoT architecture and role of each layer
- Know power consumption models and how to calculate device lifetime
- Understand why idle listening dominates energy consumption
- Compare wireless technologies (range, data rate, power, spectrum)
- Understand interference issues at 2.4 GHz
- Know Wi-Fi power saving modes and tradeoffs
- Be able to perform energy/lifetime calculations
- Understand why traditional protocols are unsuitable for IoT
- Know differences between LPWAN technologies (LoRa, NB-IoT, LTE-M)
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
## Lecture 8: Wireless Network Tools

### Tool Categories and Purpose

#### 1. Network Analysis & Monitoring Tools
- **Wireshark**: Packet analyzer (GUI-based) - captures and analyzes network traffic
- **Tcpdump**: CLI packet analyzer - command-line traffic capture
- **PRTG**: SNMP-based network monitoring for intermediate devices
- **Unix Tools**:
  - `ping`: ICMP-based connectivity testing
  - `traceroute`: Path discovery to destination
  - `iperf`: Network performance measurements
  - `netstat`, `nslookup`, `ifconfig`, `nmap`: Network configuration and scanning

#### 2. Network Simulation vs Emulation
- **Simulators**: Model network behavior mathematically
  - **Cisco Packet Tracer**: Visual network simulator (cross-platform)
  - **ns-3**: Discrete event network simulator (with app store)
  - **OMNet++**: Discrete event simulator (with INET framework)
  - Use: Research, education, protocol development

- **Emulators**: Run actual network code/software
  - **GNS3**: Network software emulator (runs real network OS images)
  - **Mininet**: Network emulator for SDN/OpenFlow
  - Use: Testing real configurations before deployment

#### 3. SDN (Software-Defined Networking) Tools
- **Mininet**: SDN network emulator
  - Lightweight virtual network on single machine
  - OpenFlow protocol support
- **ComNetsEmu**: Enhanced Mininet variant
  - SDN/NFV emulation capabilities
  - Network slicing support
  - Integration with 5G emulators

#### 4. NFV (Network Function Virtualization) Architecture
- **NFVO (NFV Orchestrator)**:
  - **ETSI Open Source MANO (OSM)**: Industry-standard NFVO
  - Manages network services lifecycle
- **VIM (Virtual Infrastructure Manager)**:
  - **OpenStack**: VM orchestration platform
  - **Kubernetes**: Container orchestration platform
- **Purpose**: Virtualize network functions (firewall, load balancer, etc.)

#### 5. Virtualization Technologies
- **VM Creation**: VirtualBox, VMware
- **Container Creation**: Docker
- **VM Orchestration**: OpenStack
- **Container Orchestration**: Kubernetes
- **Key Difference**:
  - VMs: Full OS virtualization (heavier)
  - Containers: OS-level virtualization (lighter, faster)

#### 6. MEC (Multi-access Edge Computing) Tools
- **AdvanteEdge**: Mobile edge emulation platform
- **OpenNESS**: Open Network Edge Services Software (discontinued)
- **Purpose**: Bring computation closer to users for low latency

#### 7. 5G Development & Testing Tools

**Simulation Tools**:
- **Matlab 5G Toolbox**: Physical layer modeling
- **simu5G** (OMNet++): 5G network simulation
- **5G-LENA** (ns-3): 5G NR simulation

**Emulation/Deployment Tools**:
- **OpenAirInterface**: Open-source 5G software stack
- **UERANSIM**: 5G UE/RAN simulator
- **Open5GS**: Open-source 5G Core Network

**Field Testing**:
- **G-NetTrack, CellMapper**: Cell tower mapping and signal analysis
- **Android Code**: `*#*#4636#*#*` - Advanced cellular settings
  - View: NR state, frequency, bandwidth, signal strength, network type

#### 8. Security Testing Tools
- **SEED Security Labs**: Hands-on security exercises
  - Network security labs
  - Protocol security testing
- **Purpose**: Understanding network vulnerabilities and attacks

### Key Concepts for Exam

**Tool Selection Criteria**:
- **Packet Analysis**: Use Wireshark for detailed inspection, Tcpdump for automation
- **Network Testing**: Simulators (ns-3, OMNet++) for research; emulators (GNS3, Mininet) for realistic testing
- **SDN/NFV**: Mininet for SDN, OSM for NFV orchestration
- **5G**: simu5G/5G-LENA for simulation, OpenAirInterface for actual deployment

**Important Distinctions**:
1. **Simulator vs Emulator**:
   - Simulator = Mathematical models
   - Emulator = Real software/code execution
2. **VMs vs Containers**:
   - VMs = Full OS isolation, heavier
   - Containers = Shared kernel, lighter
3. **SDN vs NFV**:
   - SDN = Control plane separation (network programmability)
   - NFV = Virtualize network functions (software-based)

**Real-World Applications**:
- **Private 5G Networks**: OpenAirInterface + Open5GS
- **Network Slicing**: ComNetsEmu, Kubernetes
- **Edge Computing**: MEC platforms for low-latency applications
- **Network Security**: SEED labs for vulnerability assessment

### Practical Examples at UiS
- **Lyse's 5G Testbed**: Private 5G network with Radio Units at Innoasis, UiS, and hospital
- **5G-MODaNeI Project**:
  - Multi-access Edge Computing research
  - AI-based resource orchestration
  - Security and dependability focus
  - Equipment: Radio Units, edge servers with GPUs, carrier-grade switches

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
