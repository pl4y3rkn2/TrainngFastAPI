from fastapi import APIRouter, Body, Path, status, HTTPException
from models.person import Person
from models.persondb import User
from models.sql import SessionLocal

persons = APIRouter()

db = SessionLocal()

@persons.post(
    path="/person/new", 
    response_model=Person,
    status_code=status.HTTP_201_CREATED, 
    tags=["Persons"],
    deprecated=False
    )
async def create_person(person: Person = Body(...)): 
    new_user = persondb.User(
                name = person.name,
                email = person.email,
                )
    db.add(new_user)
    db.commit()

    return person

@persons.get(
    path="/person/detail",
    tags=["Persons"],
    deprecated=False
    )
async def show_person():
    person = db.query(User).all()
    for users in person:
        users 
    return person
   
@persons.get(
    path="/person/detail/{person_id}",
    tags=["Persons"],
    deprecated=False
    )
async def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        example=123
        )
    ):
    person = db.query(User).filter(User.id==person_id).all()
    
    for users in person:
        users
    if person:
        if person_id != users.id:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This persons doesn't exist!"
            )
        else:
            return {users,}
    else:
        person=0
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This persons doesn't exist!"
            )

@persons.put(
    path="/person/{person_id}",
    tags=["Persons"],
    deprecated=False
    )
async def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the Person ID",
        gt=0,
        example=123
    ),
    person: Person = Body(...),
    
    ): 
    persons = db.query(User).filter(User.id == person_id).update(
                {
                User.name: person.name,
                User.email: person.email
                }
    )
    db.commit()
    return person

@persons.delete(
    path="/person/delete/{person_id}",
    tags=["Persons"],
    deprecated=False
    )
async def delete_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID to be delete",
        gt=0,
        example=123
    )   
    ): 
    person = db.query(User).filter(User.id == person_id).delete()
    db.commit()

    return {person_id: "It ID is Delete"}