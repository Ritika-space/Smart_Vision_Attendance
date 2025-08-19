📖** Overview**

This project is an AI-powered attendance system that uses face recognition to automatically mark attendance. It eliminates manual roll-calls, improves accuracy, and provides a contactless solution for classrooms, workplaces, and events.


**✨ Features**

🎥 Real-time face detection & recognition using OpenCV & deep learning
📝 Automatic attendance marking with time & date
💾 Database / CSV storage for attendance records
🖥️ User-friendly interface
⚡ Scalable for institutions, offices, and events


**🛠️ Tech Stack**

Programming Language: Python
Libraries: OpenCV, NumPy, face-recognition, dlib, Pandas
Database: CSV / SQLite (configurable)
Platform: Windows / Linux / macOS


**📂 Project Structure**
smart_vision_attendance/
│── dataset/              # Stored face images
│── attendance/           # Attendance logs
│── app.py                # Main application
│── train.py              # Training script
│── requirements.txt      # Dependencies
│── README.md             # Project documentation


**⚙️ Installation**

Clone the Repository

git clone https://github.com/your-username/face-recognition-attendance-system.git
cd face-recognition-attendance-system


Create Virtual Environment (Optional but Recommended)

python -m venv venv
venv\Scripts\activate   # For Windows
source venv/bin/activate # For Linux/Mac


Install Dependencies

pip install -r requirements.txt
