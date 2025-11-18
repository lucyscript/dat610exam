# DAT610 Wireless Communications - Comprehensive Lecture Summary

## Table of Contents
1. [Lecture 1: Technological Background](#lecture-1-technological-background)
2. [Lecture 2: Physical Layer](#lecture-2-physical-layer)
3. [Lecture 3: Data Link Layer MAC](#lecture-3-data-link-layer-mac)
4. [Lecture 4: Data Link Layer Coding](#lecture-4-data-link-layer-coding)
5. [Lecture 5a: Network Layer](#lecture-5a-network-layer)
6. [Lecture 5b: Transport Layer](#lecture-5b-transport-layer)
7. [Lecture 6: Cellular Networks](#lecture-6-cellular-networks)
8. [Lecture 7: WLAN-PAN-LPWAN](#lecture-7-wlan-pan-lpwan)
9. [Lecture 8: Tools](#lecture-8-tools)
10. [Lecture 9: Wireless Security](#lecture-9-wireless-security)
11. [Lecture 10: IoT](#lecture-10-iot)

---

## Lecture 1: Technological Background

### Overview
This lecture establishes the fundamental concepts of computer networks and introduces the unique challenges of wireless communications. Understanding these basics is critical for all subsequent lectures.

### Key Concepts

#### 1. Computer Networks Fundamentals

**What is a Computer Network?**
- Interconnected computing devices communicating through networking equipment
- Equipment: Gateways, routers, switches, bridges, hubs, repeaters

**Network Types by Scale:**
- **BAN** (Body-Area Network): On/around human body
- **PAN** (Personal-Area Network): Personal devices (~10m range)
- **LAN** (Local-Area Network): Building or campus
- **MAN** (Metropolitan-Area Network): City-wide
- **WAN** (Wide-Area Network): Country/continent-wide

#### 2. Network Topologies

**Physical Topologies:**
- **Bus**: All nodes connected to single cable
- **Ring**: Nodes in circular formation
- **Star**: All nodes connected to central hub/switch
- **Hierarchical/Tree**: Branching structure
- **Mesh**: Nodes interconnected with multiple paths

**Architectural Models:**
- **Centralized**: Single point of control (easy maintenance, single point of failure)
- **Decentralized**: Multiple control points (better fault tolerance)
- **Distributed**: No central control (maximum fault tolerance, scalability, and diversity)

#### 3. Switching Technologies

**Circuit Switching:**
- Dedicated communication path established for entire session
- Three phases: Circuit establishment → Information transfer → Circuit disconnect
- Constant resource allocation (predictable delay and jitter)
- Transparent but inefficient use of resources
- Example: PSTN (Public Switched Telephone Network)
- Connection-oriented communication

**Packet Switching:**
- Data divided into packets with headers containing control information
- No dedicated path or resource reservation
- **Datagram approach** is connectionless:
  - No call setup required
  - Each packet routed independently
  - Packets may take different routes
- More efficient resource utilization
- Variable delay and jitter

#### 4. Networking Challenges

**Link-Level Challenges:**
- Representing 1s and 0s on the physical medium (encoding)
- Fragmentation of data units
- Error detection and correction (reliability)
- Flow control (managing sending rate)
- Medium Access Control (MAC) - who can transmit when

**Network-Level Challenges:**
- **Routing**: Finding paths through the network
- **End-to-end reliability**: Ensuring data reaches destination correctly
- **End-to-end flow control**: Managing traffic across multiple hops
- **Congestion control**: Preventing network overload

**Solution**: Protocol layering and standardization

#### 5. Protocol Layering

**OSI Model (7 Layers):**

1. **Physical Layer**
   - Representing 1s and 0s on the transmission medium
   - Hardware: Repeaters, hubs

2. **Data Link Layer**
   - MAC (Medium Access Control)
   - Synchronization
   - Error control
   - Flow control
   - Framing
   - Hardware: Bridges, switches

3. **Network Layer**
   - Addressing
   - Routing
   - Packet forwarding
   - Hardware: Routers

4. **Transport Layer**
   - End-to-end reliability
   - Flow control
   - Congestion control
   - Protocols: TCP, UDP

5. **Session Layer**
   - Establishing, managing, and terminating sessions

6. **Presentation Layer**
   - Eliminating syntax differences
   - Data format conversion

7. **Application Layer**
   - Applications and services
   - Protocols: HTTP, FTP, SMTP, POP

**Key Principle**: Protocol layering divides design into manageable steps, creating a protocol stack

#### 6. Internet Protocol Suite (TCP/IP)

**"Hour Glass" Architecture:**
- Application Layer: FTP, HTTP, SMTP, POP
- Transport Layer: TCP, UDP
- **Network Layer (IP)**: Narrow waist - all traffic goes through IP
- Data Link Layer: IEEE 802.11 (wireless), IEEE 802.3 (Ethernet)
- Physical Layer: Wireless, Fiber Optic, Twisted Pair, Coax

**Supporting Protocols:**
- **ICMP**: Internet Control Message Protocol
- **IGMP**: Internet Group Management Protocol
- **ARP/RARP**: Address Resolution Protocol
- **DHCP/BOOTP**: Dynamic addressing

#### 7. Internetworking

**Concept:**
- Interconnection of multiple networks
- Each network maintains its identity
- Hierarchical organization: LAN → MAN → WAN
- **End systems**: User devices
- **Intermediate systems**: Routers, switches (ISO terminology)

**The Internet:**
- Global internetwork using the Internet Protocol Suite
- Enables communication across heterogeneous networks

#### 8. Wireless Network Challenges

**Unique Wireless Challenges:**
- **High Interference**: From other devices and environmental factors
- **Limited Coverage**: Signal attenuation over distance
- **Error Prone**: Higher bit error rates than wired
- **User Mobility**: Changing topology, handoffs
- **Variability**: Channel conditions change dynamically

**Cross-Layer Impact:**
These physical challenges affect:
- **MAC Layer**: Collision detection/avoidance mechanisms
- **Error Control**: More sophisticated FEC/ARQ needed
- **Network Layer**: Routing must handle mobility
- **Transport Layer**: TCP assumes congestion, not errors

#### 9. Wireless Communication Taxonomy

**By Range:**
- **Long Range**: Cellular technologies (1G-5G), WiMax
- **Medium Range**: Wi-Fi, Z-Wave
- **Short Range**: Bluetooth, NFC, ZigBee

**By Infrastructure:**
- **Infrastructureless**: Ad-hoc, Sensor, Mesh networks
- **Infrastructured**: LAN (WiFi with AP), WAN (Cellular)

**By Tier:**
- **High Tier**: Pedestrian and vehicular speeds, large geographical coverage
- **Low Tier**: Pedestrian speeds only, short coverage range

**By Spectrum:**
- **Licensed Spectrum**: Exclusive use (classical cellular networks)
- **Shared Spectrum**: Shared exclusive use (Authorized Shared Access - ASA)
- **Unlicensed Spectrum**: Shared use (WiFi, Bluetooth, ZigBee)

#### 10. Wireless Network Paradigms

### A. Ad-Hoc Networks

**Characteristics:**
- **Infrastructureless**: No fixed base stations
- **Multihop**: Nodes relay traffic for others
- **Dynamic topology**: Nodes can be mobile
- **Peer-to-peer**: All nodes are equal

**Applications:**
- Temporary network deployment
- Disaster relief operations
- Smart buildings
- Cooperative objects
- Healthcare monitoring

**Challenges:**
- Wireless medium issues (interference, fading)
- Hidden terminal and exposed terminal problems
- Mobility and node failures
- Self-forming and self-configuration
- Topology maintenance
- Routing in dynamic environments
- Node localization
- Time synchronization
- End-to-end reliability
- Congestion control without infrastructure

### B. Cellular Networks

**Characteristics:**
- **Infrastructured**: Fixed base stations
- **Single hop**: Devices connect directly to base station
- **Centralized control**: Network manages resources

**Architecture (hierarchical):**
- **Cell**: Geographic coverage area
- **Base Station Transceiver (BST)** / Radio Port: Communicates with mobile devices
- **Base Station Controller (BSC)** / Radio Port Controller: Controls multiple BSTs
- **Mobile Switching Center (MSC)**: Connects to other networks

**Comparison: Ad-hoc vs Cellular:**

| Aspect | Ad-hoc | Cellular |
|--------|--------|----------|
| Infrastructure | None | Fixed infrastructure |
| Topology | Dynamic, changes often | Fixed infrastructure, mobile terminals |
| Node role | Terminals relay traffic | Infrastructure relays, terminals don't |
| Links | Mostly wireless, multihop | Wireless access + wired/wireless backbone |
| Deployment | Quick, flexible | Planned, expensive |

### C. Sensor & Actuator Networks

**Components:**
- **Sensor nodes (snodes)**: Collect environmental data
- **Actuator nodes (anodes)**: Perform actions based on data
- **Collector nodes (cnodes)**: Aggregate sensor data
- **Gateway nodes (gnodes)**: Connect to external networks

**Architecture:**
- Sensor fields → Collectors → Gateway → Internet → Task Manager/Users
- Can include actuators for closed-loop control

**Design Factors:**
1. **Environment**: Often hostile, harsh, unreachable
2. **Fault Tolerance**: High requirements, redundancy needed
3. **Scalability**: Order of thousands of nodes
4. **Production Cost**: Must be cost-effective
5. **Hardware Constraints**: Tiny devices, low processing power, limited memory
6. **Topology**: Generally fixed, possible network mobility
7. **Power Consumption**: CRITICAL - battery-powered, hard to replace

**Traffic Patterns:**
- One-to-many (commands to sensors)
- Many-to-one (sensor data to collector)
- Many-to-many (sensor collaboration)
- Temporally and spatially correlated data

### D. Mesh Networks

**Architecture:**
- **Mesh Routers**: Form backbone, relay traffic
- **Mesh Clients**: End-user devices
- **Backbone Mesh**: Router-to-router communication
- **Access Mesh**: Client-to-router communication

**Integration:**
- Can connect to: Internet, Cellular networks, Wireless LANs
- Provides extended coverage and redundancy

**Applications:**
- Broadband home networking
- Community and neighborhood networking
- Enterprise networking
- Transportation systems
- Building automation and control

### Comparison: Ad-hoc vs Sensor vs Mesh

| Factor | Ad-hoc | Mesh | Sensor |
|--------|--------|------|--------|
| Wireless medium | ISM | ISM | ISM, acoustic, low antenna |
| Networking | Random one-to-one | Random one-to-one, gateways | Many-to-one, many-to-many |
| Traffic | Random, multimedia | Random, multimedia | Correlated, data |
| QoS needs | Bandwidth, delay, jitter | Bandwidth, delay, jitter | Power, delay, reliability |
| Mobility | Mobile | Typically fixed | Generally fixed |
| Fault tolerance | No critical point | Critical points | High requirements |
| Environment | Typical | Typical | Hostile, harsh |
| Power efficiency | Not very critical | Not critical | **VERY CRITICAL** |
| Scalability | Order of hundreds | Order of tens | Order of thousands |
| Hardware | Laptops, PDAs | No constraint | Tiny, limited capacity |
| Cost | No hard constraints | No constraints | Must be cost-effective |

#### 11. Standardization Organizations

**Major Organizations:**
- **IETF** (Internet Engineering Task Force): Internet protocols
- **IEEE** (Institute of Electrical and Electronics Engineers): Wireless and wired communication standards
- **ITU** (International Telecommunication Union): Telecommunication protocols and PSTN
- **ETSI** (European Telecommunications Standards Institute): European standards
- **ISO** (International Organization for Standardization): General standards
- **3GPP** (Third Generation Partnership Project): Cellular standards
- **5GPPP** (5G Infrastructure Public-Private Partnership): 5G development

#### 12. Networking Tools

**Packet Analysis:**
- **Wireshark**: Free, open-source packet analyzer (GUI)
- **Tcpdump**: Command-line packet analyzer

**Network Simulation/Emulation:**
- **Cisco Packet Tracer**: Visual network simulator
- **GNS3**: Network software emulator

**Diagnostic Tools:**
- **ping**: ICMP-based connectivity testing
- **traceroute**: Path discovery
- **iperf**: Network performance measurements
- **netstat**: Network statistics
- **nslookup**: DNS queries
- **ifconfig**: Interface configuration
- **nmap**: Network scanning

**Monitoring:**
- **PRTG**: SNMP-based intermediate device monitoring

### Exam Focus Areas

**High-Priority Topics:**
1. Understand the difference between circuit switching and packet switching
2. Know all 7 OSI layers and their functions
3. Understand the Internet Protocol Suite (TCP/IP) hour-glass model
4. Know the additional challenges of wireless networks beyond wired
5. Be able to compare ad-hoc, cellular, sensor, and mesh networks
6. Understand network topologies and their trade-offs

**Common Exam Questions:**
- Explain the challenges addressed at each layer of the OSI model
- Compare circuit switching vs packet switching
- What are the unique challenges of wireless networks compared to wired?
- Compare infrastructureless vs infrastructured wireless networks
- Explain the difference between ad-hoc, sensor, and mesh networks
- Why is power consumption critical for sensor networks but not ad-hoc networks?

**Key Takeaways:**
- Protocol layering solves complex networking problems by dividing them into manageable parts
- Wireless networks face additional challenges (mobility, interference, errors, power)
- Different wireless paradigms suit different applications
- Understanding fundamentals is essential for all wireless technologies

---

## Lecture 2: Physical Layer

*Summary will be added here*

---

## Lecture 3: Data Link Layer MAC

### Overview

The Data Link Layer's Medium Access Control (MAC) sublayer is responsible for coordinating how multiple devices share a common transmission medium. This lecture covers the fundamental question: "Who gets to transmit when?" and explores various schemes from simple contention-based approaches to sophisticated conflict-free and hybrid methods.

 

### Key Concepts

 

#### 1. Multiplexing vs Multiple Access

 

**Multiplexing (Physical Layer):**

- Function that permits two or more data sources to share a common transmission medium

- Each data source has its own channel

- How to divide a larger-capacity channel into multiple smaller-capacity subchannels

- Operates at the Physical Layer

 

**Multiple Access (Data Link Layer):**

- Function that allows multiple users to share a transmission channel

- Each user has a subchannel

- Operates at the Data Link Layer

 

**Key Questions for Multiple Access:**

- Which terminal starts transmitting?

- How long can a terminal transmit?

- How can a collision be resolved?

- Which terminal should receive?

 

#### 2. Multiple Access Scheme Categories

 

**Contention-Based Schemes:**

- Aloha, Slotted Aloha

- CSMA (Carrier Sense Multiple Access)

- CSMA/CD (Collision Detection)

- CSMA/CA (Collision Avoidance)

 

**Conflict-Free Schemes:**

- Fixed Allocation: FDMA, TDMA, CDMA, OFDMA, NOMA

- Token Based: Token Ring, Token Bus

 

**Hybrid Schemes:**

- Reservation Based: PRMA, D-TDMA, RAMA

 

#### 3. Contention-Based Schemes

 

**ALOHA:**

- Start transmitting whenever you have a frame to send

- Retransmit if the transmission is unsuccessful

- Simple but inefficient due to collisions

 

**Slotted ALOHA:**

- Time divided into discrete slots

- Wait until the beginning of the first time slot for transmission

- Reduces collision window by half compared to pure ALOHA

- Improves throughput from ~18% to ~36%

 

**Carrier Sense Multiple Access (CSMA):**

 

Three variants based on behavior when medium is busy:

 

1. **1-Persistent CSMA:**

   - Sense medium; if idle, transmit immediately

   - If busy, continuously sense and transmit when becomes idle

   - High collision probability when multiple stations waiting

 

2. **Non-Persistent CSMA:**

   - If medium busy, wait a random period without sensing

   - Then repeat algorithm

   - Reduces collisions but increases delay

 

3. **p-Persistent CSMA:**

   - When medium becomes idle, transmit with probability p

   - With probability (1-p), wait for next time slot

   - Balances collision probability and delay

   - Used in slotted systems

 

**CSMA/CD (Collision Detection):**

- Monitor for collisions during transmission

- Used in Ethernet (IEEE 802.3)

- **Collision Detection Procedure:**

  1. Continue transmission (send jam signal)

  2. Increment retransmission counter

  3. Calculate random backoff period

  4. Wait and retry

 

**Exponential Backoff:**

- After nth collision, wait random number of slots from [0, 2^n - 1]

- Time slot = 2τ, where τ is worst case propagation time

- Backoff window grows exponentially with collisions

- Example: After 1st collision: [0,1], 2nd: [0,3], 3rd: [0,7], 4th: [0,15]

 

**CSMA/CA (Collision Avoidance):**

- CSMA/CD unreliable in wireless due to hidden terminal problem

- Monitoring while transmitting is challenging in wireless

- If media busy, behaves as non-persistent CSMA

 

**Key Functionalities:**

 

1. **RTS/CTS (Request to Send / Clear to Send):**

   - Solves hidden terminal problem

   - Short control frames exchanged before data transmission

   - Sequence: RTS → CTS → DATA → ACK

   - Example: MACAW (Multiple Access with Collision Avoidance Wireless)

 

2. **DCF (Distributed Coordination Function):**

   - Selects waiting time before transmitting in idle media

   - **DIFS** (DCF Interframe Space): For media monitoring

   - **SIFS** (Short Interframe Space): For packet processing

   - **NAV** (Network Allocation Vector): Virtual carrier sensing

   - RTS contains transmission duration to set NAV in other terminals

 

3. **PCF (Point Coordination Function):**

   - Optional centralized access control

   - Polling-based approach

 

**Interframe Spaces:**

- **SIFS**: Shortest, used for ACK, CTS

- **DIFS**: Medium, used for new frame transmission

- **EIFS** (Extended Interframe Space): Longest, used when frame not decoded

  - Ensures ACK transmission proceeds without interference

  - Used by terminals in carrier sensing zone

 

**Issues with CSMA/CA:**

- RTS, CTS, frames, and interframe spaces introduce overhead and delay

- Carrier sensing range > transmission range

- Terminals in carrier sensing zone sense but cannot decode transmission

 

#### 4. Hidden and Exposed Terminal Problems

 

**Hidden Terminal Problem:**

- Two terminals (A and C) can't hear each other but both can reach middle terminal (B)

- Both may transmit simultaneously, causing collision at B

- Primary interference problem

- Solved by RTS/CTS mechanism

 

**Exposed Terminal Problem:**

- Terminal C hears transmission from A to B

- C unnecessarily defers its transmission to D

- Overhearing problem

- Reduces spatial reuse efficiency

 

#### 5. Code Division Multiple Access (CDMA)

 

**Spread Spectrum Concept:**

- Spread information signal over wider bandwidth

- Initially developed for military/intelligence purposes

- Signal modulated by pseudonoise spreading code

 

**Types of Spread Spectrum:**

 

1. **FHSS (Frequency Hopping Spread Spectrum):**

   - Signal broadcasts over seemingly random series of frequencies

   - **Slow Hopping**: Tc ≥ Ts (hop time ≥ symbol time)

   - **Fast Hopping**: Tc < Ts

   - **Process Gain**: Gp = 10 log C (dB), where C = number of frequency channels

 

2. **DSSS (Direct Sequence Spread Spectrum):**

   - Each bit represented by multiple chips in transmitted signal

   - Chip sequence spreads data across wider bandwidth

   - **Process Gain**: Gp = 10 log(Bss/B) (dB)

     - B = bandwidth for data rate

     - Bss = spread spectrum bandwidth

   - Spreads signal over wider bandwidth, making it noise-like

   - Provides interference rejection and privacy

 

**DSSS System Components:**

- **Transmitter**: Data → Spreading Code (XOR) → Modulation → Transmission

- **Receiver**: Reception → Demodulation → Correlator (with same spreading code) → Data

- Receiver narrows bandwidth of desired user's signal

- Doesn't despread signals from other users (appear as noise)

 

**DS-CDMA Codes:**

 

1. **Pseudo Noise (PN) Sequences:**

   - Resulting signal is noise-like

   - Generated deterministically with seed

   - **Short codes**: 2^15-1 (used in downlink to identify cells/location areas)

   - **Long codes**: 2^42-1 (used in uplink to identify mobile terminals)

   - Period = length before sequence repeats

 

**Maximum Length Sequences (m-sequences):**

 

Properties:

- **Balance property**: Difference in number of 1s and -1s ≤ 1

- **Run property**: 50% runs are -1 runs, 50% are 1 runs; 1/2^n of runs are length n

- **Auto-correlation property**: When shifted, number of same chips differs from different chips by ≤ 1

 

**Auto-correlation**: Ck = Σ(an × an+k) for n=1 to N

- C0 = N, Ck = -1 for k ≠ 0 (ideal for m-sequence)

 

**Maximum Length Sequence Generator:**

- Linear feedback shift register (LFSR)

- Period p = 2^n - 1, where n = number of bits in shift register

- Example: 4-bit LFSR produces sequence of length 15

 

2. **Orthogonal Codes:**

   - Used for channelization in downlink

   - Low autocorrelation

   - **Zero cross-correlation**: R0 = 0 for all shifts

   - Requires tight synchronization

 

**Cross-correlation**: Rk = Σ(an × bn+k) for n=1 to N

- Two codes orthogonal if cross-correlation = 0 for all shifts

 

**Walsh-Hadamard Codes:**

- Recursive generation: H2n = [[Hn, Hn], [Hn, H̄n]]

- H1 = [0], H2 = [[0,0],[0,1]], H4 = [[0,0,0,0],[0,1,0,1],[0,0,1,1],[0,1,1,0]]

- Every row orthogonal to every other row

- Requires tight synchronization

 

**Variable-Length Orthogonal Codes:**

- Tree structure for different code lengths

- Codes orthogonal if neither lies on path from other to root

- Supports variable data rates

 

**CDMA Environment:**

- Multiple users transmit simultaneously on same frequency

- Each user has unique spreading code

- Receiver despreads desired signal using correlator

- Other users' signals remain spread (appear as noise)

 

**Advantages of CDMA:**

1. **Soft capacity**: Limited by interference, not fixed channels

   - Voice active only 3/8 of time

   - Multi-beam/multi-sector antennas reduce interference

2. **No guard bands**: All spectrum can be reused

3. **Frequency reuse = 1**: All frequencies used in neighboring cells

4. **Soft handoff**: No frequency channel change needed during handoff

5. **Power control**: Decreases interference, increases capacity

6. **Inherent security**: Frequency diversity provides security and reliability

 

#### 6. Orthogonal Frequency Division Multiple Access (OFDMA)

 

**OFDM (Orthogonal Frequency Division Multiplexing):**

 

**Basic Concept:**

- Multiple carrier signals at different frequencies

- Send some bits on each channel

- Many subcarriers dedicated to single data source

 

**Original vs Split Datastream:**

- Original: R bps, bandwidth = N×fb, bit duration = 1/R

- Split into N substreams: R/N bps each, bandwidth = fb, bit duration = N/R

- Longer symbol duration reduces ISI

 

**Orthogonality:**

- fb: base frequency (lowest-frequency subcarrier)

- Other frequencies are integer multiples of fb

- Peak of each subcarrier's power spectrum occurs where others are zero

- Minimal interference between adjacent subcarriers

- Improved spectrum utilization vs traditional FDM

 

**Mathematical Condition:**

- Two signals s1(t) and s2(t) orthogonal if:

  Average over bit time of s1(t)×s2(t) = 0

- fb must be multiple of 1/T, where T = bit time of subcarrier

 

**Implementation:**

 

**DFT (Discrete Fourier Transform):**

X[k] = Σ x[n]e^(-j2πkn/N) for n=0 to N-1

 

**IDFT (Inverse Discrete Fourier Transform):**

x[n] = Σ X[k]e^(j2πkn/N) for k=0 to N-1

 

**FFT/IFFT (Fast Fourier Transform):**

- Number of data points N must be power of 2

- Greatly reduces computational time

- Enables practical implementation of OFDM

 

**Transmitter Chain:**

Bit stream → Serial-to-Parallel → Sub-carrier mapping → IFFT → Parallel-to-Serial → Add CP → Modulate

 

**Receiver Chain:**

Demodulate → Remove CP → Serial-to-Parallel → FFT → Sub-carrier de-mapping → EQ → Parallel-to-Serial → Bit stream

 

**Cyclic Prefix (CP):**

- Added to combat ISI

- Two functions:

  1. Guard interval (additional time)

  2. Copy of end of OFDM symbol prepended to beginning

- Makes linear convolution appear circular

- Length typically 1/4 to 1/32 of symbol duration

 

**Advantages:**

1. **Frequency selective fading** affects only some subcarriers, not whole signal

2. **ISI overcome**:

   - Distance between symbols is greater

   - Equalizer not needed with CP

3. **Efficient spectrum utilization**: No guard bands needed

4. **Flexibility**: Can allocate subcarriers based on channel conditions

 

**Difficulties:**

 

1. **Peak-to-Average Power Ratio (PAPR):**

   - Multicarrier signal = sum of many narrowband signals

   - Peak substantially larger than average

   - Requires expensive, inefficient power amplifiers

   - Non-linear amplification causes loss of orthogonality

 

2. **Intercarrier Interference (ICI):**

   - Requires tight time and frequency synchronization

   - Frequencies spaced closely → stringent frequency sync requirements

   - Tradeoff between carrier spacing and OFDM symbol length

 

**OFDMA (Orthogonal Frequency Division Multiple Access):**

 

**Key Features:**

- Subcarriers divided into groups called **subchannels**

- Each user assigned one or more subchannels

- **Subchannelization**: How subchannels allocated to users

- Important for power saving

 

**Comparison to OFDM:**

- OFDM: All subcarriers to single user

- OFDMA: Subcarriers grouped and assigned to multiple users

- Enables multi-user diversity

- Adaptive subcarrier allocation based on channel conditions

 

**SC-FDMA (Single-Carrier FDMA):**

 

**Characteristics:**

- Similar structure and performance to OFDMA

- **Lower PAPR** than OFDMA

- Used only in **uplink** (increased time-domain processing)

- Extra DFT operation before IFFT

- Spreads data symbols over all subcarriers

- Better name: SC-OFDMA-TDMA

 

**Transmitter:**

Bit stream → N-point DFT → Sub-carrier mapping → Q-point IFFT → Add CP

 

**Receiver:**

Remove CP → Q-point FFT → Sub-carrier de-mapping → EQ → N-point IDFT → Bit stream

 

**Difference from OFDMA:**

- OFDMA: Each subcarrier carries different data symbol (parallel)

- SC-FDMA: All subcarriers carry same data (spread), single-carrier-like properties

 

#### 7. Non-Orthogonal Multiple Access (NOMA)

 

**Motivation:**

- Support more end users with diverse service requirements

- More users than available orthogonal radio resources

- Meet 5G requirements: eMBB, URLLC, mMTC

 

**Categories:**

 

1. **Code Domain NOMA:**

   - Same time-frequency resources

   - Similar to CDMA but different spreading sequences

 

2. **Power Domain NOMA:**

   - Allocate different power levels to each user

   - Most common approach

 

**Key Techniques:**

 

1. **Superposition Coding (Transmitter):**

   - Simultaneously transmit multiple users' signals

   - Different power allocation based on channel conditions

   - User with worse channel gets more power

 

2. **Successive Interference Cancellation (SIC) (Receiver):**

   - Decode strongest signal first

   - Subtract from received signal

   - Decode next strongest signal

   - Repeat until all signals decoded

 

**Advantages over OMA:**

- **Higher spectral efficiency**: More users per resource block

- **Better fairness**: Can serve cell-edge and cell-center users simultaneously

- **Lower latency**: No need to wait for orthogonal resource

- **Flexibility**: Dynamic power allocation based on requirements

- **Massive connectivity**: Support for mMTC scenarios

 

**5G Service Categories Support:**

- **eMBB** (Enhanced Mobile Broadband): High data rates

- **URLLC** (Ultra-Reliable Low-Latency Communications): Stringent requirements

- **mMTC** (Massive Machine-Type Communications): Massive connectivity

 

**Comparison with Other Schemes:**

- **TDMA**: Separate time slots

- **FDMA**: Separate frequency bands

- **CDMA**: Separate codes

- **OFDMA**: Separate subcarriers (orthogonal)

- **NOMA**: Same time-frequency-code resources, different power (non-orthogonal)

 

#### 8. Hybrid Schemes

 

**Reservation-Based Schemes:**

 

**1. PRMA (Packet-Reservation Multiple Access):**

 

**Structure:**

- Time divided into frames with S slots

- Slots can be: Reserved (R) or Available (A)

- Frame: [R | A | A | ... | R]

 

**Operation:**

- Voice and data users contend for available slots

- **Voice user succeeds**: Slot becomes reserved until talk ends

- **Data user succeeds**: Slot remains available

- Unsuccessful: Retry with backoff

 

**Characteristics:**

- No dedicated reservation bandwidth

- Contention detected after whole packet transmission

- Efficient for bursty traffic

- Combines benefits of contention and reservation

 

**2. D-TDMA (Dynamic TDMA):**

 

**Frame Structure:**

- Reservation slots: Sr (fixed)

- Voice slots: Sv (fixed)

- Data slots: Sd (variable, remaining slots)

- Variable border between voice and data

 

**Operation:**

- Short reservation packet in random reservation slot

- **Successful voice**: Assigned to available voice slot (reserved)

- **Successful data**: Assigned but not reserved to data slot

- **Unsuccessful voice**: Retry next frame

- **Unsuccessful data**: Controlled retransmission probability

 

**Advantages:**

- Higher bandwidth efficiency than PRMA

- Separate contention and data transmission phases

 

**Disadvantages:**

- Fixed amount dedicated to reservation

- Difficult to change dynamically

 

**3. RAMA (Resource-Auction Multiple Access):**

 

**Structure:**

- Auction slots (Sa) instead of reservation slots

- Voice slots (Sv) - fixed

- Data slots (Sd) - variable

- Frame: [Auction | Voice | Data]

 

**Auction Procedure:**

- Users bid with ID = Random number + Priority digits

- Digit-by-digit comparison

- Highest value announced progressively

- Final winner at end

- Deterministic assignment (no contention failures)

 

**Characteristics:**

- **Channel access**: Auction procedure (not Slotted ALOHA)

- Higher success probability than D-TDMA

- Good for high traffic

- More complex hardware

- Extreme case of D-TDMA with zero contention failure

 

**Auction Slot Timing:**

- Multiple rounds of bit comparisons

- Ts: Bit transfer time (uplink and downlink)

- Td: Propagation and processing delay

- Total auction slot time accommodates all comparison rounds

 

**Token-Based Schemes:**

 

**Operation:**

- Token passed around network

- Only node possessing token may transmit

- Token released when node has nothing to send or time expires

 

**Types:**

1. **Token Ring**: Physical or logical ring topology

2. **Token Bus**: Bus topology with logical ring

 

**Characteristics:**

- Conflict-free (no collisions)

- Bounded delay (maximum wait = token rotation time)

- Fair access (each node gets turn)

- Good for real-time applications

 

### Important Formulas Reference

 

**CSMA/CD Exponential Backoff:**

- Backoff slots = random[0, 2^n - 1] after nth collision

- Time slot = 2τ (τ = worst case propagation time)

 

**Spread Spectrum Process Gain:**

- FHSS: Gp = 10 log C (dB), where C = number of channels

- DSSS: Gp = 10 log(Bss/B) (dB)

  - Bss = spread bandwidth

  - B = original bandwidth

 

**Auto-correlation:**

Ck = Σ(an × an+k) for n=1 to N

 

**Cross-correlation:**

Rk = Σ(an × bn+k) for n=1 to N

 

**Walsh-Hadamard Generation:**

H2n = [[Hn, Hn], [Hn, H̄n]]

 

**DFT:**

X[k] = Σ x[n]e^(-j2πkn/N) for n=0 to N-1

 

**IDFT:**

x[n] = Σ X[k]e^(j2πkn/N) for k=0 to N-1

 

**Maximum Length Sequence Period:**

p = 2^n - 1 (n = bits in shift register)

 

### Exam Focus Areas

 

**High-Priority Topics:**

1. **CSMA variants** and when to use each

2. **Hidden and exposed terminal problems** and solutions (RTS/CTS)

3. **CDMA spreading codes**: PN sequences vs orthogonal codes

4. **OFDM orthogonality** and how it achieves spectrum efficiency

5. **OFDMA vs SC-FDMA**: Differences and why SC-FDMA used in uplink

6. **NOMA principles**: Superposition coding and SIC

7. **Hybrid schemes**: Comparison of PRMA, D-TDMA, RAMA

 

**Common Exam Questions:**

1. Explain how RTS/CTS solves the hidden terminal problem

2. Calculate exponential backoff window after n collisions

3. Compare OFDMA and NOMA for 5G applications

4. Describe Walsh-Hadamard code generation

5. Explain why PAPR is a problem in OFDM

6. Compare process gain in FHSS vs DSSS

7. Describe how RAMA auction procedure works

 

**Critical Concepts to Master:**

1. **Contention vs Conflict-Free**: When each approach is appropriate

2. **Orthogonality**: Mathematical definition and practical implications

3. **Spread Spectrum**: How spreading provides multiple access and security

4. **Cyclic Prefix**: Why it eliminates ISI in OFDM

5. **Power Domain NOMA**: How different power levels enable simultaneous transmission

6. **Reservation Mechanisms**: Tradeoffs in different hybrid schemes

 

**Practical Applications:**

1. **WiFi (IEEE 802.11)**: Uses CSMA/CA with RTS/CTS

2. **Ethernet (IEEE 802.3)**: Uses CSMA/CD

3. **3G (UMTS)**: Uses CDMA with Walsh codes

4. **4G LTE**: Uses OFDMA (downlink) and SC-FDMA (uplink)

5. **5G NR**: Uses NOMA for massive connectivity and diverse services

6. **Token Ring**: Legacy IBM networks

 

### Summary

 

Lecture 3 covers the fundamental problem of Medium Access Control: coordinating multiple devices sharing a common transmission medium. The lecture progresses from simple contention-based schemes (ALOHA, CSMA) through collision detection and avoidance (CSMA/CD, CSMA/CA), to sophisticated conflict-free approaches (CDMA, OFDMA, NOMA) and hybrid schemes combining benefits of both approaches.

 

**Key Takeaways:**

1. **Contention-based schemes** are simple but suffer from collisions and unpredictable delays

2. **Carrier sensing** improves efficiency but requires solutions for hidden/exposed terminals

3. **CDMA** uses spreading codes to allow simultaneous transmission on same frequency

4. **OFDMA** divides spectrum into orthogonal subcarriers for efficient multi-user access

5. **NOMA** allows non-orthogonal transmission through power-domain multiplexing

6. **Hybrid schemes** combine contention and reservation for better efficiency

7. **Choice of scheme** depends on traffic patterns, latency requirements, and complexity constraints

 

The evolution from ALOHA to NOMA represents increasing sophistication in MAC design, trading simplicity for efficiency, fairness, and support for diverse service requirements crucial for modern wireless networks.

---

## Lecture 4: Data Link Layer Coding

### Overview

This lecture covers error control mechanisms in the Data Link Layer, including both error detection and error correction techniques. Understanding these mechanisms is crucial for reliable data transmission in wireless communications where bit error rates can be high.

 

### 1. Need for Error Control

 

**Frame Error Probability:**

- **P₁** = Probability of no bit errors in frame = (1 - Pᵦ)^F

- **P₂** = Probability of one or more errors = (1 - P₁)

- Example: With Pᵦ = 10⁻⁵ and F = 2046 bits → P₂ = 0.02 (2% frame error rate)

 

**Error Control Approaches:**

- **Forward Error Correction (FEC):** Error correction codes

- **Backward Error Correction (BEC):** Error detection + ARQ

- **Reliable Delivery:** Error correction + sequence control + flow control

 

### 2. Error Detection

 

#### Parity Check

- Simple error detection with single parity bit

- **n - k = 1** (one check bit)

- Detects odd number of bit errors

- **Limitation:** Cannot detect even number of bit errors

 

#### Cyclic Redundancy Check (CRC)

- Check bits called **Frame Check Sequence (FCS)**

- Frame divisible by predetermined polynomial

- Three implementation approaches:

  - Modulo-2 arithmetic

  - Polynomials

  - Digital logic

 

**CRC Calculation Example:**

```

Data: D = 1101011011 (10 bits)

Pattern: P = 10011 (5 bits)

FCS: R = 4 bits

 

Append 4 zeros: 11010110110000

Divide by P using XOR

Remainder = 1110 (FCS)

Transmitted: 1101011011 1110

```

 

### 3. Automatic Repeat Request (ARQ)

 

#### ARQ Components

- **ACK:** Acknowledgement for correct delivery

- **Timeout:** Period to wait for ACK

- **Retransmission:** Send again if timeout expires

- **Storage:** PDUs stored at sender

- **Windows:** Buffers at sender and receiver

 

**Flow Control:** Prevent sender from overwhelming receiver

**Error Control:** Detect and correct transmission errors

 

#### Stop-and-Wait ARQ

- Transmitter sends one PDU at a time

- Waits for ACK before sending next

- Receiver checks errors and order

- Sends NAK (Negative ACK) if error detected

- **Timeout:** Slightly higher than Round-Trip Time (RTT)

 

**Critical Issues:**

- RTT estimation

- Inefficient: waits entire RTT between PDUs

 

#### Go-Back-N ARQ

- **Tx window = W; Rx window = 1**

- Transmitter can send W PDUs without ACKs

- Receiver sends cumulative ACK for last correct in-order PDU

- On timeout: retransmit from error point

- **More efficient** than stop-and-wait

- **Limitation:** Out-of-order PDUs discarded

 

#### Selective Repeat ARQ

- **Tx window = W; Rx window > 1**

- Transmitter behaves like Go-Back-N

- Receiver sends selective NAK for single PDU

- **Accepts out-of-order PDUs** and sends ACK

- **Most efficient** but more complex

 

#### ARQ Details

 

**Piggybacking:** ACK embedded in data PDU for bidirectional flow

 

**Sequence Numbers (Modulo K):**

- **Stop-and-Wait:** K = 2

- **Go-Back-N:** K = W + 1

- **Selective Repeat:** K = 2W + 1

 

#### Limitations in Wireless

- **High BER** → excessive retransmissions

- **Long propagation delay** (e.g., satellite) → inefficient

- **Solution:** Need Forward Error Correction (FEC)

 

### 4. Error Correction - Block Codes

 

#### Key Concepts

 

**Hamming Distance:** Number of bits where two sequences disagree

- Example: d(011011, 110010) = 3

 

**Block Code Parameters (n, k):**

- **k:** Data bits

- **n:** Codeword bits (n > k)

- **Redundancy:** (n - k) / k

- **Code Rate:** k / n

- **Valid codewords:** 2^k out of 2^n possible

 

**Minimum Hamming Distance (d_min):**

- d_min = min[d(w_i, w_j)] for all codeword pairs

- **Correctable errors:** t = ⌊(d_min - 1) / 2⌋

- **Detectable errors:** d_min - 1

 

**Design Considerations:**

1. Maximize d_min for given n and k

2. Easy encoding/decoding

3. Small (n - k) to reduce bandwidth

4. Large (n - k) to reduce error rate

5. **Trade-off required!**

 

**Coding Gain:** Reduction in Eᵦ/N₀ (dB) needed for target BER

 

### 5. Hamming Codes

 

**Parameters:**

- Block length: n = 2^m - 1

- Data bits: k = 2^m - m - 1

- Check bits: m = n - k

- Minimum distance: d_min = 3

- **Corrects single-bit errors**

 

**Check Bit Calculation:**

- Inserted at positions 2^0, 2^1, 2^2, ... (powers of 2)

- XOR of position numbers of data bits equal to 1

 

**Syndrome Word:**

- XOR of received bit positions and check bits

- All 0s → no error

- One 1 → check bit error

- Multiple 1s → indicates error position

 

### 6. Cyclic Codes

 

**Property:** Cyclic shift of valid codeword is also valid

- If c = (c₀, c₁, ..., c_{n-1}) valid → (c_{n-1}, c₀, c₁, ..., c_{n-2}) valid

 

**Examples:**

- **Bose-Chaudhuri-Hocquenghem (BCH) codes:** Most powerful cyclic code

- **Reed-Solomon (RS) codes:**

  - Subclass of BCH codes

  - Well-suited for burst error correction

  - Widely used in wireless

 

### 7. Parity-Check Matrix Codes

 

**Matrix Representation:**

- **H:** m × n parity-check matrix

- **Codeword condition:** Hcᵀ = 0

- **Structure:** H = [A I_{n-k}]

  - A: (n - k) × k matrix

  - I_{n-k}: identity matrix

 

**Generator Matrix:**

- **G = [I_k Aᵀ]:** k × n matrix

- **Encoding:** c = uG (u = data bits)

 

**Error Detection:** Hcᵀ yields nonzero vector (syndrome)

 

**Error Correction:** Choose closest valid codeword by Hamming distance

 

### 8. Low-Density Parity-Check (LDPC) Codes

 

**Regular LDPC Properties:**

1. Each code bit in w_c parity constraints

2. Each row has w_r ones (constant)

3. Each column has w_c ones (constant)

4. At most one common 1 between columns

5. **Low density:** w_r << n and w_c << m

 

**Irregular LDPC:** Average ones per row/column small

 

**Code Construction:**

- Various approaches (Gallagher, MacKay-Neal)

- Repeat-accumulate codes (systematic)

 

**Encoding:**

- Easy for repeat-accumulate

- Resource-intensive for others

 

**Decoding:**

- **Tanner graph** representation

- **Iterative message passing:**

  1. Bit nodes send values to check nodes

  2. Check nodes calculate estimates (XOR of others)

  3. Bit nodes use majority voting

  4. Repeat until constraints satisfied

- Probabilistic approaches available

 

### 9. Polar Codes

 

**Characteristics:**

- Efficient implementation

- Performance slightly worse than LDPC

- Based on synthetic channel concept

 

**Recursive Structure:**

- Repeated use of XOR

- Codeword length: power of 2

- Example: x₁ = u₁ ⊕ u₂, x₂ = u₂

 

**Encoding:**

- Generator: G_N recursively defined

- Reverse shuffle permutation R_{2N}

- K data bits assigned to inputs

- Remaining lines frozen (0)

 

**Decoding:**

- **Successive cancellation** algorithm

- More efficient complex approaches exist

 

### 10. Convolutional Codes

 

**Parameters (n, k, K):**

- **k:** Data bits processed at a time

- **n:** Output bits from each k bits

- **K:** Constraint factor (K-1 previous data sets)

- n output bits depend on K × k input bits

 

**Encoder:**

- Shift register implementation

- State = K-1 past values

 

**State Diagram:**

- Shows transitions between encoder states

- Solid lines: input bit = 0

- Dashed lines: input bit = 1

 

**Trellis Diagram:**

- State diagram over time

- All possible paths through states

- Valid paths follow state transitions

 

**Viterbi Decoding:**

- Find most likely input producing invalid output

- **Metric:** Hamming distance

- Trace paths with minimum cumulative distance

- Decoding window b determines latency

 

### 11. Error Bursts and Interleaving

 

**Burst Errors:**

- Caused by impulse noise or fading

- Worse at higher data rates

 

**Block Interleaving:**

- Spread burst errors over multiple blocks

- Write data row-by-row into m × n matrix

- Read out column-by-column

- Burst error distributed across m blocks

 

### 12. Turbo Codes

 

**Characteristics:**

- Performance close to Shannon limit

- Based on convolutional encoding

- Used in 3G and 4G

 

**Encoder:**

- Two parallel RSC (Recursive Systematic Convolutional) encoders

- Interleaver between encoders

- **Puncturing:** Remove check bits to adjust code rate

  - Rate 1/3 → Rate 1/2

- Input bit preserved

 

**Decoder:**

- **Depuncturing:** Estimate missing check bits

- **Soft decision decoding:** Probability-based

- **Iterative decoding:**

  - Multiple iterations between decoders

  - High confidence but increased delay

 

### 13. Hybrid ARQ (HARQ)

 

**Motivation:**

- Good channel: FEC adds unnecessary overhead

- Bad channel: ARQ causes excessive delay

 

**Type-I HARQ:**

- FEC corrects common errors

- ARQ for retransmission when FEC fails

 

**Type-II HARQ:**

- Alternate between error detection only and FEC messages

- Adaptive redundancy

 

**Additional Techniques:**

- **Soft decision decoding:** Use confidence levels

- **Chase combining:** Combine previous frames

- **Incremental redundancy:** Increase redundancy with retransmissions

- **Puncturing:** Remove bits instead of changing FEC

 

---

 

### Important Formulas Reference

 

**Frame Error Probability:**

```

P₁ = (1 - Pᵦ)^F

P₂ = 1 - P₁

```

 

**Block Code Parameters:**

```

Redundancy = (n - k) / k

Code Rate = k / n

Correctable errors: t = ⌊(d_min - 1) / 2⌋

Detectable errors: d_min - 1

```

 

**Hamming Code:**

```

n = 2^m - 1

k = 2^m - m - 1

m = n - k

d_min = 3

```

 

**ARQ Sequence Numbers (Modulo K):**

```

Stop-and-Wait: K = 2

Go-Back-N: K = W + 1

Selective Repeat: K = 2W + 1

```

 

**Parity-Check Matrix:**

```

H = [A I_{n-k}]

Generator: G = [I_k Aᵀ]

Encoding: c = uG

Validation: Hcᵀ = 0

```

 

**Convolutional Codes:**

```

Output depends on K × k input bits

State = K - 1 past values

```

 

---

 

### Exam Focus Areas

 

#### High-Priority Topics

1. **CRC calculation** and polynomial division

2. **ARQ protocols** (Stop-and-Wait, Go-Back-N, Selective Repeat) and their differences

3. **Hamming codes** - check bit calculation and syndrome decoding

4. **Block code parameters** (n, k, dmin, code rate, redundancy)

5. **Convolutional codes** - encoder design and Viterbi algorithm

6. **LDPC codes** - Tanner graph and iterative decoding

7. **HARQ types** and when to use each

 

#### Common Exam Questions

1. Calculate CRC for given data and polynomial

2. Compare ARQ protocols (efficiency, complexity, use cases)

3. Design Hamming code for given parameters

4. Calculate minimum distance and error correction capability

5. Draw convolutional encoder state/trellis diagram

6. Trace Viterbi decoding path

7. Explain HARQ vs pure ARQ/FEC

 

#### Critical Concepts to Master

1. **Trade-offs:**

   - ARQ vs FEC (delay vs overhead)

   - Code rate vs error correction capability

   - Complexity vs performance

2. **Error types:**

   - Random errors vs burst errors

   - Single-bit vs multi-bit errors

3. **Decoding algorithms:**

   - Hard vs soft decision

   - Iterative decoding

4. **Wireless-specific challenges:**

   - High BER requirements

   - Propagation delay impact

5. **Code selection criteria:**

   - Channel conditions

   - Latency requirements

   - Computational resources

6. **Interleaving benefits** for burst errors

 

#### Practical Applications

1. **CRC:** Ethernet, Wi-Fi frame check

2. **Hamming codes:** Memory error correction

3. **Reed-Solomon:** CD/DVD, QR codes, satellite

4. **Convolutional + Viterbi:** GSM, satellite

5. **Turbo codes:** 3G/4G LTE

6. **LDPC codes:** Wi-Fi 802.11n/ac, DVB-S2, 5G

7. **Polar codes:** 5G control channels

8. **HARQ:** LTE, 5G adaptive error control

 

---

 

### Key Takeaways

 

1. **Error control is essential** in wireless due to high bit error rates

2. **Detection is simpler** than correction (CRC vs FEC)

3. **ARQ provides reliability** but adds delay (RTT impact)

4. **FEC enables real-time** applications but adds overhead

5. **Block codes** operate on fixed-size data blocks

6. **Convolutional codes** process continuous streams

7. **Modern codes** (LDPC, Polar, Turbo) approach Shannon limit

8. **HARQ combines** benefits of ARQ and FEC

9. **Interleaving spreads** burst errors for better correction

10. **Code selection** depends on channel, latency, and resources

---

## Lecture 5a: Network Layer

### Overview

 

The Network Layer (Layer 3) is responsible for routing packets across networks from source to destination. This lecture covers the fundamental protocols and mechanisms that enable internetworking, with focus on the Internet Protocol (IP), addressing schemes, routing algorithms, and Quality of Service (QoS) considerations critical for wireless communications.

 

**Key Topics:**

- TCP/IP and OSI Model relationship

- Internet Protocol (IPv4 and IPv6)

- IP Addressing and subnetting

- Routing fundamentals and algorithms

- Mobile IP for wireless mobility

- QoS models and mechanisms

 

---

 

### 1. Network Layer and Protocol Models

 

**TCP/IP vs OSI Model:**

 

The TCP/IP model is a practical 4-layer model used in the Internet:

- **Application Layer** (combines OSI Layers 5-7)

- **Transport Layer** (OSI Layer 4)

- **Internet Layer** (OSI Layer 3 - Network Layer)

- **Network Access Layer** (combines OSI Layers 1-2)

 

**Network Layer Functions:**

- **Logical Addressing**: IP addresses identify devices globally

- **Routing**: Determines best path from source to destination

- **Packet Forwarding**: Moves packets from input to output interface

- **Fragmentation/Reassembly**: Handles different MTU sizes

- **Error Handling**: ICMP for diagnostics and error reporting

 

---

 

### 2. Internet Protocol (IP) Fundamentals

 

**IP Characteristics:**

- **Connectionless**: Each packet treated independently

- **Best-Effort Delivery**: No guarantees (reliability handled by upper layers)

- **Media Independent**: Works over any Layer 2 technology

 

**IP Versions:**

- **IPv4**: 32-bit addresses (≈4.3 billion addresses)

- **IPv6**: 128-bit addresses (≈340 undecillion addresses)

 

**IP Packet Structure (IPv4):**

- **Version** (4 bits): IP version (4 for IPv4)

- **Header Length** (4 bits): Length in 32-bit words

- **Type of Service** (8 bits): QoS parameters

- **Total Length** (16 bits): Entire packet size (max 65,535 bytes)

- **Identification, Flags, Fragment Offset**: For fragmentation

- **Time to Live (TTL)** (8 bits): Hop limit to prevent loops

- **Protocol** (8 bits): Upper layer protocol (6=TCP, 17=UDP)

- **Header Checksum** (16 bits): Error detection for header

- **Source/Destination IP Address** (32 bits each)

 

---

 

### 3. IPv4 Addressing

 

**Address Structure:**

- 32-bit address divided into Network and Host portions

- Written in dotted decimal notation: `192.168.1.1`

 

**Classful Addressing (Legacy):**

- **Class A**: 0.0.0.0 to 127.255.255.255 (first bit = 0)

- **Class B**: 128.0.0.0 to 191.255.255.255 (first bits = 10)

- **Class C**: 192.0.0.0 to 223.255.255.255 (first bits = 110)

- **Class D**: 224.0.0.0 to 239.255.255.255 (Multicast)

- **Class E**: 240.0.0.0 to 255.255.255.255 (Reserved)

 

**Classless Inter-Domain Routing (CIDR):**

- Replaces classful addressing with flexible prefix lengths

- Notation: `192.168.1.0/24` (24-bit network prefix)

- Subnet Mask: Identifies network vs host bits

  - `/24` = `255.255.255.0`

  - `/16` = `255.255.0.0`

  - `/8` = `255.0.0.0`

 

**Special Addresses:**

- **Network Address**: All host bits = 0 (e.g., `192.168.1.0/24`)

- **Broadcast Address**: All host bits = 1 (e.g., `192.168.1.255/24`)

- **Loopback**: `127.0.0.0/8` (local testing)

- **Private Addresses** (RFC 1918):

  - `10.0.0.0/8`

  - `172.16.0.0/12`

  - `192.168.0.0/16`

 

**Subnetting:**

- Divides a network into smaller sub-networks

- Borrows host bits to create subnet bits

- Number of subnets = 2^(borrowed bits)

- Hosts per subnet = 2^(remaining host bits) - 2

 

**Example:** Subnet `192.168.1.0/24` into 4 subnets

- Need 2 bits (2² = 4 subnets)

- New prefix: `/26` (24 + 2)

- Hosts per subnet: 2^6 - 2 = 62

- Subnets:

  - `192.168.1.0/26` (0-63)

  - `192.168.1.64/26` (64-127)

  - `192.168.1.128/26` (128-191)

  - `192.168.1.192/26` (192-255)

 

---

 

### 4. Network Address Translation (NAT)

 

**Purpose:**

- Conserves IPv4 addresses by allowing multiple devices to share one public IP

- Provides basic security by hiding internal network structure

 

**NAT Types:**

- **Static NAT**: 1-to-1 mapping (one private to one public)

- **Dynamic NAT**: Many-to-many mapping from a pool

- **Port Address Translation (PAT)**: Many-to-one using port numbers (most common)

 

**PAT Operation:**

1. Inside device sends packet with private IP and source port

2. NAT router translates to public IP and unique port

3. Maintains translation table

4. Reverse translation for return traffic

 

**NAT Limitations:**

- Breaks end-to-end connectivity principle

- Complicates peer-to-peer applications

- Issues with IPsec, SIP, and other protocols

- Not needed with IPv6

 

---

 

### 5. IPv6 - Next Generation IP

 

**Why IPv6?**

- **Address Exhaustion**: IPv4 addresses depleted

- **Simplified Header**: More efficient processing

- **Better Support**: For mobility, QoS, and security

- **Auto-configuration**: Stateless address autoconfiguration (SLAAC)

 

**IPv6 Address Format:**

- 128 bits written as 8 groups of 4 hexadecimal digits

- Example: `2001:0db8:0000:0000:0000:ff00:0042:8329`

 

**IPv6 Address Compression:**

- Leading zeros in a group can be omitted

- Consecutive groups of zeros replaced with `::`

- Example: `2001:db8::ff00:42:8329`

 

**IPv6 Address Types:**

 

1. **Unicast** (one-to-one):

   - **Global Unicast Address (GUA)**: Public, routable addresses

     - Prefix: `2000::/3` (starts with 2 or 3)

     - Structure: Global Routing Prefix (48) | Subnet ID (16) | Interface ID (64)

   - **Link-Local Address (LLA)**: Local link communication only

     - Prefix: `fe80::/10`

     - Not routable beyond local link

     - Auto-generated using EUI-64 or random

 

2. **Multicast** (one-to-many):

   - Prefix: `ff00::/8`

   - Replaces broadcast in IPv4

   - Examples:

     - `ff02::1` - All nodes on link

     - `ff02::2` - All routers on link

 

3. **Anycast** (one-to-nearest):

   - Same address assigned to multiple interfaces

   - Packet delivered to nearest one

 

**IPv6 Header Simplification:**

- Fixed 40-byte header (vs variable in IPv4)

- Removed: Header checksum, fragmentation fields, options

- Extension headers for additional functionality

- Improved processing efficiency in routers

 

**IPv6 Transition Mechanisms:**

- **Dual Stack**: Run IPv4 and IPv6 simultaneously

- **Tunneling**: Encapsulate IPv6 in IPv4 packets

  - 6to4, ISATAP, Teredo

- **Translation**: NAT64/DNS64 for IPv6-only to IPv4 communication

 

---

 

### 6. IP Routing Fundamentals

 

**Routing Table:**

Each router maintains a routing table with entries containing:

- **Destination Network**: Target network address

- **Next Hop**: IP address of next router or "directly connected"

- **Outgoing Interface**: Physical/logical interface to use

- **Metric**: Cost of the route

 

**Route Types:**

 

1. **Directly Connected Routes:**

   - Networks directly attached to router interfaces

   - Added automatically when interface is up

   - Administrative Distance (AD) = 0

 

2. **Static Routes:**

   - Manually configured by administrator

   - Format: `ip route <destination> <mask> <next-hop|interface>`

   - AD = 1

   - Use cases: Small networks, stub networks, default routes

 

3. **Dynamic Routes:**

   - Learned from routing protocols

   - Automatically adapt to topology changes

   - AD varies by protocol (lower = more trusted)

 

4. **Default Route:**

   - Catch-all route: `0.0.0.0/0` (IPv4) or `::/0` (IPv6)

   - Used when no specific route matches

   - Typically points to ISP or Internet gateway

 

**Routing Decision Process:**

1. Check for directly connected networks

2. Find longest prefix match in routing table

3. If multiple routes, use lowest administrative distance

4. If same AD, use lowest metric

5. If no match, use default route

6. If no default route, drop packet and send ICMP unreachable

 

**Longest Prefix Match:**

- More specific routes (longer prefix) preferred over less specific

- Example: Packet to `192.168.1.50`

  - Match: `192.168.1.0/24` (24 bits match) ✓ SELECTED

  - Match: `192.168.0.0/16` (16 bits match)

  - Use `/24` route (more specific)

 

---

 

### 7. Routing Algorithms

 

**Distance Vector (DV) Routing:**

 

**Principle:**

- Each router knows distance (metric) to directly connected neighbors

- Routers exchange entire routing tables with neighbors periodically

- Uses Bellman-Ford algorithm

 

**Operation:**

1. Each router advertises its routing table to neighbors

2. Receiving router updates its table:

   - For each destination: Distance = neighbor's distance + link cost

   - Keep route with minimum distance

3. Repeat until convergence

 

**Characteristics:**

- **Routing by Rumor**: Routers don't have complete topology

- **Metrics**: Hop count, delay, bandwidth

- **Updates**: Periodic (e.g., every 30 seconds) + triggered

- **Examples**: RIPv1, RIPv2, IGRP

 

**Problems:**

- **Count to Infinity**: Routing loops due to slow convergence

- **Solutions**:

  - Maximum hop count (RIP uses 15, 16 = unreachable)

  - Split Horizon: Don't advertise route back to source

  - Route Poisoning: Advertise failed routes with infinite metric

  - Hold-Down Timers: Ignore updates for period after route fails

 

**Link State (LS) Routing:**

 

**Principle:**

- Each router has complete topology map

- Routers flood link state information

- Uses Dijkstra's Shortest Path First (SPF) algorithm

 

**Operation:**

1. Each router discovers neighbors and link costs

2. Creates Link State Advertisement (LSA) with local links

3. Floods LSAs to all routers

4. Each router builds identical topology database

5. Runs SPF algorithm to compute best paths

6. Populates routing table with best routes

 

**Characteristics:**

- **Full Topology Knowledge**: Each router has complete map

- **Faster Convergence**: Changes propagated quickly

- **More Resources**: Higher CPU and memory requirements

- **Scalability**: Uses hierarchical areas

- **Examples**: OSPF, IS-IS

 

**Advantages over DV:**

- No count-to-infinity problem

- Faster convergence

- Support for VLSM and CIDR

- Hierarchical design for scalability

 

**Path Vector Routing:**

 

**Principle:**

- Similar to DV but includes entire AS path

- Prevents loops by rejecting routes containing own AS

- Used for inter-domain routing

 

**Operation:**

- Each AS advertises reachable networks with full AS path

- Receiving AS can apply policies based on path

- Best path selected based on policies, not just metric

 

**Characteristics:**

- **Policy-Based**: Allows complex routing policies

- **Loop Prevention**: AS path prevents loops

- **Scalability**: Handles Internet-scale routing

- **Example**: BGP (Border Gateway Protocol)

 

---

 

### 8. Dynamic Routing Protocols

 

**Interior Gateway Protocols (IGP):**

Used within an Autonomous System (AS)

 

**RIPv2 (Routing Information Protocol version 2):**

- **Type**: Distance Vector

- **Metric**: Hop count (max 15)

- **Algorithm**: Bellman-Ford

- **Updates**: Multicast to 224.0.0.9 every 30 seconds

- **Features**: VLSM support, authentication

- **Use Case**: Small, simple networks

- **AD**: 120

 

**EIGRP (Enhanced Interior Gateway Routing Protocol):**

- **Type**: Advanced Distance Vector (Hybrid)

- **Metric**: Composite (bandwidth, delay, load, reliability)

- **Algorithm**: DUAL (Diffusing Update Algorithm)

- **Updates**: Incremental, triggered (not periodic)

- **Features**: Fast convergence, unequal cost load balancing

- **Cisco proprietary** (now open standard)

- **AD**: 90 (internal), 170 (external)

 

**OSPF (Open Shortest Path First):**

- **Type**: Link State

- **Metric**: Cost based on bandwidth

- **Algorithm**: Dijkstra's SPF

- **Updates**: Multicast LSAs (224.0.0.5/6) on topology changes

- **Features**: Hierarchical (areas), VLSM, fast convergence

- **Versions**: OSPFv2 (IPv4), OSPFv3 (IPv6)

- **AD**: 110

 

**IS-IS (Intermediate System to Intermediate System):**

- **Type**: Link State

- **Metric**: Cost (default 10 per interface)

- **Algorithm**: SPF

- **Features**: Integrated routing (IPv4 and IPv6), very stable

- **Use Case**: Large ISP networks

- **AD**: 115

 

**Exterior Gateway Protocol (EGP):**

 

**BGP (Border Gateway Protocol):**

- **Type**: Path Vector

- **Purpose**: Inter-AS routing (Internet backbone)

- **Metric**: AS path length + policies

- **Protocol**: TCP port 179 (reliable)

- **Features**: Policy-based routing, prefix filtering

- **Versions**: BGP-4 (current, supports CIDR)

- **AD**: 20 (eBGP), 200 (iBGP)

- **Types**:

  - **eBGP**: Between different ASes

  - **iBGP**: Within same AS

 

**Protocol Comparison:**

 

| Protocol | Type | Metric | Convergence | Scalability | AD |

|----------|------|--------|-------------|-------------|-----|

| RIPv2 | DV | Hop (max 15) | Slow | Small | 120 |

| EIGRP | Hybrid | Composite | Fast | Medium | 90 |

| OSPF | LS | Bandwidth | Fast | Large | 110 |

| IS-IS | LS | Cost | Fast | Very Large | 115 |

| BGP | PV | Policy | Slow | Internet | 20/200 |

 

---

 

### 9. Mobile IP

 

**Problem:**

Traditional IP assumes fixed location. When mobile device moves to new network:

- IP address would change (breaks ongoing connections)

- Routing becomes inefficient

 

**Mobile IP Solution:**

Allows mobile node to maintain permanent IP address while moving between networks

 

**Mobile IP Architecture:**

 

**Components:**

1. **Mobile Node (MN)**: Device that moves (smartphone, laptop)

2. **Home Agent (HA)**: Router on MN's home network

   - Maintains MN's home address

   - Tunnels packets to MN's current location

3. **Foreign Agent (FA)**: Router on visited network (optional in some versions)

   - Assists MN in foreign network

4. **Correspondent Node (CN)**: Device communicating with MN

 

**Key Addresses:**

- **Home Address (HoA)**: Permanent IP address in home network

- **Care-of Address (CoA)**: Temporary IP address in foreign network

  - **Foreign Agent CoA**: FA's address

  - **Colocated CoA**: Temporary address assigned to MN

 

**Mobile IP Operation:**

 

1. **Agent Discovery:**

   - Agents broadcast advertisement messages

   - MN listens to determine if in home or foreign network

 

2. **Registration:**

   - MN in foreign network obtains CoA

   - MN registers CoA with HA (possibly via FA)

   - HA updates binding: HoA ↔ CoA

 

3. **Tunneling (Packet Delivery):**

   - CN sends packet to MN's HoA

   - HA intercepts packet (acts as proxy)

   - HA encapsulates packet with CoA as destination (IP-in-IP tunnel)

   - Packet delivered to MN at foreign network

   - MN decapsulates and processes packet

 

4. **Return Path:**

   - MN can send directly to CN (source = HoA)

   - OR use reverse tunnel through HA

 

**Triangle Routing Problem:**

- Packets from CN → MN go via HA (inefficient if CN and MN are close)

- **Solution**: Route Optimization

  - CN caches binding (HoA ↔ CoA)

  - Sends packets directly to CoA

  - Requires MN to inform CN of binding

 

**Mobile IPv6 Improvements:**

- No need for Foreign Agent

- Built-in route optimization

- Better security (IPsec)

- Smooth handoff support

 

---

 

### 10. Quality of Service (QoS)

 

**Need for QoS:**

Different applications have different requirements:

- **VoIP**: Low delay, low jitter, moderate bandwidth

- **Video Streaming**: High bandwidth, moderate delay tolerance

- **File Transfer**: High bandwidth, delay-tolerant

- **Gaming**: Low delay, low jitter

 

**QoS Parameters:**

- **Bandwidth**: Data rate (bps)

- **Delay**: End-to-end latency

- **Jitter**: Delay variation

- **Packet Loss**: Percentage of lost packets

 

**QoS Models:**

 

**1. Best Effort (No QoS):**

- Default Internet model

- All packets treated equally (FIFO queuing)

- No guarantees

- Simple, scalable, but no service differentiation

 

**2. Integrated Services (IntServ):**

 

**Principle:**

- Per-flow resource reservation

- Hard QoS guarantees

 

**Protocol: RSVP (Resource Reservation Protocol)**

- Sender sends PATH message describing traffic

- Receiver sends RESV message to reserve resources

- Each router along path reserves bandwidth

- Admission control: Accept or reject based on available resources

 

**Service Classes:**

- **Guaranteed Service**: Strict bounds on delay

- **Controlled Load**: Approximates unloaded network

 

**Limitations:**

- **Scalability**: Per-flow state in every router

- **Complexity**: RSVP signaling overhead

- Not practical for large networks

 

**3. Differentiated Services (DiffServ):**

 

**Principle:**

- Classify and mark packets at network edge

- Core routers apply per-hop behaviors based on marking

- Scalable (no per-flow state in core)

 

**DSCP (Differentiated Services Code Point):**

- 6-bit field in IP ToS/Traffic Class field

- 64 possible values

- Standard classes:

  - **EF (Expedited Forwarding)**: DSCP 46 - Premium (VoIP)

  - **AF (Assured Forwarding)**: DSCP 10-46 - Multiple classes with drop precedence

  - **DF (Default Forwarding)**: DSCP 0 - Best effort

 

**Per-Hop Behaviors (PHB):**

- **Class-Based Queuing**: Multiple queues for different classes

- **Priority Queuing**: High-priority traffic served first

- **Weighted Fair Queuing (WFQ)**: Bandwidth shared based on weights

- **Traffic Shaping**: Smooth traffic to match rate limits

- **Policing**: Drop or mark excess traffic

 

**DiffServ Operation:**

1. **Classification**: At edge, classify packets into classes

2. **Marking**: Set DSCP value

3. **Conditioning**: Police or shape traffic

4. **Queuing**: Core routers use appropriate queue based on DSCP

5. **Scheduling**: Serve queues according to priority/weights

 

**QoS Mechanisms:**

 

**Traffic Classification:**

- Based on Layer 2-4 headers

- IP addresses, port numbers, protocols, VLAN tags

 

**Queuing Algorithms:**

- **FIFO**: First In First Out (no QoS)

- **Priority Queuing (PQ)**: Strict priority (risk of starvation)

- **Weighted Fair Queuing (WFQ)**: Fair bandwidth sharing

- **Class-Based WFQ (CBWFQ)**: Classes with bandwidth guarantees

- **Low Latency Queuing (LLQ)**: Priority queue + CBWFQ

 

**Congestion Avoidance:**

- **Tail Drop**: Drop packets when queue full (bursty drops)

- **Random Early Detection (RED)**: Drop packets probabilistically before queue fills

- **Weighted RED (WRED)**: Different drop probabilities for different classes

 

**Traffic Shaping vs Policing:**

- **Shaping**: Buffers excess traffic, smooths traffic (adds delay)

- **Policing**: Drops or marks excess traffic (no delay)

 

---

 

### Important Formulas Reference

 

**1. IPv4 Subnetting:**

```

Number of Subnets = 2^n (n = borrowed host bits)

Hosts per Subnet = 2^h - 2 (h = remaining host bits)

Subnet Increment = 256 - subnet mask octet

Network Address = all host bits = 0

Broadcast Address = all host bits = 1

First Usable Host = Network Address + 1

Last Usable Host = Broadcast Address - 1

```

 

**2. CIDR Prefix Length:**

```

Number of Addresses = 2^(32 - prefix_length)

Example: /24 → 2^(32-24) = 2^8 = 256 addresses

```

 

**3. Subnet Mask Conversion:**

```

CIDR to Decimal:

/24 = 255.255.255.0

/16 = 255.255.0.0

/8 = 255.0.0.0

 

Binary 1s in mask = CIDR prefix length

```

 

**4. Routing Metrics:**

```

RIP: Metric = Hop Count

OSPF: Cost = Reference Bandwidth / Interface Bandwidth

       (Reference = 100 Mbps by default)

       Cost = 100,000,000 / BW(bps)

```

 

**5. Administrative Distance (Trustworthiness):**

```

Lower AD = More Trusted

Directly Connected: 0

Static Route: 1

EIGRP: 90

OSPF: 110

RIP: 120

External EIGRP: 170

iBGP: 200

```

 

**6. QoS Bandwidth Calculation:**

```

Required Bandwidth = Packet Size × Packets per Second

Example: VoIP G.711

  - Codec: 64 kbps

  - IP/UDP/RTP overhead: ~40 bytes

  - Total per packet: 200 bytes

  - 50 packets/sec

  - Bandwidth: 80 kbps per call

```

 

**7. Queue Depth:**

```

Queue Depth = Bandwidth × Delay

Example: 1 Gbps link, 10 ms delay

  Queue = 1,000,000,000 bps × 0.01 s = 10,000,000 bits = 1.25 MB

```

 

---

 

### Exam Focus Areas

 

**High Priority Topics:**

 

1. **IP Addressing and Subnetting:**

   - CIDR notation and subnet calculations

   - Determining network, broadcast, and host addresses

   - Private vs public address ranges

   - IPv6 address types and notation

 

2. **Routing Fundamentals:**

   - Routing table structure and lookup process

   - Longest prefix match principle

   - Administrative distance and metric comparison

   - Static vs dynamic routing trade-offs

 

3. **Routing Algorithms:**

   - Distance Vector vs Link State differences

   - Understanding of DV problems (count-to-infinity)

   - SPF algorithm concept

   - Path Vector for inter-domain routing

 

4. **Dynamic Routing Protocols:**

   - RIP, OSPF, EIGRP, BGP characteristics

   - Appropriate protocol selection for different scenarios

   - Convergence time comparison

   - Administrative distance values

 

5. **Mobile IP:**

   - Architecture components (HA, FA, MN)

   - Tunneling mechanism

   - Triangle routing problem

   - Home address vs Care-of Address

 

6. **QoS Models:**

   - IntServ vs DiffServ comparison

   - DSCP marking and PHBs

   - Queuing algorithms (PQ, WFQ, CBWFQ)

   - Application requirements (VoIP, video, data)

 

7. **IPv6:**

   - Address format and compression

   - GUA vs LLA addresses

   - Advantages over IPv4

   - Transition mechanisms

 

**Common Exam Question Types:**

 

1. **Subnetting Problems:**

   - "Given network 192.168.10.0/24, subnet into 4 equal subnets"

   - "What is the broadcast address for host 172.16.45.123/20?"

   - "How many usable hosts in a /26 network?"

 

2. **Routing Decisions:**

   - "Given routing table, which route is selected for destination X?"

   - "Explain longest prefix match with example"

   - "Compare routes with different AD and metrics"

 

3. **Protocol Comparisons:**

   - "Compare DV and LS routing algorithms"

   - "When to use static vs dynamic routing?"

   - "OSPF vs BGP: differences and use cases"

 

4. **Mobile IP Scenarios:**

   - "Describe packet flow when MN is in foreign network"

   - "Explain triangle routing and how to avoid it"

   - "What is the role of Home Agent?"

 

5. **QoS Design:**

   - "Design QoS policy for VoIP, video, and data traffic"

   - "Explain DiffServ vs IntServ scalability"

   - "What DSCP marking for real-time video?"

 

6. **IPv6 Questions:**

   - "Compress IPv6 address: 2001:0db8:0000:0000:0000:0000:0000:0001"

   - "Identify address type: fe80::1, ff02::1, 2001:db8::1"

   - "Why IPv6 doesn't need NAT?"

 

7. **Troubleshooting:**

   - "Device can't reach Internet - check routing table and identify problem"

   - "Why is routing protocol not converging?"

   - "QoS not working - identify misconfiguration"

 

**Critical Concepts to Master:**

 

1. **Subnetting Math**: Practice rapid subnet calculations

2. **Routing Table Lookup**: Understand complete decision process

3. **Protocol Selection**: Know when to use each routing protocol

4. **Mobile IP Flow**: Trace packets through HA and tunnels

5. **QoS Classes**: Match applications to QoS treatments

6. **IPv6 Addressing**: Master compression and address type identification

 

---

 

### Practical Applications in Wireless Networks

 

1. **Mobile Device Handoff:**

   - Mobile IP enables seamless handoff between cellular towers

   - Care-of Address updates as device moves

   - Maintains TCP connections during movement

 

2. **IoT Device Addressing:**

   - IPv6 essential for massive IoT deployments

   - Each sensor can have globally unique address

   - No NAT simplifies end-to-end connectivity

 

3. **VoIP over Wireless:**

   - QoS critical for voice quality

   - Priority queuing for RTP packets

   - DSCP EF marking for VoIP traffic

   - Jitter buffers at receivers

 

4. **Video Streaming:**

   - DiffServ AF classes for different video qualities

   - Traffic shaping to match available bandwidth

   - Adaptive bitrate based on network conditions

 

5. **Cellular Network Architecture:**

   - Each cell (base station) is an IP subnet

   - Mobile IP or similar for inter-cell mobility

   - QoS for different service levels (voice, data, emergency)

 

6. **Wi-Fi Roaming:**

   - Fast handoff between access points

   - Consistent IP address within same subnet

   - 802.11r for optimized roaming

 

7. **SD-WAN and Multi-Path:**

   - Dynamic routing based on link quality

   - Application-aware routing (DiffServ classes)

   - BGP for multi-homed connections

 

8. **Network Function Virtualization (NFV):**

   - Virtual routers using OSPF/BGP

   - Software-defined QoS policies

   - Dynamic network slicing using IPv6 and QoS

 

---

 

### Key Takeaways

 

1. **Network Layer provides logical addressing and routing** across multiple networks, enabling the Internet to function as a global interconnected system

 

2. **IPv4 uses 32-bit addresses with CIDR for flexible subnetting**, while IPv6 provides 128-bit addresses eliminating address exhaustion concerns

 

3. **Subnetting allows efficient IP address allocation** by dividing networks into smaller segments with formula: Subnets = 2^n, Hosts = 2^h - 2

 

4. **NAT conserves IPv4 addresses** by allowing multiple private addresses to share one public address, but breaks end-to-end connectivity

 

5. **Routing algorithms fall into three categories**: Distance Vector (routing by rumor), Link State (complete topology), and Path Vector (policy-based)

 

6. **Interior routing protocols (RIP, OSPF, EIGRP) operate within an AS**, while BGP handles inter-domain routing at Internet scale

 

7. **Mobile IP solves mobility problem** by maintaining permanent home address while using Care-of Address in visited networks, with Home Agent tunneling packets

 

8. **QoS models differ in scalability**: Best Effort (no guarantees), IntServ (per-flow reservations), DiffServ (scalable class-based treatment)

 

9. **DiffServ uses DSCP marking and PHBs** to provide differentiated service without per-flow state in core routers

 

10. **IPv6 improvements include**: Larger address space, simplified header, built-in mobility support, no NAT requirement, and autoconfiguration

 

11. **Longest prefix match ensures** most specific route is always selected, enabling hierarchical routing and aggregation

 

12. **Wireless networks heavily depend on** Mobile IP for device mobility, IPv6 for IoT scalability, and QoS for real-time applications like VoIP and video

---

## Lecture 5b: Transport Layer

### Overview

 

The Transport Layer (Layer 4 in OSI, Layer 3 in TCP/IP) provides end-to-end communication between applications. This lecture covers the fundamental transport protocols (TCP and UDP), their mechanisms for reliability and congestion control, and the challenges of operating over wireless networks. Understanding transport layer behavior is critical for wireless communications where links are lossy, dynamic, and resource-constrained.

 

**Key Topics:**

- Transport layer addressing and connection establishment

- UDP and TCP protocols

- TCP reliability mechanisms (ACKs, timeouts, retransmissions)

- Flow control and congestion control

- Alternative transport protocols (SCTP, DCCP, QUIC)

- Transport layer challenges over wireless links

 

---

 

### 1. Transport Layer Fundamentals

 

**Role of Transport Layer:**

- Provides **end-to-end communication** between applications

- Operates **on top of the Network Layer** (IP)

- Transports data from **app A to remote app B**

- Handles **multiplexing** of multiple applications

 

**Position in Stack:**

- **OSI Model**: Layer 4 (Transport)

- **TCP/IP Model**: Layer 3 (Transport)

 

**Transport Layer Services:**

- **Reliable end-to-end communication** for services/applications

- **Flow control**: Don't exceed receiver's available capacity

- **Congestion control**: Don't exceed network's available capacity

- **Multiplexing**: Multiple applications sharing network layer

- **Connection-oriented or connectionless** communication

 

**Data Units:**

- **TPDU** (Transport Protocol Data Unit) in OSI terminology

- **Segment** (TCP) or **Datagram** (UDP) in Internet terminology

- **PDU** (Protocol Data Unit): Data sent to peer protocol layer

- **SDU** (Service Data Unit): Data sent from one layer to lower layer

 

---

 

### 2. Transport Layer Addressing

 

**Port Numbers:**

- 16-bit numbers identifying applications/services

- Range: 0-65535

 

**Port Types and Ranges (RFC 1700):**

 

1. **Well-known ports (0-1023)**:

   - Reserved for standard services

   - Maintained by IANA

   - Used by servers

   - Examples:

     - Port 20/21: FTP (data/control)

     - Port 22: SSH

     - Port 25: SMTP (email)

     - Port 53: DNS

     - Port 80: HTTP

     - Port 123: NTP (Network Time Protocol)

     - Port 443: HTTPS

 

2. **Registered ports (1024-49151)**:

   - Assigned by IANA to requesting entities

   - Not controlled by IANA

   - Used by client applications

   - Example: Port 6073 for DirectX gaming

 

3. **Private/Dynamic ports (49152-65535)**:

   - Assigned dynamically by client OS

   - Identify application/service endpoints

   - Used as ephemeral ports

 

**5-Tuple for Flow Identification:**

 

To distinguish a particular communication process (conversation):

1. **Source port**: Selected dynamically, used as return address

2. **Destination port**: Well-known or registered port

3. **Source IP address**: Sender's IP

4. **Destination IP address**: Receiver's IP

5. **Protocol**: TCP or UDP

 

**Service Access Points:**

- **TSAP** (Transport Service Access Point): Port number

- **NSAP** (Network Service Access Point): IP address

 

**Sockets:**

- **Socket**: One endpoint to a two-way communication

  - Format: IP_address:port (e.g., 192.168.1.1:80)

- **Socket Pair**: Two ends of communication (local and remote)

 

**Berkeley Sockets API Primitives:**

- **SOCKET**: Create a new communication endpoint

- **BIND**: Attach a local address to a socket

- **LISTEN**: Announce willingness to accept connections

- **ACCEPT**: Block until connection attempt arrives

- **CONNECT**: Actively attempt to establish a connection

- **SEND**: Send data over the connection

- **RECEIVE**: Receive data from the connection

- **CLOSE**: Release the connection

 

---

 

### 3. User Datagram Protocol (UDP)

 

**UDP Characteristics:**

- **Connectionless/stateless**: No connection establishment

- **Message-based**: Sends datagrams

- **Unreliable**: No delivery guarantees

- **Unordered**: Packets may arrive out of order

- **No flow control**: Must be implemented in application

- **No congestion control**: Must be implemented in application

 

**UDP = IP + 2 features:**

1. **Ports** (multiplexing/demultiplexing)

2. **Checksum** (optional error detection)

 

**UDP Header Format:**

```

| Source Port (16 bits) | Destination Port (16 bits) |

| UDP Length (16 bits)  | UDP Checksum (16 bits)     |

```

- **Total header size**: 8 bytes (very lightweight)

 

**UDP Specification:**

- Defined in RFC 768 (1980)

- Only 3 pages long (compared to TCP's 85 pages)

 

**Advantages:**

- **Less overhead**: Minimal header, no connection state

- **Lower delay**: No connection setup, no retransmissions

- **Simple**: Easy to implement

 

**Disadvantages:**

- **Unreliable**: Packets can be lost

- **No congestion control**: Can flood network

- **No flow control**: Can overwhelm receiver

 

**UDP Use Cases:**

- **Live media streaming**: Video, audio (VoIP)

- **DNS**: Domain Name System queries

- **SNMP**: Network management

- **DHCP**: Dynamic IP configuration

- **Online games**: Real-time interaction

- **IPTV**: Internet television

 

---

 

### 4. Transmission Control Protocol (TCP) - Overview

 

**TCP Characteristics:**

- **Connection-oriented**: Establishes connection before data transfer

- **Byte-stream based**: Divides data into segments

- **Reliable delivery**: Uses ACKs and retransmissions

- **In-order delivery**: Sequence numbers ensure correct order

- **Flow control**: Prevents overwhelming receiver

- **Congestion control**: Adapts to network capacity

- **Single stream**: One data stream per connection

 

**TCP Specification:**

- Defined in RFC 793 (1981)

- Complex: 85 pages (vs UDP's 3 pages)

- Originally developed for DARPA

 

**TCP Header Format:**

```

32 bits wide:

| Source Port (16) | Destination Port (16) |

| Sequence Number (32)                    |

| Acknowledgment Number (32)              |

| Hlen | Rsvd | Flags | Window (16)      |

| Checksum (16)    | Urgent Pointer (16) |

| Options (variable)                      |

```

 

**Header size**: 20-60 bytes (20 bytes minimum, up to 40 bytes options)

 

**Key TCP Header Fields:**

 

1. **Sequence Number** (32 bits):

   - Sequence number of first byte in segment

   - If SYN bit set, this is **Initial Sequence Number (ISN)**

   - Data begins at ISN+1

 

2. **Acknowledgment Number** (32 bits):

   - If ACK bit set, value of next sequence number expected

   - **Cumulative**: ACK n acknowledges everything up to n-1

 

3. **Header Length (Hlen)** (4 bits):

   - Header length in 32-bit words

   - Indicates where data begins

 

4. **Window** (16 bits):

   - Number of bytes receiver willing to receive

   - **Receiver advertised window (rwnd)**

 

5. **Checksum** (16 bits):

   - Error checking for header and data

 

6. **TCP Flags**:

   - **SYN**: Synchronize, establish connection

   - **ACK**: Acknowledgment

   - **FIN**: Finish, terminate connection

   - **RST**: Reset connection

   - **URG**: Urgent pointer valid (rarely used)

   - **PSH**: Push data immediately (rarely used)

   - **CWR**: Congestion Window Reduced (ECN)

   - **ECE**: ECN Echo (ECN)

 

**TCP Encapsulation:**

```

| IP header | TCP header | TCP data (optional) |

           <------- TCP segment -------->

<-------------- IP packet --------------->

```

 

**TCP Use Cases:**

- **Web browsing**: HTTP/HTTPS

- **Email**: SMTP, IMAP, POP3

- **File transfer**: FTP, SFTP

- **Remote access**: SSH, Telnet

- **Any application requiring reliability**

 

---

 

### 5. TCP Connection Management

 

**TCP Connection Establishment: 3-Way Handshake**

 

Minimum time: **2 RTT** (Round-Trip Times)

 

**Steps:**

1. **Client → Server: SYN**

   - Client sends SYN packet with initial sequence number (ISN)

   - `SEQ=100, CTL=SYN`

 

2. **Server → Client: SYN/ACK**

   - Server acknowledges client's SYN

   - Server sends its own SYN with its ISN

   - `SEQ=300, ACK=101, CTL=SYN,ACK`

 

3. **Client → Server: ACK**

   - Client acknowledges server's SYN

   - Connection established, can send data

   - `SEQ=101, ACK=301, CTL=ACK`

 

**Why 3-way handshake?**

- Prevents old duplicate connections from causing confusion

- Synchronizes sequence numbers in both directions

- Allows negotiation of parameters (window size, MSS, etc.)

 

**TCP Connection Termination: 4-Way Handshake**

 

Actually **two 2-way handshakes** (one for each direction)

 

**Steps:**

1. **A → B: FIN**

   - Side A wants to close connection

   - Can still receive data

 

2. **B → A: ACK**

   - Side B acknowledges FIN

   - Side B can still send data

 

3. **B → A: FIN**

   - Side B finished sending data

   - Wants to close its side

 

4. **A → B: ACK**

   - Side A acknowledges FIN

   - Connection fully closed

 

**Why 4-way (2×2-way)?**

- TCP provides **bidirectional data transfer**

- One side might still have data to send

- Each direction closed independently

 

**Connection States:**

- LISTEN, SYN-SENT, SYN-RECEIVED, ESTABLISHED

- FIN-WAIT-1, FIN-WAIT-2, CLOSING, TIME-WAIT, CLOSE-WAIT, LAST-ACK, CLOSED

 

---

 

### 6. TCP Reliability Mechanisms

 

**In-Order Data Delivery:**

 

- TCP data stream pushed to application **in-order only**

- Segments can arrive **out-of-order** (different routes, router parallelism)

- **Sequence numbers** enable reassembly at receiver

- Receiver buffers out-of-order segments until gaps filled

 

**Process:**

1. Data divided into segments at sender

2. Each segment numbered with sequence number

3. Segments may take different routes

4. Receiver reorders using sequence numbers

5. Application receives ordered byte stream

 

**Acknowledgments (ACKs):**

 

**Cumulative ACKs:**

- **ACK n** acknowledges all data up to byte n-1

- Next expected byte is n

- Example: ACK=170 means bytes 0-169 received

 

**Delayed ACKs (RFC 1122):**

- Don't ACK every segment immediately

- **ACK every 2 segments** OR

- **Once every 500ms** (or 200ms in Windows)

- Exception: Send DupACKs immediately

 

**Duplicate ACKs (DupACKs):**

- Sent when receiver sees a **gap** in sequence numbers

- Indicates missing segment

- **3 DupACKs** trigger Fast Retransmit

 

**ACK Characteristics:**

- ACK packets are **unreliable**

- Less costly to drop than data packets

- ACK loss doesn't stop communication (cumulative nature helps)

 

**Retransmission Mechanisms:**

 

**1. Timeout-Based Retransmission:**

 

**Retransmission Timeout (RTO):**

- Timer for detecting packet loss

- When expires, retransmit missing packet

- Set cwnd=1 (restart slow start)

 

**RTO Calculation (RFC 6298):**

- Based on measured RTT

- Must handle RTT variation

- Minimum RTO ≥ 1 second

 

**Challenges:**

- **Too long**: Slow to detect loss

- **Too short**: False positives, unnecessary retransmissions

 

**2. Fast Retransmit:**

- Triggered by **3 duplicate ACKs**

- Don't wait for RTO timeout

- Retransmit missing segment immediately

- More efficient than timeout

 

**Fast Recovery:**

- After Fast Retransmit, don't reset to cwnd=1

- Set cwnd=SSThresh (skip slow start)

- Start from half the previous cwnd

- Faster recovery from loss

 

---

 

### 7. TCP Flow Control

 

**Purpose:**

- Prevent sender from overwhelming **receiver's buffer**

- Different from congestion control (network capacity)

 

**Receiver Advertised Window (rwnd):**

- **Sliding window** based on available TCP receive buffer

- Receiver announces in TCP header Window field

- Indicates how many bytes receiver can accept

 

**Send Window (Congestion Window - cwnd):**

- Number of bytes TCP sender allowed to inject into network

- **Dynamically adjusted** based on network conditions

- **Capped at rwnd**: `effective_cwnd = min(cwnd, rwnd)`

 

**Sliding Window Mechanism:**

```

[------Already ACKed------][--Can Send--][--Future--]

                          ^              ^

                      Send window      rwnd

```

 

**Window Evolution:**

- Window slides forward as ACKs received

- Allows continuous data transmission

- Implements **pipelining** for efficiency

 

**Flow Control vs Congestion Control:**

- **Flow control**: Limited **receiver capacity** → overflow at receiver

- **Congestion control**: Limited **network capacity** → congestion in network

 

---

 

### 8. TCP Congestion Control

 

**Objective:**

- Adapt sending rate to **available network capacity**

- Prevent network congestion

- Share bandwidth fairly among flows

 

**Congestion Window (cwnd):**

- Number of bytes sender can inject before expecting ACK

- Dynamically adjusted based on network feedback

- **Updated on every ACK received**

 

**Initial Window (IW / initcwnd):**

- Starting cwnd value

- ~3 packets (MSS) since 2002

- **10 packets** since ~2013 (RFC 6928, Linux 2.6.39+)

 

**Slow Threshold (SSThresh):**

- Boundary between Slow Start and Congestion Avoidance

- Initially set to large value (max advertised window)

- Updated on congestion events

 

**TCP Congestion Control Phases:**

 

**1. Slow Start (SS):**

- **Exponential growth** (binary search for capacity)

- **For every ACK**: `cwnd = cwnd + 1 MSS`

- **Doubles every RTT**

- Continue until: cwnd ≥ SSThresh OR packet loss

 

**Example:**

```

RTT 1: cwnd = 1  → Send 1 packet  → Receive 1 ACK  → cwnd = 2

RTT 2: cwnd = 2  → Send 2 packets → Receive 2 ACKs → cwnd = 4

RTT 3: cwnd = 4  → Send 4 packets → Receive 4 ACKs → cwnd = 8

```

 

**2. Congestion Avoidance (CA):**

- **Linear growth** (additive increase)

- **For every ACK**: `cwnd = cwnd + 1/cwnd`

- **~1 packet per RTT**

- Continues until packet loss

 

**AIMD (Additive Increase Multiplicative Decrease):**

- **Additive Increase**: cwnd += 1/cwnd per ACK

- **Multiplicative Decrease**: cwnd = cwnd × β on loss

  - Standard TCP: β = 0.5 (RFC 6582)

  - TCP CUBIC: β = 0.7 (RFC 8312, Linux default)

 

**Loss Detection and Response:**

 

**On 3 DupACKs:**

```

SSThresh = cwnd / 2

cwnd = SSThresh

# Fast Retransmit + Fast Recovery

```

 

**On RTO (Timeout):**

```

SSThresh = cwnd / 2

cwnd = 1 MSS

# Restart from Slow Start

```

 

**Congestion Control Behavior:**

```

cwnd

  ^

  |      /\      /\

  |     /  \    /  \

  |    /    \  /    \

  |   /      \/      \

  +----------------------> time

     SS  CA  Loss  CA

```

 

---

 

### 9. Alternative Transport Protocols

 

**Stream Control Transmission Protocol (SCTP - RFC 4960):**

 

**Features:**

- **Message-oriented** data transfer (chunks)

- **Connection-oriented** with reliability

- **Congestion control** (TCP-like)

- **Multi-streaming**: Multiple independent streams in one connection

- **Multi-homing**: Multiple IP addresses per endpoint

- **Unordered reliable delivery**: Optionally

- **Partial reliability**: Optional (RFC 3758)

- **4-way handshake**: Cookie exchange prevents SYN flooding

 

**SCTP Header:**

- Common header with chunks

- Each chunk: type, flags, length, data

 

**Use Cases:**

- Signaling (SS7 over IP)

- WebRTC data channels

- Applications needing multi-streaming

 

**Datagram Congestion Control Protocol (DCCP - RFC 4340):**

 

**Formula:**

```

DCCP = UDP + congestion control

  OR

DCCP = TCP − bytestream semantics − full reliability

```

 

**Features:**

- **Message-oriented**, **unreliable**, **unordered**

- **Provides congestion control** (using ACKs)

- **Explicit Congestion Notification (ECN)** support

- **Reliable connection setup/teardown**

- **Negotiable congestion control** mechanism

- **Bi-directional** communication

 

**Use Cases:**

- Interactive multimedia

- Online gaming

- Applications needing congestion control without TCP overhead

 

**Quick UDP Internet Connections (QUIC):**

 

**Development:**

- Developed by Google (2012)

- Rapidly deployed to break "deployment impossibility cycle"

- Standardized at IETF (ongoing)

- **7.8% of Internet traffic** by 2018 (APNIC)

 

**Key Features:**

- **Runs over UDP** (bypasses middleboxes)

- **Encrypted by default** (TLS 1.3 integrated)

- **Userland implementation** (faster evolution)

- **0-RTT connection establishment** (with cookies)

- **Multiplexed streams** (solves TCP head-of-line blocking)

- **In-order reliable delivery** (per stream)

- **Connection migration** (survives IP changes)

 

**QUIC vs TCP+TLS:**

```

TCP + TLS:

- Connection setup: 100 ms (1 RTT)

- TLS handshake: 200 ms (2 RTT, if not resumed)

- Total: ~300 ms before first byte

 

QUIC:

- Connection setup: 0 ms (0-RTT with cookie)

- Total: ~0 ms before first byte (if resumed)

```

 

**Stack Comparison:**

```

Traditional:          QUIC:

HTTP/2               HTTP/2

TLS 1.2              TLS 1.3 (integrated)

TCP                  QUIC

IP                   UDP

                     IP

```

 

**Benefits:**

- Faster connection establishment

- Better performance over lossy links

- No head-of-line blocking across streams

- Easier to evolve (userland, encrypted)

 

---

 

### 10. Transport Layer over Wireless Medium

 

**Challenges:**

 

**1. Lossy Wireless Links:**

- **Frame collisions**: CSMA/CA contention on shared medium

- **Environmental noise**: High Bit Error Rate (BER)

- **Interference**: From other devices

- **Most MAC frame losses masked** by L2 retransmissions

  - 802.11 retry limit: 4 (short) to 7 (long) frames

 

**Multi-Rate Retry Chain:**

- `([r0, c0], [r1, c1], [r2, c2], [r3, c3])`

- r = Modulation and Coding Scheme (MCS)

- c = retry count at each MCS

- Adapts to channel conditions

 

**2. Loss Ambiguity:**

 

TCP cannot distinguish:

- **Congestion loss** (full buffer in network)

- **Wireless loss** (noise, interference, collision)

 

**Problem:**

- TCP treats all loss as congestion

- Reduces cwnd unnecessarily for wireless loss

- **Suboptimal performance** over wireless

 

**3. Variable RTT:**

- Affected by MAC layer retransmissions

- Can vary from tens of ms to seconds

- **High RTT variability** confuses:

  - RTO calculation

  - Delay-based congestion control

 

**Impact of Rate Adaptation:**

- Low MCS (bit rates) → High transmission time

- Many retries → Increased latency

- Can trigger transport layer timeouts

- Reduced throughput

 

**4. Dynamic Wireless Conditions:**

 

Unlike wired switched networks:

 

a) **Channel conditions**: Noise, interference, contention

b) **RTT variability**: Both from conditions and distance

   - CDN: tens of ms

   - Poor Wi-Fi: hundreds of ms to seconds

c) **Dynamic topology**: Movement, node density, obstacles, distance

 

**5. Bandwidth Constraints (changing):**

- **802.11 MAC layer bit rates:**

  - 802.11g: 54 Mbps

  - 802.11n: ~300 Mbps

  - 802.11ac: ~1.5 Gbps

  - 802.11ax: several Gbps

- **Cellular peak data rates:**

  - 4G (IMT-Advanced): 1 Gbps

  - 5G (IMT-2020): 20 Gbps

 

**6. Power Constraints:**

- Battery life limitations (4G/Wi-Fi)

- Retransmissions more costly

- Resource-constrained IoT devices:

  - LoRaWAN, BLE, Zigbee (802.15.4)

  - Can't run full TCP/IP stack

  - Use lightweight protocols (uTCP/uIP)

  - Sporadic small packets (cwnd=1)

 

---

 

### 11. Mitigating Wireless Transport Issues

 

**Strategies:**

 

**1. Explicit Congestion Notification (ECN - RFC 3168):**

 

**Purpose:**

- Network **explicitly signals** congestion

- Avoids packet drops

- Better for wireless (distinguish from wireless loss)

 

**ECN Operation:**

 

**Setup:**

1. Sender and receiver **negotiate ECN** during connection establishment

   - Client: `SYN, CWR, ECE`

   - Server: `SYN, ACK, ECE`

 

**During Data Transfer:**

2. Router marks packets when **detecting congestion** (AQM)

   - Sets **CE (Congestion Experienced)** bit in IP header

3. Receiver **echoes CE mark** back to sender using **ECE flag** in TCP header

4. Sender **reduces sending rate** (cwnd) and sets **CWR flag**

5. Receiver stops echoing upon seeing CWR

 

**ECN Bits in IP Header:**

- 2 bits in TOS field:

  - `00`: Not ECN-capable

  - `10`: ECT(0) - ECN-capable

  - `01`: ECT(1) - ECN-capable

  - `11`: CE - Congestion Experienced

 

**ECN Bits in TCP Header:**

- **CWR**: Congestion Window Reduced

- **ECE**: ECN Echo

 

**Benefits:**

- Avoid packet drops

- Faster congestion response

- Better for wireless links

 

**2. Active Queue Management (AQM):**

 

**Purpose:**

- Drop/mark packets **before queue full**

- Signal congestion early

- Reduce latency (combat bufferbloat)

 

**AQM Algorithms:**

 

**Random Early Detection (RED):**

- Probabilistic dropping based on average queue length

- `p = f(avg_queue_length)`

- **Problems**: Complex, requires tuning

 

**Modern AQMs (for Bufferbloat):**

- **CoDel (2012)**: Delay-based, no configuration

- **FQ_CoDel**: CoDel with fair queuing

- **PIE (2013)**: Proportional Integral controller Enhanced

- **Adaptive RED (2001)**: Self-tuning RED

 

**ECN-capable AQMs:**

- Mark packets (set CE) instead of dropping

- Works with ECN-enabled endpoints

- Example: FQ_CoDel with ECN

 

**3. Advanced Congestion Control:**

 

**Delay-Based CC:**

- Observe RTT or One-Way Delay (OWD) trends

- Reduce rate on increasing delay (before loss)

- Examples:

  - TCP Vegas, FAST TCP, TCP-Africa

  - CTCP (Compound TCP)

  - CDG (CAIA Delay Gradient)

 

**Problems:**

- Need to predict base-RTT

- Unfair coexistence with loss-based TCP

- Wireless RTT variability challenges measurement

 

**Model-Based CC:**

- **BBR (Bottleneck Bandwidth and RTT)**:

  - Developed by Google

  - Actively measures available capacity

  - Maintains sending rate near capacity

  - Better performance on wireless

 

**Hybrid Approaches:**

- Combine loss, delay, and model-based signals

- Example: TCP CUBIC (default in Linux)

  - Loss-based with cubic growth function

  - β = 0.7 (less aggressive reduction)

 

**4. Better Transport Protocols:**

- **Message-based** instead of byte-stream

- **Per-stream prioritization** (SCTP, QUIC)

- **Application-layer FEC**: Forward Error Correction

- **Challenges**: Can't pick transport based on one link segment

 

**5. TCP Over Satellite (SATCOM):**

 

**Problem:**

- **Very high RTT**: ~650 ms (GEO satellite)

- Slow cwnd growth (feedback loop too long)

- Retransmissions very costly

 

**HTTP Request Latency:**

```

DNS lookup + 3-way handshake + TLS 1.2 handshake + HTTP request

= ~4 RTT + DNS

≈ 2.6 seconds over SATCOM

```

 

**Solution: TCP Splitting (Performance Enhancing Proxy - PEP):**

 

```

[Client]--[PEP]--[Satellite]--[PEP]--[Server]

   TCP      TCP   optimized     TCP     TCP

           split      link      split

```

 

**Benefits:**

- Fast connection establishment on terrestrial segments

- Optimized CC for satellite segment

- Transparent to endpoints

 

**QUIC Challenge:**

- Encrypted headers prevent PEP inspection

- Can't perform TCP splitting

- Future: QUIC-aware proxies or expose some headers

 

---

 

### Important Formulas Reference

 

**1. TCP Window Sizes:**

```

Effective cwnd = min(cwnd, rwnd)

 

where:

  cwnd = Congestion window (network capacity)

  rwnd = Receiver advertised window (receiver capacity)

```

 

**2. Slow Start:**

```

Per ACK: cwnd = cwnd + 1 MSS

Per RTT: cwnd doubles (exponential growth)

```

 

**3. Congestion Avoidance:**

```

Per ACK: cwnd = cwnd + (1 MSS / cwnd)

Per RTT: cwnd increases by ~1 MSS (linear growth)

```

 

**4. Loss Response:**

```

On 3 DupACKs (Fast Retransmit):

  SSThresh = cwnd / 2

  cwnd = SSThresh  (Fast Recovery)

 

On Timeout (RTO):

  SSThresh = cwnd / 2

  cwnd = 1 MSS  (Restart Slow Start)

```

 

**5. AIMD Parameters:**

```

Standard TCP:

  Multiplicative Decrease: β = 0.5

 

TCP CUBIC:

  Multiplicative Decrease: β = 0.7

```

 

**6. Initial Window:**

```

Traditional (pre-2002): IW = 1-2 MSS

RFC 3390 (2002): IW = min(4*MSS, max(2*MSS, 4380 bytes)) ≈ 3-4 MSS

RFC 6928 (2013): IW = 10 MSS (Linux default since 2.6.39)

```

 

**7. Bandwidth-Delay Product:**

```

BDP = Bandwidth × RTT

 

Optimal cwnd for full utilization:

  cwnd ≥ BDP

 

Example: 100 Mbps link, 100 ms RTT

  BDP = 100,000,000 bps × 0.1 s = 10,000,000 bits = 1.25 MB

```

 

**8. Throughput Estimation:**

```

TCP Throughput ≈ (cwnd / RTT)

 

Mathis formula (steady state with loss):

  Throughput ≈ (MSS / RTT) × (C / √p)

 

where:

  p = packet loss rate

  C ≈ 1.22 for standard TCP

  MSS = Maximum Segment Size

```

 

**9. Connection Establishment Time:**

```

TCP: 1 RTT (3-way handshake)

TCP + TLS 1.2: 3 RTT (handshake + TLS full handshake)

TCP + TLS 1.3: 2 RTT (handshake + TLS)

QUIC: 0 RTT (with previous connection cookie)

 

HTTP request time:

  DNS lookup + connection setup + request/response

```

 

---

 

### Exam Focus Areas

 

**High Priority Topics:**

 

1. **Transport Layer Addressing:**

   - Port numbers and ranges (well-known, registered, private)

   - 5-tuple for flow identification

   - Socket concept and socket pairs

   - Berkeley sockets API primitives

 

2. **UDP vs TCP Comparison:**

   - Connectionless vs connection-oriented

   - Message-based vs byte-stream

   - Reliability mechanisms

   - Use cases for each

 

3. **TCP Connection Management:**

   - 3-way handshake process and purpose

   - 4-way handshake for termination

   - Why 4-way instead of 3-way for termination

   - Connection states

 

4. **TCP Reliability:**

   - Sequence numbers and ACK numbers

   - Cumulative ACKs

   - Delayed ACKs (every 2 segments or 500ms)

   - Duplicate ACKs and Fast Retransmit

   - Timeout and RTO calculation

 

5. **TCP Flow Control:**

   - Receiver advertised window (rwnd)

   - Sliding window mechanism

   - Difference from congestion control

 

6. **TCP Congestion Control:**

   - Slow Start exponential growth

   - Congestion Avoidance linear growth

   - AIMD principle

   - Initial Window values

   - SSThresh and state transitions

   - Fast Retransmit and Fast Recovery

 

7. **Alternative Protocols:**

   - SCTP features (multi-streaming, multi-homing)

   - DCCP = UDP + congestion control

   - QUIC advantages (0-RTT, multiplexing, encryption)

 

8. **Wireless Challenges:**

   - Loss ambiguity (congestion vs wireless)

   - Impact of MAC retransmissions on RTT

   - Dynamic conditions and variable RTT

   - Power constraints

 

9. **ECN and AQM:**

   - ECN operation and bit meanings

   - Benefits over packet dropping

   - AQM purpose and algorithms (RED, CoDel, PIE)

 

10. **TCP over SATCOM:**

    - High latency problem (~650 ms RTT)

    - PEP and TCP splitting

    - QUIC challenges with PEP

 

**Common Exam Question Types:**

 

1. **Protocol Comparison:**

   - "Compare UDP and TCP in terms of reliability, ordering, and overhead"

   - "When would you use UDP instead of TCP?"

   - "Explain QUIC advantages over TCP+TLS"

 

2. **Connection Management:**

   - "Draw and explain TCP 3-way handshake"

   - "Why does TCP use 4-way handshake for termination?"

   - "Calculate time to establish TCP connection given RTT"

 

3. **Sequence Number Calculations:**

   - "Given ISN=1000, after sending 500 bytes, what is next SEQ?"

   - "If ACK=1500, what bytes have been acknowledged?"

   - "Explain how out-of-order segments are handled"

 

4. **Congestion Control Evolution:**

   - "Trace cwnd evolution through slow start and congestion avoidance"

   - "What happens to cwnd on 3 DupACKs vs RTO?"

   - "Calculate cwnd after N RTTs in slow start starting from IW=10"

 

5. **Flow vs Congestion Control:**

   - "Explain difference between flow and congestion control"

   - "What is the effective sending window?"

   - "Why do we need both rwnd and cwnd?"

 

6. **Wireless Issues:**

   - "Why does TCP perform poorly over lossy wireless links?"

   - "How do MAC retransmissions affect transport layer?"

   - "Explain loss ambiguity problem"

 

7. **Solutions and Mitigations:**

   - "How does ECN help wireless performance?"

   - "Explain AQM purpose and operation"

   - "Why is delay-based CC better for wireless?"

 

8. **Practical Calculations:**

   - "Given 100 Mbps link with 50 ms RTT, calculate optimal cwnd"

   - "Estimate throughput given cwnd=20 MSS, RTT=100ms, MSS=1460 bytes"

   - "How long to transfer 10 MB over 1 Mbps with 200 ms RTT?"

 

9. **Port Numbers:**

   - "What port does HTTP use? HTTPS? DNS? SSH?"

   - "What is the range of well-known ports?"

   - "Explain ephemeral ports"

 

10. **Header Analysis:**

    - "Identify TCP header fields and their purposes"

    - "What flags are set during connection establishment?"

    - "Calculate header overhead for UDP vs TCP"

 

**Critical Concepts to Master:**

 

1. **5-tuple and port ranges**: Know port categories and common services

2. **TCP handshakes**: Draw and explain 3-way and 4-way processes

3. **Cwnd evolution**: Trace through SS, CA, loss events

4. **ACK behavior**: Cumulative, delayed, duplicate

5. **Loss detection**: 3 DupACKs vs RTO timeout

6. **Wireless challenges**: Loss ambiguity, variable RTT, power

7. **ECN operation**: Negotiation, marking, echoing, response

8. **Protocol selection**: When to use UDP, TCP, SCTP, QUIC

 

---

 

### Practical Applications in Wireless Networks

 

1. **VoIP over Wi-Fi:**

   - Uses UDP (low latency priority)

   - Can use RTP (Real-time Transport Protocol) over UDP

   - Tolerates some packet loss

   - Jitter buffers at receiver

   - QoS markings (DSCP EF) for priority

 

2. **Video Streaming:**

   - Often TCP (HTTP-based: HLS, DASH)

   - Adaptive bitrate based on bandwidth

   - Buffering to handle variability

   - Increasingly using QUIC (YouTube, Netflix)

 

3. **Web Browsing over Cellular:**

   - HTTP/2 or HTTP/3 (QUIC)

   - Benefits from 0-RTT in QUIC

   - TCP splitting at cellular gateways

   - Connection migration during handoff

 

4. **IoT Device Communication:**

   - Lightweight protocols (MQTT over TCP)

   - CoAP over UDP for constrained devices

   - Small, infrequent transmissions

   - Long sleep periods to save power

 

5. **Online Gaming:**

   - Primarily UDP (low latency critical)

   - Custom reliability at application layer

   - Position updates can tolerate loss

   - Critical events (e.g., shots) need reliability

 

6. **Satellite Internet:**

   - High latency (~650 ms GEO)

   - PEP for TCP splitting

   - Specialized congestion control

   - QUIC challenges due to encryption

 

7. **WebRTC:**

   - SCTP over DTLS over UDP for data channels

   - SRTP over UDP for media

   - Multi-streaming benefits

   - NAT traversal with ICE

 

8. **Mobile App Background Sync:**

   - TCP for reliability

   - Periodic keep-alives drain battery

   - Push notifications to wake app

   - Batch transfers to minimize radio on-time

 

---

 

### Key Takeaways

 

1. **Transport layer provides end-to-end communication between applications** using port numbers for multiplexing and demultiplexing

 

2. **UDP is simple, fast, and unreliable** (only adds ports and optional checksum to IP), suitable for real-time applications that tolerate loss

 

3. **TCP provides reliable, ordered, byte-stream delivery** using sequence numbers, ACKs, retransmissions, flow control, and congestion control

 

4. **TCP uses 3-way handshake to establish connections** (SYN, SYN/ACK, ACK) taking minimum 1 RTT before data transfer begins

 

5. **TCP reliability achieved through cumulative ACKs and retransmissions** triggered by duplicate ACKs (Fast Retransmit) or timeouts (RTO)

 

6. **Flow control prevents overwhelming the receiver** using receiver advertised window (rwnd), while congestion control prevents overwhelming the network using cwnd

 

7. **TCP congestion control has two phases**: Slow Start (exponential growth) and Congestion Avoidance (linear growth following AIMD)

 

8. **Fast Retransmit/Recovery triggered by 3 DupACKs** reduces cwnd to half, while RTO timeout reduces cwnd to 1 MSS

 

9. **Alternative protocols address TCP limitations**: SCTP (multi-streaming), DCCP (UDP+CC), QUIC (0-RTT, encryption, multiplexing)

 

10. **Wireless networks challenge transport protocols** due to loss ambiguity, variable RTT, MAC retransmissions, and power constraints

 

11. **ECN allows explicit congestion signaling** avoiding packet drops, beneficial for wireless where loss may be non-congestion related

 

12. **AQM mechanisms mark/drop packets before queue full** to signal congestion early and reduce latency (bufferbloat mitigation)

 

13. **Loss-based TCP performs poorly over wireless** because it cannot distinguish congestion loss from wireless channel loss

 

14. **TCP splitting via PEPs helps high-latency links** like satellites but faces challenges with encrypted protocols like QUIC

 

15. **QUIC is rapidly gaining adoption** (7.8% of Internet traffic by 2018) due to faster connection setup, better wireless performance, and easier evolution

---

## Lecture 6: Cellular Networks

*Summary will be added here*

---

## Lecture 7: WLAN-PAN-LPWAN

*Summary will be added here*

---

## Lecture 8: Tools

*Summary will be added here*

---

## Lecture 9: Wireless Security

*Summary will be added here*

---

## Lecture 10: IoT

*Summary will be added here*

---

## Quick Reference

For formulas and calculations, see [FORMULAS_REFERENCE.md](./FORMULAS_REFERENCE.md)
For study strategy and schedule, see [EXAM_PREPARATION_PLAN.md](./EXAM_PREPARATION_PLAN.md)
