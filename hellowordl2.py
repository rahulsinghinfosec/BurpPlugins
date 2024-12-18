from burp import IBurpExtender
from java.io import PrintWriter

class BurpExtender(IBurpExtender):

	def registerExtenderCallbacks(self, callbacks):
		callbacks.setExtensionName("Test Extension 3")


		callbacks.issueAlert("This is an alert")
