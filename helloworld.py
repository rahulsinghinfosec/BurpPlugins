from burp import IBurpExtender

class BurpExtender(IBurpExtender):

	def registerExtenderCallbacks(self, callbacks):
		callbacks.setExtensionName("Test Extension")
