from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class GuestHouses(Base):
    __tablename__ = 'GuestHouses'
    
    GuestHouse_id = Column(String, primary_key=True, index=True)
    Name = Column(String)
    Region = Column(String)
    City = Column(String)
    Address = Column(String)
    Description = Column(String)
    Phone = Column(String)
    EcoCertification = Column(Boolean)
    PricePerNight = Column(Integer)

    # Establishing a one-to-many relationship with Activities
    activities = relationship("Activities", back_populates="guest_house")

class Activities(Base):
    __tablename__ = "activities"

    Activity_id = Column(String, primary_key=True, index=True)
    GuestHouse_id = Column(String,ForeignKey('GuestHouses.GuestHouse_id'), index=True)
    Name = Column(String, nullable=False)
    Description = Column(String, nullable=True)
    Type = Column(String, nullable=False)
    Region = Column(String, nullable=False)
    City = Column(String, nullable=False)
    Price = Column(Integer, nullable=True)


    # Establishing the relationship back to GuestHouses
    guest_house = relationship("GuestHouses", back_populates="activities")