from pathlib import Path, PurePath
import shutil
import sys
import file_parser as parser
from normalize import normalize
import os


def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_documents(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_add_on_stuff(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_other(filename: Path, target_folder: Path):
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
        print(f'is not an archive {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folders(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'The {folder} could not be deleted.')


def main(folder: Path):
    parser.scan(folder)

    for file in parser.JPEG_IMAGES:
        handle_media(file, folder / 'images')
        print(f'{file.name:<40} |{"in":^4} | {"image folder":>13}'.format())
    for file in parser.JPG_IMAGES:
        handle_media(file, folder / 'images')
        print(f'{file.name:<40} |{"in":^4} | {"image folder":>13}'.format())
    for file in parser.PNG_IMAGES:
        handle_media(file, folder / 'images')
        print(f'{file.name:<40} |{"in":^4} | {"image folder":>13}'.format())
    for file in parser.SVG_IMAGES:
        handle_media(file, folder / 'images')
        print(f'{file.name:<40} |{"in":^4} | {"image folder":>13}'.format())
    for file in parser.BMP_IMAGES:
        handle_media(file, folder / 'images')
        print(f'{file.name:<40} |{"in":^4} | {"image folder":>13}'.format())
    for file in parser.GIF_IMAGES:
        handle_media(file, folder / 'images')
        print(f'{file.name:<40} |{"in":^4} | {"image folder":>13}'.format())
    ...
    for file in parser.MP3_AUDIO:
        handle_media(file, folder / 'audio')
        print(f'{file.name:<40} |{"in":^4} | {"audio folder":>13}'.format())
    for file in parser.WAV_AUDIO:
        handle_media(file, folder / 'audio')
        print(f'{file.name:<40} |{"in":^4} | {"audio folder":>13}'.format())
    for file in parser.OGG_AUDIO:
        handle_media(file, folder / 'audio')
        print(f'{file.name:<40} |{"in":^4} | {"audio folder":>13}'.format())
    for file in parser.AMR_AUDIO:
        handle_media(file, folder / 'audio')
        print(f'{file.name:<40} |{"in":^4} | {"audio folder":>13}'.format())
    for file in parser.FLAC_AUDIO:
        handle_media(file, folder / 'audio')
        print(f'{file.name:<40} |{"in":^4} | {"audio folder":>13}'.format())
    ...
    for file in parser.MP4_VIDEO:
        handle_media(file, folder / 'video')
        print(f'{file.name:<40} |{"in":^4} | {"video folder":>13}'.format())
    for file in parser.VIDEOS_IN_3GP:
        handle_media(file, folder / 'video')
        print(f'{file.name:<40} |{"in":^4} | {"video folder":>13}'.format())
    for file in parser.AVI_VIDEO:
        handle_media(file, folder / 'video')
        print(f'{file.name:<40} |{"in":^4} | {"video folder":>13}'.format())
    for file in parser.MOV_VIDEO:
        handle_media(file, folder / 'video')
        print(f'{file.name:<40} |{"in":^4} | {"video folder":>13}'.format())
    for file in parser.MKV_VIDEO:
        handle_media(file, folder / 'video')
        print(f'{file.name:<40} |{"in":^4} | {"video folder":>13}'.format())
    for file in parser.WEBM_VIDEO:
        handle_media(file, folder / 'video')
        print(f'{file.name:<40} |{"in":^4} | {"video folder":>13}'.format())
    ...
    for file in parser.DOC_DOCUMENT:
        handle_documents(file, folder / 'documents')
        print(f'{file.name:<40} |{"in":^4} | {"documents folder":>18}'.format())
    for file in parser.DOCX_DOCUMENT:
        handle_documents(file, folder / 'documents')
        print(f'{file.name:<40} |{"in":^4} | {"documents folder":>18}'.format())
    for file in parser.MPP_DOCUMENT:
        handle_documents(file, folder / 'documents')
        print(f'{file.name:<40} |{"in":^4} | {"documents folder":>18}'.format())
    for file in parser.PDF_DOCUMENT:
        handle_documents(file, folder / 'documents')
        print(f'{file.name:<40} |{"in":^4} | {"documents folder":>18}'.format())
    for file in parser.PPTX_DOCUMENT:
        handle_documents(file, folder / 'documents')
        print(f'{file.name:<40} |{"in":^4} | {"documents folder":>18}'.format())
    for file in parser.XLSX_DOCUMENT:
        handle_documents(file, folder / 'documents')
        print(f'{file.name:<40} |{"in":^4} | {"documents folder":>18}'.format())
    for file in parser.TXT_DOCUMENT:
        handle_documents(file, folder / 'documents')
        print(f'{file.name:<40} |{"in":^4} | {"documents folder":>18}'.format())
    ...
    for file in parser.TORRENT_TYPE:
        handle_add_on_stuff(file, folder / 'torrents')
        print(f'{file.name:<40} |{"in":^4} | {"torrents folder":>15}'.format())
    for file in parser.APP_TYPE:
        handle_add_on_stuff(file, folder / 'applications')
        print(f'{file.name:<40} |{"in":^4} | {"applications folder":>19}'.format())
    for file in parser.PY_TYPE:
        handle_add_on_stuff(file, folder / 'python_files(scripts)')
        print(f'{file.name:<40} |{"in":^4} | {"scripts folder":>14}'.format())
    ...
    for file in parser.OTHER:
        handle_other(file, folder / 'uncertain_types')
        print(f'{file.name:<40} |{"in":^4} | {"unknown types":>20}'.format())
    ...
    for file in parser.ARCHIVES:
        handle_archives(file, folder / 'archives')
        print(f'{file.name:<40} |{"in":^4} | {"archives folder":>15}'.format())
    ...
    # Выполняем реверс списка для того, чтобы все папки удалить
    for folder in parser.FOLDERS[::-1]:
        handle_folders(folder)


def start():
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        print(f'Start in folder {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())


if __name__ == '__main__':
    # інформацію про роботу в деталях
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        print(f'Start in folder {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())
        print('Names of files was changed to latin.')
        print(f'Show all sorted extensions :\n{parser.EXTENSIONS}')
        print(f'Unknown files of types:\n{parser.UNKNOWN}')
