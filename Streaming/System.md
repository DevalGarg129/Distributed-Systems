# Ques 1: Design a system like JioHotstar for live cricket streaming.
Ans: https://www.youtube.com/watch?v=wUenT-azY6Q&start=24

copy this link and paste on yt answer you will be getting there

# Functional:
Live video streaming 🏏
Millions of concurrent users (1M–10M+)
Multiple video qualities (240p–1080p)
Minimal buffering
Real-time score updates

# Non-Functional:
High scalability 📈
Low latency (few seconds delay)
Fault tolerance 💥
High availability (99.99%)


# Assume:

5M concurrent users
Each user ~2 Mbps

👉 Total bandwidth:

5M × 2 Mbps = 10 Tbps 😳

👉 Conclusion:

Single server impossible ❌
Need distributed system ✅