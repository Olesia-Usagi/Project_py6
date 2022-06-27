import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
BMP_IMAGES = []
GIF_IMAGES = []

MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
FLAC_AUDIO = []

AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
VIDEOS_IN_3GP = []
WEBM_VIDEO = []

DOC_DOCUMENT = []
DOCX_DOCUMENT = []
TXT_DOCUMENT = []
PDF_DOCUMENT = []
XLSX_DOCUMENT = []
PPTX_DOCUMENT = []
MPP_DOCUMENT = []

ARCHIVES = []

APP_TYPE = []
TORRENT_TYPE = []
PY_TYPE = []

OTHER = []

REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'BMP': BMP_IMAGES,
    'GIF': GIF_IMAGES,

    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'FLAC': FLAC_AUDIO,

    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    '3GP': VIDEOS_IN_3GP,
    'WEBM': WEBM_VIDEO,

    'DOC': DOC_DOCUMENT,
    'DOCX': DOCX_DOCUMENT,
    'TXT': TXT_DOCUMENT,
    'PDF': PDF_DOCUMENT,
    'XLSX': XLSX_DOCUMENT,
    'PPTX': PPTX_DOCUMENT,
    'MPP': MPP_DOCUMENT,

    'ZIP': ARCHIVES,
    'RAR': ARCHIVES,
    'GZ': ARCHIVES,
    'ISO': ARCHIVES,
    'TAR': ARCHIVES,

    'EXE': APP_TYPE,
    'TORRENT': TORRENT_TYPE,
    'PY': PY_TYPE
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()
SHOW_ALL_FOUND = []


def get_extension(filename: str) -> str:
    # перетворюємо розширення файла в назві папки .jpg -> JPG
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        # якщо папка то додаємо її у список FOLDERS і переходимо до наступного елементу папки
        if item.is_dir():
            # перевіряємо щоб це не була папка у яку ми вже складаємо файли
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images',
                                 'torrents', 'applications',
                                 'python_files', 'indefinite'):
                FOLDERS.append(item)
                #  скануємо цю вкладену папку - рекурсія
                scan(item)
            continue
        #  робота з файлом
        ext = get_extension(item.name)  # взяти розширення
        fullname = folder / item.name  # повний шлях до файлу
        if not ext:
            OTHER.append(fullname)
            SHOW_ALL_FOUND.append(item.name)
        else:
            try:
                # беремо список у кий покладемо весь шлях до файлу
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
                SHOW_ALL_FOUND.append(item.name)
            except KeyError:
                # Если мы не регистрировали расширение, то добавить в другое
                UNKNOWN.add(ext)
                OTHER.append(fullname)
                SHOW_ALL_FOUND.append(item.name)


if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f'Start in folder {folder_for_scan}')
    scan(Path(folder_for_scan))
    print(f'Types of files in folder:\n{EXTENSIONS}')
    print(f'Unknown files of types: {UNKNOWN}')
    print(FOLDERS[::-1])
