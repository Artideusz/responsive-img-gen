#!/usr/bin/env python3

from os import walk, path
import re

#PRaca tuu

def listOutFilePaths(inputDirectoryPath, outputDirectoryPath):
    paths = []
    
    for root, _, files in walk(inputDirectoryPath):
            # All folders that are in the input dir path
            relativeDirectoryPath = root[len(inputDirectoryPath):]

            for filename in files:
                if(filename.lower().endswith(('jpeg','jpg','webp','tiff','png','bmp'))):
                    inputPath = path.join(root, filename)
                    outputPath = path.join(outputDirectoryPath, relativeDirectoryPath, filename)

                    paths.append({
                        'inputLocation': splitFilePath(inputPath),
                        'outputLocation': splitFilePath(outputPath)
                    })
                    

    return paths

def splitFilePath(str):
    splittedPath = re.findall(r'((.*)\/(.+)(\..+))', str)[0]
    
    return {
        'fullPath':     splittedPath[0],
        'folder':       splittedPath[1],
        'filename':     splittedPath[2],
        'extension':    splittedPath[3]
    }