import os
import cv2
import face_recognition
import numpy as np
from datetime import datetime
import csv

path = 'images'
images = []
names = []

# Load images and names
for file_name in os.listdir(path):
    img = cv2.imread(os.path.join(path, file_name))
    if img is None:
        continue
    images.append(img)
    names.append(os.path.splitext(file_name)[0])

# Encode faces
def encode_faces(image_list):
    encodings = []
    for img in image_list:
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_encodings(rgb_img)
        if faces:
            encodings.append(faces[0])
    return encodings

known_encodings = encode_faces(images)

 
    # load additional information
def mark_attendance(name):
    filename = 'attendance.csv'
    info_file = 'info.csv'
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H:%M:%S')

        # Load additional info
    roll_no = ""
    course = ""

    if os.path.isfile(info_file):
        with open(info_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Name'] == name:
                    roll_no = row['RollNo']
                    course = row['Course']
                    break

        # Create attendance.csv if not exists
        if not os.path.isfile(filename):
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'RollNo', 'Course', 'Date', 'Time'])

        # Check if already marked today
        already_marked = False
        with open(filename, 'r') as f:
            for line in f:
                if name in line and date_str in line:
                    already_marked = True
                    break

        if not already_marked:
            with open(filename, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([name, roll_no, course, date_str, time_str])
                print(f"[✔] Attendance marked for {name} ({roll_no})")

# Start webcam
cap = cv2.VideoCapture(0)
while True:
    success, frame = cap.read()
    if not success:
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_loc in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)

        name = "Unknown"
        if len(face_distances) > 0:
            best_match = np.argmin(face_distances)
            if matches[best_match]:
                name = names[best_match]
                mark_attendance(name)  # ✅ Mark attendance here

        y1, x2, y2, x1 = [v * 4 for v in face_loc]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, name, (x1, y2 + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow('Face Recognition Attendance', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()