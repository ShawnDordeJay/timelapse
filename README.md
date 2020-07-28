# timelapse

taking_pictures.py -> taking a picture every 8 seconds

convert_to_video.py
- converts every day at 00:00
- creates a folder with timestamp as foldername
- moves all found img*.jpg in this folder
- starts the convertion
- moves the converted file (.mp4) into the new folder
- deletes all pictures after that

This program is set to be a service. To implement this python script as a service I used this site: https://gist.github.com/emxsys/a507f3cad928e66f6410e7ac28e2990f.
