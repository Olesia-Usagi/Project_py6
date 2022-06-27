from pathlib import Path, PurePath
import shutil
import sys
import collector
from normalize import normalize
import os


def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_add_on_stuff(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_another_of_types(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_archives(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()), str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'\tDIRECTED BY:')
        print('\tRobert B Weide')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folders(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Oops, the things gone wrong with -- {folder}')


def main(folder: Path):
    collector.searcher(folder)

    for file in collector.JPEG_IMAGES:
        handle_media(file, folder / 'images')
        print(f'{file.name:<40} |{"in":^4} | {"image folder":>13}'.format())
    for file in collector.JPG_IMAGES:
        handle_media(file, folder / 'images')
        print(f'{file.name:<40} |{"in":^4} | {"image folder":>13}'.format())
    for file in collector.PNG_IMAGES:
        handle_media(file, folder / 'images')
        print(f'{file.name:<40} |{"in":^4} | {"image folder":>13}'.format())
    for file in collector.SVG_IMAGES:
        handle_media(file, folder / 'images')
        print(f'{file.name:<40} |{"in":^4} | {"image folder":>13}'.format())
    for file in collector.BMP_IMAGES:
        handle_media(file, folder / 'images')
        print(f'{file.name:<40} |{"in":^4} | {"image folder":>13}'.format())
    ...
    for file in collector.MP3_AUDIO:
        handle_media(file, folder / 'audio')
        print(f'{file.name:<40} |{"in":^4} | {"audio folder":>13}'.format())
    for file in collector.WAV_AUDIO:
        handle_media(file, folder / 'audio')
        print(f'{file.name:<40} |{"in":^4} | {"audio folder":>13}'.format())
    for file in collector.OGG_AUDIO:
        handle_media(file, folder / 'audio')
        print(f'{file.name:<40} |{"in":^4} | {"audio folder":>13}'.format())
    for file in collector.AMR_AUDIO:
        handle_media(file, folder / 'audio')
        print(f'{file.name:<40} |{"in":^4} | {"audio folder":>13}'.format())
    for file in collector.FLAC_AUDIO:
        handle_media(file, folder / 'audio')
        print(f'{file.name:<40} |{"in":^4} | {"audio folder":>13}'.format())
    ...
    for file in collector.MP4_VIDEOS:
        handle_media(file, folder / 'video')
        print(f'{file.name:<40} |{"in":^4} | {"video folder":>13}'.format())
    for file in collector.VIDEOS_IN_3GP:
        handle_media(file, folder / 'video')
        print(f'{file.name:<40} |{"in":^4} | {"video folder":>13}'.format())
    for file in collector.AVI_VIDEOS:
        handle_media(file, folder / 'video')
        print(f'{file.name:<40} |{"in":^4} | {"video folder":>13}'.format())
    for file in collector.MOV_VIDEOS:
        handle_media(file, folder / 'video')
        print(f'{file.name:<40} |{"in":^4} | {"video folder":>13}'.format())
    for file in collector.MKV_VIDEOS:
        handle_media(file, folder / 'video')
        print(f'{file.name:<40} |{"in":^4} | {"video folder":>13}'.format())
    ...
    for file in collector.DOC_DOCS:
        handle_media(file, folder / 'documents')
        print(f'{file.name:<40} |{"in":^4} | {"documents folder":>18}'.format())
    for file in collector.DOCX_DOCS:
        handle_media(file, folder / 'documents')
        print(f'{file.name:<40} |{"in":^4} | {"documents folder":>18}'.format())
    for file in collector.MPP_DOCS:
        handle_media(file, folder / 'documents')
        print(f'{file.name:<40} |{"in":^4} | {"documents folder":>18}'.format())
    for file in collector.PDF_DOCS:
        handle_media(file, folder / 'documents')
        print(f'{file.name:<40} |{"in":^4} | {"documents folder":>18}'.format())
    for file in collector.PPTX_DOCS:
        handle_media(file, folder / 'documents')
        print(f'{file.name:<40} |{"in":^4} | {"documents folder":>18}'.format())
    for file in collector.XLSX_DOCS:
        handle_media(file, folder / 'documents')
        print(f'{file.name:<40} |{"in":^4} | {"documents folder":>18}'.format())
    for file in collector.TXT_DOCS:
        handle_media(file, folder / 'documents')
        print(f'{file.name:<40} |{"in":^4} | {"documents folder":>18}'.format())
    ...
    for file in collector.TORRENT_TYPE:
        handle_add_on_stuff(file, folder / 'torrents')
        print(f'{file.name:<40} |{"in":^4} | {"torrents folder":>15}'.format())
    for file in collector.APP_TYPE:
        handle_add_on_stuff(file, folder / 'applications')
        print(f'{file.name:<40} |{"in":^4} | {"applications folder":>19}'.format())
    for file in collector.PYTHON_TYPE:
        handle_add_on_stuff(file, folder / 'python_files(scripts)')
        print(f'{file.name:<40} |{"in":^4} | {"scripts folder":>14}'.format())
    ...
    for file in collector.ANOTHER_TYPES:
        handle_another_of_types(file, folder / 'uncertain_types')
        print(f'{file.name:<40} |{"in":^4} | {"folder for unknown types":>20}'.format())
    ...
    for file in collector.ZIP_ARCHIVES:
        handle_archives(file, folder / 'archives')
        print(f'{file.name:<40} |{"in":^4} | {"archives folder":>15}'.format())
    for file in collector.ISO_ARCHIVES:
        handle_archives(file, folder / 'archives')
        print(f'{file.name:<40} |{"in":^4} | {"archives folder":>15}'.format())
    for file in collector.RAR_ARCHIVES:
        handle_archives(file, folder / 'archives')
        print(f'{file.name:<40} |{"in":^4} | {"archives folder":>15}'.format())
    for file in collector.GZ_ARCHIVES:
        handle_archives(file, folder / 'archives')
        print(f'{file.name:<40} |{"in":^4} | {"archives folder":>15}'.format())
    for file in collector.TAR_ARCHIVES:
        handle_archives(file, folder / 'archives')
        print(f'{file.name:<40} |{"in":^4} | {"archives folder":>15}'.format())
    ...
    for folder in collector.FOLDERS[::-1]:
        handle_folders(folder)


def start():
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        print(f'Start in folder {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())


if __name__ == '__main__':
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        print(f'Sorting will start in folder -- {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())
        print('Names of all files was changed from cyrillic to latin.')
        print(f'And so we have this extentions in this folder:\n{collector.EXTENTIONS}')
        print(f'And files with this extentions we couldnt sort:\n{collector.UNKNOWN}')
