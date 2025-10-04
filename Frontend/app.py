
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("💰 Personal Finance Tracker")

menu = st.sidebar.selectbox(
    "Choose an action",
    ["Add User", "Update Password", "Delete User", "View Users",
     "Add Transaction", "Update Transaction Type", "Delete Transaction", "View Transactions"]
)

# ---------------- USERS ----------------
if menu == "Add User":
    st.subheader("Add New User")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Add User"):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        }
        try:
            res = requests.post(f"{API_URL}/users/add", json=payload)
            if res.status_code == 200:
                st.success("User added successfully")
            else:
                st.error(f"Error: {res.json()['detail']}")
        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to API. Make sure the backend is running on 127.0.0.1:8000")

# ---------------- TRANSACTIONS ----------------
elif menu == "Add Transaction":
    st.subheader("Add Transaction")
    user_id = st.number_input("User ID", min_value=1, step=1)
    amount = st.number_input("Amount", step=0.01)
    category = st.text_input("Category (e.g., Food, Shopping)")
    t_type = st.selectbox("Type", ["income", "expense"])

    if st.button("Add Transaction"):
        payload = {"user_id": user_id, "amount": amount, "category": category, "t_type": t_type}
        res = requests.post(f"{API_URL}/transactions/add", json=payload)
        st.write(res.json())

elif menu == "Update Transaction Type":
    st.subheader("Update Transaction Type")
    transaction_id = st.number_input("Transaction ID", min_value=1, step=1)
    new_type = st.selectbox("New Type", ["income", "expense"])

    if st.button("Update Type"):
        payload = {"transaction_id": transaction_id, "new_type": new_type}
        res = requests.put(f"{API_URL}/transactions/update-type", json=payload)
        st.write(res.json())

elif menu == "Delete Transaction":
    st.subheader("Delete Transaction")
    transaction_id = st.number_input("Transaction ID", min_value=1, step=1)

    if st.button("Delete Transaction"):
        res = requests.delete(f"{API_URL}/transactions/delete/{transaction_id}")
        st.write(res.json())

elif menu == "View Transactions":
    st.subheader("All Transactions")
    res = requests.get(f"{API_URL}/transactions")
    if res.status_code == 200:
        st.table(res.json())
    else:
        st.error("Error fetching transactions")
