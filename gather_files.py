#!/usr/bin/python3 

#Walks a directory structure to find image files.  Change the walk_dir to your preferred directory and change the re.search line if you want to include additional image extensions.

import os, re

walk_dir = '/picturepi/Camera Uploads/' 
db = 'picture_db.txt'
count = 0
print('walk_dir = ' + walk_dir)
if os.path.isfile(db):
  os.remove(db)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))
print('db_filename = ' + db)

for root, subdirs, files in os.walk(walk_dir):
  list_file_path = os.path.join(db)
  with open(list_file_path, 'a') as list_file:
    for subdir in subdirs:
      print('\t- subdirectory ' + subdir)

    for filename in files:
      file_path = os.path.join(root, filename)
      if re.search('\.BMP$|\.bmp$|\.JPG$|\.jpg$|\.JPEG$|\.jpeg$|\.GIF$|\.gif|\.PNG$|\.png$', str(filename)):
        print('\t- file %s (full path: %s)' % (filename, file_path))
        list_file.write('%s' % file_path)
        list_file.write('\n')
        count += 1

print("\nTotal files loaded: " + str(count))

