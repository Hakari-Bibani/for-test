import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Connect to Google Sheets
def connect_to_gsheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Chemistry Test Responses").sheet1  # Change name if your sheet is named differently
    return sheet

def submit_to_gsheet(data):
    sheet = connect_to_gsheet()
    sheet.append_row(data)

# Streamlit App
st.title("Chemistry Test")
st.image("https://drive.google.com/uc?export=view&id=1PpiIFmMgQu-XOoIf9PMLnI3QA_WE0bfG", caption="Chemistry Test", use_column_width=True)

st.markdown("Welcome to the Chemistry Test. Please fill out the form below carefully.")

# Personal Information Section
st.markdown("### Personal Information")
full_name = st.text_input("1. Full Name", placeholder="Enter your full name")
school = st.text_input("2. Your School", placeholder="Enter the name of your school")
code = st.text_input("3. Enter the code to access the test (Hint: Hakari)", type="password")

# Conditional Test Questions
if code == "Hakari":
    st.success("Access granted! Please complete the questions below.")
    st.markdown("### Test Questions")

    # Short Answer Questions
    username = st.text_input("4. Username", placeholder="Enter your username")
    python_1 = st.text_input("5. What is Python 1?")
    python_2 = st.text_input("6. What is Python 2?")
    python_3 = st.text_input("7. What is Python 3?")
    python_4 = st.text_input("8. What is Python 4?")

    # Multiple Choice Questions
    apple_1 = st.radio("9. What is Apple?", ["Orange", "Blue", "Yellow", "Green"])
    apple_2 = st.radio("10. What is Apple?", ["Orange", "Blue", "Yellow", "Green"])
    apple_3 = st.radio("11. What is Apple?", ["Orange", "Blue", "Yellow", "Green"])

    # Additional Short Answer Questions
    python_5 = st.text_input("12. What is Python?")
    python_6 = st.text_input("13. What is Python 2?")

    # Submit Button
    if st.button("Submit"):
        if not full_name or not school or not username:
            st.error("Please fill out all the required fields.")
        else:
            try:
                # Collect responses and submit to Google Sheet
                responses = [
                    full_name, school, code, username,
                    python_1, python_2, python_3, python_4,
                    apple_1, apple_2, apple_3, python_5, python_6
                ]
                submit_to_gsheet(responses)
                st.success("Your responses have been submitted successfully!")
            except Exception as e:
                st.error(f"An error occurred while submitting your responses: {e}")
else:
    if code:
        st.error("Incorrect code. Please try again.")
    else:
        st.info("Enter the code to unlock the test questions.")

st.markdown("---")
st.markdown("© 2024 Chemistry Test | Designed for Educational Purposes")

