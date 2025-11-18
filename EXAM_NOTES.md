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

### Computer Networks and Types

**Computer Network Definition**:
- Interconnected devices (computers, routers, switches, etc.) that communicate and share resources
- Network components: gateways, routers, switches, bridges, hubs, repeaters

**Network Types by Coverage**:
- **BAN (Body Area Network)**: On-body or implanted devices
- **PAN (Personal Area Network)**: Personal devices (~10m)
- **LAN (Local Area Network)**: Building or campus
- **MAN (Metropolitan Area Network)**: City-wide
- **WAN (Wide Area Network)**: Country/global scale

**Network Topologies**:
- **Bus**: All devices on single shared medium (hub or bus)
- **Ring**: Circular connection pattern
- **Star**: Central switch/hub with spoke connections
- **Hierarchical/Tree**: Multi-level switch/bridge structure
- **Mesh**: Interconnected routers with multiple paths

**Topology Characteristics**:
- **Centralized**: Single point of failure, limited scalability, easy development
- **Decentralized**: Multiple control points, better fault tolerance
- **Distributed**: No central control, high fault tolerance, complex development, high scalability

### Communication Methods

**Circuit Switching**:
- **Characteristics**: Dedicated communication path, constant resource allocation
- **Three phases**: Circuit establishment → Information transfer → Circuit disconnect
- **Connection-oriented** communication
- **Advantages**: Constant delay/jitter, transparent
- **Disadvantages**: Inefficient resource use
- **Example**: PSTN (Public Switched Telephone Network)

**Packet Switching**:
- **Characteristics**: Data divided into packets with headers
- **No dedicated path/resource** allocation
- **Datagram approach**: Connectionless
  - No call setup required
  - Each packet independent
- **Advantages**: Efficient resource sharing
- **Example**: Internet

### Link-Based Connection Challenges

**Physical Layer Challenges**:
- Representing 1s and 0s on the medium
- Signal propagation

**Data Link Layer Challenges**:
- **Fragmentation**: Dividing information into subunits
- **Error detection and correction**: Ensuring reliability
- **Flow control**: Deciding sending rate
- **Medium Access Control (MAC)**: Shared medium access

**Network Layer Challenges**:
- **Routing**: Finding paths through network
- **End-to-end reliability**: Guaranteed delivery
- **End-to-end flow control**: Preventing receiver overflow
- **Congestion control**: Managing network load

### Protocols and Layering

**Protocol Definition**:
- Formal standards and policies with rules, procedures, and formats
- Define communication between devices over a network
- Enable **interoperability and reusability**

**Protocol Layering**:
- Divides protocol design into smaller steps
- Creates **protocol stack**
- Each layer addresses specific challenges

**OSI (Open Systems Interconnection) 7-Layer Model**:
1. **Physical**: Representing 1s and 0s on medium
2. **Data Link**: MAC, synchronization, error control, flow control
3. **Network**: Addressing, routing
4. **Transport**: Reliability, flow and congestion control
5. **Session**: Establishing, managing, terminating sessions
6. **Presentation**: Eliminating syntax differences
7. **Application**: Applications

**Encapsulation/Decapsulation**:
- **Encapsulation**: Each layer adds header (some add trailer)
  - Application Header (AH) → Transport Header (TH) → Network Header (NH) → MAC Header (MH) + MAC Trailer (MT)
- **Decapsulation**: Reverse process at receiver

**End Systems vs Intermediate Systems**:
- **End systems**: All 7 OSI layers
- **Routers**: Network, Data Link, Physical layers
- **Switches/Bridges**: Data Link, Physical layers

### Networking Equipment by OSI Layer

**Physical Layer**:
- **Repeater**: Amplifies signal
- **Hub**: Multi-port repeater

**Data Link Layer (MAC)**:
- **Bridge**: Connects network segments
- **Switch**: Multi-port bridge with forwarding table

**Network Layer**:
- **Router**: Forwards packets between networks using routing tables

### Internetworking

**Concept**:
- Interconnection of multiple networks
- **Hierarchical structure**: LAN → MAN → WAN
- Each network maintains its identity
- Uses end systems and intermediate systems

**Internet Protocol Suite (TCP/IP)**:
- **5 Layers** (simplified from OSI):
  1. **Application**: ftp, http, smtp, pop
  2. **Transport**: TCP (reliable), UDP (unreliable)
  3. **Network**: IP, ICMP, IGMP, ARP, RARP, BOOTP, DHCP
  4. **Data Link**: IEEE 802.11 (Wireless), IEEE 802.3 (Ethernet)
  5. **Physical**: Wireless, Fiber Optic, Twisted Pair, Coax

**Hour Glass Architecture**:
- Narrow waist at Network layer (IP)
- Many applications and physical technologies
- IP provides universal interconnection

### Standardization Organizations

- **IETF**: Internet Engineering Task Force (Internet protocols)
- **IEEE**: Institute of Electrical and Electronics Engineers (Wireless/wired communication)
- **ITU**: International Telecommunication Union (Telecom protocols, PSTN)
- **ETSI**: European Telecommunications Standards Institute
- **ISO**: International Organization for Standardization
- **3GPP**: Third Generation Partnership Project (Cellular standards)
- **5GPPP**: 5G Infrastructure Public-Private Partnership

### Wireless Network Challenges

**Wireless Channel Characteristics**:
- **High interference**: Radio signals interfere
- **Limited coverage**: Distance and obstacles limit range
- **Error prone**: Higher bit error rate than wired
- **User mobility**: Devices move during communication
- **Variability**: Channel conditions change dynamically

**Impact Across Layers**:
- Challenges affect multiple layers:
  - Physical layer: Signal quality
  - Data Link layer: Multiple access control, error control
  - Network layer: Routing with mobility
  - Transport layer: TCP performance degradation

### Wireless Network Taxonomy

**By Range and Technology**:
- **Long Range**:
  - Cellular technologies (2G-5G)
  - WiMax
- **Medium Range**:
  - WiFi (802.11)
  - Z-Wave
- **Short Range**:
  - Bluetooth
  - NFC (Near Field Communication)
  - ZigBee

**By Infrastructure**:
- **Infrastructureless**:
  - Ad-Hoc Networks
  - Sensor Networks
  - Mesh Networks
- **Infrastructured**:
  - LAN (WiFi access points)
  - WAN (Cellular networks)

**By Tier**:
- **High Tier**:
  - Designed for pedestrian AND vehicular speeds
  - Coverage of large geographical areas
  - Example: Cellular networks
- **Low Tier**:
  - Designed for pedestrian speeds only
  - Short coverage range
  - Example: WiFi, Bluetooth

**By Spectrum**:
- **Licensed Spectrum**:
  - Exclusive use
  - Classical cellular networks
  - Requires license from regulatory authority
- **Shared Spectrum**:
  - Shared exclusive use
  - Authorized Shared Access (ASA)
- **Unlicensed Spectrum**:
  - Shared use by multiple technologies
  - WiFi, Bluetooth, ZigBee (ISM bands)

### Ad-Hoc Networking

**Characteristics**:
- **Infrastructureless**: No fixed base stations
- **Multihop**: Data relayed through intermediate nodes
- **Dynamic topology**: Nodes can be mobile
- **Self-organizing**: No centralized control

**Applications**:
- Temporary network deployment (conferences, meetings)
- Disaster relief operations
- Smart buildings
- Cooperative objects (vehicles, robots)
- Healthcare (patient monitoring)

**Challenges**:
- **Wireless medium**: All general wireless challenges
- **Interference**: Hidden terminal and exposed terminal problems
- **Mobility**: Topology changes frequently
- **Node failures**: Unreliable nodes
- **Self-forming and self-configuration**: Automatic network setup
- **Topology maintenance**: Adapting to changes
- **Routing**: Finding paths in dynamic topology
- **Self-healing**: Recovering from failures
- **Node localization**: Determining positions
- **Time synchronization**: Coordinating time across nodes
- **End-to-end reliability**: Multi-hop reliability
- **Congestion control**: Distributed control

### Cellular Networking

**Characteristics**:
- **Infrastructured**: Fixed base stations and switches
- **Single hop**: Terminals communicate directly with base station
- **Planned deployment**: Engineered coverage

**Architecture Components**:
- **Cell**: Geographic coverage area
- **Base Station Transceiver (Radio Port)**: Wireless interface
- **Base Station Controller (Radio Port Controller)**: Manages multiple base stations
- **Mobile Switching Center**: Connects to other networks/cells

**Ad-hoc vs Cellular Comparison**:

| Aspect | Ad-Hoc | Cellular |
|--------|--------|----------|
| **Infrastructure** | None | Fixed infrastructure |
| **Topology** | May change often (mobility/failures) | Infrastructure seldom changes |
| **Node Role** | Terminals relay others' traffic | Infrastructure relays, terminals don't |
| **Links** | Mostly wireless, multi-hop | Wireless access + wired/wireless backbone |

### Sensor Networks

**Architecture Components**:
- **Sensor Nodes (snode)**: Sense environment
- **Actuator Nodes (anode)**: Act on environment
- **Collector Nodes (cnode)**: Aggregate sensor data
- **Gateway Nodes (gnode)**: Connect to external networks
- **Task Manager**: Coordinates sensing tasks
- **Proxy Server**: Data storage and processing

**Design Factors**:
- **Environment**: Often harsh, hostile, unreachable
- **Fault Tolerance**: High requirements, critical points of failure
- **Scalability**: Order of thousands of nodes
- **Production Cost**: Must be cost-effective (mass deployment)
- **Hardware Constraints**: Tiny, low processing power, limited memory
- **Topology**: Generally fixed, network mobility possible
- **Power Consumption**: VERY CRITICAL (battery-powered)

**Networking Regime**:
- One-to-many (broadcast commands)
- Many-to-one (data collection)
- Many-to-many (distributed sensing)

**Traffic Characteristics**:
- Temporally and spatially correlated
- Data-centric (not address-centric)

**QoS Requirements**:
- Power consumption (most critical)
- Delay
- Reliability

### Mesh Networks

**Architecture**:
- **Mesh Routers**: Form backbone, relay traffic
- **Mesh Clients**: End devices (laptops, phones)
- **Backbone Mesh**: Router-to-router connections
- **Access Mesh**: Client-to-router connections

**Integration**:
- Connect to Internet
- Interwork with Cellular networks
- Extend Wireless LAN coverage

**Applications**:
- Broadband home networking
- Community and neighborhood networking
- Enterprise networking
- Transportation systems
- Building automation and control networks

**Characteristics**:
- **Infrastructure**: Typically fixed mesh routers
- **Self-forming**: Automatic network configuration
- **Self-healing**: Automatic route recovery
- **Multi-hop**: Extended coverage through relaying

### Network Paradigm Comparison

| Factor | Ad-Hoc | Mesh | Sensor/Actuator |
|--------|--------|------|-----------------|
| **Medium** | ISM | ISM | ISM, acoustic, low antenna |
| **Networking** | Random 1-to-1 | Random 1-to-1, gateway nodes | 1-to-many, many-to-1, many-to-many |
| **Traffic** | Random, multimedia | Random, multimedia | Correlated, data |
| **QoS** | Bandwidth, delay, jitter | Bandwidth, delay, jitter | Power, delay, reliability |
| **Mobility** | Mobile | Typically fixed | Generally fixed, network mobility |
| **Fault Tolerance** | No critical point | Critical points | Critical points, high requirements |
| **Environment** | Day-to-day | Day-to-day | Hostile, harsh, unreachable |
| **Power** | Not very critical | Not critical | VERY critical |
| **Scalability** | Hundreds | Tens | Thousands |
| **Hardware** | Laptops, PDAs | No constraint | Tiny, low power/memory |
| **Cost** | No hard constraints | No hard constraints | Must be cost-effective |

### Networking Tools

**Packet Analyzers**:
- **Wireshark**: Free, open-source, GUI-based
- **Tcpdump**: CLI-based packet capture

**Network Simulators/Emulators**:
- **Cisco Packet Tracer**: Visual simulator
- **GNS3**: Network software emulator

**Diagnostic Tools (Unix/Linux)**:
- **ping**: ICMP echo test (reachability)
- **traceroute**: Path discovery
- **iperf**: Network performance measurements
- **netstat**: Network statistics
- **nslookup**: DNS queries
- **ifconfig**: Interface configuration
- **nmap**: Network scanning

**Monitoring**:
- **PRTG**: SNMP-based device performance monitoring

### Exam Tips for Lecture 1:

- Understand **difference between circuit and packet switching**
- Know **OSI layers** and their functions
- Understand **encapsulation process** (headers/trailers)
- Be able to **compare ad-hoc, cellular, sensor, and mesh networks**
- Know **wireless network challenges** and how they differ from wired
- Understand **network taxonomy** (by range, infrastructure, tier, spectrum)
- Know **standardization organizations** and their roles
- Understand **networking equipment** at each OSI layer
- Be able to explain **hidden/exposed terminal problems** (from wireless challenges)
- Know **design factors for sensor networks** (especially power consumption)
- Understand **Internet Protocol Suite hour glass architecture**

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

### Multiple Access Schemes - Classification

**Three Categories:**
1. **Contention-Based**: Aloha, Slotted Aloha, CSMA variants
2. **Conflict-Free (Fixed Allocation)**: FDMA, TDMA, CDMA, OFDMA, NOMA
3. **Hybrid**: Reservation-based (PRMA, D-TDMA, RAMA), Token-based (Token Ring/Bus)

### CSMA (Carrier Sense Multiple Access)

**Basic Principle**: Sense the media before transmitting

**CSMA Variants:**
- **1-Persistent CSMA**: If idle → transmit immediately; if busy → wait and sense continuously
- **Non-Persistent CSMA**: If idle → transmit; if busy → wait random time, then repeat
- **p-Persistent CSMA**: If idle → transmit with probability p; if not → wait next slot

**CSMA/CD (Collision Detection)**:
- Monitor for collisions DURING transmission
- **Exponential Backoff**: After nth collision, wait random slots from [0, 2^n-1]
- Time slot = 2τ (τ = worst-case propagation time)
- **Used in**: Ethernet (IEEE 802.3)

**CSMA/CA (Collision Avoidance)**:
- **Why needed**: Cannot detect collisions in wireless (hidden terminal problem)
- **RTS/CTS mechanism**: Request to Send → Clear to Send → Data → ACK
- **DCF (Distributed Coordination Function)**: Controls waiting time (DIFS, SIFS)
- **NAV (Network Allocation Vector)**: Counter for transmission duration
- **Used in**: WiFi (IEEE 802.11)

### Hidden and Exposed Terminal Problems

**Hidden Terminal Problem**:
- Two nodes (A and C) transmit to B simultaneously
- A and C cannot sense each other (hidden)
- Causes collision at B
- **Solution**: RTS/CTS mechanism in CSMA/CA

**Exposed Terminal Problem**:
- Node C wants to transmit to D but senses transmission from B→A
- C defers unnecessarily (overhearing)
- Reduces channel efficiency

### CDMA (Code Division Multiple Access)

**Core Concept**: Spread Spectrum - spread signal over wider bandwidth using codes

**Spread Spectrum Types:**
1. **FHSS (Frequency Hopping)**: Signal hops across frequencies
   - Slow Hopping: Tc ≥ Ts
   - Fast Hopping: Tc < Ts
   - Process Gain: Gp = 10 log C (C = number of frequency channels)

2. **DSSS (Direct Sequence)**: Each bit spread by chip sequence
   - Process Gain: Gp = 10 log (Bss/B)
   - Implemented using DFT/IDFT (FFT/IFFT)

**PN Sequences (Pseudonoise):**
- **Maximum Length Sequence Properties**:
  1. **Balance**: |#(1s) - #(-1s)| ≤ 1
  2. **Run**: 50% are -1 runs, 50% are 1 runs; 1/2^n are n-length runs
  3. **Auto-correlation**: C0 = N, Ck = -1 for k ≠ 0 (mod N)

- **Short Codes**: Length 2^15-1 (used in downlink, identify cells)
- **Long Codes**: Length 2^42-1 (used in uplink, identify mobile terminals)

**Orthogonal Codes:**
- **Walsh-Hadamard Codes**: Cross-correlation = 0
- Used for channelization in downlink
- Variable-length codes from code tree

**CDMA Advantages:**
- Soft capacity (limited by interference)
- All frequencies reused in neighboring cells
- Soft handoff (no frequency change needed)
- Power control reduces interference
- Inherent frequency diversity

### OFDM/OFDMA

**OFDM (Orthogonal Frequency Division Multiplexing)**:
- Multiple closely-spaced subcarriers at different frequencies
- Original stream R bps split into N substreams of R/N bps
- Bit duration increases from 1/R to N/R

**Orthogonality Property**:
- Peak of each subcarrier occurs where others are zero
- No interference between subcarriers
- fb must be multiple of 1/T (T = bit time of subcarrier)
- Two signals orthogonal if: Average[s1(t)s2(t)] = 0

**Implementation**:
- **FFT/IFFT**: Efficient DFT computation (N must be power of 2)
- **Cyclic Prefix (CP)**: Guard interval + copy of OFDM symbol
  - Combats ISI
  - Maintains orthogonality

**OFDM Advantages**:
- Frequency selective fading affects only some subcarriers
- ISI overcome (longer symbol duration)
- No equalizer needed (with CP)
- Efficient spectrum utilization

**OFDM Difficulties**:
- **PAPR (Peak-to-Average Power Ratio)**: High peak values require expensive power amplifiers
- **ICI (Intercarrier Interference)**: Requires tight frequency synchronization

**OFDMA**:
- Subcarriers divided into **subchannels**
- Each user assigned one or more subchannels
- **Subchannelization**: How subchannels allocated to users (important for power saving)

**SC-FDMA (Single-Carrier FDMA)**:
- Extra DFT before subcarrier mapping
- Lower PAPR than OFDMA
- Used in **uplink only** (e.g., LTE uplink)
- Same data stream on all subcarriers (spread)

### NOMA (Non-Orthogonal Multiple Access)

**Goal**: Support more users than available orthogonal resources

**Two Categories**:
1. **Code Domain**: Different spreading sequences (like CDMA but improved)
2. **Power Domain**: Different power levels allocated to users

**Key Techniques**:
- **Superposition Coding** at transmitter
- **Successive Interference Cancellation (SIC)** at receiver

**Advantages**:
- Supports diverse service requirements (eMBB, URLLC, mMTC)
- Better spectrum efficiency than OMA
- Enables network slicing for 5G

### Comparison: CDMA vs OFDMA

| Feature | CDMA | OFDMA |
|---------|------|-------|
| **Separation** | Code | Frequency |
| **Bandwidth** | Wide (spread) | Divided into subcarriers |
| **Flexibility** | Limited | High (adaptive modulation per subcarrier) |
| **PAPR** | Low | High (issue for uplink) |
| **Frequency Reuse** | 1 (all frequencies) | Requires planning |
| **Multipath** | Rake receiver | Cyclic prefix |
| **Complexity** | High (code synchronization) | Moderate (FFT/IFFT) |

### Key Formulas

**Auto-correlation**: Ck = Σ(an × an+k) for n=1 to N

**Cross-correlation**: Rk = Σ(an × bn+k) for n=1 to N

**Process Gain (FHSS)**: Gp = 10 log C dB

**Process Gain (DSSS)**: Gp = 10 log (Bss/B) dB

### Exam Tips for Lecture 3:
- Understand **why CSMA/CA** instead of CSMA/CD for wireless
- Be able to **explain hidden/exposed terminal** with diagrams
- Know **properties of PN sequences** (balance, run, auto-correlation)
- Understand **orthogonality** concept in both CDMA and OFDMA
- Know **differences between OFDM and SC-FDMA** (especially PAPR)
- Understand **NOMA benefits** for 5G diverse services
- Be able to **compare CDMA vs OFDMA** (pros/cons)
- Understand **cyclic prefix** purpose in OFDM

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
