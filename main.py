import cv2
import numpy as np
import math
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


model_path = "hand_landmarker.task"

BaseOptions = python.BaseOptions
HandLandmarker = vision.HandLandmarker
HandLandmarkerOptions = vision.HandLandmarkerOptions
VisionRunningMode = vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=2
)

landmarker = HandLandmarker.create_from_options(options)


cap = cv2.VideoCapture(0)
ret, frame = cap.read()

if not ret:
    print("Ошибка камеры")
    exit()

canvas = np.zeros_like(frame)

prev_x_left, prev_y_left = 0, 0
timestamp = 0


colors = [
    (255, 0, 255),
    (0, 255, 0),
    (255, 0, 0),
    (0, 0, 255),
    (0, 255, 255)
]

selected_color = colors[0]
palette_height = 80
box_width = 100


HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (5,9),(9,10),(10,11),(11,12),
    (9,13),(13,14),(14,15),(15,16),
    (13,17),(17,18),(18,19),(19,20),
    (0,17)
]

def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    result = landmarker.detect_for_video(mp_image, timestamp)
    timestamp += 1

    h, w, _ = frame.shape

    for i, color in enumerate(colors):
        x1 = i * box_width
        x2 = (i + 1) * box_width
        cv2.rectangle(frame, (x1, 0), (x2, palette_height), color, -1)

        if color == selected_color:
            cv2.rectangle(frame, (x1, 0), (x2, palette_height), (255,255,255), 3)

    if result.hand_landmarks:

        for i, hand_landmarks in enumerate(result.hand_landmarks):

            handedness = result.handedness[i][0].category_name

            thumb = hand_landmarks[4]
            index = hand_landmarks[8]

            thumb_x, thumb_y = int(thumb.x * w), int(thumb.y * h)
            index_x, index_y = int(index.x * w), int(index.y * h)

            dist = distance((thumb_x, thumb_y), (index_x, index_y))

            if index_y < palette_height:
                color_index = index_x // box_width
                if 0 <= color_index < len(colors):
                    selected_color = colors[color_index]

            if handedness == "Left":

                if dist < 40 and index_y > palette_height:
                    if prev_x_left == 0 and prev_y_left == 0:
                        prev_x_left, prev_y_left = index_x, index_y

                    cv2.line(canvas,
                             (prev_x_left, prev_y_left),
                             (index_x, index_y),
                             selected_color, 5)

                    prev_x_left, prev_y_left = index_x, index_y
                else:
                    prev_x_left, prev_y_left = 0, 0

            elif handedness == "Right":
                if dist < 40:
                    canvas = np.zeros_like(frame)

            for lm in hand_landmarks:
                x, y = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (x,y), 4, (255,255,255), -1)

            for connection in HAND_CONNECTIONS:
                start = hand_landmarks[connection[0]]
                end = hand_landmarks[connection[1]]
                x1, y1 = int(start.x * w), int(start.y * h)
                x2, y2 = int(end.x * w), int(end.y * h)
                cv2.line(frame, (x1,y1), (x2,y2), (200,200,200), 2)

    frame = cv2.add(frame, canvas)

    cv2.imshow("Air Drawing PRO - Palette Mode", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()