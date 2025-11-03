from sqlalchemy.orm import Session
from . import models, schemas
from datetime import date

def create_user(db: Session, email: str, full_name: str=None):
    u = models.User(email=email, full_name=full_name)
    db.add(u)
    db.commit()
    db.refresh(u)
    return u

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id==user_id).first()

def get_item_by_barcode(db: Session, barcode: str, user_id: int):
    return db.query(models.Item).filter(models.Item.barcode==barcode, models.Item.user_id==user_id).first()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, user_id: int):
    return db.query(models.Item).filter(models.Item.user_id==user_id).all()

def update_item_quantity(db: Session, item_id: int, new_qty: float):
    item = db.query(models.Item).filter(models.Item.id==item_id).first()
    if item and new_qty is not None:
        item.quantity = new_qty
        db.commit()
        db.refresh(item)
    return item

def log_usage(db: Session, usage: schemas.UsageCreate):
    usage_db = models.UsageLog(item_id=usage.item_id, used_quantity=usage.used_quantity, remarks=usage.remarks)
    item = db.query(models.Item).filter(models.Item.id==usage.item_id).first()
    if item:
        item.quantity = max(0.0, item.quantity - usage.used_quantity)
    db.add(usage_db)
    db.commit()
    db.refresh(usage_db)
    return usage_db

def get_low_stock_items(db: Session, user_id: int):
    return db.query(models.Item).filter(models.Item.user_id==user_id, models.Item.quantity <= models.Item.threshold).all()

def add_to_shopping_list(db: Session, item_id: int, quantity: float = None):
    # avoid duplicates when already present and not purchased
    existing = db.query(models.ShoppingList).filter(models.ShoppingList.item_id==item_id, models.ShoppingList.is_purchased==False).first()
    if existing:
        return existing
    entry = models.ShoppingList(item_id=item_id, quantity=quantity)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

def mark_shopping_purchased(db: Session, shopping_id: int):
    entry = db.query(models.ShoppingList).filter(models.ShoppingList.id==shopping_id).first()
    if entry:
        entry.is_purchased = True
        db.commit()
        db.refresh(entry)
    return entry

def get_expiring_items(db: Session, user_id: int, days: int = 3):
    from datetime import date, timedelta
    cutoff = date.today() + timedelta(days=days)
    return db.query(models.Item).filter(models.Item.user_id==user_id, models.Item.expiry_date != None, models.Item.expiry_date <= cutoff).all()
