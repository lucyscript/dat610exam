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
