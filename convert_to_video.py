from time import sleep
from datetime import datetime as DateTime
import glob
import os
from shutil import copyfile
import shutil
import sys

#WAIT_TIME = 3600
path = '/home/pi/pictures'

#start every day
secondslefttillmidnight = (3600*(24-DateTime.now().hour-1))+(60*(60-DateTime.now().minute-1))+(60-DateTime.now().seconds)
sleep(secondslefttillmidnight)

while 1 :
	#get all pictures form path and sort them
	files = glob.glob(path+'/img*.jpg')
	files.sort(key=os.path.getmtime)

	now = DateTime.now()
	now_string = DateTime.now().strftime('%d_%m_%Y_%H_%M')

	#create new folder
	newfolder = path+'/'+now_string
	try:
		os.mkdir(newfolder)
	except OSError:
                print("Creation of the directory %s failed" % newfolder)
        else:
                print("Successfully created the directory %s " % newfolder)

	#move files to new folder
        sys.stdout.write('start converting\n')
        sys.stdout.flush()
	for f in files:
                shutil.move(f, newfolder)

	#converting to .mp4
	sys.stdout.write('start converting\n')
        sys.stdout.flush()

	os.system('ffmpeg -y -r 24 -pattern_type glob -i \'' + newfolder + '/img*.jpg\' -s hd1080 -vcodec libx264 timelapse.mp4')

	#rename mp4
	sys.stdout.write('rename\n')
        sys.stdout.flush()

	os.rename('timelapse.mp4', now_string+'.mp4')

	#move file to created folder
        sys.stdout.write('move file\n')
        sys.stdout.flush()
	shutil.move(now_string+'.mp4', newfolder)

	#remove pictures from folder
        sys.stdout.write('remove files\n')
        sys.stdout.flush()

	files = glob.glob(newfolder+'/img*.jpg')
	for f in files :
		os.remove(f)


	sys.stdout.write('sleeping\n')
	sys.stdout.flush()
	secondslefttillmidnight = (3600*(24-DateTime.now().hour-1))+(60*(60-DateTime.now().minute-1))+(60-DateTime.now().seconds)
	sleep(secondslefttillmidnight)

