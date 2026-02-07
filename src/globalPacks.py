from src import util, paths, log
import os

globalPacksFolderName = 'global_packs'
requiredDataFolderNames = [
	'required_data',
	'fc_packs'
]
requiredResourceFolderName = 'required_resources'

def deployGlobalPacks():
	log.log('## Deploying Global Packs')
	copyDatapacks()
	copyResources()

def copyDatapacks():
	log.log(' # Copying Global Datapacks')
	deployInsts = [paths.modsSrc] + paths.otherInsts + paths.servers
	for dataFolderName in requiredDataFolderNames:
		util.simpleDeploy(
			paths.configSrc,
			deployInsts,
			os.path.join(globalPacksFolderName, dataFolderName)
		)

def copyResources():
	log.log(' # Copying Global Resources')
	deployInsts = [paths.modsSrc] + paths.otherInsts
	util.simpleDeploy(
		paths.configSrc,
		deployInsts,
		os.path.join(globalPacksFolderName, requiredResourceFolderName)
	)