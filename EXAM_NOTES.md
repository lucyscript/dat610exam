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
