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

### Key Learning Questions (Part 1):
- Principles of cellular networks?
- Operations of cellular networks?
- Evolution of cellular networks?
- Architecture of 4G and new features?
- Current vision of 6G?
- Different LPWAN technologies? Differences?
- What is private 5G?

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
- Architecture of 5G and new features?
- Principles and characteristics of 5G Core Network and RAN?
- Technologies used in 5G NR Air Interface?
- Enabling technologies of 5G?
- How can be 5G deployed?
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
