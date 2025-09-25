# src/logic.py

from src.db import DatabaseManager

class UserManager:
    """
    Acts as a bridge between frontend (Streamlit/FastAPI) and the database.
    """

    def __init__(self):
        self.db = DatabaseManager()

    def add_user(self, first_name, last_name, email, password):
        if not first_name or not last_name or not email or not password:
            return {"Success": False, "Message": "Fill all required details"}

        result = self.db.create_user(first_name, last_name, email, password)

        if result.get("error"):
            return {"Success": False, "Message": f"Error: {result.get('error')}"}
        else:
            return {"Success": True, "Message": "User added successfully"}

    def update_user_password(self, user_id, new_password):
        result = self.db.update_user_password(user_id, new_password)
        if result.get("error"):
            return {"Success": False, "Message": f"Error: {result.get('error')}"}
        return {"Success": True, "Message": "Password updated successfully"}

    def delete_user(self, user_id):
        result = self.db.delete_user(user_id)
        if result.get("error"):
            return {"Success": False, "Message": f"Error: {result.get('error')}"}
        return {"Success": True, "Message": "User deleted successfully"}

    def get_users(self):
        return self.db.get_all_users()

# src/transaction_manager.py


class TransactionManager:

    def __init__(self):
        self.db = DatabaseManager()

    def add_transaction(self, user_id, date, type, category, amount, note=""):
        if not user_id or not date or not type or not category or not amount:
            return {"Success": False, "Message": "Fill all required fields"}

        result = self.db.create_transaction(user_id, date, type, category, amount, note)

        if result.get("error"):
            return {"Success": False, "Message": f"Error: {result.get('error')}"}
        else:
            return {"Success": True, "Message": "Transaction added successfully"}

    def update_transaction_type(self, transaction_id, new_type):
        result = self.db.update_transaction(transaction_id, new_type)
        if result.get("error"):
            return {"Success": False, "Message": f"Error: {result.get('error')}"}
        return {"Success": True, "Message": "Transaction type updated successfully"}

    def delete_transaction(self, transaction_id):
        result = self.db.delete_transaction(transaction_id)
        if result.get("error"):
            return {"Success": False, "Message": f"Error: {result.get('error')}"}
        return {"Success": True, "Message": "Transaction deleted successfully"}

    def get_transactions(self, user_id=None):
        result = self.db.get_all_transactions()
        if result.get("error"):
            return {"Success": False, "Message": f"Error: {result.get('error')}"}
        transactions = result.get("data", [])
        if user_id:
            transactions = [t for t in transactions if t["user_id"] == user_id]
        return {"Success": True, "Data": transactions}
