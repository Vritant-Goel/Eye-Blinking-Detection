import cv2
import numpy as np
import os
# init video
# dataset = open('mp4all',r)
# cap = cv2.VideoCapture('mp4all/mp4all/000001M_FBN.mp4')





# Function to load and preprocess video frames
def load_and_preprocess_videos(video_folder):
    video_files = os.listdir(video_folder)
    videos = []

    # Iterate through each video file
    for file in video_files:
        video_path = os.path.join(video_folder, file)
        frames = []

        # Load the video
        cap = cv2.VideoCapture(video_path)

        # Read frames until the video ends
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Preprocess frame (e.g., resize, normalize, etc.)
            # Add preprocessing steps as per your requirements

            # Append preprocessed frame to frames list
            frames.append(frame)

        # Release the video capture object
        cap.release()

        # Append frames to videos list
        videos.append(frames)

    return videos





# Specify the path to the folder containing your video files
video_folder = 'mp4all/mp4all'

# Call the function to load and preprocess the videos
video_data = load_and_preprocess_videos(video_folder)
for video in video_data:
    # Iterate through each frame in the video
    for frame in video:
        # Display the frame
        cv2.imshow("Video Frame", frame)

        # Wait for a key press to move to the next frame
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# Close the OpenCV window after displaying all frames
cv2.destroyAllWindows()

# The 'video_data' variable will contain a list of videos, where each video is a list of preprocessed frames
# You can further process and extract features from these frames for training your model


# while True:
#     ret, frame = cap.read()
#     if not ret:
#         continue
#
#
#     cv2.imshow("Video", frame)
#
#
#
#
#
#
#     key_pressed = cv2.waitKey(20) & 0xFF
#     if key_pressed == ord('q'):
#         break
#
#
# cap.release()
# cv2.destroyAllWindows()
