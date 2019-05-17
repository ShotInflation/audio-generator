import os
import sys

import re
from mutagen.mp3 import MP3

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def main(argv):
    assert len(argv) == 2, "Usage: python folder_scan.py folder"
    folder = argv[1]
    files = os.listdir(folder)
    files.sort(key=natural_keys)
    print "FILES = {"
    for filename in files:
        if filename.endswith(".mp3"):
            name = os.path.splitext(filename)[0].upper()
            length = MP3(os.path.join(folder, filename)).info.length
            print '    "{name}": AudioFile("{filename}", {seconds}, None),'.format(
                name=name,
                filename=filename,
                seconds=str(int(length))
            )
    print "}"
    return 0


if __name__ == '__main__':
    exit(main(sys.argv))