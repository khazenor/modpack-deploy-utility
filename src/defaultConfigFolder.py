from src import configFolder
from src import log
def deployDefaultConfigs():
	log.log('deploying default configs ...')
	backupConfigFolder = configFolder.configFolderName
	configFolder.configFolderName = 'configureddefaults\\config'
	configFolder.deployConfigs()
	configFolder.configFolderName = backupConfigFolder