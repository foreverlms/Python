## biaoqingImageDownloader

A simple demo of downloading related pics from [doutula](http://www.doutula.com/)

>usage: downloader.py [-h] [-t {0,1,2}] [-n NUM] [-c] [-d DIR] [-v]
                     [KEYWORD [KEYWORD ...]]

>download interesting emoj images from www.doutula.com via command line

>positional arguments:
  KEYWORD               the keywords to be searched

>optional arguments:
  -h, --help            show this help message and exit
  -t {0,1,2}, --type {0,1,2}
                        choose image type to be downloaded. 0 represents all,
                        1 represents GIF , 2 represents static image
  -n NUM, --num NUM     number of images to be downloaded
  -c, --clear           enable clear the log file
  -d DIR, --dir DIR     where to store the images, default is ./tmp/keyword/
  -v, --verbose         enable show the whole downloading info


## GUI

GUI designed with `tkinter`, which really sucks... 

## TODO LIST

* The download speed of those images are really slow. So if I have the chance to update this, I want to try multi threads to download images.
* Some logical operations need to have more consideration.
