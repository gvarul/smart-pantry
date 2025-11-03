from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import crud, schemas, models

router = APIRouter(prefix="/shopping", tags=["shopping"])

@router.get("/user/{user_id}", response_model=list[schemas.ShoppingOut])
def get_shopping_for_user(user_id: int, db: Session = Depends(get_db)):
    entries = db.query(models.ShoppingList).join(models.Item).filter(models.ShoppingList.is_purchased == False, models.Item.user_id == user_id).all()
    return entries

@router.post("/mark_purchased/{shopping_id}")
def mark_purchased(shopping_id: int, db: Session = Depends(get_db)):
    entry = crud.mark_shopping_purchased(db, shopping_id)
    if not entry:
        raise HTTPException(404, "Shopping entry not found")
    return {"ok": True}
