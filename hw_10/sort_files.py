import os
import shutil


class SortFiles:

    def __init__(self, path: str):
        self.path = path

    def sort_files(self) -> None:
        ex_txt = ['txt', 'pdf', 'doc', 'zip', 'csv', 'html']
        ex_video = ['mp4', 'avi', 'mkv']
        ex_images = ['jpeg', 'bmp', 'gif']
        path, dirs, files = next(os.walk(self.path))
        for file in files:
            f = file.split('.')[-1]
            if f in ex_txt:
                shutil.move(os.path.join(path, file), 'C:\\Users\Serge\\Documents')
            elif f in ex_video:
                shutil.move(os.path.join(path, file), 'C:\\Users\Serge\\Videos')
            elif f in ex_images:
                shutil.move(os.path.join(path, file), 'C:\\Users\Serge\\Images')
            else:
                continue


if __name__ == '__main__':
    path = 'C:\\Users\Serge\\Downloads'
    s_f = SortFiles(path)
    s_f.sort_files()
