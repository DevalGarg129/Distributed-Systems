from flask import Flask, request, jsonify
from queue import Queue
import threading
import time

app = Flask(__name__)

#in memmory queue to hold notifications
notification_queue = Queue()

#in memory Db
notification_logs = []

#Worker Function
def worker():
    while True:
        job = notification_queue.get()

        if job is None:
            break

        print(f"Processing notification for user: {job['user_id']}")
        send_notification(job)

        notification_queue.task_done()

def send_notification(job):
    user_id = job['user_id']
    message = job['message']
    notif_type = job['type']

    time.sleep(1)
    print(f"[{notif_type}] Notification sent to user {user_id}: {message}")

    notification_logs.append({
        "user_id": user_id,
        "message": message,
        "type": notif_type,
        "status": "sent"
    })

@app.route("/notify", methods=["POST"])
def notify():
    data = request.json

    job = {
        "user_id": data.get("user_id"),
        "message": data.get("message"),
        "type": data.get("type", "push")
    }    

    notification_queue.put(job)
    return jsonify({"status": "Notification queued"}), 200

#Get logs
@app.route("/logs", methods=['GET'])
def logs():
    return jsonify(notification_logs)

def start_workers(n=2):
    for _ in range(n):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

if __name__ == "__main__":
    start_workers()
    app.run(debug=True)