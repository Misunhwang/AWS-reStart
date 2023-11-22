from typing import Optional, List

# One line of FastAPI imports here later &#x1f448;
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import FastAPI, HTTPException


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/heroes/")
def create_hero(hero: Hero):
    with Session(engine) as session:
        session.add(hero)
        session.commit()


# DTO
class HeroUpdate(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None


@app.patch("/heroes/", response_model=Hero)
def change_secret_name(heroUpdate: HeroUpdate):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == heroUpdate.name)
        db_hero = session.exec(statement).first()

        if not db_hero:
            raise HTTPException(status_code=404, detail="Hero not found")

        hero_data = heroUpdate.dict(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(db_hero, key, value)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return db_hero


@app.get("/heroes/{name}", response_model=Hero)
def get_hero(name: str):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == name)
        # statement = select(Hero).where(Hero.name)

        hero = session.exec(statement).first()  # return only one record
        if not hero:
            raise HTTPException(status_code=404, detail="Hero not found")
        print(hero)
        return hero


@app.get("/heroes/", response_model=List[Hero])
def get_heroes():
    with Session(engine) as session:
        statement = select(Hero)

        heroes = session.exec(statement).all()  # return list of all records
        print(heroes)
        return heroes
