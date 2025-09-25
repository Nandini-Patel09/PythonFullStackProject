# api/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys, os

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import UserManager, TransactionManager

# ------------------------------- APP Setup --------------------------------------
app = FastAPI(title="Personal Finance Tracker", version="1.0")

# ---------------- CORS Middleware -----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------- Create Manager Instances -------------------
user_manager = UserManager()
transaction_manager = TransactionManager()

# ------------------- Pydantic Models -------------------

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class UserUpdatePassword(BaseModel):
    user_id: int
    new_password: str

class TransactionCreate(BaseModel):
    user_id: int
    date: str          # "YYYY-MM-DD"
    type: str          # "income" or "expense"
    category: str
    amount: float
    note: str = ""

class TransactionUpdateType(BaseModel):
    transaction_id: int
    new_type: str   # "income" or "expense"

# ------------------- API Endpoints -------------------

@app.get("/")
def home():
    return {"message": "Personal Finance Tracker API is running"}

# ----------- User Endpoints ------------

@app.post("/users/add")
def add_user(user: UserCreate):
    result = user_manager.add_user(user.first_name, user.last_name, user.email, user.password)
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

@app.put("/users/update-password")
def update_user_password(payload: UserUpdatePassword):
    result = user_manager.update_user_password(payload.user_id, payload.new_password)
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

@app.delete("/users/delete/{user_id}")
def delete_user(user_id: int):
    result = user_manager.delete_user(user_id)
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

@app.get("/users")
def get_users():
    return user_manager.get_users()

# ----------- Transaction Endpoints ------------

@app.post("/transactions/add")
def add_transaction(tx: TransactionCreate):
    result = transaction_manager.add_transaction(
        tx.user_id, tx.date, tx.type, tx.category, tx.amount, tx.note
    )
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

@app.put("/transactions/update-type")
def update_transaction_type(payload: TransactionUpdateType):
    result = transaction_manager.update_transaction_type(payload.transaction_id, payload.new_type)
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

@app.get("/transactions")
def get_transactions(user_id: int = None):
    return transaction_manager.get_transactions(user_id)

@app.delete("/transactions/delete/{transaction_id}")
def delete_transaction(transaction_id: int):
    result = transaction_manager.delete_transaction(transaction_id)
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

# ------------------- Run with uvicorn -------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True)
