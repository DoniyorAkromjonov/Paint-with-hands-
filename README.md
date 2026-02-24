# ✋🎨 Paint-with-hands

Air drawing application using OpenCV and MediaPipe Hand Landmarker.  
Draw in the air with your fingers, select colors from a palette, and clear the canvas using hand gestures in real-time.

---

## 🚀 Features

- ✏️ Draw in the air using pinch gesture (thumb + index finger)
- 🎨 5-color interactive palette
- 🖐 Left hand → Drawing mode
- 🖐 Right hand → Clear canvas
- 🧠 Real-time hand tracking (supports 2 hands)
- 📹 Live webcam input
- 🔥 Smooth drawing experience

---

## 🛠 Technologies Used

- Python 3.9+
- OpenCV
- MediaPipe Tasks API
- NumPy
- Math

---

## 📦 Installation

### 1️⃣ Clone the repository

git clone https://github.com/yourusername/Paint-with-hands.git
cd Paint-with-hands


2️⃣ Install dependencies
pip install opencv-python mediapipe numpy
3️⃣ Download MediaPipe Model

Download the official model file:

hand_landmarker.task

Place it in the root folder of the project.

▶️ Run the Project
python main.py

Press ESC to exit the application.

🎮 Controls
Gesture	Action
🤏 Left hand pinch	Draw
🤏 Right hand pinch	Clear canvas
☝ Move finger to top palette	Select color
ESC key	Exit
🧠 How It Works
Hand Detection

The program initializes MediaPipe Hand Landmarker:

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=2
)

landmarker = HandLandmarker.create_from_options(options)
Pinch Gesture Detection
def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

dist = distance((thumb_x, thumb_y), (index_x, index_y))

If the distance between thumb and index finger is small → drawing starts.

Drawing on Canvas
cv2.line(canvas,
         (prev_x_left, prev_y_left),
         (index_x, index_y),
         selected_color, 5)

The drawing layer is merged with the webcam frame:

frame = cv2.add(frame, canvas)
📁 Project Structure
Paint-with-hands/
│
├── main.py
├── hand_landmarker.task
├── README.md
└── requirements.txt
🧩 Future Improvements

Adjustable brush size

Eraser mode

Save drawing as image

More color options

Gesture-based brush thickness

UI improvements

FPS counter

🎯 Use Cases

Computer Vision portfolio project

AI / ML learning

Gesture-based UI experiments

Interactive installations

University applications
