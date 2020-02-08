


# 1. High Speed Traffic recording
- Lossless capture 10Gbps traffic and store in industry-standard PCAP format.
- Unlimited size of captured file (capture as much as the storage solution can hold)
- Automatically purging out-of-date captured files when the disk reaches threshold usage

# 2. Offline analysis of PCAP files

# 3. Detect well-known attack by rule-driven NIDS:
- Detect exactly events of known malicious, anomalous or otherwise suspicious traffic based on rich rule set which covers most of critical security cases
- Automaticaly update rules for newest security cases from trursted and experienced sources

# 4. Detect 0-day attack by analysis-driven NIDS 
- Using DPI to extract asset, session, transaction data of all activities in networks. This data will be used to reconstruct context of activities to find out 0-day attack

- Discover of over 3000 applications in home, office, industrial control network enviroments: Web services, VoIP, Instant message and chat, gaming, streaming, mobile, file transferring, remote access, industrial control protocols. 

- Automatically capture files as they pass through your network and automatically pass them to a sandbox or a file share for antivirus scanning

# 5. Powerful analysis framework
- Alert continuously and impressively of events on dashboard 
- Fastly and easily pivot from an alert to its context (pcap files, extracted files, flow and session information ...) with powerful analysis tools
- Query all captured packets to correlate traffic that may not have triggered any alerts but still could be associated with malicious or undesired activity 
- Support multi-tier architecture for analysis: allows collaboration among analysts by allowing alerts to be commented on and escalated to more senior analysts who can take action on the alerts
- Optimize the time for analyzing by a suite of convinient tools: reverse DNS and whois lookups of IP by Sguil; geo-IP mapping by Squert; visualize in charts, tables, maps by Kibana
- Support web-based interface

# 6. Operating System Support
Linux
macOS / Mac OS X
Windows

# 7. Comprehensive protocol parsers
1. Support for packet decoding of
- IPv4, IPv6, TCP, UDP, SCTP, ICMPv4, ICMPv6, GRE
- Ethernet, PPP, PPPoE, Raw, SLL, VLAN, QINQ, MPLS, ERSPAN, VXLAN
2. App layer decoding of:
- HTTP, SSL, TLS, SMB, DCERPC, SMTP, FTP, SSH, DNS, Modbus, ENIP/CIP, DNP3, NFS, NTP, DHCP, TFTP, KRB5, IKEv2, SIP, SNMP, RDP
- New protocols developed in the Rust language, for safe and fast decoding.

# 8. Multi-thread & Dominated cores for Very high-speed Processing
- Support upto 3Gbps version

# 9. IP Reputation
- loading of large amounts host based reputation data
- matching on reputation data in the rule language using the “iprep” keyword
- live reload support
- supports CIDR ranges

# 10. Tools
- Update in portal for easy rule update management

# 11. Alert/Event filtering
- per rule alert filtering and thresholding
- global alert filtering and thresholding
- per host/subnet thresholding and rate limiting settings

# 12. Outputs
- Eve log, all JSON alert and event output
- Lua output scripts for generating your own output formats
- Redis support
- HTTP request logging
- TLS handshake logging
- Unified2 output — compatible with Barnyard2
- Alert fast log
- Alert debug log — for rule writers
- Traffic recording using pcap logger
- Prelude support
- syslog — alert to syslog
- stats — engine stats at fixed intervals
- File logging including MD5 checksum in JSON format
- Extracted file storing to disk, with deduplication in the v2 format
- DNS request/reply logger, including TXT data
- Signal based Log rotation
- Flow logging
