from burp import IBurpExtender
from java.io import PrintWriter

class BurpExtender(IBurpExtender):

	def registerExtenderCallbacks(self, callbacks):
		callbacks.setExtensionName("Test Extension 2")


		stdout = PrintWriter(callbacks.getStdout(),True)

		stdout.println("This is output")
