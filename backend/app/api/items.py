from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import crud, schemas

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=schemas.ItemOut)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    if item.barcode:
        existing = crud.get_item_by_barcode(db, item.barcode, item.user_id)
        if existing:
            raise HTTPException(status_code=400, detail="Item with barcode already exists")
    return crud.create_item(db, item)

@router.get("/user/{user_id}", response_model=list[schemas.ItemOut])
def list_items(user_id: int, db: Session = Depends(get_db)):
    return crud.get_items(db, user_id)

@router.patch("/{item_id}/quantity", response_model=schemas.ItemOut)
def update_quantity(item_id: int, qty: float, db: Session = Depends(get_db)):
    item = crud.update_item_quantity(db, item_id, qty)
    if not item:
        raise HTTPException(404, "Item not found")
    return item
