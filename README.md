

# 📌 Face Recognition Attendance System

## 📖 Overview

This project is an **AI-powered attendance system** that uses **face recognition** to automatically mark attendance. It eliminates manual roll-calls, improves accuracy, and provides a contactless solution for classrooms, workplaces, and events.

---

## ✨ Features

* 🎥 **Real-time face detection & recognition** using OpenCV & deep learning
* 📝 **Automatic attendance marking** with time & date
* 💾 **Database / CSV storage** for attendance records
* 🖥️ **User-friendly interface**
* ⚡ **Scalable** for institutions, offices, and events

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:** OpenCV, NumPy, face-recognition, dlib, Pandas
* **Database:** CSV / SQLite (configurable)
* **Platform:** Windows / Linux / macOS

---

## 📂 Project Structure

```
smart_vision_attendance/
│── dataset/              # Stored face images
│── attendance/           # Attendance logs
│── app.py                # Main application
│── train.py              # Training script
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
```

---

## ⚙️ Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/face-recognition-attendance-system.git
   cd face-recognition-attendance-system
   ```

2. **Create Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # For Windows
   source venv/bin/activate # For Linux/Mac
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

1. **Collect Face Data**

   ```bash
   python collect_faces.py
   ```

2. **Train the Model**

   ```bash
   python train.py
   ```

3. **Run the Attendance System**

   ```bash
   python app.py
   ```

---

## 📊 Output

* Attendance is automatically saved in `attendance/` as a CSV file with:

  ```
  Name | Date | Time
  ```

---

## 📸 Screenshots

(Add images of your app running here — e.g., face recognition window, attendance log)

---

## 🚀 Future Improvements

* Cloud-based attendance management
* Mobile app integration
* Integration with biometric systems
* Admin dashboard for analytics

---

## 🤝 Contributing

Contributions are welcome! Please fork this repository and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License** – you are free to use and modify with attribution.

---
