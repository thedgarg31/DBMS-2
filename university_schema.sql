
-- University Database Schema

-- Department table
CREATE TABLE Department (
    dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dept_name TEXT NOT NULL UNIQUE
);

-- Student table
CREATE TABLE Student (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- Professor table
CREATE TABLE Professor (
    professor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- Course table
CREATE TABLE Course (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    dept_id INTEGER,
    professor_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id),
    FOREIGN KEY (professor_id) REFERENCES Professor(professor_id)
);

-- Enrollment table
CREATE TABLE Enrollment (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_id INTEGER,
    grade TEXT,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);
