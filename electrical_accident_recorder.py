# IoT-Based Electrical Accident Recorder
# Basic prototype for recording abnormal electrical events

from datetime import datetime
import json

def record_event(event_type, details):
    event = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "details": details
    }

    with open("electrical_events.json", "a") as file:
        file.write(json.dumps(event) + "\n")

    print("Electrical event recorded:", event)

if __name__ == "__main__":
    record_event(
        "ABNORMAL_CONDITION",
        "Sample test event - not from real hardware"
    )
record_event(
        "OVERLOAD",
        "Sample overload test - not from real hardware"
    )
