from pydantic import BaseModel



class Activity(BaseModel):
    Activity_id: str 
    Name: str
    Description : str
    Type: str
    Region: str
    City: str
    Price: int | None = None


    class Config:
        from_attributes = True  # instead of orm_mode = True



class GuestHouse(BaseModel):
    GuestHouse_id: str | None = None
    Name: str
    Region: str
    City: str
    Address: str
    Description: str
    Phone: str
    EcoCertification: bool
    PricePerNight: int


    class Config:
        from_attributes = True
