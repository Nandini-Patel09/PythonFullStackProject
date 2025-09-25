# src/db.py
import os
from supabase import create_client
from dotenv import load_dotenv

# load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

class DatabaseManager:

    # -------- Users --------
    def create_user(self, first_name, last_name, email, password):
        return supabase.table("finusers").insert({
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        }).execute()

    def get_all_users(self):
        return supabase.table("finusers").select("*").order("first_name").execute()

    def update_user_password(self, user_id, password):
        return supabase.table("finusers").update({"password": password}).eq("user_id", user_id).execute()

    def delete_user(self, user_id):
        return supabase.table("finusers").delete().eq("user_id", user_id).execute()

    # -------- Transactions --------
    def create_transaction(self, user_id, date, type, category, amount, note=""):
        return supabase.table("fintransactions").insert({
            "user_id": user_id,
            "date": date,
            "type": type,
            "category": category,
            "amount": amount,
            "note": note
        }).execute()

    def get_all_transactions(self):
        return supabase.table("fintransactions").select("*").order("date").execute()

    def update_transaction(self, transaction_id, type):
        return supabase.table("fintransactions").update({
            "type": type
        }).eq("transaction_id", transaction_id).execute()

    def delete_transaction(self, transaction_id):
        return supabase.table("fintransactions").delete().eq("transaction_id", transaction_id).execute()
