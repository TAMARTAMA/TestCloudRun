from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import API_PREFIX, APP_NAME, VERSION, PORT,CORS_ORIGINS
from app.api.router import api_router

app = FastAPI(
    title=APP_NAME,
    version=VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello from Cloud Run!"}


app.include_router(api_router, prefix=API_PREFIX)
# @app.get("/health")
# async def health_check():
#     return {"status": "healthy"}

# @app.get("/healt")
# async def health_check():
#     return {"status": "healt"}

# @app.get("/api/users/{user_id}")
# async def get_user(user_id: int):
#     return {"user_id": user_id, "name": f"User {user_id}"}
