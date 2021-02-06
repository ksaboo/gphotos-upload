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
session = get_authorized_session('newFile.json')
i = 0
logging.basicConfig(format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I_%M_%S %p',
                    filename='yoloOLD2.txt',
                    level=logging.ERROR)


imageFolders = ['images3/Photos Unsorted']
imageFolders = ['images3/Photos Unsorted','images3\Photos Another copy','images3/Photos Unsorted Nov 2012/pics']
imageFolders = ['images3/Raghav Shadi','images3/Raghav Shadi/Wedding']
imageFolders = ['d/BaiPhotosFolders']
for imageFolder in imageFolders:
    folders = getFileNames(imageFolder)
    folderName = imageFolder.split('/')[-1]
    print(folderName)
    for album in folders:
        albumPath = imageFolder + '/{albumName}'.format(albumName = album)
        images = getFileNames(albumPath)
        paths = []
        for image in images:
            imagePath = albumPath + '/{imageName}'.format(imageName = image)
            paths.append(imagePath)
        print(album)
        #combinedAlbum = album + ' - Combined'
        upload_photos(session, paths, 'Bai Photos')

print(timer.stop())