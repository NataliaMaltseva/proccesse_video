0. Скопировать видео в папку video (необязательно, достаточно указать путь до видео в файле .env_template)
1. Указать параметры:
   -Сохранение фрагмента:
    - START_TIME, END_TIME - время фрагмента в минутах.секундах.
   -Сохранение кадров:
    - FRAME_PERIOD - количество пропускаемых кадров при сохранении кадров
3. Переименовать файл .env_template в .env
4. Указать в файле .env время начало и конца фрагмента в минутах.секундах
5. Нарезать видео на фрагменты:
    - запустить скрипт cut_video.py: python cut_video.py
3. Сохранить кадры из фрагмента:
- запустить скрипт saved_frames.py: python saved_frames.py
