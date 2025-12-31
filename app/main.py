from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="My API")

# הגדרת CORS (אופציונלי)
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

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/healt")
async def health_check():
    return {"status": "healt"}

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "name": f"User {user_id}"}
