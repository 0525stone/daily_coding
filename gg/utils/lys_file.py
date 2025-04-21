"""
utils of functions related to os.

"""
import os

def list_from_dir(dirname):
    filelist = os.listdir(dirname)
    filelist = sorted(filelist, key=lambda x: os.path.getmtime(os.path.join(dirname, x)))
    return filelist