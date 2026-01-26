import time
from collections import defaultdict, deque

class RateLimiter:
    def __init__(self, limit=5, window=10):
        self.limit = limit
        self.window = window
        self.calls = defaultdict(deque)

    def allow_request(self, user_id):
        current_time = time.time()
        q = self.calls[user_id]
        while q and current_time - q[0] > self.window:
            q.popleft()
        
        if len(q) < self.limit:
            q.append(current_time)
            return True
        else:
            return False
        
r1 = RateLimiter()
for i in range(7):
    print(i, r1.allow_request("user1"))