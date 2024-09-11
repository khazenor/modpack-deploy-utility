from src import paths

def log(logStr):
	print(logStr)
	with open(paths.logFile, 'a') as f:
		f.write(logStr + "\n")

def init(filename='log.txt'):
	paths.logFile = filename
	with open(paths.logFile, 'w') as f:
		f.write('')
