#FastAPI
from fastapi import Cookie, FastAPI, Header, status
from pydantic import EmailStr

#Routes
from router.products import products
from router.persons import persons

app = FastAPI()

@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"],
    deprecated=True #<--- para desavilitar False se pude ver / True no se puede ver
    )
def home(): 
    return {"Hello": "World"}

app.include_router(persons)
app.include_router(products)
