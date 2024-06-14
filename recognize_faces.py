import cv2
import os

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

# Load registered faces
data_dir = 'data'

def load_registered_faces():
    registered_faces = {}
    for person_name in os.listdir(data_dir):
        person_dir = os.path.join(data_dir, person_name)
        if os.path.isdir(person_dir):
            for filename in os.listdir(person_dir):
                if filename.endswith('.jpg'):
                    img_path = os.path.join(person_dir, filename)
                    registered_faces[filename] = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    return registered_faces

def recognize_faces():
    # Initialize camera
    cap = cv2.VideoCapture(0)

    # Load registered faces
    registered_faces = load_registered_faces()

    while True:
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
            face_region = gray[y:y+h, x:x+w]

            # Match detected face with registered faces
            for filename, registered_face in registered_faces.items():
                # Perform template matching or other recognition methods here
                match_result = cv2.matchTemplate(face_region, registered_face, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match_result)

                if max_val > 0.8:  # Adjust threshold as needed
                    person_name = filename.split('_')[0]
                    cv2.putText(frame, f"{person_name}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

        # Display the frame
        cv2.imshow('Recognize Faces', frame)

        # Exit on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_faces()
