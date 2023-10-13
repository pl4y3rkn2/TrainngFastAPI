from fastapi import APIRouter, Body, Path, status, HTTPException
from models import persondb
from models.product import Product
from models.persondb import Item
from models.sql import SessionLocal

products = APIRouter()

db = SessionLocal()
  
@products.post(
    path="/product/new", 
    response_model=Product,
    status_code=status.HTTP_201_CREATED, 
    tags=["Products"],
    deprecated=False
    )
async def create_product(product: Product = Body(...)): 
    new_product = persondb.Item(
                name = product.name,
                price = product.price,
                )
    db.add(new_product)
    db.commit()

    return product

@products.get(
    path="/product/detail",
    tags=["Products"],
    deprecated=False
    )
async def show_product():
    item = db.query(Item).all()
    print(item)
    for items in item:
        items 
    return item

@products.get(
    path="/product/detail/{product_id}",
    tags=["Products"],
    deprecated=False
    )
async def show_product(
    product_id: int = Path(
        ..., 
        gt=0,
        example=123
        )
    ):
    item = db.query(Item).filter(Item.id==product_id).all()
    
    for items in item:
        items
    if items:
        if product_id != items.id:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This product doesn't exist!"
            )
        else:
            return {items,}
    else:
        item=0
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This product doesn't exist!"
            )

@products.put(
    path="/product/{product_id}",
    tags=["Products"],
    deprecated=False
    )
async def update_product(
    product_id: int = Path(
        ...,
        title="Product ID",
        description="This is the product ID",
        gt=0,
        example=123
    ),
    product: Product = Body(...),
    
    ): 
    items = db.query(Item).filter(Item.id == product_id).update(
                {
                Item.name: product.name,
                Item.price: product.price
                }
    )
    db.commit()
    return product

@products.delete(
    path="/product/delete/{product_id}",
    tags=["Products"],
    deprecated=False
    )
async def delete_product(
    product_id: int = Path(
        ...,
        title="Product ID",
        description="This is the product ID to be delete",
        gt=0,
        example=123
    )   
    ): 
    item = db.query(Item).filter(Item.id == product_id).delete()
    db.commit()

    return {product_id: "It ID is Delete"}