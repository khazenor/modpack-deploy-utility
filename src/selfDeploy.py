import os
from src import paths, log
from src import util

srcFolderName = 'src'

def deploySelf():
	log.log('## Deploy Self ...')
	if paths.dropboxDeployScriptLoc != "":
		util.copyFolder(
			srcFolderName,
			paths.dropboxDeployScriptLoc
		)
