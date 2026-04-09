### 👤 Task 4: Face Detection Attendance System

An automated computer vision script that uses your webcam to detect faces and automatically logs the presence into a CSV database.

#### ✨ Features
- **Real-Time Detection**: Accesses the webcam to draw boxes around recognized faces instantly.
- **Automated Logging**: Saves the detected user data into an `attendance.csv` file automatically.
- **Duplicate Prevention**: Avoids logging the same face multiple times in rapid succession.

#### 🚀 How to Run
This project requires OpenCV. Install it via pip:
```bash
pip install opencv-python
```
Then execute the script:
```bash
python attendance_system.py
```
*(Press `q` on your keyboard to quit the webcam window).*

#### 🧠 Concepts Learned
- Implementing OpenCV (`cv2`) for live video capturing.
- Utilizing Haar Cascades for object and face detection.
- Reading and writing local files, specifically CSV formats, dynamically through Python.