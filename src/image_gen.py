#!/usr/bin/env python3

from PIL import Image
from os import path

def generateResponsiveImages(configs, splittedFilePath):
    image = Image.open(splittedFilePath['fullPath'])
    base_width = image.size[0]
    base_height = image.size[1]

    readyImages = []

    for config in configs:
        newFileName = f"{splittedFilePath['filename']}{config['suffix']}{splittedFilePath['extension']}"

        if(isinstance(config['size'], list)):
            newWidth    = int( config['size'][0] )
            newHeight   = int( config['size'][1] )
            
        else:
            newWidth    = int( (base_width  * config['size']) / 100)
            newHeight   = int( (base_height * config['size']) / 100)

        if(newWidth < 5 or newHeight < 5): # if the file is too small
            print(f"Error: {newFileName} is too small, skipping...")
    
        else:
            imageObject = {
                "image":    image.resize((newWidth, newHeight), Image.ANTIALIAS),
                "filename": newFileName
            }
            readyImages.append(imageObject)
            print(f"{splittedFilePath['filename']}{splittedFilePath['extension']}: Created {config['suffix']} image - {newWidth} X {newHeight}")

    return readyImages

# Output : 
# {
#   image: PIL Object,
#   filename: new filename
# }

def saveResponsiveImage(image, outputDirectory):
    image['image'].save(path.join(outputDirectory, image['filename']))
    print(f"{image['filename']} has been saved to {outputDirectory}")