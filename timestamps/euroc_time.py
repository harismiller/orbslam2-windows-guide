import os
import os.path as osp
import shutil as sh
from decimal import *

#Initial variables
direc = "PATH_TO_IMAGES" #Directory where files are pulled from
selfdirec = os.path.dirname(os.path.realpath(__file__))
exten = ".png" #The extension type of the files

#Grabs the files from the directory
#It is recommended to make a duplicate of the files if possible 
onlyFiles = [f for f in os.listdir(direc) if osp.isfile(osp.join(direc, f))]

#Renames the files
onlyFilesRename = []
nameStart = Decimal("1305031229.528748") #The name of the initial file without extension
start = nameStart
renameGoFormat = "y" #Decides if the file names are to be changed
if renameGoFormat == "y":
	for h in onlyFiles[:]:
		fileDirec = "\{}".format(h)
		strDirec = str(direc)
		strSelfDirec = str(selfdirec)
		name = str(start) + exten
		os.rename(str(direc + fileDirec), name)
		newFileDirec = "\{}".format(name)
		sh.move(str(selfdirec + newFileDirec), direc)
		onlyFilesRename.append(start)
		increment = Decimal("0.058064") #The increment to increase the value of the file name
		start += increment
else: 
	for j in onlyFiles: 
		onlyFilesRename.append(j)

print("Rename - Done")

#Takes file names without extensions
newOnlyFiles = []
for i in onlyFilesRename:
	iString = str(i)
	newFileName = iString.replace(exten,"")
	newOnlyFiles.append(newFileName)

#Creates text file
destFile = "timestamp.txt" #Name of destination text file
textFile = open(destFile, "w")
#File names in desired format in the text file
for k in newOnlyFiles:
	textFile.write(k)
	textFile.write("\n")

textFile.close()
print("{} - Generated".format(destFile))
