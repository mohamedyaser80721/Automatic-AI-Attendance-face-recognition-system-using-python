# Face Recognition Attendance System

This project implements a **real-time Face Recognition Attendance System** using Python, OpenCV, and `face_recognition` library. It detects faces from a webcam, identifies known faces, and logs attendance with **timestamp, location, and face image** to both an **Excel file** and a **Supabase database**.

---

## 🛠 Features

- **Real-time Face Recognition:** Detects faces from a webcam stream.
- **Known Faces Encoding:** Encodes known faces and saves them in `encodings.pkl`.
- **Unknown Faces Handling:** Marks unknown faces automatically.
- **Location Tracking:** Retrieves current location using OpenCage API.
- **Attendance Logging:**  
  - Saves attendance to `attendance.xlsx`.  
  - Uploads face images and metadata to **Supabase**.
- **Multiple Face Detection:** Can handle more than one face in the camera frame.
- **Customizable Tolerance:** Adjust the recognition strictness (`TOLERANCE`).

---

## 📂 Project Structure

project/
│
├─ dataset/known/ # Folder containing images of known people
│ ├─ person1/
│ ├─ person2/
│
├─ encodings.pkl # Pickle file storing face encodings
├─ attendance.xlsx # Excel file storing attendance logs
├─ main.py # Main Python script
├─ requirements.txt # Required Python packages

Data Base used
Supabase : https://supabase.com/dashboard
---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-folder>

Install required packages:
pip install face_recognition opencv-python imutils pandas openpyxl requests supabase-py numpy

Make sure your dataset folder contains known faces:
dataset/known/<person_name>/<image>.jpg

