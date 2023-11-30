import os

from moviepy.tools import subprocess_call
from moviepy.config import get_setting
from dotenv import load_dotenv

def ffmpeg_extract_subclip(filename: str, t1: float, t2: float, saved_path: str = "video", targetname: str = None):
    """
    Makes a new video file playing video file ``filename`` between
    the times ``t1`` in minutes and ``t2``  in minutes.
    """
    os.makedirs(saved_path, exist_ok=True)

    if t2 < t1:
        print(f"Некорректный интервал времени!")
        return None
    basename = os.path.basename(filename)
    name, ext = os.path.splitext(basename)
    min_t = [int(t) for t in [t1, t2]]
    sec_t = [int(round(t % 1, 2) * 100) for t in [t1, t2]]
    T1, T2 = [int(60 * m) + (s) for m, s in zip(min_t, sec_t)]
    if not targetname:  
        save_video_path = os.path.join(saved_path,"%sSUB%d_%d.%s" % (name, T1, T2, ext[1:]))
    else:
        save_video_path = os.path.join(saved_path,targetname)

    cmd = [
        get_setting("FFMPEG_BINARY"),
        "-y",
        "-ss",
        "%0.2f" % T1,
        "-i",
        filename,
        "-t",
        "%0.2f" % (T2 - T1),
        "-vcodec",
        "copy",
        "-acodec",
        "copy",
        save_video_path,
    ]
    try:
        subprocess_call(cmd)
    except ValueError:
        print(f"{ValueError}")
        return None

    return 1


if __name__ == "__main__":
    load_dotenv()
    saved_path = os.getenv("SAVEPATHSEGMENTS")
    video_path = os.getenv("VIDEOPATH")
    # начало фрагмента. Формат: минуты.секунды
    try:
        start_time = float(os.getenv("START_TIME"))
        try:
            # конец фрагмента. Формат: минуты.секунды
            end_time = float(os.getenv("END_TIME"))
            result = ffmpeg_extract_subclip(filename=video_path, t1=start_time, t2=end_time, saved_path=saved_path)
            if result is not None:
                print("Done!")
            else:
                print("Error!")
        except ValueError:
            print(f"Не правильно задан конец отрезка. {ValueError}")
    except ValueError:
        print(f"Не правильно задано начало отрезка. {ValueError}")
