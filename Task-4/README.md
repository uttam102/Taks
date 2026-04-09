# Face Recognition Attendance System - Setup Guide

## 📋 Requirements

This system requires the following Python libraries:
- `opencv-python` - Webcam and image processing
- `face_recognition` - Face detection and recognition
- `cmake` - Build tool (required for dlib)
- `dlib` - Machine learning library (required for face_recognition)
- `numpy` - Numerical computing

## 🚀 Installation Steps

### Step 1: Install Dependencies

Run these commands in order:

```bash
pip install opencv-python
pip install cmake
pip install dlib
pip install face_recognition
pip install numpy
```

**Note**: Installation may take 5-10 minutes and download ~500MB of data.

### Step 2: Setup Known Faces

1. Create a folder named `known_faces` in the Task-4 directory
2. Add photos of people you want to recognize
3. Name format: `PersonName.jpg` (e.g., `John.jpg`, `Sarah.jpg`)
4. Use clear, front-facing photos with good lighting

### Step 3: Run the System

```bash
cd Task-4
python attendance_system.py
```

## 📸 Usage Instructions

1. **Start the program** - Webcam will activate
2. **Position your face** in front of the camera
3. **Wait for recognition** - Green box = recognized, Red box = unknown
4. **Attendance logged** - Message appears in console
5. **Press 'q'** to quit

## 📊 Attendance Records

- Attendance is saved in `attendance.csv`
- Format: Name, Date, Time
- One entry per person per day (no duplicates)

## 🎯 Features

✅ Real-time face detection
✅ Face recognition with name display
✅ Automatic attendance logging
✅ CSV file generation
✅ Duplicate prevention (one entry per day)
✅ Visual feedback with bounding boxes

## 🔧 Troubleshooting

**Webcam not working?**
- Check if another app is using the webcam
- Grant camera permissions when prompted

**Face not recognized?**
- Ensure good lighting
- Face the camera directly
- Use a clear photo in known_faces folder

**Installation errors?**
- Install Visual C++ Build Tools (Windows)
- Use Python 3.7-3.10 (face_recognition compatibility)