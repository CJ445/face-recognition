import cv2
import os

# Create directory if it doesn't exist
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

def register_faces():
    # Initialize camera
    cap = cv2.VideoCapture(0)

    # Load Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

    # Prompt for person's name
    person_name = input("Enter the name of the person to register: ")
    print(f"Registering {person_name}...")

    # Create a folder for the person if it doesn't exist
    person_dir = os.path.join(data_dir, person_name)
    os.makedirs(person_dir, exist_ok=True)

    # Capture 50 images
    count = 0
    while count < 100:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            face_region = frame[y:y+h, x:x+w]

            # Save face image with unique identifier
            img_name = os.path.join(person_dir, f"{person_name}_{count}.jpg")
            cv2.imwrite(img_name, face_region)
            print(f"Image saved: {img_name}")
            count += 1

        # Display the frame
        cv2.imshow('Register Faces', frame)

        # Exit on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    register_faces()
