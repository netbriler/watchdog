import argparse
import time
from pathlib import Path

from watchdog.observers import Observer

from handler import Handler
from utils.logging import logger

parser = argparse.ArgumentParser(description='Simple auto sorting files')
parser.add_argument('-t', help='Which folder should you track?', required=True)
parser.add_argument('-d', help='Which folder should you put sorted files?', required=True)

args = parser.parse_args()

track_folder = Path(args.t)
dest_folder = Path(args.d)

if not track_folder.exists():
    track_folder.mkdir(parents=True, exist_ok=True)

if not dest_folder.exists():
    dest_folder.mkdir(parents=True, exist_ok=True)

handle = Handler(track_folder, dest_folder)

observer = Observer()
observer.schedule(handle, track_folder, recursive=True)
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
    logger.info('Program started')

    handle.on_modified()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
        logger.info('Program stopped')
        exit()

    observer.join()
