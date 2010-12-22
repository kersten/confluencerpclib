import xmlrpclib


class confluencerpclib():

    def __init__(self, confluenceRpcUrl=None, verbose=False):
        if confluenceRpcUrl is None or confluenceRpcUrl == "":
            raise ConfluenceException("Confluence rpc url must be given")

        self.url = confluenceRpcUrl
        self.verbose = verbose

    def login(self, username, password):
        self.server = xmlrpclib.ServerProxy(self.url, verbose=self.verbose)

        try:
            self.token = self.server.confluence1.login(username, password)
            return self.token
        except xmlrpclib.Fault, err:
            raise ConfluenceException(err.faultString)

    def logout(self):
        try:
            self.server.confluence1.logout(self.token)
            return True
        except xmlrpclib.Fault, err:
            raise ConfluenceException(err.faultString)


class ConfluenceException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
