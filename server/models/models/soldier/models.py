from sqlmodel import Field, SQLModel, DATE, create_engine

class Soldier(SQLModel, table=True):
    personal_number: int = Field(primary_key=True)
    firs_name: str
    last_name: str
    city_of_residence: str
    distance_base: int
    placement_mode: str


# class     