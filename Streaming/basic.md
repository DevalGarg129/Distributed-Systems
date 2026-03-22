# Ques 1: What challenges arise when 1M users join a live stream simultaneously?
Ans :Scaling to 1 million simultaneous viewers is an engineering "perfect storm" that hits four specific bottlenecks:

1. The "Thundering Herd" Effect
When 1M people click "Join" at once, the TCP/TLS handshake storm can crash load balancers before video even starts. If the first video segment isn't already cached on the edge server, a "cache miss" sends 1M requests back to the origin server, potentially knocking it offline.

2. Massive Bandwidth Egress
A 1080p stream at 5 Mbps for 1M users requires 5 Terabits per second (Tbps) of throughput. No single data center can handle this; it requires a massive, globally distributed Content Delivery Network (CDN) to split the traffic across thousands of edge nodes.

3. The "State" Bottleneck
Video is "stateless" (the same file goes to everyone), but Live Chat and View Counts are "stateful."

Chat: Delivering 100k messages/sec to 1M users creates billions of delivery operations.

Counters: Updating a single database row for the view count 1M times a second causes "lock contention," freezing the database.

4. The Latency Trade-off
Scaling requires "chunking" video into 2–6 second segments (HLS/DASH), which adds 30+ seconds of delay. Reducing this to "real-time" (WebRTC) is exponentially harder to scale because it requires a persistent, bi-directional connection for every single user.

# Ques 2: How to reduce the buffering during the streaming of the IPL match ?
Ans: . Reducing Buffering for a Live Match
Adaptive Bitrate (ABR): Automatically dropping video quality (e.g., 1080p to 720p) prevents the stream from stopping when your internet dips.

Edge Caching: Placing video "chunks" on servers physically close to the viewer (the "Edge") to reduce travel time for data packets.

Wired Connection: Switching from Wi-Fi to Ethernet eliminates local signal interference, which is the #1 cause of "stuttering."

# Ques 3: what happens if one server crashes during IPL streaming?
Ans 3: If an "Edge" Server Crashes (Most Common)
Edge servers are the ones closest to you that actually deliver the video segments.

The Experience: You might see a momentary buffer (1–2 seconds).

The Fix: The Load Balancer detects the crash instantly and redirects your "request" to the next nearest healthy server. Since streaming uses small chunks of video, your player simply asks a different server for the next 2-second chunk.




