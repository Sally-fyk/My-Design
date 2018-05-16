from pycocotools.coco import COCO 
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt 
import pylab
pylab.rcParams['figure.figsize'] = (8.0, 10.0)
dataDir='/root/noc'
dataType='val2014'  
# initialize COCO api for caption annotations\n",
annFile = '{}/annotations/captions_{}.json'.format(dataDir,dataType)
coco=COCO(annFile)

file = open('coco2014_cocoid.val.txt')
f=open('id_captions_val.txt','a')
line = file.readline()
line = line.strip()

while line:
    line = int(line)
    print('id:',line)

    imgIds = coco.getImgIds(imgIds = [line])
    img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]
    # load and display caption annotations\n",
    annIds = coco.getAnnIds(imgIds=img['id'])
    anns = coco.loadAnns(annIds)
    image_id = str(line)
    
    for i in range(5):
        f.write(image_id)
        f.write('    ')
        f.write(anns[i]['caption'])
        f.write('\n')
    line = file.readline()

    #coco.showAnns(anns)
file.close()
f.close()