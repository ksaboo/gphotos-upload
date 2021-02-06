from upload import upload_photos,get_authorized_session
from os import listdir
from tqdm import tqdm
from timer import Timer
import logging
import logging.config

timer = Timer()
timer.start()
def getFileNames(dire):
    names = listdir(dire)
    return names
imageFolder = 'Scanned Photos'
folders = getFileNames(imageFolder)
session = get_authorized_session('newFile.json')
i = 0
logging.basicConfig(format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I_%M_%S %p',
                    filename='yoloOLDER.txt',
                    level=logging.ERROR)
for album in folders:
    albumPath = imageFolder + '/{albumName}'.format(albumName = album)
    images = getFileNames(albumPath)
    pathsRestored = []
    pathsOriginal = []
    for image in images:
        imagePath = albumPath + '/{imageName}'.format(imageName = image)
        if image[-5] == 'a':
            pathsRestored.append(imagePath)
        else:
            pathsOriginal.append(imagePath)
    print(album)
    originalAlbum = album + ' - Original'
    restoredAlbum = album + ' - Restored'
    upload_photos(session, pathsOriginal, originalAlbum)
    upload_photos(session, pathsRestored, restoredAlbum)

print(timer.stop())