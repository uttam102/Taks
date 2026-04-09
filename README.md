# InCodeVision - Python Learning Projects

A collection of Python projects demonstrating various programming concepts including password generation, to-do list management, API integration, and computer vision.

## 📚 Projects Overview

### Task 1: Password Generator
Generate strong random passwords with customizable length.
- **Features**: Mix of letters, numbers, and symbols
- **Concepts**: Loops, string handling, random module

[View Code](Task-1/password_generator.py)

---

### Task 2: To-Do List App (Console Based)
Simple console-based task management system.
- **Features**: Add, view, mark complete, delete tasks
- **Concepts**: Lists, loops, user input, data structures

[View Code](Task-2/todo_list.py)

---

### Task 3: Weather App Using API
Real-time weather information using OpenWeatherMap API.
- **Features**: Fetches weather data, displays temperature, humidity, conditions
- **Concepts**: API integration, JSON parsing, error handling

[View Code](Task-3/weather_app.py)

---

### Task 4: Face Detection Attendance System
Webcam-based attendance system using face detection.
- **Features**: Real-time face detection, CSV logging, duplicate prevention
- **Concepts**: Computer vision, OpenCV, file handling

[View Code](Task-4/attendance_system.py) | [Documentation](Task-4/README.md)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/incodevision.git
cd incodevision
```

2. (Optional) Create a virtual environment:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. Install dependencies:
```bash
# For Task 4 (Face Detection)
pip install opencv-python

# For Task 3 (Weather App)
pip install requests
```

### Running the Projects

**Task 1 - Password Generator:**
```bash
cd Task-1
python password_generator.py
```

**Task 2 - To-Do List:**
```bash
cd Task-2
python todo_list.py
```

**Task 3 - Weather App:**
```bash
cd Task-3
python weather_app.py
```
*Note: Requires OpenWeatherMap API key*

**Task 4 - Face Detection Attendance:**
```bash
cd Task-4
python attendance_system.py
```
*Note: Requires webcam access*

---

## 📖 Learning Objectives

Each project is designed to teach specific Python concepts:

| Task | Key Concepts |
|------|-------------|
| Task 1 | Random module, string manipulation, loops |
| Task 2 | Lists, dictionaries, user input, file operations |
| Task 3 | API calls, JSON parsing, HTTP requests, error handling |
| Task 4 | Computer vision, OpenCV, real-time processing, CSV files |

---

## 📝 Project Structure

```
incodevision/
├── Task-1/
│   └── password_generator.py
├── Task-2/
│   └── todo_list.py
├── Task-3/
│   └── weather_app.py
├── Task-4/
│   ├── attendance_system.py
│   ├── README.md
│   └── attendance.csv (generated)
└── README.md
```

---

## 🔧 Configuration

### Task 3: Weather App
1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Open `Task-3/weather_app.py`
3. Replace `YOUR_API_KEY_HERE` with your actual API key

### Task 4: Face Detection
- Ensure your webcam is connected and accessible
- Grant camera permissions when prompted

---

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements!

---

## 📄 License

This project is open source and available for educational purposes.

---

## 👨‍💻 Author

Created as part of Python learning journey.

---

## 🙏 Acknowledgments

- OpenWeatherMap API for weather data
- OpenCV for computer vision capabilities
