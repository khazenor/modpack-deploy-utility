from src import util, paths, log
import os

globalPacksFolderName = 'global_packs'
requiredDataFolderName = 'required_data'
requiredResourceFolderName = 'required_resources'

def deployGlobalPacks():
	log.log('## Deploying Global Packs')
	copyDatapacks()
	copyResources()

def copyDatapacks():
	log.log(' # Copying Global Datapacks')
	deployInsts = [paths.modsSrc] + paths.otherInsts + paths.servers
	util.simpleDeploy(
		paths.configSrc,
		deployInsts,
		os.path.join(globalPacksFolderName, requiredDataFolderName)
	)

def copyResources():
	log.log(' # Copying Global Resources')
	deployInsts = [paths.modsSrc] + paths.otherInsts
	util.simpleDeploy(
		paths.configSrc,
		deployInsts,
		os.path.join(globalPacksFolderName, requiredResourceFolderName)
	)