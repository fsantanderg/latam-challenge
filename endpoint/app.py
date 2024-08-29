from fastapi import FastAPI, HTTPException
import asyncpg

app = FastAPI()

DATABASE_URL = "postgresql://latam_user:latam_password@localhost/latam"

# Conectar a la base de datos
async def get_db_pool():
    return await asyncpg.create_pool(DATABASE_URL)

@app.get("/data/{item_id}")
async def read_data(item_id: int):
    pool = await get_db_pool()
    async with pool.acquire() as connection:
        row = await connection.fetchrow("SELECT * FROM ingresar_datos WHERE id = $1", item_id)
        if row:
            return {"id": row["id"], "datos": row["datos"]}
        else:
            raise HTTPException(status_code=404, detail="Item not found")

