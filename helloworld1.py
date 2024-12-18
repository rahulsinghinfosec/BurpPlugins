from burp import IBurpExtender
from java.lang import RuntimeException

class BurpExtender(IBurpExtender):

	def registerExtenderCallbacks(self, callbacks):
		callbacks.setExtensionName("Test Extension 1")

		raise RuntimeException("Exception Raised")
