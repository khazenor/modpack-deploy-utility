from src import util, paths, log
import os

resourcesNames = [
	"xali's Enchanted Books"
]

resourceFolderName = 'resourcepacks'

def deployResourcepacks():
	log.log('## Deploy Resourcepacks ... ')
	copyClients()
	copyServers()

def copyClients():
	log.log(' # Updating clients')
	deployInsts = paths.otherInsts + [paths.configSrc]
	for deployInst in deployInsts:
		util.copyFolderRecur(
			os.path.join(paths.modsSrc, resourceFolderName),
			deployInst
		)

def copyServers():
	log.log(' # Updating servers')
	for deployInst in paths.servers:
		util.copyFolderRecur(
			os.path.join(paths.modsSrc, resourceFolderName),
			deployInst,
			denySubStrList=resourcesNames
		)