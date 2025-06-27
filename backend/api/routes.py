from fastapi import APIRouter, Request, HTTPException
from backend.auth.jwt_auth import create_access_token, verify_token
from backend.models.site import create_site, list_sites
import os, uuid

router = APIRouter(prefix="/api")

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

@router.get("/health")
async def health_check():
    return {"status": "ok", "detail": "API running smoothly"}

@router.post("/admin/login")
async def admin_login(req: Request):
    data = await req.json()
    if data.get("email") == ADMIN_EMAIL and data.get("password") == ADMIN_PASSWORD:
        token = create_access_token({"sub": ADMIN_EMAIL})
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.post("/admin/sites")
async def add_site(req: Request):
    token = req.headers.get("Authorization")
    user = verify_token(token.replace("Bearer ", "")) if token else None
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    data = await req.json()
    site_id = uuid.uuid4().hex[:8]
    await create_site(site_id, data.get("name"))
    return {
        "site_id": site_id,
        "script": f'<script defer src="https://analytics.edge21marketing.com/tracker.js" data-site-id="{site_id}"></script>'
    }

@router.get("/admin/sites")
async def sites_list(req: Request):
    token = req.headers.get("Authorization")
    user = verify_token(token.replace("Bearer ", "")) if token else None
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await list_sites()
