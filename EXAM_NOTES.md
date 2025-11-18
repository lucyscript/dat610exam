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

### Transport Layer Fundamentals

**Role**: End-to-end communication between applications on top of network layer

**Addressing & Connection**:
- **Port Numbers**:
  - Well-known (0-1023): Reserved for services (HTTP=80, HTTPS=443, DNS=53, SSH=22, FTP=20/21, SMTP=25)
  - Registered (1024-49151): Assigned by IANA for applications
  - Dynamic/Private (49152-65535): Assigned by OS dynamically
- **5-Tuple**: (Source IP, Source Port, Dest IP, Dest Port, Protocol) - uniquely identifies a connection
- **Socket**: One endpoint of two-way communication (e.g., 192.168.1.1:80)
- **TSAP** (Transport Service Access Point) & **NSAP** (Network Service Access Point)

---

### User Datagram Protocol (UDP)

**Characteristics**:
- Connectionless/stateless
- Unreliable, unordered delivery
- Message-based (datagrams)
- No flow control, no congestion control
- Minimal overhead (8-byte header)

**Header Fields**: Source port, Dest port, Length, Checksum

**Use Cases**: Live streaming, DNS, VoIP, online games, IPTV (applications tolerant to loss but sensitive to delay)

**Formula**: UDP = IP + Port numbers + Checksum

---

### Transmission Control Protocol (TCP)

**Characteristics**:
- Connection-oriented (stateful)
- Reliable, in-order delivery
- Byte-stream based (segments)
- Flow control & congestion control
- Full-duplex bidirectional

**TCP Header** (20-60 bytes):
- **Sequence number**: First byte in segment (or ISN if SYN set)
- **Acknowledgment number**: Next expected byte (cumulative ACKs)
- **Flags**: SYN (establish), ACK (acknowledge), FIN (terminate), RST (reset), CWR/ECE (ECN)
- **Window**: Receiver advertised window (rwnd) - bytes receiver can accept
- **Checksum**: Error checking

#### Connection Management

**3-Way Handshake** (Connection Establishment):
1. Client → Server: SYN (with ISN)
2. Server → Client: SYN/ACK
3. Client → Server: ACK
- Takes 2 RTTs minimum

**4-Way Handshake** (Connection Termination):
1. A → B: FIN
2. B → A: ACK
3. B → A: FIN
4. A → B: ACK
- Why 4-way? TCP is bi-directional; one side may still have data to send

#### Error Control & Reliability

**ACKs (Acknowledgments)**:
- Cumulative: ACK n acknowledges all bytes up to n-1
- Should be delayed: every 2 segments or 500ms (200ms Windows)
- **Duplicate ACKs (DupACKs)**: Sent when receiver sees gap; sender retransmits after 3 DupACKs

**Retransmission Timeout (RTO)**:
- Based on RTT calculation (RFC 6298)
- RTO > 1 second minimum
- When expires: retransmit packet, cwnd=1

**Sequence Numbers**:
- Enable in-order delivery and detection of duplicates
- ISN exchanged during handshake
- Incremented by number of bytes sent

#### Flow Control

**Purpose**: Prevent sender from overwhelming receiver's buffer

**Mechanism**: Sliding window based on receiver advertised window (rwnd)
- Receiver tells sender how much buffer space available
- Sender limits sending based on rwnd

#### Congestion Control

**Purpose**: Adapt to available network capacity, prevent network congestion

**Congestion Window (cwnd)**: Number of bytes sender can inject before expecting ACK
- **Effective window**: min(cwnd, rwnd)

**Initial Window (IW)**: ~3 packets (pre-2013) or 10 packets (post-2013, Linux 2.6.39+)

**Slow Start (SS)**:
- Exponential growth: cwnd = cwnd + 1 for each ACK
- Doubles every RTT
- Continues until SSThresh reached

**Congestion Avoidance (CA)**:
- Linear growth (AIMD): cwnd = cwnd + 1/cwnd per ACK (~1 packet per RTT)
- **Additive Increase, Multiplicative Decrease**

**Loss Recovery**:
- **On 3 DupACKs**:
  - Fast Retransmit: Retransmit lost packet immediately
  - Fast Recovery: SSThresh = cwnd/2, cwnd = SSThresh (skip slow start)
- **On RTO**: SSThresh = cwnd/2, cwnd = 1 (restart from slow start)

**Multiplicative Decrease Factor (beta)**:
- Standard TCP: β = 0.5 (RFC 6582)
- TCP Cubic (Linux default): β = 0.7 (RFC 8312)

---

### Other Transport Protocols

**Stream Control Transmission Protocol (SCTP)** (RFC 4960):
- Message-oriented, reliable, connection-oriented
- **Multi-streaming**: Multiple independent streams in one association
- **Multi-homing**: Multiple IP addresses per endpoint
- **Partial reliability**: Optional (RFC 3758)
- **Unordered reliable delivery**
- 4-way handshake (cookie exchange) - resistant to SYN flood attacks

**Datagram Congestion Control Protocol (DCCP)** (RFC 4340):
- Message-oriented, unreliable, unordered
- **With congestion control** (negotiable mechanisms)
- Reliable connection setup/teardown
- Use case: Interactive multimedia, gaming
- Formula: DCCP = UDP + congestion control = TCP - byte-stream - full reliability

**Quick UDP Internet Connections (QUIC)** (IETF draft):
- Developed by Google (2012), rapidly deployed
- Runs over UDP (encrypted with TLS 1.3)
- **0-RTT connection establishment** (with cookies)
- **Multiplexed streams** (solves TCP head-of-line blocking)
- Userland implementation (faster evolution)
- By 2018: 7.8% of total Internet traffic
- Formula: QUIC = TCP improvements over UDP

---

### Transport Layer over Wireless Networks

#### Challenges

**1. Lossy Medium**:
- Frame collisions (shared medium, CSMA/CA)
- Environmental noise → high BER → frame loss
- MAC-level retries (4-7 times in 802.11) mask most losses
- Multi-rate retry chains affect RTT

**2. Ambiguous Loss Signals**:
- TCP cannot distinguish: wireless noise vs. network congestion
- Both cause packet loss
- **Problem**: Unnecessary cwnd reduction on wireless-induced loss
- **Impact**: Sub-optimal utilization, especially on high-latency wireless links

**3. Dynamic Characteristics**:
- **Variable RTT**: Tens of ms (wired CDN) to hundreds of ms or seconds (poor Wi-Fi)
- **Dynamic topology**: Movement, node density, obstacles
- **Channel conditions**: Noise, interference, contention

**4. Generally Lower Bandwidth** (historically):
- 802.11g: 54 Mbps | 802.11n: ~300 Mbps | 802.11ac: ~1.5 Gbps | 802.11ax: several Gbps
- 4G: 1 Gbps | 5G: 20 Gbps

**5. Power Constraints**:
- Battery life concerns (4G/WiFi on phones)
- Losses/retransmissions costly
- IoT devices (LoRaWAN, BLE, Zigbee) are resource-constrained
  - Run lightweight protocols (uTCP/uIP) or proprietary protocols
  - Very small/sporadic packets (cwnd=1)

**6. High-Latency Links**:
- **GEO SATCOM**: RTT ~650ms (speed of light delay)
- TCP feedback loop too slow
- Slow cwnd growth, costly retransmissions
- HTTP request process over SATCOM: 4RTT + DNS ≈ 2.6 seconds

#### Impact on TCP Performance

**Rate Adaptation Impact**:
- Many MAC retries with low MCS (bit-rates) increases perceived RTT
- Slows TCP cwnd growth rate
- Can trigger transport-layer loss (3 DupACKs/timeout)

**Packet Loss Recovery**:
- Harder on high-latency paths
- Each retransmission costs full RTT

---

### Solutions for Transport over Wireless

**1. Explicit Congestion Notification (ECN)** (RFC 3168):
- Network explicitly signals congestion (instead of implicit loss signal)
- **ECN bits in IP header**: 00 (not ECN-capable), 10 (ECT(0)), 11 (CE - congestion experienced), 01 (ECT(1))
- **ECN bits in TCP header**: CWR, ECE
- **Process**:
  1. Negotiate ECN during connection establishment (SYN: CWR+ECE)
  2. Router CE-marks packet if congested
  3. Receiver echoes CE-mark using ECE flag
  4. Sender reduces rate, sets CWR flag
  5. Receiver stops echoing ECN upon seeing CWR

**2. Active Queue Management (AQM)**:
- Drop/mark packets before buffer is full
- Signals congestion early
- **Random Early Detection (RED)**: Too complex, not widely deployed
- **Modern AQMs** (for bufferbloat):
  - **FQ_CoDel** (2012): Flow queuing + Controlled Delay
  - **PIE** (2013): Proportional Integral controller Enhanced
  - **Adaptive RED (ARED)** (2001)
- ECN-capable routers should use ECN-supporting AQM for marking

**3. Better Congestion Control Algorithms**:

**Loss-based** (standard TCP):
- React to packet loss
- Problem: Wireless loss ≠ congestion
- Examples: TCP Reno, TCP Cubic

**Delay-based**:
- Observe RTT/OWD trends
- Examples: TCP Vegas, FAST TCP, TCP-Africa, CTCP, CAIA Delay Gradient (CDG)
- **Problems**:
  - Need to predict base-RTT
  - Unfairness with loss-based TCP

**Model-based**:
- Actively measure available capacity
- Example: **Google BBR**
- Tries to stay around measured capacity

**4. Better Transport Protocols**:
- Message-based instead of byte-stream (QUIC, SCTP, DCCP)
- Challenge: Can't pick protocol based on one path segment
- Apps tied to specific transport semantics
- **Good news**: World moving towards QUIC

**5. TCP Splitting with Performance Enhancing Proxy (PEP)**:
- Used for SATCOM links
- Splits TCP connection at satellite gateway
- Speeds up connection setup and cwnd growth
- **Challenge**: QUIC's encrypted headers prevent traditional TCP splitting
  - Future: QUIC proxy or exposing some QUIC headers

**6. Cross-Layer Optimization**:
- Inform transport layer about wireless link presence
- Adjust parameters based on link conditions

---

### Key Formulas & Values

**TCP Congestion Control**:
- Slow Start: cwnd = cwnd + 1 (per ACK) → doubles per RTT
- Congestion Avoidance: cwnd = cwnd + 1/cwnd (per ACK) → +1 packet per RTT
- Multiplicative Decrease: β_standard = 0.5, β_cubic = 0.7

**Initial Window (IW)**:
- Legacy: 3 packets (~4.5 KB)
- Modern (2013+): 10 packets (~15 KB)

**ACK Delay**:
- Every 2 segments or 500ms (RFC 1122)
- Windows: 200ms

**Port Ranges**:
- Well-known: 0-1023
- Registered: 1024-49151
- Dynamic: 49152-65535

**RTT Examples**:
- Wired CDN: 10-50ms
- Good Wi-Fi: 20-100ms
- Poor Wi-Fi: 200-2000ms
- GEO SATCOM: ~650ms

---

### Exam-Critical Comparison Table

| Feature | TCP | UDP | QUIC |
|---------|-----|-----|------|
| Connection | Connection-oriented | Connectionless | Connection-oriented |
| Reliability | Reliable | Unreliable | Reliable |
| Ordering | In-order | Unordered | In-order per stream |
| Data Type | Byte-stream | Message | Byte-stream |
| Flow Control | Yes | No | Yes |
| Congestion Control | Yes | No | Yes |
| Streams | Single | N/A | Multiple |
| Handshake | 3-way (2 RTT) | None | 0-RTT (with cookies) |
| Header Overhead | 20-60 bytes | 8 bytes | Variable (encrypted) |
| Encryption | No (use TLS) | No | Built-in (TLS 1.3) |
| Use Cases | Web, Email, FTP | Streaming, DNS, VoIP | Web (HTTP/3) |

---

### Common Exam Question Topics

1. **Explain why TCP is not suitable for wireless networks** (3 reasons):
   - Cannot distinguish wireless loss from congestion → unnecessary rate reduction
   - High/variable RTT slows cwnd growth
   - Costly retransmissions on high-latency/lossy links

2. **TCP mechanisms**: 3-way handshake, sliding window, slow start vs congestion avoidance, fast retransmit/recovery

3. **Transport solutions for wireless**: ECN+AQM, delay-based CC, QUIC, TCP splitting (PEP)

4. **TCP vs UDP differences**: See comparison table above

5. **Acknowledgment schemes**: Positive ACK (cumulative), Duplicate ACK, Selective ACK (SACK)

6. **ECN operation**: Negotiation, CE-marking, ECE echoing, CWR response

7. **QUIC advantages**: 0-RTT, multiplexing (no HOL blocking), encrypted, userland, rapidly deployable

8. **Port numbers**: Well-known examples (80, 443, 53, 22, 25)

9. **5-tuple**: Source IP/Port, Dest IP/Port, Protocol

10. **Congestion window evolution**: Slow start (exponential) → Congestion avoidance (linear) → Loss recovery (multiplicative decrease)

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
