from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models
from sqlalchemy.orm import Session 
from ..hashing import Hash
from datetime import timedelta
from ..routers import token



router = APIRouter(
    prefix='/login',
    tags=['Authentication']
)

@router.post('/')
def login(requests: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == requests.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    
    if not Hash.verify(user.password, requests.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password ") 
    
    #generate a jwk token and return 
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {'access_token': access_token, 'token_type': 'bearer'}