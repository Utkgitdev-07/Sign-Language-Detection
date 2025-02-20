# ✋ Sign Language Detection using Deep Learning 🤖  

## 📌 Project Overview 
This project is a **real-time sign language recognition system** that uses **OpenCV, Mediapipe, and an LSTM-based neural network** to detect and recognize hand gestures.  

✅ **If you have already collected data and trained the model, you ONLY need to run:**  

python app.py

🚀 No need to run collectdata.py, data.py, or trainmodel.py again unless you want to add new gestures!

## 📂 Project Structure

sign-language-detection/
│── 📂 Image/         # Stores captured images (A-Z folders)
│── 📂 Logs/          # Stores TensorBoard logs for training visualization
│── 📂 MP_Data/       # Stores processed `.npy` files used for training
│── 📂 Screenshots/   # Stores images of working examples (upload here)
│── 📜 app.py         # Runs real-time hand sign detection
│── 📜 collectdata.py # Captures images from webcam and saves them in Image/
│── 📜 data.py        # Converts images to `.npy` format
│── 📜 trainmodel.py  # Trains the LSTM model using the `.npy` files
│── 📜 function.py    # Helper functions for image processing & detection
│── 📜 model.json     # Stores the trained model architecture
│── 📜 model.h5       # Stores trained model weights
│── 📜 commands.txt   # Instructions for running the project
│── 📜 README.md      # Project documentation

## 🚀 Running the Project

**Directly Run Sign Detection**
👉 If you already have a trained model (model.json and model.h5), simply run the following command to start detection:--python app.py

-> The webcam will open and detect hand signs in real-time.
-> The recognized sign will be displayed on the screen.
-> Press 'q' to exit.

## 🖼️ Screenshots & Working Demonstration
📌 Upload screenshots of  project working inside the Screenshots/ folder.

📷 Example Screenshots:
Gesture Detection	Screenshots\{66D8AA31-067B-4CAF-82C4-3FE029783F2E}.png
Model Training      Screenshots\{59760626-581D-46BF-8D92-B5ECAF4D5275}.png

## ⚙️ When Should You Run Other Scripts?

Script Name	                                  Run it when...
collectdata.py	                   You want to add new gesture images to train.
data.py	                           You have collected new images and need .npy files.
trainmodel.py	                   You want to retrain the model with new data.
Otherwise, just run app.py         for sign detection! ✅


## 🛠️ Full Setup (Only If Adding New Data)

**1️⃣ Install Dependencies**
Make sure you have Python 3.x installed. Then install the required libraries:
---> pip install opencv-python numpy mediapipe tensorflow keras

**2️⃣ (ONLY IF ADDING NEW DATA) Collect Gesture Images**
Run this command to capture new hand gesture images from the webcam:
---> python collectdata.py

-> The webcam will open.
-> Make a sign & press the corresponding key (A-Z) to save images.
-> Each keypress saves one image.
**3️⃣ (ONLY IF ADDING NEW DATA) Convert Images to .npy Data**
---> python data.py

-> Processes collected images and extracts hand keypoints.
-> Saves .npy files in MP_Data/ for model training.

**4️⃣ (ONLY IF ADDING NEW DATA) Train the Model**
---> python trainmodel.py

-> Loads .npy files from MP_Data/.
-> Trains an LSTM-based neural network to recognize gestures.
-> Saves the trained model as model.json and model.h5.

## 🛠️ Troubleshooting & Common Errors
❌ FileNotFoundError: 'MP_Data/A/24/14.npy' not found
✅ Run python collectdata.py again to ensure all gestures are recorded.
✅ Run python data.py to regenerate missing .npy files.

❌ Model not detecting gestures?
✅ Ensure model.json and model.h5 exist.
✅ Train the model again using python trainmodel.py.

## 🎯 How the Project Works
1️⃣ Image Collection (collectdata.py)
📌 Captures images for different gestures and stores them in Image/{A-Z}/.

2️⃣ Data Processing (data.py)
📌 Converts images into numerical .npy files using Mediapipe keypoints.
📌 Saves processed data in MP_Data/{A-Z}/.

3️⃣ Model Training (trainmodel.py)
📌 Loads .npy data and trains an LSTM-based neural network.
📌 Saves model as model.json & model.h5.

4️⃣ Real-time Prediction (app.py)
📌 Opens a webcam, tracks hand gestures, and predicts signs live.


