import streamlit as st
import cv2
import os
import numpy as np
import pandas as pd
from datetime import datetime

st.set_page_config(layout="wide")
st.title("📸 Fast Face Attendance System")

# Initialize session state
if "monitoring" not in st.session_state:
    st.session_state.monitoring = False
if "attendance_log" not in st.session_state:
    st.session_state.attendance_log = {}
if "df_log" not in st.session_state:
    st.session_state.df_log = pd.DataFrame(columns=["Name", "Entry Time", "Exit Time", "Duration"])

# Load face recognizer and Haar cascade
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Load names from folder
faces_dir = r"C:\Users\ASUS\Downloads\face_recognition_attendance\Face_recognition_based_attendance_system-master\TrainingImage"
names = {}
if os.path.exists(faces_dir):
    for i, person_name in enumerate(os.listdir(faces_dir)):
        names[i] = person_name
else:
    st.error(f"⚠️ Folder not found: {faces_dir}")

# Attendance logging function
def log_attendance(name):
    now = datetime.now()
    if name not in st.session_state.attendance_log:
        st.session_state.attendance_log[name] = {"entry": now, "exit": now}
    else:
        st.session_state.attendance_log[name]["exit"] = now

# Buttons
start = st.button("▶️ Start Monitoring")
stop = st.button("⏹️ Stop Monitoring")

frame_placeholder = st.empty()
csv_placeholder = st.empty()

# Start webcam
if start:
    st.session_state.monitoring = True
    cap = cv2.VideoCapture(0)
    st.info("📷 Monitoring...")

    while st.session_state.monitoring:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (130, 100))
            label, confidence = recognizer.predict(face)

            if confidence < 80:
                name = names.get(label, "Unknown")
                log_attendance(name)
                cv2.putText(frame, name, (x + 5, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Unknown", (x + 5, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)

        frame_placeholder.image(frame, channels="BGR")

    cap.release()
    cv2.destroyAllWindows()

# Stop button handler
if stop:
    st.session_state.monitoring = False

    for name, times in st.session_state.attendance_log.items():
        duration = times["exit"] - times["entry"]
        st.session_state.df_log.loc[len(st.session_state.df_log)] = [
            name,
            times["entry"].strftime("%H:%M:%S"),
            times["exit"].strftime("%H:%M:%S"),
            str(duration)
        ]

    st.session_state.df_log.to_csv("attendance_log.csv", index=False)
    csv_placeholder.subheader("📄 Attendance Log")
    csv_placeholder.dataframe(st.session_state.df_log)
    st.success("✅ Attendance logged successfully.")
