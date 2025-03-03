from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ServiceRequest(BaseModel):
    title: str
    icon: str
    description: str


services = {
    "finchat": {
        "id": 1,
        "title": "FinChat - Banking Hub",
        "icon": "https://www.finchat.com/assets/images/icons/finchat.png",
        "description":"Welcome to the FinChat Banking Hub! This is where you can find all the latest news, updates, and resources related to banking and finance. Whether you're a financial professional or just interested in learning more about the industry, you've come to the right place. Stay tuned for the latest news and insights from the world of banking and finance."
    },
    "kyc": {
        "id": 2,
        "title": "KYC Connect",
        "icon": "https://www.finchat.com/assets/images/icons/kyc.png",
        "description": "Streamline your KYC process with secure, real-time document collection and verification via WhatsApp."
    },
    "coop-pulse": {
        "id": 3,
        "title": "Co-op Pulse",
        "icon": "https://www.finchat.com/assets/images/icons/coop-pulse.png",
        "description": "Engage with cooperative bank members using interactive sessions, updates, and voting through WhatsApp."
    },
    "customer-support": {
        "id": 4,
        "title": "Customer Support Chat",
        "icon": "https://www.finchat.com/assets/images/icons/customer-support.png",
        "description": "Enhance customer experience with instant assistance for banking queries, issue resolution, and AI-powered navigation via WhatsApp."
    },
    "notify": {
        "id": 5,
        "title": "Notify",
        "icon": "https://www.finchat.com/assets/images/icons/notify.png",
        "description": "Stay informed with real-time updates, alerts, and notifications via WhatsApp."
    }
}


@app.get("/services")
def get_all_services():
    return {"services": list(services.values())}


@app.get("/{service_name}")
def get_service(service_name: str):
    service = services.get(service_name)
    if not service:
        return {"error": "Service not found"}
    return service

if __name__ == "__main__":
    import uvicorn
    