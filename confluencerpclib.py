import xmlrpclib


class connect():

    def __init__(self, confluenceRpcUrl=None, verbose=False):
        if confluenceRpcUrl is None or confluenceRpcUrl == "":
            raise ConfluenceException("Confluence rpc url must be given")

        self.url = confluenceRpcUrl
        self.verbose = verbose

    def login(self, username, password):
        self.server = xmlrpclib.ServerProxy(self.url, verbose=self.verbose)

        try:
            self.token = self.server.confluence1.login(username, password)
            return True
        except xmlrpclib.Fault, err:
            raise ConfluenceException(err.faultString)

    def logout(self):
        try:
            return self.server.confluence1.logout(self.token)
        except xmlrpclib.Fault, err:
            raise ConfluenceException(err.faultString)

    def exportSite(self, exportAttachments=False):
        raise ConfluenceException("Not implemented yet.")

    def getClusterInformation(self):
        raise ConfluenceException("Not implemented yet.")

    def getClusterNodeStatuses(self):
        raise ConfluenceException("Not implemented yet.")

    def isPluginEnabled(self, pluginKey):
        raise ConfluenceException("Not implemented yet.")

    def installPlugin(self, pluginFileName, pluginData):
        raise ConfluenceException("Not implemented yet.")

    def getServerInfo(self):
        raise ConfluenceException("Not implemented yet.")

    def getSpaces(self):
        raise ConfluenceException("Not implemented yet.")

    def getSpace(self, spaceKey):
        raise ConfluenceException("Not implemented yet.")

    def exportSpace(self, spaceKey, exportType="TYPE_XML"):
        raise ConfluenceException("Not implemented yet.")

    def addSpace(self, space):
        raise ConfluenceException("Not implemented yet.")

    def removeSpace(self, spaceKey):
        raise ConfluenceException("Not implemented yet.")

    def addPersonalSpace(self, personalSpace, userName):
        raise ConfluenceException("Not implemented yet.")

    def convertToPersonalSpace(self, userName, spaceKey, newSpaceName,
        updateLinks=True):
        raise ConfluenceException("Not implemented yet.")

    def storeSpace(self, space):
        raise ConfluenceException("Not implemented yet.")

    def importSpace(self, zippedImportData):
        raise ConfluenceException("Not implemented yet.")

    def getPages(self, spaceKey):
        raise ConfluenceException("Not implemented yet.")

    def getPageByName(self, spaceKey, pageTitle):
        raise ConfluenceException("Not implemented yet.")

    def getPage(self, pageId):
        raise ConfluenceException("Not implemented yet.")

    def getPageHistory(self, pageId):
        raise ConfluenceException("Not implemented yet.")

    def getContentPermissionSets(self, contentId):
        raise ConfluenceException("Not implemented yet.")

    def getContentPermissionSet(self, contentId, permissionType):
        raise ConfluenceException("Not implemented yet.")

    def setContentPermissions(self, contentId, permissionType, permissions):
        raise ConfluenceException("Not implemented yet.")

    def getAttachments(self, pageId):
        raise ConfluenceException("Not implemented yet.")

    def getAncestors(self, pageId):
        raise ConfluenceException("Not implemented yet.")

    def getChildren(self, pageId):
        raise ConfluenceException("Not implemented yet.")

    def getDescendents(self, pageId):
        raise ConfluenceException("Not implemented yet.")

    def getComments(self, pageId):
        raise ConfluenceException("Not implemented yet.")

    def getComment(self, commentId):
        raise ConfluenceException("Not implemented yet.")

    def addComment(self, comment):
        raise ConfluenceException("Not implemented yet.")

    def removeComment(self, commentId):
        raise ConfluenceException("Not implemented yet.")

    def storePage(self, page):
        raise ConfluenceException("Not implemented yet.")

    def updatePage(self, page, pageUpdateOptions):
        raise ConfluenceException("Not implemented yet.")

    def renderContent(self, spaceKey, pageId, content, parameters=None):
        raise ConfluenceException("Not implemented yet.")

    def removePage(self, pageId):
        raise ConfluenceException("Not implemented yet.")

    def movePage(self, targetPageId, position):
        raise ConfluenceException("Not implemented yet.")

    def movePageToTopLevel(self, targetSpaceKey):
        raise ConfluenceException("Not implemented yet.")

    def getAttachment(self, pageId, fileName, versionNumber):
        raise ConfluenceException("Not implemented yet.")

    def getAttachmentData(self, pageId, fileName, versionNumber):
        raise ConfluenceException("Not implemented yet.")

    def addAttachment(self, contentId, attachment, attachmentData):
        raise ConfluenceException("Not implemented yet.")

    def removeAttachment(self, contentId, fileName):
        raise ConfluenceException("Not implemented yet.")

    def moveAttachment(self, originalContentId, originalName,
        newContentEntityId, newName):
        raise ConfluenceException("Not implemented yet.")

    def getBlogEntries(self, spaceKey):
        raise ConfluenceException("Not implemented yet.")

    def getBlogEntry(self, pageId):
        raise ConfluenceException("Not implemented yet.")

    def storeBlogEntry(self, entry):
        raise ConfluenceException("Not implemented yet.")

    def getBlogEntryByDayAndTitle(self, spaceKey, dayOfMonth, postTitle):
        raise ConfluenceException("Not implemented yet.")

    def search(self, query, maxResults, parameters=None):
        raise ConfluenceException("Not implemented yet.")

    def getPermissions(self, spaceKey):
        raise ConfluenceException("Not implemented yet.")

    def getPermissionsForUser(self, spaceKey, userName):
        raise ConfluenceException("Not implemented yet.")

    def getPagePermissions(self, pageId):
        raise ConfluenceException("Not implemented yet.")

    def getSpaceLevelPermissions(self):
        raise ConfluenceException("Not implemented yet.")

    def addPermissionToSpace(self, permission, remoteEntityName, spaceKey):
        raise ConfluenceException("Not implemented yet.")

    def addPermissionsToSpace(self, permissions, remoteEntityName, spaceKey):
        raise ConfluenceException("Not implemented yet.")

    def removePermissionFromSpace(self, permission, remoteEntityName,
        spaceKey):
        raise ConfluenceException("Not implemented yet.")

    def addAnonymousPermissionToSpace(self, permission, spaceKey):
        raise ConfluenceException("Not implemented yet.")

    def addAnonymousPermissionsToSpace(self, permissions, spaceKey):
        raise ConfluenceException("Not implemented yet.")

    def removeAnonymousPermissionFromSpace(self, permission, spaceKey):
        raise ConfluenceException("Not implemented yet.")

    def removeAllPermissionsForGroup(self, groupname):
        raise ConfluenceException("Not implemented yet.")

    def getUser(self, username):
        raise ConfluenceException("Not implemented yet.")

    def addUser(self, user, password):
        raise ConfluenceException("Not implemented yet.")

    def addGroup(self, group):
        raise ConfluenceException("Not implemented yet.")

    def getUserGroups(self, username):
        raise ConfluenceException("Not implemented yet.")

    def addUserToGroup(self, username, groupname):
        raise ConfluenceException("Not implemented yet.")

    def removeUserFromGroup(self, username, groupname):
        raise ConfluenceException("Not implemented yet.")

    def removeUser(self, username):
        raise ConfluenceException("Not implemented yet.")

    def removeGroup(self, groupname, defaultGroupName):
        raise ConfluenceException("Not implemented yet.")

    def getGroups(self):
        raise ConfluenceException("Not implemented yet.")

    def hasUser(self, username):
        raise ConfluenceException("Not implemented yet.")

    def hasGroup(self, groupname):
        raise ConfluenceException("Not implemented yet.")

    def editUser(self, remoteUser):
        raise ConfluenceException("Not implemented yet.")

    def deactivateUser(self, username):
        raise ConfluenceException("Not implemented yet.")

    def reactivateUser(self, username):
        raise ConfluenceException("Not implemented yet.")

    def getActiveUsers(self, viewAll):
        raise ConfluenceException("Not implemented yet.")

    def setUserInformation(self, userInfo):
        raise ConfluenceException("Not implemented yet.")

    def getUserInformation(self, username):
        raise ConfluenceException("Not implemented yet.")

    def changeMyPassword(self, oldPass, newPass):
        raise ConfluenceException("Not implemented yet.")

    def changeUserPassword(self, username, newPass):
        raise ConfluenceException("Not implemented yet.")

    def addProfilePicture(self, userName, fileName, mimeType, pictureData):
        raise ConfluenceException("Not implemented yet.")

    def getLabelsById(self, objectId):
        raise ConfluenceException("Not implemented yet.")

    def getMostPopularLabels(self, maxCount):
        raise ConfluenceException("Not implemented yet.")

    def getMostPopularLabelsInSpace(self, spaceKey, maxCount):
        raise ConfluenceException("Not implemented yet.")

    def getRecentlyUsedLabels(self, maxResults):
        raise ConfluenceException("Not implemented yet.")

    def getRecentlyUsedLabelsInSpace(self, spaceKey, maxResults):
        raise ConfluenceException("Not implemented yet.")

    def getSpacesWithLabel(self, labelName):
        raise ConfluenceException("Not implemented yet.")

    def getRelatedLabels(self, labelName, maxResults):
        raise ConfluenceException("Not implemented yet.")

    def getRelatedLabelsInSpace(self, labelName, spaceKey, maxResults):
        raise ConfluenceException("Not implemented yet.")

    def getLabelsByDetail(self, labelName, namespace, spaceKey, owner):
        raise ConfluenceException("Not implemented yet.")

    def getLabelContentById(self, labelId):
        raise ConfluenceException("Not implemented yet.")

    def getLabelContentByName(self, labelName):
        raise ConfluenceException("Not implemented yet.")

    def getLabelContentByObject(self, labelObject):
        raise ConfluenceException("Not implemented yet.")

    def getSpacesContainingContentWithLabel(self, labelName):
        raise ConfluenceException("Not implemented yet.")

    def addLabelByName(self, labelName, objectId):
        raise ConfluenceException("Not implemented yet.")

    def addLabelById(self, labelId, objectId):
        raise ConfluenceException("Not implemented yet.")

    def addLabelByObject(self, labelObject, objectId):
        raise ConfluenceException("Not implemented yet.")

    def addLabelByNameToSpace(self, labelName, spaceKey):
        raise ConfluenceException("Not implemented yet.")

    def removeLabelByName(self, labelName, objectId):
        raise ConfluenceException("Not implemented yet.")

    def removeLabelById(self, labelId, objectId):
        raise ConfluenceException("Not implemented yet.")

    def removeLabelByObject(self, labelObject, objectId):
        raise ConfluenceException("Not implemented yet.")

    def removeLabelByNameFromSpace(self, labelName, spaceKey):
        raise ConfluenceException("Not implemented yet.")


class ConfluenceException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
