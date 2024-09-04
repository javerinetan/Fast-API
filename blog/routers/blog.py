from fastapi import APIRouter, Depends, FastAPI, Depends, status, Response, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session, Relationship
from typing import List
from passlib.context import CryptContext
from ..hashing import Hash
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db : Session = Depends(get_db)):
    return blog.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db : Session = Depends(get_db)):
    return blog.delete(id,db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def updated(id: int, request: schemas.Blog, db: Session = Depends(get_db), synchronize_session=False):
    return blog.update(id, request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, response: Response, db:Session = Depends(get_db)):
    return blog.show(id, db)