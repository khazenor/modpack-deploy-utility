from src import util, paths, log
import os

shaderpacksFolderName = 'shaderpacks'
excludeStrings = [
	'.txt'
]
def deployShaderpacks():
	log.log('Deploying shaderpacks ...')
	deployInsts = paths.otherInsts + [paths.configSrc]

	for deployInst in deployInsts:
		util.copyFolderRecur(
			os.path.join(paths.modsSrc, shaderpacksFolderName),
			deployInst,
			denySubStrList=excludeStrings
		)