import os
import logging
from dotenv import load_dotenv
import cv2

load_dotenv()

saved_path = os.getenv("SAVEPATHFRAME")
videos_path = [os.getenv("VIDEOPATH")]
fp = int(os.getenv("FRAME_PREIOD"))
print(f"Process {videos_path} video")
# start index
i = 75123
# сколько кадров пропускать
key = 0
# count frame
num_frame = 2000
count_frames = 1
for video_file in videos_path:
    print(f"Process {video_file} video")
    cap = cv2.VideoCapture(video_file)
    while 1:
        ret, frame = cap.read()
        if not ret:
            break
        uuid_name = f"images_{i}_p2.jpg"

        if key % fp == 0:
            logging.info(f"{uuid_name} saved")
            image_path = f"{saved_path}/{str(uuid_name)}"
            cv2.imwrite(image_path, frame)
            count_frames += 1
            if count_frames >= num_frame:
                break
        i += 1
        key += 1
    print("Done.")
