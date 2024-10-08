import shutil
from pathlib import Path
import random
import logging

class RandomChoosed():
    def __init__(self) -> None:
        logging.basicConfig(filename="import_logs.log", level=logging.INFO)
        self.logs = logging.getLogger(name=__name__)
        self.image_folder = Path("/media/nataly/STORAGE/Nataly_projects/Datasets/ball_fix_cam")
        self.folders = list(self.image_folder.iterdir())

        self.saved_path = Path("/media/nataly/STORAGE/Nataly_projects/Datasets/random_choosed_fix_cam")
        self.count_files = 2000

    def choose_files(self):
        i = 0
        while i<self.count_files:
            folder = random.choice(self.folders)
            self.logs.info(f"{folder}")
            files = list(folder.iterdir())
            if len(files)>0:
                file = random.choice(files)
                self.logs.info(f"{file}")
                try:
                    shutil.copy(file,self.saved_path.joinpath(file.name))
                    i+=1
                except:
                    self.logs.info(f"{file} repeated")
            else:
                self.logs.info(f"{folder} is empty")       


if __name__=="__main__":
    rnd_choose = RandomChoosed()
    rnd_choose.choose_files()
