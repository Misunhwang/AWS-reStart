from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


engine = create_engine("sqlite:///database.db")

# Initialize connection
# SQLModel.metadata.create_all(engine)

"""
with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()
"""

with Session(engine) as session:
    statement = select(Hero).where(Hero.name == "Spider-Boy")

    heroes = session.exec(statement).all()  # return list of all records
    print(heroes)
    print(type(heroes))

    hero = session.exec(statement).first()  # return only one record
    print(hero)
    print(type(hero))
