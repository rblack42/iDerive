import iDerive

class Cli(object):

	def __init__(self, fname):
		self.fname = fname
		print("iDerive v%s" % iDerive.__version__)

	def run(self):
		print("running...")

