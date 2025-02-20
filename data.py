from function import *
from time import sleep
import os
import cv2
import numpy as np

# Ensure all A-Z folders exist inside MP_Data
for action in actions:
    action_path = os.path.join(DATA_PATH, action)
    os.makedirs(action_path, exist_ok=True)

# Loop through each action and sequence and create directories to store data
for action in actions:
    for sequence in range(no_sequences):
        sequence_path = os.path.join(DATA_PATH, action, str(sequence))
        os.makedirs(sequence_path, exist_ok=True)  # Ensure sequence folder exists

# Initialize Mediapipe Hands model for hand tracking
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    # Loop through each action
    for action in actions:
        
        # Loop through each sequence (video)
        for sequence in range(no_sequences):
            
            # Loop through each frame in the sequence
            for frame_num in range(sequence_length):

                # Check if image file exists before reading
                image_path = 'Image/{}/{}.png'.format(action, sequence)
                if not os.path.exists(image_path):
                    print(f"Warning: Image {image_path} not found. Skipping...")
                    continue  # Skip this frame if missing

                # Read the frame from the stored images
                frame = cv2.imread(image_path)
                
                # Make detections using the Mediapipe Hands model
                image, results = mediapipe_detection(frame, hands)
                
                # Draw landmarks on the image
                draw_styled_landmarks(image, results)

                # Display messages during data collection
                if frame_num == 0:
                    cv2.putText(image, 'STARTING COLLECTION', (120, 200),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
                    cv2.putText(image, f'Collecting frames for {action} Video Number {sequence}', (15, 12),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.imshow('OpenCV Feed', image)
                    cv2.waitKey(200)
                else:
                    cv2.putText(image, f'Collecting frames for {action} Video Number {sequence}', (15, 12),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.imshow('OpenCV Feed', image)

                # Extract keypoints from the detection results
                keypoints = extract_keypoints(results)

                # Ensure keypoints are not empty (handle missing detections)
                if keypoints is None:
                    keypoints = np.zeros(21 * 3)  # 21 keypoints with (x, y, z) values

                # Define the path to save keypoints in a .npy file
                npy_path = os.path.join(DATA_PATH, action, str(sequence), f"{frame_num}.npy")
                
                # Save the keypoints as a .npy file
                np.save(npy_path, keypoints)

                # Break the loop gracefully if the 'q' key is pressed
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

# Close all OpenCV windows
cv2.destroyAllWindows()
