import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DIR = os.path.dirname(os.path.abspath(__file__))


class Handler(FileSystemEventHandler):
    folder_track = 'D:/Загрузки'
    folder_dest = 'D:/Загрузки'

    def on_modified(self, event):
        for filename in os.listdir(self.folder_track):
            file = self.folder_track + '/' + filename
            file_extension = os.path.splitext(file)[1]

            if os.path.isfile(file):
                extension_folder = '/else/'
                if file_extension in ['.jpg', '.jpeg', '.png', '.tiff', '.tif', '.svg', '.gif']:
                    extension_folder = '/images/'

                if file_extension in ['.mp3' '.wav', '.aiff', '.aac', '.wma']:
                    extension_folder = '/audios/'

                if file_extension in ['.mp4', '.3gp', '.ogg', '.wmv', '.webm', '.flv', '.avi', '.oga']:
                    extension_folder = '/videos/'

                if file_extension in ['.exe']:
                    extension_folder = '/programs/'

                if file_extension in ['.rar', '.rar4', '.zip', '.zipx', '.7z', '.tar', '.tar.gz', '.tgz', '.tar.Z', '.tar.bz2',
                                      '.tbz2', '.tar.lz', '.tlz', '.tar.xz', '.txz']:
                    extension_folder = '/archives/'

                if file_extension in ['.doc', '.docx', '.pdf', '.odt', '.xls', '.xlsx', '.xml', '.json', '.ods', '.ppt', '.pptx',
                                      '.txt', '.epub']:
                    extension_folder = '/documents/'

                directory = self.folder_dest + extension_folder

                if not os.path.exists(directory):
                    os.makedirs(directory)

                new_path = directory + filename
                os.rename(file, new_path)
                logging.info('"{}" moved to ------> "{}"'.format(file, directory))


handle = Handler()
observer = Observer()
observer.schedule(handle, handle.folder_track, recursive=True)
observer.start()

if __name__ == "__main__":
    print('''
░██╗░░░░░░░██╗██╗░░██╗░█████╗░████████╗░█████╗░██╗░░██╗██████╗░░█████╗░░██████╗░
░██║░░██╗░░██║██║░░██║██╔══██╗╚══██╔══╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██╔════╝░
░╚██╗████╗██╔╝███████║███████║░░░██║░░░██║░░╚═╝███████║██║░░██║██║░░██║██║░░██╗░
░░████╔═████║░██╔══██║██╔══██║░░░██║░░░██║░░██╗██╔══██║██║░░██║██║░░██║██║░░╚██╗
░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║██████╔╝╚█████╔╝╚██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░░╚═════╝░
    ''')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[logging.FileHandler(filename=DIR + '/debug.log', encoding='utf-8', mode='a+')])
    logging.info("Program started")

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Program stopped")
        exit()

    observer.join()