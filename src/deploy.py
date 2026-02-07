from src import mods
from src import configFolder
from src import simpleFolders
from src import globalPacks
from src import kubejs
from src import resourcepacks
from src import shaderpacks
from src import selfDeploy
from src import customFilesFolder
from src import defaultConfigFolder
from src import deleteFilesFromExport

def deployModpack():
	mods.deployMods()
	configFolder.deployConfigs()
	defaultConfigFolder.deployDefaultConfigs()
	simpleFolders.deploySimpleFolders()
	globalPacks.deployGlobalPacks()
	kubejs.deployKubejs()
	resourcepacks.deployResourcepacks()
	shaderpacks.deployShaderpacks()
	selfDeploy.deploySelf()
	customFilesFolder.deployCustomFilesFolder()
	deleteFilesFromExport.deleteFilesFromExports()
