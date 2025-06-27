import asyncpg
import os

DB_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/analytics")

async def create_site(site_id: str, name: str):
    conn = await asyncpg.connect(DB_URL)
    await conn.execute("""
        INSERT INTO sites (site_id, name, created_at)
        VALUES ($1, $2, NOW())
    """, site_id, name)
    await conn.close()

async def list_sites():
    conn = await asyncpg.connect(DB_URL)
    rows = await conn.fetch("SELECT site_id, name, created_at FROM sites ORDER BY created_at DESC")
    await conn.close()
    return [dict(row) for row in rows]
