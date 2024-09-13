from src import util, paths, log
import os

clientSideModNames = [
	'badpackets',
	'brb',
	'Controlling',
	"DrawersTooltip",
	'entityculling',
	'extreamesoundmuffler',
	'farsight',
	'NekosEnchantedBooks',
	'wthit',
	'oculus',
	'rubidium',
	'wthitharvestability',
	'RubidiumExtra',
	'light-overlay',
	'MoreCosmetics',
	'guicompass',
	'betterf3',
	'betterf3plus',
	'BetterAdvancements',
	'controllable',
	'entity_model_features',
	'entity_texture_features',
	'InventoryProfilesNext',
	'citresewn',
	'tagtooltips',
	'World Stripper',
	'embeddium',
	'tagtooltips',
	'XaeroPlus',
	'XaerosWorldMap',
	'Xaeros_Minimap',
	'realcamera',
	'Tips',
	'iris-neoforge',
	'sodium-neoforge',
	'ExtremeSoundMuffler',
	'ProbeJS',
	'NBTcopy'
]

devOnlyMods = [
	'ProbeJS'
]

modsFolder = 'mods'
modlistFile = 'modlist.txt'
serverModlistFile = 'serverModlist.txt'

def deployMods():
	log.log('## Deploying Mods...')
	deployToClients()
	deployToServers()
	deployDevMods()
	writeModlists()

def deployToClients():
	log.log(' # Deploy Clients')
	util.copyFolder(
		modsSrc(),
		paths.configSrc
	)
	for clientInst in paths.otherInsts:
		copyModsFolderWithDenyList(clientInst, devOnlyMods)

def deployToServers():
	log.log(' # Deploy Servers')
	for serverInst in paths.servers:
		copyModsFolderWithDenyList(serverInst, clientSideModNames)

def copyModsFolderWithDenyList(inst, denyList):
	instModsFolder = instMods(inst)
	util.removeExtraFilesRecur(
		modsSrc(),
		instModsFolder,
		removeSubStrList=denyList
	)
	util.copyFolderRecur(
		modsSrc(),
		inst,
		denySubStrList=denyList
	)


def deployDevMods():
	devModsFolder = os.path.join(paths.configSrc, 'mods_dev', modsFolder)
	util.copyFolder(devModsFolder, paths.configSrc, deleteExtraFiles=False)

def writeModlists():
	writeMods(modlistFile, os.listdir(modsSrc()))
	if len(paths.servers) > 0:
		exportServerMods = os.listdir(instMods(paths.servers[0]))
		writeMods(serverModlistFile, exportServerMods)

def writeMods(filename, mods):
	with open(os.path.join(paths.configSrc, filename), "w") as f:
		for mod in mods:
			f.write(f"{mod}\n")

def modsSrc():
	return instMods(paths.modsSrc)

def instMods(inst):
	return os.path.join(inst, modsFolder)
