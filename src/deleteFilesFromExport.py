from src import paths
import os
import shutil
from src import log
foldersToDelete = {
	'config': {
		'exceptions': [
			'ftbquests',
			'easy_npc'
		]
	}
}

def deleteFilesFromExports():
	log.log('deleting files from export paths ...')
	for exportPath in paths.exportInsts:
		for folder in foldersToDelete:
			exceptions = foldersToDelete[folder]['exceptions']
			for subFolder in os.listdir(os.path.join(exportPath, folder)):
				subFolderDir = os.path.join(exportPath, folder, subFolder)
				if subFolder not in exceptions:
					if os.path.isfile(subFolderDir):
						os.remove(subFolderDir)
					else:
						shutil.rmtree(subFolderDir)
