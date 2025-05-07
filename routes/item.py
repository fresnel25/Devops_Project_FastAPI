from fastapi import APIRouter
from schemas.index import Item
from config.db import con
from models.index import items

itemRouter = APIRouter()


# Get all items
@itemRouter.get("/api/getallitems")
async def index():
    data = con.execute(items.select()).fetchall()
    result = [dict(row._mapping) for row in data]
    return {"success": True, "data": result}


# Get single item by ID
@itemRouter.get("/api/getitem/{id}")
async def get_item(id: int):
    result = con.execute(items.select().where(items.c.id == id)).fetchone()
    if result:
        return {"success": True, "data": dict(result._mapping)}
    else:
        return {"success": False, "message": "Item not found"}


# Create a new item
@itemRouter.post("/api/createitem")
async def store(item: Item):
    result = con.execute(
        items.insert().values(
            name=item.name,
            price=item.price,
            quantity=item.quantity,
            in_stock=item.in_stock,
        )
    )
    con.commit()
    if result.rowcount > 0:
        return {"success": True, "message": "Item stored successfully"}
    else:
        return {"success": False, "message": "Problem storing item"}


# Update item
@itemRouter.put("/api/edititem/{id}")
async def edit_data(id: int, item: Item):
    result = con.execute(
        items.update()
        .values(
            name=item.name,
            price=item.price,
            quantity=item.quantity,
            in_stock=item.in_stock,
        )
        .where(items.c.id == id)
    )
    con.commit()
    if result.rowcount > 0:
        return {"success": True, "message": "Item updated successfully"}
    else:
        return {"success": False, "message": "Item not found or update failed"}


# Delete item
@itemRouter.delete("/api/deleteitem/{id}")
async def delete_data(id: int):
    result = con.execute(items.delete().where(items.c.id == id))
    con.commit()
    if result.rowcount > 0:
        return {"success": True, "message": "Item deleted successfully"}
    else:
        return {"success": False, "message": "Item not found or delete failed"}
