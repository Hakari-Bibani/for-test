import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Connect to Google Sheets
def connect_to_gsheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Chemistry Test Responses").sheet1
    return sheet

def submit_to_gsheet(data):
    sheet = connect_to_gsheet()
    sheet.append_row(data)

# Streamlit App
st.title("Chemistry Test")
st.image("https://drive.google.com/uc?export=view&id=1PpiIFmMgQu-XOoIf9PMLnI3QA_WE0bfG")

st.markdown("### Please fill out this test form:")

full_name = st.text_input("1. Full Name")
school = st.text_input("2. Your School")
code = st.text_input("3. Enter the code (Hint: Hakari)")

if code == "Hakari":
    st.markdown("### Test Questions")
    username = st.text_input("4. Username")
    python_1 = st.text_input("5. What is Python 1?")
    python_2 = st.text_input("6. What is Python 2?")
    python_3 = st.text_input("7. What is Python 3?")
    python_4 = st.text_input("8. What is Python 4?")
    apple_1 = st.radio("9. What is Apple?", ["Orange", "Blue", "Yellow", "Green"])
    apple_2 = st.radio("10. What is Apple?", ["Orange", "Blue", "Yellow", "Green"])
    apple_3 = st.radio("11. What is Apple?", ["Orange", "Blue", "Yellow", "Green"])
    python_5 = st.text_input("12. What is Python?")
    python_6 = st.text_input("13. What is Python 2?")

    if st.button("Submit"):
        if not full_name or not school or not username:
            st.error("Please complete all fields.")
        else:
            submit_to_gsheet([
                full_name, school, code, username,
                python_1, python_2, python_3, python_4,
                apple_1, apple_2, apple_3, python_5, python_6
            ])
            st.success("Your responses were submitted!")
else:
    st.warning("Please enter the correct code to continue.")
