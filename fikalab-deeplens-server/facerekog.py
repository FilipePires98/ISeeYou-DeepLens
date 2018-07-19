import base64
import cv2

import face_recognition

def encode(imgpath):
    #Load Image
    print "Load Image"
    image=face_recognition.load_image_file(path)
    #Encode face

    print "Encoding Image"
    return face_recognition.face_encodings(image)[0]


def rekog(frame,known_face_encodings,known_face_names):
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        face_names.append(name)

    #process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    return frame

#def img2b64(img):
    #return base64.b64encode(img.tobytes())

#def b642img(b64):
    #return base64.b64decode(bytes()


def init_facerekog():
    #faz o treino
    path_dir=r'C:\Users\joaof\PycharmProjects\face_recognition-master\examples\'
    p_fig=['ines1_s',
           'joaoc_s',
           'hugo']
    known_face_names=[  "Ines Valentim",
    "Joao Carvalho",
    "Hugo Marques"
    ]

    known_face_encodings=[]
    for i in range(len(p_fig)):
        known_face_encodings.append(encode(path_dir+p_fig[i]+'.jpg'))

    return known_face_encodings








