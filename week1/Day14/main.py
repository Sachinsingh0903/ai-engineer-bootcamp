from fastapi import FastAPI, Depends

app = FastAPI()

def get_app_name():
    return "AI Engineer Bootcamp"

@app.get("/")
def home(
    app_name: str = Depends(get_app_name)
):
    return {
        "application": app_name
    }

def current_user():
    return {
        "name": "Sakshi",
        "role": "CSE"
    }

@app.get("/profile")
def profile(
    user: dict = Depends(current_user)
):
    return user

class MessageService:
    def get_message(self):
        return "Learning dependency injection"

def get_message_Service():
    return MessageService()

@app.get("/message")
def message(
    service: MessageService = Depends(get_message_Service)
):
    return {
        "message": service.get_message()
    }