from src import paths
from src import util
import os

def deployCustomFilesFolder():
	if paths.customFilesFolder:
		for instLoc in paths.otherInsts + paths.servers:
			for element in os.listdir(paths.customFilesFolder):
				util.copyFolderRecur(
					os.path.join(paths.customFilesFolder, element),
					instLoc,
					checkTime=False
				)
