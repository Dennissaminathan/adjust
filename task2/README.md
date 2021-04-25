# Adjust - Home task2
## Monitoring flow for SSL offloading server and proxies

### Environment Assumption
- node exporter is used to collect metrics from the server
- Promethoues time series data is used for monitoring.
- Other solutions like Nagios or ELK also can be used.

### Solution
- Below table explains the metrics should be collected for the seerver which is handling SSH offloading process.


Key_metrics | Description | Why? |
--- | --- | --- 
CPU Stats | Time CPU spent | SSL Offloading is cpu sensitive process so its important to monitor CPU metrics (user,system,io) 
 | Disk Stats | Disk I/O metrics from /proc/diskstats | To measure DISK IO of the server while performing Encrytion / Decryption 
FileSystem | Exposes filesystem statistics, such as disk space used. | To track the disk space of the server from different partitions
loadavg | System’s workload for last 15 minutes./proc/loadavg | Load averages can be useful for a quick and dirty idea if a machine has gotten busier (for some definition of busier) recently
netstat | Network statistics from /proc/net/netstat | Get key network metrics from SSL-offloading server 
meminfo | Exposes the memory stat | Memory related metrics of server to identify memory issues 
filefd | Exposes metrics of file descriptor. Exposes file descriptor statistics from /proc/sys/fs/file-nr. | To check number of FD of the server 

- Below table explains the metrics should be collected for the seerver which is proxy requestes.

Key_metrics | Description | Why? |
--- | --- | --- 
Inbound Traffic | The number of bytes sent from external endpoints to configured backends through the SSL-Offloading Server (in bytes per sec). | To understand inbound traffic rate 
 | Outbound Traffic | The number of bytes sent from configured backends to external endpoints through the SSL-Offloading Server (in bytes per sec). | To understand outbound traffic rate 
Open Connections |The number of connections open at the given sample moment. | To track TCP Open Connections
New Connections Per Second | The number of connections that were created (client successfully connected to backend) | To track the rate of newly added connection to open connection
Closed Connections per second | The number of connections that were closed. | To track TCP Closed Connections
RTT | RTT measured for each connection between client and SSL-Offloading Server | To track RTT

#### Key metrics for alerts on SSL Offloading Server :
- CPU load (SSL-Offloading is CPU sensitive process)
- Increase in file descriptor (Slower responses and higher wait time will cause high FD’s on server)
- TCP Open Connections (TCP Connections open (Internet<->Proxy<->Backend) )
- SSL Certificate Expiry on Proxy Server
- Memory Free (Free memory on the server)
- SSL-Offloading Proxy Server Process Aliveness (With Nagios )

#### Challenges of SSL-Offloading Proxy Server Monitoring :
- Compatibility metrics for clients: In some cases, the application is not compatible at all with SSL offloading. How to differentiate those clients ?
- HTTPS -> HTTP decryption inspection : HTTP inspection (When encrypted request decrypted by SSL-Offloading server) is difficult to choose (for which http requests)?. Hackers are using the SSL/TLS protocols as a tool to obfuscate their attack payloads. A security device may be able to identify a cross-site scripting or SQL injection attack in plaintext, but if the same attack is encrypted using SSL/TLS, the attack will go through unless it has been decrypted first for inspection.
- Key Sizes of Requests : As key sizes increases SSL processing will be CPU intensive. How to measure Key sizes ?
- Internet Facing Firewall Monitoring : Catch Security Threats, DDoS attacks , Spoofing
- Monitoring of Monitoring and HA of monitoring itself : Its always a challenge.


