from src import util, paths, log

simpleFolders = [
	'defaultconfigs',
	'scripts'
]

def deploySimpleFolders():
	deployInsts = [paths.modsSrc] + paths.otherInsts + paths.servers
	for simpleFolder in simpleFolders:
		log.log(f'## Deploying {simpleFolder} ...')
		util.simpleDeploy(
			paths.configSrc,
			deployInsts,
			simpleFolder
		)
