from apscheduler.schedulers.background import BackgroundScheduler
from .database import SessionLocal
from .crud import get_expiring_items, get_low_stock_items, add_to_shopping_list
from .utils import send_email
from .config import settings

def check_items_job():
    db = SessionLocal()
    try:
        users = db.query.__class__  # placeholder to avoid lint; we'll query users via ORM
        users = db.execute("SELECT id, email FROM users").fetchall()
        for u in users:
            user_id = u[0]
            email = u[1]
            expiring = get_expiring_items(db, user_id, days=3)
            if expiring:
                html = "<p>The following items are expiring soon:</p><ul>" + "".join([f"<li>{it.name} — {it.expiry_date}</li>" for it in expiring]) + "</ul>"
                send_email(email, "Items expiring soon", html)
            low = get_low_stock_items(db, user_id)
            for it in low:
                add_to_shopping_list(db, it.id, quantity=it.threshold)
                send_email(email, "Low stock item added to shopping list", f"<p>{it.name} is low in stock. It was added to your shopping list.</p>")
    except Exception as e:
        print("Error in scheduled job:", e)
    finally:
        db.close()

def start_scheduler():
    sched = BackgroundScheduler()
    sched.add_job(check_items_job, 'interval', minutes=settings.CHECK_INTERVAL_MINUTES)
    sched.start()
    print("Scheduler started")
