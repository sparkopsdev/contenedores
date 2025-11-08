from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from . import models, schemas, crud
from .config import settings

Base.metadata.create_all(bind=engine)

personAPI = FastAPI(
    title=settings.appName,
    debug=settings.debug
)


@personAPI.get("/person", response_model=List[schemas.PersonRead])
def list_persons(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    """
    GET /person
    List all persons in the database.
    """
    persons = crud.get_persons(db=db, skip=skip, limit=limit)
    if not persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The list is empty."
        )
    return persons


@personAPI.get("/person/{person_id}", response_model=schemas.PersonRead)
def get_person(
    person_id: int,
    db: Session = Depends(get_db),
):
    """
    GET /person/{id}
    Retrieve a specific person by ID.
    """
    person = crud.get_person(db=db, person_id=person_id)
    if not person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Person with id {person_id} not found.",
        )
    return person


@personAPI.post(
    "/person",
    response_model=schemas.PersonRead,
    status_code=status.HTTP_201_CREATED,
)
def create_person(
    person_in: schemas.PersonCreate,
    db: Session = Depends(get_db),
):
    """
    POST /person
    Create a new person.
    """
    # Check for duplicated DNI
    existing = crud.get_person_by_dni(db=db, dni=person_in.dni)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Person with DNI '{person_in.dni}' already exists",
        )

    person = crud.create_person(db=db, person_in=person_in)
    return person


@personAPI.delete(
    "/person/{person_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_person(
    person_id: int,
    db: Session = Depends(get_db),
):
    """
    DELETE /person/{id}
    Delete a person by ID.
    """
    deleted = crud.delete_person(db=db, person_id=person_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Person with id {person_id} not found",
        )
    # 204 No Content => empty response body
    return None
