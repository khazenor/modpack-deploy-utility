from src import util, paths, log
import os

clientConfigsToCopy = [
	"bettertitlescreen-client.toml",
	"sebastrnlib-client.toml"
]

foldersToDeleteExtrasFrom = [
	"ftbquests"
]

personalConfigs = [
	'config\\defaultoptions\\optionsof.txt',
	'config\\defaultoptions\\servers.dat',
	'config\\brb.toml',
	'config\\xaeropatreon.txt',
	'config\\xaerominimap_entities.json',
	'config\\xaerominimap-common.txt',
	'config\\xaeroworldmap-common.txt',
	'config\\dynamic_lights_reforged.toml',
	'config\\constantmusic.toml',
	'config\\realcamera.json',
	'config\\controlify.json'
]

configFolderName = 'config'

def deployConfigs():
	log.log('## Deploying Configs ...')
	deployInsts = [paths.modsSrc] + paths.otherInsts + paths.servers
	for deployInst in deployInsts:
		deleteExtraConfigs(deployInst)
		destConfigFolderPath = os.path.join(deployInst, configFolderName)
		if not os.path.exists(destConfigFolderPath):
			os.makedirs(destConfigFolderPath)
		util.copyFolderRecur(
			os.path.join(paths.configSrc, configFolderName),
			destConfigFolderPath + '\\..',
			allowSubStrList=clientConfigsToCopy,
			denySubStrList=personalConfigs
		)

def deleteExtraConfigs(deployInst):
	for deleteFolder in foldersToDeleteExtrasFrom:
		util.removeExtraFilesRecur(
			os.path.join(paths.configSrc, configFolderName, deleteFolder),
			os.path.join(deployInst, configFolderName, deleteFolder)
		)

