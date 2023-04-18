import glob, os

class PathFinder:
    fileName=""
    def __init__(self,fileName):
        self.fileName = fileName

    def find(self):
        os.chdir("./project")
        path=""
        for filePath in glob.glob("**/"+self.fileName,recursive=True):
            path=filePath

        return path

