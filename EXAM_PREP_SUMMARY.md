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

*Summary will be added here*

---

## Lecture 4: Data Link Layer Coding

*Summary will be added here*

---

## Lecture 5a: Network Layer

*Summary will be added here*

---

## Lecture 5b: Transport Layer

*Summary will be added here*

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
