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
