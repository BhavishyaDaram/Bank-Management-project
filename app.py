import streamlit as st
from bank import Bank

st.set_page_config(page_title="Simple Bank App", layout="centered")
st.title("🏦 Welcome to Streamlit Bank")

menu = st.sidebar.selectbox(
    "Choose Action",
    ["Create Account", "Deposit", "Withdraw", "Show Details", "Update Info", "Delete Account"]
)

# ---------------- CREATE ACCOUNT ----------------
if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Your Name")
    age = st.number_input("Your Age", min_value=0, step=1)
    email = st.text_input("Your Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create"):
        if name and email and pin:
            result = Bank.create_account(name, int(age), email, int(pin))

            if isinstance(result, dict):
                st.success("Account created successfully!")
                st.info(f"Account No: {result['accountNo']}")
            else:
                st.error(result)
        else:
            st.warning("Fill all fields")

# ---------------- DEPOSIT ----------------
elif menu == "Deposit":
    st.subheader("Deposit Money")

    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        msg = Bank.deposit(acc_no, int(pin), int(amount))
        st.success(msg) if msg == "Deposited" else st.error(msg)

# ---------------- WITHDRAW ----------------
elif menu == "Withdraw":
    st.subheader("Withdraw Money")

    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        msg = Bank.withdraw(acc_no, int(pin), int(amount))
        st.success(msg) if msg == "Withdrawn" else st.error(msg)

# ---------------- SHOW DETAILS ----------------
elif menu == "Show Details":
    st.subheader("Account Details")

    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        user = Bank.get_details(acc_no, int(pin))
        if user:
            st.json(user)
        else:
            st.error("No account found")

# ---------------- UPDATE ----------------
elif menu == "Update Info":
    st.subheader("Update Your Info")

    acc_no = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    name = st.text_input("New Name (Optional)")
    email = st.text_input("New Email (Optional)")
    new_pin = st.text_input("New PIN (Optional)")

    if st.button("Update"):
        st.warning("Update function not implemented yet in backend")

# ---------------- DELETE ----------------
elif menu == "Delete Account":
    st.subheader("Delete Account")

    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        msg = Bank.delete_account(acc_no, int(pin))
        st.success(msg) if msg == "Deleted" else st.error(msg)