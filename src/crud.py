from typing import List, Optional

from sqlalchemy.orm import Session

from . import models, schemas


def get_person(db: Session, person_id: int) -> Optional[models.Person]:
    """
    Retrieve a single person by primary key.
    """
    return db.query(models.Person).filter(models.Person.id == person_id).first()


def get_person_by_dni(db: Session, dni: str) -> Optional[models.Person]:
    """
    Retrieve a person by DNI.
    """
    return db.query(models.Person).filter(models.Person.dni == dni).first()


def get_persons(db: Session, skip: int = 0, limit: int = 100) -> List[models.Person]:
    """
    Retrieve a list of persons.
    """
    return db.query(models.Person).offset(skip).limit(limit).all()


def create_person(db: Session, person_in: schemas.PersonCreate) -> models.Person:
    """
    Create a new person in the database.
    """
    db_person = models.Person(
        firstName=person_in.firstName,
        lastName=person_in.lastName,
        dni=person_in.dni,
        birthProvince=person_in.birthProvince,
    )
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


def delete_person(db: Session, person_id: int) -> bool:
    """
    Delete a person by ID.

    Returns True if a person was deleted, False otherwise.
    """
    person = get_person(db, person_id)
    if not person:
        return False

    db.delete(person)
    db.commit()
    return True
