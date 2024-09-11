from src import paths
from src import deploy
from src import log

# note: this utility only works on windows because I'm lazy and wanted
# to use '\\' in directory string
if __name__ == "__main__":
	log.init()

	# directory of modpack where you want the configs to come from
	paths.configSrc = ''

	# directory of modpack where you want the mods to come from
	# usually the same as the configSrc
	paths.modsSrc = ''

	# directories you want to export both configs and mods to
	paths.otherInsts = [
	]

	# directories you want to deploy server configs and mods to
	paths.servers = [
	]

	deploy.deployModpack()
	input('press enter to exit...')
