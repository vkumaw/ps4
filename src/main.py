from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Creator Optimization System Running"}

@app.get("/get_recommendation")
def get_recommendation():

    return {
        "content_id": 1,
        "platform": "Instagram",
        "time_slot": 20,
        "decision": "SCHEDULE"
    }