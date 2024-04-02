import os 
import shutil

src="c:/Users/Win10/OneDrive/Desktop/garbage1"
dest="c:/Users/Win10/OneDrive/Desktop/garbage"

listsrc=os.listdir(src)

# print(listsrc)

for lis in listsrc:
    name,extension=os.path.splitext(lis)

    if extension=='':
        continue
    
    if extension in [".jpeg","jpg"]:
        shutil.move(f'{src}/{lis}',f'{dest}')












