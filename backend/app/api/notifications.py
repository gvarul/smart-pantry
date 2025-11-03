from fastapi import APIRouter
from ..utils import send_email, send_fcm_notification
from ..config import settings

router = APIRouter(prefix="/notify", tags=["notifications"])

@router.post("/email")
def notify_email(to: str, subject: str, message: str):
    send_email(to, subject, message)
    return {"ok": True}

@router.post("/fcm")
def notify_fcm(token: str, title: str, body: str):
    send_fcm_notification(settings.FCM_SERVER_KEY, token, title, body)
    return {"ok": True}
