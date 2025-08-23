
import streamlit as st
import sqlite3
import pandas as pd

# Database connection
def get_connection():
    conn = sqlite3.connect("university.db")
    return conn

# Initialize DB
def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    with open("university_schema.sql", "r") as f:
        schema = f.read()
    cursor.executescript(schema)
    conn.commit()
    conn.close()

# Insert Data Functions
def insert_department(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Department (dept_name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def insert_student(name, age, dept_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Student (name, age, dept_id) VALUES (?, ?, ?)", (name, age, dept_id))
    conn.commit()
    conn.close()

def insert_professor(name, dept_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Professor (name, dept_id) VALUES (?, ?)", (name, dept_id))
    conn.commit()
    conn.close()

def insert_course(course_name, dept_id, professor_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Course (course_name, dept_id, professor_id) VALUES (?, ?, ?)", (course_name, dept_id, professor_id))
    conn.commit()
    conn.close()

def insert_enrollment(student_id, course_id, grade):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Enrollment (student_id, course_id, grade) VALUES (?, ?, ?)", (student_id, course_id, grade))
    conn.commit()
    conn.close()

# Fetch Data Function
def fetch_table(table_name):
    conn = get_connection()
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df

# Streamlit UI
st.title("University Management System")

menu = ["Initialize DB", "Add Department", "Add Student", "Add Professor", "Add Course", "Add Enrollment", "View Data"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Initialize DB":
    if st.button("Initialize Database"):
        init_db()
        st.success("Database Initialized Successfully!")

elif choice == "Add Department":
    name = st.text_input("Department Name")
    if st.button("Add Department"):
        insert_department(name)
        st.success("Department Added!")

elif choice == "Add Student":
    name = st.text_input("Student Name")
    age = st.number_input("Age", min_value=16, max_value=100)
    dept_id = st.number_input("Department ID", min_value=1)
    if st.button("Add Student"):
        insert_student(name, age, dept_id)
        st.success("Student Added!")

elif choice == "Add Professor":
    name = st.text_input("Professor Name")
    dept_id = st.number_input("Department ID", min_value=1)
    if st.button("Add Professor"):
        insert_professor(name, dept_id)
        st.success("Professor Added!")

elif choice == "Add Course":
    course_name = st.text_input("Course Name")
    dept_id = st.number_input("Department ID", min_value=1)
    professor_id = st.number_input("Professor ID", min_value=1)
    if st.button("Add Course"):
        insert_course(course_name, dept_id, professor_id)
        st.success("Course Added!")

elif choice == "Add Enrollment":
    student_id = st.number_input("Student ID", min_value=1)
    course_id = st.number_input("Course ID", min_value=1)
    grade = st.text_input("Grade")
    if st.button("Add Enrollment"):
        insert_enrollment(student_id, course_id, grade)
        st.success("Enrollment Added!")

elif choice == "View Data":
    table_name = st.selectbox("Select Table", ["Department", "Student", "Professor", "Course", "Enrollment"])
    if st.button("Show Data"):
        df = fetch_table(table_name)
        st.dataframe(df)
