<h1 align="center">🐍 InCodeVision - Python Learning Projects</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV Badge"/>
  <img src="https://img.shields.io/badge/API-Integration-success?style=for-the-badge" alt="API Badge"/>
</p>

<p align="center">
  <i>A collection of hands-on Python projects demonstrating various programming concepts including password generation, task management, API integration, and real-time computer vision.</i>
</p>

---

## 📌 Table of Contents
- [Projects Overview](#-projects-overview)
- [Quick Start](#-quick-start)
- [Learning Objectives](#-learning-objectives)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Author](#-author)

---

## 📚 Projects Overview

### [Task 1: Password Generator](./Task-1) 🔐
Generate strong, highly secure, and random passwords with customizable lengths.
- **Features**: Mixes uppercase, lowercase, numbers, and symbols.
- **Learning Concepts**: Loops, advanced string manipulation, Python's `random` module.

### [Task 2: To-Do List App](./Task-2) 📝
A straightforward console-based task management system to keep track of daily activities.
- **Features**: Add, view, mark as complete, and delete tasks dynamically.
- **Learning Concepts**: Lists, dictionary handling, loops, user input validation.

### [Task 3: Weather App Using API](./Task-3) ⛅
Fetch real-time weather information from any global city using the OpenWeatherMap API.
- **Features**: Displays temperature, humidity, and weather conditions.
- **Learning Concepts**: API integration, JSON data parsing, robust error handling, `requests` library.

### [Task 4: Face Detection Attendance System](./Task-4) 👤
A system to automate attendance taking by logging faces detected via a webcam feed into a CSV database.
- **Features**: Real-time face detection, CSV automated logging, duplicate entry prevention.
- **Learning Concepts**: Computer vision integration, Haar Cascades, file handling.

---

## 🚀 Quick Start

### 📋 Prerequisites
Make sure you have the following installed:
- Python 3.7+
- `pip` (Python package installer)
- A working webcam (For Task 4)

### 🛠️ Installation

**1. Clone the repository:**
```bash
git clone https://github.com/uttam102/Intership_Python.git
cd Intership_Python
```

**2. Set up a virtual environment (Recommended):**
```bash
python -m venv .venv

# On Windows:
.venv\Scripts\activate
# On Linux/Mac:
source .venv/bin/activate
```

**3. Install required libraries:**
```bash
pip install opencv-python requests
```

### 🏃 Running the Projects
Navigate to any task directory and run its primary Python file. For example:
```bash
cd Task-3
python weather_app.py
```

---

## 🧠 Learning Objectives

This repository is designed to teach and master foundational-to-advanced Python concepts.

| Task | Core Focus | Key Technologies & Libraries |
|------|-----------|------------------------------|
| **Task 1** | Logic & Randomness | `random`, string operators, functions |
| **Task 2** | Data Structures & CLI | `dict`, `list`, standard I/O streams |
| **Task 3** | Network Requests & JSON | REST APIs, HTTP status codes, `requests` |
| **Task 4** | Machine Vision & File I/O | Face Detection, `cv2` (OpenCV), `csv` |

---

## 📁 Project Structure

```text
📦 incodevision
 ┣ 📂 Task-1
 ┃ ┗ 📜 password_generator.py
 ┣ 📂 Task-2
 ┃ ┗ 📜 todo_list.py
 ┣ 📂 Task-3
 ┃ ┗ 📜 weather_app.py
 ┣ 📂 Task-4
 ┃ ┣ 📜 attendance_system.py
 ┃ ┣ 📜 README.md
 ┃ ┗ 📜 attendance.csv (auto-generated)
 ┗ 📜 README.md
```

---

## ⚙️ Configuration

### For Task 3: Weather App
1. Get a **Free API Key** from [OpenWeatherMap](https://openweathermap.org/api).
2. Open `Task-3/weather_app.py`.
3. Replace the placeholder `YOUR_API_KEY_HERE` with your actual key.

### For Task 4: Face Detection
- Make sure your webcam is not being used by another application.
- The script uses `cv2.VideoCapture(0)`. Adjust the ID if you have multiple cameras.

---

## 👨‍💻 Author

Built with ❤️ by **Uttam**
> GitHub: [@uttam102](https://github.com/uttam102)

---
*Happy Coding! 🎉*
