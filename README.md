# Face Recognition Application
This Python application uses OpenCV for face detection and recognition. It allows users to register faces by capturing multiple images per person and then recognizes registered faces in real-time using a webcam feed.

## Features
- 'Face Registration': Capture 50 images of a person's face for registration. Images are saved with the person's name and an image number.
- 'Face Recognition': Real-time recognition of registered faces using template matching based on OpenCV's cv2.matchTemplate() function.
- 'Graphical User Interface (GUI)': Basic tkinter GUI for user interaction, providing options to register faces and recognize registered faces.

## Prerequisites
- Python 3.x
- OpenCV (opencv-python)
- numpy
- Pillow (PIL)
- tkinter (for GUI)

Install the required Python libraries using pip:
```
pip install opencv-python numpy Pillow tkinter
```

## Project Structure
```
face_recognition_project/
│
├── haarcascades/          # Folder for storing Haar cascade XML files
│   └── haarcascade_frontalface_default.xml
│
├── data/                  # Folder to store registered face images
│
├── register_faces.py      # Script to register faces by capturing images
├── recognize_faces.py     # Script to recognize registered faces in real-time
└── face_recognition_gui.py # Script for tkinter GUI to interact with the application

```

## Usage

### Registering Faces
- Run 'register_faces.py'.
- Enter the name of the person you want to register.
- The application will capture 50 images of the person's face.
- Images will be saved in the data directory under a folder named after the person.

### Recognizing Faces
- After registering faces for multiple persons, run 'recognize_faces.py'.
- The application will use the webcam feed to detect and recognize registered faces.
- Detected faces will be labeled with the corresponding person's name if recognized.

### Graphical User Interface (GUI)
- Run 'face_recognition_gui.py' for a tkinter GUI interface.
- Use buttons to register faces or recognize faces.

## Notes
- Ensure the 'haarcascade_frontalface_default.xml' file is located in the haarcascades directory for face detection.
- Adjust recognition thresholds and methods (cv2.matchTemplate() parameters) based on your specific requirements for accuracy and performance.
