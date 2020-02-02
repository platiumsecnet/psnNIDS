EAGLE_EYE IDS
---

# Advantages
1. Detect Advanced Network Threats: Surface even the most advanced threats in real time with application recognition, customizable Deep Packet Analytics, and multidimensional network traffic and behavioral analytics <br>
- Detect even the most sophisticated threats across a broad set of IT environment-generated log and audit data, endpoint activity, and Layer 7 application flow
- Recognize data exfiltration, spear phishing, botnet beaconing, inappropriate network usage, lateral movement, and suspicious file transfers
- Corroborate high-risk events at the network or application level with environmental activity from your SIEM
2. Take the Guesswork out of Incident Response: Enable your incident response team to work effectively and efficiently with unstructured search, session playback, and file reconstruction.<br>
- Determine the scope of the incident and understand exactly which systems have been compromised
- Generate irrefutable network-based evidence
- Reconstruct files transferred across the network to investigate suspicious data exfiltration, malware infiltration, and unauthorized data access

# Features
1. True Application Identification: Automatically identify over 3,000 applications to expedite network forensics with advanced classification methods and deep packet inspection.
2. SmartFlow™ Session Classification: Recover Layer 7 application details and packet data for all sessions.
3. Deep Packet Analytics (DPA): Automate threat detection by correlating against full packet payload and SmartFlow data using out-of-the-box rules and customizable scripts.
4. Full Packet Capture: See every bit that crosses your network with Layer 2–7 packet capture stored in industry-standard PCAP format.
5. SmartCapture™: Automatically capture sessions based on application or packet content to preserve the information you need.
Unstructured Search: Drill down to critical packet and flow data with our Elasticsearch backend to streamline your investigation.
6. File Reconstruction: Reconstruct email file attachments to support malware analysis and data loss monitoring.
7. Alerts & Dashboards: Surface continuous, automated analysis on saved searches through customizable analyst dashboards.
8. API Integration: Provide third-party tools access to session-based packet captures and reconstructed files.

# Supported Data Types
1. Alert Data: HIDS alerts from Wazuh and NIDS alerts from Snort/Suricata
2. Asset Data: Asset Data from Bro
3. Full content data: Full packet capture from netsniff-ng
4. Host data: Host data via Beats, Wazuh, syslog, and more
5. Session data: Session data from Bro
6. Transaction data: http/ftp/dns/ssl/other logs from Bro

# Screenshots

# Hardware Requirements

# Datasheet

# Use cases
1. Surface data exfiltration activities: Identify long-running sessions, “low and slow” sessions hidden in normal traffic, anomalous outbound network sessions, and other activities indicative of data exfiltration.
2. Discover operational anomalies: Verify that you aren’t seeing protocols or traffic that you think you’ve blocked or traffic between systems that should be isolated from each other.
3. Find hiding security threats: Catch security threats hiding in low-level chatty protocol like DNS, SNMP, or Kerberos.
4. Detect botnets and beaconing: Identify traffic using anomalous ports. View malformed packet headers. Recognize command and control callbacks.
5. Expose nuisance apps and bandwidth hogs: Discover when apps that are against corporate policy are being used. Find out who or what is taking up the most bandwidth.
6. See where your network traffic is going: Identify outbound IP and URL destinations and classify traffic by ingress, egress or lateral motion in your network.

# Competitors
_*OpenSource*_
1. Suricata
2. https://logrhythm.com/products/logrhythm-netmon-freemium/

_*Commercial*_
1. SecurityOnion
2. Waterfall IDS: https://waterfall-security.com/waterfall-for-ids/
3. NIKSUN NetDetector: https://www.niksun.com/product.php?id=112
4. Bro IDS/Zeek

# Refs
1. https://gallery.logrhythm.com/data-sheets/logrhythm-netmon-data-sheet.pdf
2. http://doc.haka-security.org/haka/release/v0.3.0/doc/developer/arch.html
3. 

