from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import crud, schemas

router = APIRouter(prefix="/usage", tags=["usage"])

@router.post("/", response_model=schemas.UsageOut)
def log_usage(usage: schemas.UsageCreate, db: Session = Depends(get_db)):
    result = crud.log_usage(db, usage)
    return result
