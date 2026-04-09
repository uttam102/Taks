import cv2
import csv
from datetime import datetime
import os

class AttendanceSystem:
    """Simple Face Detection-Based Attendance System using OpenCV"""
    
    def __init__(self):
        """Initialize the attendance system."""
        self.attendance_file = "attendance.csv"
        self.attendance_marked = set()
        self.face_cascade = None
        
        # Load face detection model
        self.load_face_detector()
        
        # Initialize CSV file
        self.initialize_csv()
    
    def load_face_detector(self):
        """Load OpenCV's Haar Cascade face detector."""
        print("\nLoading face detection model...")
        
        # Try to load the pre-trained face detection model
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        
        if self.face_cascade.empty():
            print("Error: Could not load face detection model!")
            return False
        
        print("✓ Face detection model loaded successfully")
        return True
    
    def initialize_csv(self):
        """Initialize the CSV file with headers if it doesn't exist."""
        if not os.path.exists(self.attendance_file):
            with open(self.attendance_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Person ID', 'Date', 'Time'])
            print(f"✓ Created attendance file: {self.attendance_file}")
    
    def mark_attendance(self, person_id):
        """
        Mark attendance for a person in the CSV file.
        
        Args:
            person_id (str): Identifier for the person
        """
        # Check if attendance already marked today
        today = datetime.now().strftime('%Y-%m-%d')
        attendance_key = f"{person_id}_{today}"
        
        if attendance_key not in self.attendance_marked:
            now = datetime.now()
            date_string = now.strftime('%Y-%m-%d')
            time_string = now.strftime('%H:%M:%S')
            
            with open(self.attendance_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([person_id, date_string, time_string])
            
            self.attendance_marked.add(attendance_key)
            print(f"✓ Attendance marked for: {person_id} at {time_string}")
            return True
        return False
    
    def run(self):
        """Run the face detection attendance system."""
        print("\n" + "=" * 60)
        print("FACE DETECTION ATTENDANCE SYSTEM")
        print("=" * 60)
        print("\nInstructions:")
        print("- Position your face in front of the camera")
        print("- Press SPACE to mark attendance when face is detected")
        print("- Press 'q' or ESC to quit")
        print("=" * 60)
        
        if self.face_cascade is None or self.face_cascade.empty():
            print("\nError: Face detection model not loaded!")
            return
        
        print("\nStarting webcam...")
        
        # Open webcam
        video_capture = cv2.VideoCapture(0)
        
        if not video_capture.isOpened():
            print("Error: Could not access webcam!")
            return
        
        person_counter = 1
        face_detected = False
        
        while True:
            # Capture frame
            ret, frame = video_capture.read()
            
            if not ret:
                print("Error: Failed to capture frame!")
                break
            
            # Convert to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Detect faces
            faces = self.face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )
            
            face_detected = len(faces) > 0
            
            # Draw rectangles around detected faces
            for (x, y, w, h) in faces:
                # Draw green rectangle around face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                # Add label
                cv2.putText(frame, "Face Detected", (x, y-10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
            # Display instructions on screen
            status_text = "Press SPACE to mark attendance" if face_detected else "No face detected"
            cv2.putText(frame, status_text, (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            
            # Display frame
            cv2.imshow('Face Detection Attendance System', frame)
            
            # Handle key presses
            key = cv2.waitKey(1) & 0xFF
            
            # Quit on 'q' key or ESC key (27)
            if key == ord('q') or key == 27:
                break
            
            # Mark attendance on SPACE key
            elif key == ord(' ') and face_detected:
                person_id = f"Person_{person_counter}"
                if self.mark_attendance(person_id):
                    person_counter += 1
                    # Show confirmation
                    print(f"✓ Attendance recorded!")
        
        # Cleanup
        video_capture.release()
        cv2.destroyAllWindows()
        print("\n" + "=" * 60)
        print("Attendance system closed.")
        print(f"Total attendance records: {person_counter - 1}")
        print(f"Attendance saved in: {self.attendance_file}")
        print("=" * 60)


def main():
    """Main function to run the attendance system."""
    print("\n" + "=" * 60)
    print("FACE DETECTION ATTENDANCE SYSTEM")
    print("=" * 60)
    print("\nThis system uses OpenCV for face detection.")
    print("When a face is detected, press SPACE to mark attendance.")
    print("=" * 60)
    
    # Create and run attendance system
    system = AttendanceSystem()
    system.run()


if __name__ == "__main__":
    main()
