import cv2
import logging
from pathlib import Path
import uuid

videos_path = Path("/media/nataly/STORAGE/Nataly_projects/PIRS/video/20.08.24_fix_cam_7m")
saved_path = Path("/media/nataly/STORAGE/Nataly_projects/Datasets/ball_fix_cam")

# сколько кадров пропускать
key = 0
fp = 3
count_frames = 1
max_count_frames = 2000
for video_file in videos_path.iterdir():
    video_name = video_file.stem
    saved_path_subfolder = saved_path.joinpath(str(video_name))
    saved_path_subfolder.mkdir(parents=True, exist_ok=True)
    print(f"Process {video_file} video")
    cap = cv2.VideoCapture(str(video_file))
    while 1:
        ret, frame = cap.read()
        if not ret:
            break
        
        if key % fp == 0:
            uuid_name = f"{video_file.stem}_{str(uuid.uuid4())}.jpg"
            logging.info(f"{uuid_name} saved")
            image_path = saved_path_subfolder.joinpath(str(uuid_name))
            cv2.imwrite(str(image_path), frame)
            count_frames += 1
            
        if max_count_frames<=count_frames:
            break
        
        key += 1
    print("Done.")
