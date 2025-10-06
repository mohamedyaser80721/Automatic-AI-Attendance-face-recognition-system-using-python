import os
import face_recognition
import pickle
from imutils import paths

KNOWN_FACES_DIR = "dataset/known"
ENCODINGS_PATH = "encodings.pkl"

known_encodings = []
known_names = []

image_paths = list(paths.list_images(KNOWN_FACES_DIR))
print(f"Found {len(image_paths)} images. Encoding...")

for img_path in image_paths:
    # folder name is the label
    name = os.path.basename(os.path.dirname(img_path))
    image = face_recognition.load_image_file(img_path)
    # detect face locations (use model="hog" or "cnn" if installed)
    boxes = face_recognition.face_locations(image, model="hog")
    encs = face_recognition.face_encodings(image, boxes)

    if len(encs) == 0:
        print(f"WARNING: no face found in {img_path} — skipping")
        continue

    # if multiple faces, store all with same name
    for enc in encs:
        known_encodings.append(enc)
        known_names.append(name)

# save
data = {"encodings": known_encodings, "names": known_names}
with open(ENCODINGS_PATH, "wb") as f:
    pickle.dump(data, f)

print(f"Saved {len(known_encodings)} encodings to {ENCODINGS_PATH}")
