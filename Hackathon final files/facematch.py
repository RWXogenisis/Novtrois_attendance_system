import face_recognition
def face(rn, i):
    known_image = face_recognition.load_image_file(str(rn)+".jpg")
    unknown_image = face_recognition.load_image_file(str(i)+".jpg")            
    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

    if results==[True]:
        return 0
    else:
        return 1
