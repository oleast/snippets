from __future__ import unicode_literals
import youtube_dl

from sys import stdin, stdout
from math import floor

links = stdin.readlines()

previous = ''

class MyLogger(object):

    def __init__(self):
        self.newline = False

    def debug(self, msg):
        pass

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('\tDone!')
    if d['status'] == 'downloading':
        filename = d['filename']
        speed = d['_speed_str']
        percentage = d['_percent_str']
        if percentage != 'Unknown' and percentage != 'Unknown ':
            progress = '='*floor(float(percentage.strip('%'))/2)
            left = ' '*(50-len(progress))
            stdout.write('\r')
            stdout.write("Downloading '{}'\t[{}] {}".format(filename, progress + left, percentage))
            stdout.flush()
        else:
            stdout.write('\r')
            stdout.write(d)
            stdout.flush()
            

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(links)
