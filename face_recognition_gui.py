import tkinter as tk
import subprocess

def register_faces_gui():
    subprocess.run(["python", "register_faces.py"])

def recognize_faces_gui():
    subprocess.run(["python", "recognize_faces.py"])

# Create main window
root = tk.Tk()
root.title("Face Recognition Application")

# Register Faces Button
register_btn = tk.Button(root, text="Register Faces", command=register_faces_gui)
register_btn.pack(pady=20)

# Recognize Faces Button
recognize_btn = tk.Button(root, text="Recognize Faces", command=recognize_faces_gui)
recognize_btn.pack(pady=20)

# Run the application
root.mainloop()
