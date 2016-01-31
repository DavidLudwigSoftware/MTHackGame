import os
import shutil
import sys


def scanDirectory(dir = os.getcwd()):

    for file in os.listdir(dir):

        if os.path.isdir(os.path.join(dir, file)):

            if file == '__pycache__':

                shutil.rmtree(os.path.join(dir, file))

            else:

                scanDirectory(os.path.join(dir, file))

scanDirectory()
