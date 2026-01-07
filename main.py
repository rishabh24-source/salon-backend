from fastapi import FastAPI
from datetime import datetime, timedelta

app = FastAPI(title="Salon Queue Product API")

@app.get("/")
def root():
    return {"status": "Backend running 🚀"}

@app.get("/predict-wait-time")
def predict_wait_time(
    queue_length: int,
    avg_service_time: int,
    active_staff: int
):
    if active_staff <= 0:
        return {"error": "No active staff available"}

    # Core logic
    estimated_wait = (queue_length * avg_service_time) / active_staff
    buffer_time = 3  # minutes
    final_wait = round(estimated_wait + buffer_time)

    # Best arrival time
    now = datetime.now()
    best_arrival = now + timedelta(minutes=final_wait)

    # Confidence logic
    if active_staff >= 3 and queue_length <= 5:
        confidence = "HIGH"
    elif active_staff >= 2 and queue_length <= 8:
        confidence = "MEDIUM"
    else:
        confidence = "LOW"

    return {
        "current_time": now.strftime("%H:%M"),
        "estimated_wait_minutes": final_wait,
        "best_arrival_time": best_arrival.strftime("%H:%M"),
        "confidence": confidence
    }
@app.get("/queue-status")
def queue_status(user_id: int = 1):
    """
    Temporary demo logic:
    position decreases over time to simulate real queue movement.
    """

    from datetime import datetime

    # Fake but deterministic logic for demo
    minute = datetime.now().minute

    # Example: position cycles 3 -> 2 -> 1
    position = 3 - (minute % 3)
    if position < 1:
        position = 1

    return {
        "user_id": user_id,
        "position": position,
        "status": "NOW" if position == 1 else "WAITING"
    }
@app.get("/predict-wait-time")
def predict_wait_time(queue_length: int, avg_service_time: int, active_staff: int):
    wait = max(1, int((queue_length * avg_service_time) / active_staff))

    return {
        "best_arrival_time": "5:40 – 6:00 PM",
        "estimated_wait_minutes": wait,
        "confidence": "HIGH"
    }
