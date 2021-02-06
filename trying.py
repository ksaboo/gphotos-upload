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
imageFolder = 'images3\Photos Another copy'
folders = getFileNames(imageFolder)
session = get_authorized_session('newFile.json')
i = 0
logging.basicConfig(format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I_%M_%S %p',
                    filename='yoloOLD.txt',
                    level=logging.ERROR)
for album in folders:
    albumPath = imageFolder + '/{albumName}'.format(albumName = album)
    images = getFileNames(albumPath)
    paths = []
    for image in images:
        imagePath = albumPath + '/{imageName}'.format(imageName = image)
        paths.append(imagePath)
    print(album)
    #combinedAlbum = album + ' - Combined'
    upload_photos(session, paths, 'Photos Another copy')

print(timer.stop())