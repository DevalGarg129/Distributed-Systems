# Load Balancer 
The ones who distributes the traffic during heavy spiking of the request over multiple server
Example: Nginx, AWS ELB

1 Million -> 100 Servers
Each Server -> 10,000 users

# Types of Load Balancer
1) Based on Deployment: 

# --- Hardware: It is the dedicated physical device used in large centers to distribute traffice across multiple server

Example: Enterprise data centers often use hardware appliances from companies like F5 networks to manage heavy traffic.

# --- Software : These Runs as an Application on the server and distributed traffic among backend servers.

Example: Nginx, HAProxy

# --- Cloud : It is a managed service provided by Cloud platforms to automatically distribute incoming traffic across cloud servers.

Example: AWS Elastic Load Balancing

2) Based on OSI Model:

# --- Layer 4(Transport Layer): Operates at transpor layer of the OSI Model and distributes traffic based on network information such as IP Addresses and TCP/UDP Port Numbers.

Example: Layer 4 Load Balancer forwards incoming TCP requests to different servers based on destination port and IP Address

# --- Layer 7(Application Layer): Operates at Application layer and distributes traffic based on Application level information such as HTTP headers, URLs and Cookies

Example: Layer 7 Load Balancer can route request to one server and api requests to another server using nginx.