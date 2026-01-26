Requirements:
1) Million of users
2) low latency
3) O(1) per request

Approach: sliding window logic
For each user: Store timestamps of request
on new Request:
1) Remove timeStamps older than 10 seconds
2) if count < 5 allow
3) else deny

Time complexity : O(1)
High Level thinking : SlidingWindow, hashmap, deque, time


Askable question : 
1) What if multiple servers,  ans = store data in redis
2) what about memory growth, ans = cleanup idle users
3) what about high precision, ans = token bucket
4) what if we want per-IP + per-user limits ??, ans = use composite key


