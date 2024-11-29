import requests
from barcode import Code128
from barcode.writer import ImageWriter
import streamlit as st
import os

# Canvas API details
BASE_URL = "https://canvas.instructure.com/api/v1"
API_TOKEN = "7~Gc7HmJLnvhMPKemRKk44avE6ntBZTMwwekf6cTAPhPUCW2vc7xceUhQfEwNe4xWD"

# Function to fetch grades from Canvas
def fetch_grades(course_id):
    url = f"{BASE_URL}/courses/{course_id}/students/submissions"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error {response.status_code}: Unable to fetch grades")
        return None

# Function to generate barcode
def generate_barcode(data, output_file):
    barcode = Code128(data, writer=ImageWriter())
    barcode.save(output_file)

# Streamlit App
st.title("Canvas Grades and Barcode Generator")

course_id = st.text_input("Enter Canvas Course ID (e.g., 10606184)")

if st.button("Fetch and Generate"):
    grades = fetch_grades(course_id)
    if grades:
        for submission in grades:
            if "user" in submission and "score" in submission:
                student_name = submission["user"]["name"]
                grade = submission["score"]
                credential_data = f"{student_name}:{grade}"
                
                # Generate barcode
                output_file = f"{student_name}_barcode.png"
                generate_barcode(credential_data, output_file)
                
                # Display in Streamlit
                st.write(f"Student: {student_name}, Grade: {grade}")
                st.image(output_file)
                
                # Clean up
                os.remove(output_file)
    else:
        st.warning("No grades found for the given course ID.")
