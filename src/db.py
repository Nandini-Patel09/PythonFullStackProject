# db_manager.py
import os
from supabase import create_client
from dotenv import load_dotenv

# load environment variables
load_dotenv()
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

supabase = create_client(url,key)

# Create Task
def create_user(first_name, last_name, email, password):
    return supabase.table("finusers").insert({
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password
    }).execute()

# Get all Users
def get_all_users():
    return supabase.table("finusers").select("*").order("first_name").execute()

# Update User Password
def update_user_password(user_id, password):
    return supabase.table("finusers").update({"password": password}).eq("user_id", user_id).execute()

#Delete user
def delete_user(user_id):
    return supabase.table("finusers").delete().eq("user_id", user_id).execute()

# Create Transaction
def create_transaction(user_id, date, type, category, amount, note):
    return supabase.table("fintransactions").insert({
        "user_id": user_id,
        "date": date,
        "type": type,
        "category": category,
        "amount": amount,
        "note": note
    }).execute()

# Get all Transactions
def get_all_transactions():
    return supabase.table("fintransactions").select("*").order("date").execute()

# Update Transaction Type
def update_transaction(transaction_id, type):
    return supabase.table("fintransactions").update({
        "type": type
    }).eq("transaction_id", transaction_id).execute()

# Delete Transaction
def delete_transaction(transaction_id):
    return supabase.table("fintransactions").delete().eq("transaction_id", transaction_id).execute()

