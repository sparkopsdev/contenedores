from sqlalchemy import Column, Integer, String, UniqueConstraint

from .database import Base


class Person(Base):
    """
    ORM model representing a person in the database.
    """
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String(100), nullable=False)
    lastName = Column(String(150), nullable=False)
    dni = Column(String(20), nullable=False, unique=True, index=True)
    birthProvince = Column(String(100), nullable=False)

    __table_args__ = (
        UniqueConstraint("dni", name="uq_person_dni"),
    )
