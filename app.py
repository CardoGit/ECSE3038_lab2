from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

data = []

class Person(BaseModel):
    name: str
    occupation: str
    address: str

#POST request handler to add a new person 
@app.post("/person")
async def add_person(person: Person):
    if not person.name or not person.occupation or not person.address:
        return {"success": False, "result": {"error_message": "invalid request"}}
    
    new_entry = {
        "name": person.name,
        "occupation": person.occupation,
        "address": person.address
    }
    data.append(new_entry)

    return {"success": True, "result": new_entry}

#GET request handler to return all stored people
@app.get("/person")
async def get_people():
    return data

