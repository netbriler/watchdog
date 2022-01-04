import shutil
from pathlib import Path

from watchdog.events import FileSystemEventHandler

from utils.logging import logger


class Handler(FileSystemEventHandler):
    def __init__(self, track_folder, dest_folder):
        self.track_folder = Path(track_folder)
        self.dest_folder = Path(dest_folder)

    def on_modified(self, event=None):
        for file in self.track_folder.glob('*.*'):
            if not file.is_file():
                continue

            file_extension = file.suffix.lower()

            extension_folder = 'else/'
            if file_extension in ['.jpg', '.jpeg', '.png', '.tiff', '.tif', '.svg', '.gif']:
                extension_folder = 'images/'

            if file_extension in ['.mp3' '.wav', '.aiff', '.aac', '.wma']:
                extension_folder = 'audios/'

            if file_extension in ['.mp4', '.3gp', '.ogg', '.wmv', '.webm', '.flv', '.avi', '.oga']:
                extension_folder = 'videos/'

            if file_extension in ['.exe']:
                extension_folder = 'programs/'

            if file_extension in ['.rar', '.rar4', '.zip', '.zipx', '.7z', '.tar', '.tar.gz', '.tgz', '.tar.Z',
                                  '.tar.bz2', '.tbz2', '.tar.lz', '.tlz', '.tar.xz', '.txz']:
                extension_folder = 'archives/'

            if file_extension in ['.doc', '.docx', '.pdf', '.odt', '.xls', '.xlsx', '.xml', '.json', '.ods', '.ppt',
                                  '.pptx', '.txt', '.epub']:
                extension_folder = 'documents/'

            directory = self.dest_folder / extension_folder

            if not directory.exists():
                directory.mkdir(parents=True, exist_ok=True)

            new_path = directory / file.name

            try:
                shutil.move(file, new_path)
                logger.debug(f'"{file.name}" moved to ------> "{directory}"')
            except Exception as e:
                logger.error(f'"{file.name}" "{new_path}" {e}')
