import os
import shutil
from pathlib import Path
from src import log

def simpleDeploy(srcInst, deployInsts, folderName):
	for deployInst in deployInsts:
		copyToFolder = os.path.join(
			deployInst,
			Path(folderName).parents[0]
		)
		if not os.path.exists(copyToFolder):
			os.mkdir(copyToFolder)
		copyFolder(
			os.path.join(srcInst, folderName),
			copyToFolder
		)

def copyFolder(src, dest, deleteExtraFiles=True):
	folderName = Path(src).name
	destFolderWName = os.path.join(dest, folderName)
	log.log(f'   - Copy and Delete: {destFolderWName}')
	copyFolderRecur(src, dest, doLog=False)
	if deleteExtraFiles:
		removeExtraFilesRecur(src, destFolderWName, doLog=False)

def copyFolderRecur(src, destFolder, allowSubStrList=[], denySubStrList=[], doLog=True, checkTime=True):
	if os.path.exists(src) and os.path.exists(destFolder):
		srcName = Path(src).name
		existingDestFilePath = os.path.join(destFolder, srcName)
		copyAllowed = (
			src != existingDestFilePath and (
				strContainsStrFromSubStrList(src, allowSubStrList) or
				not strContainsStrFromSubStrList(src, denySubStrList)
			)
		)
		if copyAllowed:
			if doLog:
				log.log(f'   - Copy: {existingDestFilePath}')
			if os.path.isfile(src):
				if Path(existingDestFilePath).is_file():
					if checkTime and os.stat(src).st_mtime - os.stat(existingDestFilePath).st_mtime > 0:
						shutil.copy2(src, destFolder)
				else:
					shutil.copy2(src, destFolder)
			else:
				newDestFolder = os.path.join(destFolder, srcName)
				if not os.path.exists(newDestFolder):
					os.makedirs(newDestFolder)
				itemsToCopy = os.listdir(src)
				for itemToCopy in itemsToCopy:
					copyFolderRecur(
						os.path.join(src, itemToCopy),
						newDestFolder,
						denySubStrList=denySubStrList,
						allowSubStrList=allowSubStrList,
						doLog=False
					)

def removeExtraFilesRecur(src, dest, removeSubStrList = [], doLog=True):
	if Path(dest).is_dir() and src != dest:
		if Path(src).is_dir():
			if doLog:
				log.log(f'   - Delete Extra: {dest}')
			for item in os.listdir(dest):
				destItemPath = os.path.join(dest, item)
				srcItemPath = os.path.join(src, item)
				if Path(destItemPath).is_file():
					doRemove = (
						not os.path.exists(srcItemPath) or
						strContainsStrFromSubStrList(destItemPath, removeSubStrList)
					)
					if doRemove:
						os.remove(destItemPath)
				elif Path(destItemPath).is_dir():
					removeExtraFilesRecur(srcItemPath, destItemPath, doLog=False)
		else:
			shutil.rmtree(dest)

def subFolders(location, folderArray):
	paths = []
	for folder in folderArray:
		paths.append(os.path.join(location, folder))
	return paths

def strContainsStrFromSubStrList(fullString, subStrList):
	for subStr in subStrList:
		if subStr in fullString:
			return True
	return False