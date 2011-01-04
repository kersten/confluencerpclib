import xmlrpclib


class Confluence(object):

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
        try:
            responses = self.server.confluence1.getSpaces(self.token)
            spaces = []

            for response in responses:
                spaces += [SpaceSummary().display(response),]

            return spaces
        except xmlrpclib.Fault, err:
            raise ConfluenceException(err.faultString)

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
        """Returns all the PageSummaries in the space. Doesn't
        include pages which are in the Trash.
        :parma space_key:
        :type space_key: str:
        :rtype: list
        """
        try:
            responses = self.server.confluence1.getPages(self.token, spaceKey)
            pages = []
            for response in responses:
                pages += [PageSummary().display(response),]
            return pages
        except xmlrpclib.Fault, err:
            raise ConfluenceException(err.faultString)

    def getPageByName(self, spaceKey, pageTitle):
        raise ConfluenceException("Not implemented yet.")

    def getPage(self, pageId):
        try:
            response = self.server.confluence1.getPage(self.token, pageId)
            page = Page().display(response)
            return page
        except xmlrpclib.Fault, err:
            raise ConfluenceException(err.faultString)

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
        try:
            #id, space, title, content and version
            newPage = {
                'space': page.space,
                'title': page.title,
                'content': page.content
            }
            
            try:
                newPage['parentId'] = page.parentId
            except:
                pass
            response = self.server.confluence1.storePage(self.token, newPage)
            page = Page().display(response)
            return page
        except xmlrpclib.Fault, err:
            raise ConfluenceException(err.faultString)

    def updatePage(self, page, pageUpdateOptions=None):
        try:
            #id, space, title, content and version
            newPage = {
                'id': page.id,
                'space': page.space,
                'title': page.title,
                'content': page.content,
                'version': str(page.version)
            }
            response = self.server.confluence1.updatePage(self.token, newPage, pageUpdateOptions)
            page = Page().display(response)
            return page
        except xmlrpclib.Fault, err:
            raise ConfluenceException(err.faultString)

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
        """Returns all the labels for the objectId.
        :param objectId:
        :type objectId: str:
        :rtype: list
        """
        try:
            responses = self.server.confluence1.getLabelsById(self.token, objectId)
            labels = []
            for response in responses:
                labels += [Label().display(response),]
            return labels
        except xmlrpclib.Fault, err:
            raise ConfluenceException(err.faultString)

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
        try:
            responses = self.server.confluence1.addLabelByName(self.token, labelName, objectId)
            return responses
        except xmlrpclib.Fault, err:
            raise ConfluenceException(err.faultString)

    def addLabelById(self, labelId, objectId):
        raise ConfluenceException("Not implemented yet.")

    def addLabelByObject(self, labelObject, objectId):
        raise ConfluenceException("Not implemented yet.")

    def addLabelByNameToSpace(self, labelName, spaceKey):
        raise ConfluenceException("Not implemented yet.")

    def removeLabelByName(self, labelName, objectId):
        raise ConfluenceException("Not implemented yet.")

    def removeLabelById(self, labelId, objectId):
        try:
            responses = self.server.confluence1.removeLabelByName(self.token, labelId, objectId)
            return responses
        except xmlrpclib.Fault, err:
            raise ConfluenceException(err.faultString)

    def removeLabelByObject(self, labelObject, objectId):
        raise ConfluenceException("Not implemented yet.")

    def removeLabelByNameFromSpace(self, labelName, spaceKey):
        raise ConfluenceException("Not implemented yet.")


class ServerInfo(object):
    """
    :param majorVersion: the major version number of the Confluence instance
    :type key: int
    :param minorVersion: the minor version number of the Confluence instance
    :type key: int
    :param patchLevel: the patch-level of the Confluence instance
    :type key: int
    :param buildId: the build ID of the Confluence instance (usually a number)
    :type key: str
    :param developementBuild: Whether the build is a developer-only
        release or not
    :type key: bool
    :param baseUrl: The base URL for the confluence instance
    :type key: str
    """

    def __init__(self):
        self.majorVersion = 0
        self.minorVersion = 0
        self.patchLevel = 0
        self.buildId = ''
        self.developmentBuild = False
        self.baseUrl = ''

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.baseUrl)

    def __str__(self):
        return "Atlassian Confluence %s" % (self.version)

    def __unicode__(self):
        return unicode(__str__)

    @property
    def version(self):
        return ".".join(map(str, (self.major_version,
               self.minor_version, self.patch_level)))

    def display(self, info):
        """Convert the XML-RPC dict to the ServerInfo class.
        :param info: The XML-RPC dict
        :type info: dict
        """
        self.majorVersion = int(info['majorVersion'])
        self.minorVersion = int(info['minorVersion'])
        self.patchLevel = int(info['patchLevel'])
        self.buildId = str(info['buildId'])
        self.developmentBuild = bool(info['developmentBuild'])
        self.baseUrl = str(info['baseUrl'])
        return self


class SpaceSummary(object):
    """
    :param key: the space key
    :type key: str
    :param name: the name of the space
    :type key: str
    :param type: type of the space
    :type type: str
    :param url: the url to the view this space online
    :type url: str
    """

    def __init__(self):
        self.key = ''
        self.name = ''
        self.type = ''
        self.url = ''

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.key)

    def __str__(self):
        return "%s" % (self.name)

    def __unicode__(self):
        return unicode(__str__)

    def display(self, summary):
        """Convert the XML-RPC dict to the SpaceSummary class.
        :param summary: The XML-RPC dict
        :type summary: dict
        """
        self.key = str(summary['key'])
        self.name = str(summary['name'])
        self.type = str(summary['type'])
        self.url = str(summary['url'])
        return self


class Space(object):
    """
    :param key: the space key
    :type key: str
    :param name: the name of the space
    :type name: str
    :param url: the url to view this space online
    :type url: str
    :param homepage: the id of the space homepage
    :type homepage: str
    :param description: the HTML rendered space description
    :type description: str
    """

    def __init__(self):
        self.key = ''
        self.name = ''
        self.url = ''
        self.homePage = ''
        self.description = ''

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.key)

    def __str__(self):
        return "%s" % (self.name)

    def __unicode__(self):
        return unicode(__str__)

    def display(self, space):
        """Convert the XML-RPC dict to the Space class.
        :param space: The XML-RPC dict
        :type space: dict
        """
        self.key = str(space['key'])
        self.name = str(space['name'])
        self.type = str(space['type'])
        self.url = str(space['url'])
        self.homePage = str(space['homePage'])
        try:
            self.description = str(space['description'])
        except KeyError:
            self.description = None
        return self


class PageSummary(object):
    """
    :param id: the id of the page
    :type key: str
    :param space: the key of the space that this page belongs to
    :type key: str
    :param parentId: the id of the parent page
    :type type: str
    :param title: the title of the page
    :type type: str
    :param url: the url to view this page online
    :type url: str
    :param locks: the number of locks current on this page
    :type type: int
    """

    def __init__(self):
        self.id = ''
        self.space = ''
        self.parentId = ''
        self.title = ''
        self.url = ''
        self.locks= 0

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.id)

    def __str__(self):
        return "%s" % (self.title)

    def __unicode__(self):
        return unicode(__str__)

    def display(self, summary):
        """Convert the XML-RPC dict to the PageSummary class.
        :param summary: The XML-RPC dict
        :type summary: dict
        """
        self.id = str(summary['id'])
        self.space = str(summary['space'])
        self.parentId = str(summary['parentId'])
        self.title = str(summary['title'])
        self.url = str(summary['url'])
        #self.locks = int(summary['locks'])
        return self


class Page(object):
    """
    :param id: the id of the page
    :type id: str
    :param space: the key of the space taht this page belongs to
    :type space: str
    :param parentId: the id of the parent page
    :type parentId: str
    :param title: the title of the page
    :type title: str
    :param url: the url to view this page online
    :type url: str
    :param version: the version number of this page
    :type version: int
    :param content: the page content
    :type content: str
    :param created: timestamp page was created
    :type created: datetime
    :param creator: username of the creator
    :type creator: str
    :param modified: timestamp page was modified
    :type modified: str
    :param modifier: username of page's last modifier
    :type modifier: str
    :param homePage: whether or not his is a space's homepage
    :type homePage: bool
    :param locks: the number of locks current on this page
    :type locks: int
    :param contentStatus: status of the page (eg. current or deleted)
    :type cotnentStatus: str
    :param current: whether the page is current and not deleted
    :type current: bool
    """

    def __init__(self):
        self.id = ''
        self.space = ''
        self.parentId = ''
        self.title = ''
        self.url = ''
        self.version = 0
        self.content = ''
        self.created = ''
        self.creator = ''
        self.modified = ''
        self.modifier = ''
        self.homePage = ''
        self.lock = 0
        self.contentStatus = ''
        self.current = ''

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.id)

    def __str__(self):
        return "%s" % (self.title)

    def __unicode__(self):
        return unicode(__str__)

    def display(self, page):
        """Convert the XML-RPC dict to the Page class.
        :param page: The XML-RPC dict
        :type page: dict
        """
        self.id = str(page['id'])
        self.space = str(page['space'])
        self.parentId = str(page['parentId'])
        self.title = str(page['title'])
        self.url = str(page['url'])
        self.version = int(page['version'])
        self.content = str(page['content'])
        self.created = str(page['created'])
        self.creator = str(page['creator'])
        self.modified = str(page['modified'])
        self.modifier = str(page['modifier'])
        self.homePage = bool(page['homePage'])
        #self.lock = int(page['locks'])
        self.contentStatus = str(page['contentStatus'])
        self.current = bool(page['current'])
        return self


class PageUpdateOptions(object):
    """
    :param versionComment: Edit comment for the updated page
    :type versionComment: str
    :param minorEdit: Is this update a 'minor edit'? (default value: false)
    :type minorEdit: bool
    """

    def __init__(self):
        self.versionComment = ''
        self.minorEdit = False

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.versionComment)

    def __str__(self):
        return "%s" % (self.versionComment)

    def __unicode__(self):
        return unicode(__str__)

    def display(self, page):
        """Convert the XML-RPC dict to the Page class.
        :param page: The XML-RPC dict
        :type page: dict
        """
        self.versionComment = str(page['versionComment'])
        self.minorEdit = bool(page['minorEdit'])
        return self


class PageHistorySummary(object):
    """
    :param id: the id of the historical page
    :type id: str
    :param version: the version of the historical page
    :type versoin: int
    :param modifier: the user who made the change
    :type modifier: str
    :param modified: timestamp change was made
    :type modified: datetime
    :param versionComment: the comment made when the version was changed
    :type versionComment: str
    """

    def __init__(self):
        self.id = ''
        self.version = 0
        self.modifier = ''
        self.modified = ''
        self.versionComment = ''

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.id)

    def __str__(self):
        return "%s" % (self.id)

    def __unicode__(self):
        return unicode(__str__)

    def display(self, page):
        """Convert the XML-RPC dict to the Page class.
        :param space: The XML-RPC dict
        :type space: dict
        """
        self.id = str(page['id'])
        self.version = int(page['version'])
        self.modifier = str(page['modifier'])
        self.modified = page['modified']
        try:
            self.versionComment = str(page['versionComment'])
        except KeyError:
            self.versionComment = ''
        return self


class BlogEntrySummary(object):
    """
    :param id: the id of the blog entry
    :type id: str
    :param space: the key of the space that this blog entry belongs to
    :type space: str
    :param title: the title of the blog entry
    :type title: str
    :param url: the url to view this blog entry online
    :type url: str
    :param locks: the number of locks current on this page
    :type locks: int
    :param publishDate: the date the blog post was published
    :type publishDate: datetime
    """

    def __init__(self):
        self.id = ''
        self.space = ''
        self.title = ''
        self.url = ''
        self.locks = 0
        self.publishDate = ''

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.id)

    def __str__(self):
        return "[%s] %s" % (self.space, self.title)

    def __unicode__(self):
        return unicode(__str__)

    def display(self, entry):
        """Convert the XML-RPC dict to the BlogEntrySummary class.
        :param entry: The XML-RPC dict
        :type entry: dict
        """
        self.id = str(entry['id'])
        self.space = str(entry['space'])
        self.title = str(entry['title'])
        self.url = str(entry['url'])
        self.locks = int(entry['locks'])
        self.publishDate = entry['publishDate']
        return self


class BlogEntry(object):
    """
    :param id: the id of the blog entry
    :type id: str
    :param space: the key of the space that this blog entry belongs to
    :type space: str
    :param title: the title of the blog entry
    :type title: str
    :param url: the url to view this blog entry online
    :type url: str
    :param version: the version number of this blog entry
    :type version: int
    :param content: the blog entry content
    :type content: str
    :param locks: the number of locks current on this page
    :type locks: int
    """

    def __init__(self):
        self.id = ''
        self.space = ''
        self.title = ''
        self.url = ''
        self.version = 0
        self.content = ''
        self.locks = 0

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.id)

    def __str__(self):
        return "[%s] %s" % (self.space, self.title)

    def __unicode__(self):
        return unicode(__str__)

    def display(self, entry):
        """Convert the XML-RPC dict to the BlogEntry class.
        :param entry: The XML-RPC dict
        :type entry: dict
        """
        self.id = str(entry['id'])
        self.space = str(entry['space'])
        self.title = str(entry['title'])
        self.url = str(entry['url'])
        self.version = int(entry['version'])
        self.content = str(entry['content'])
        self.locks = int(entry['locks'])
        return self


class RSSFeed(object):
    """
    :param url: the URL of the RSS feed
    :type url: str
    :param title: the feed's title
    :type title: str
    """

    def __init__(self):
        self.url = ''
        self.title = ''

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.title)

    def __str__(self):
        return "%s" % (self.title)

    def __unicode__(self):
        return unicode(__str__)

    def display(self, feed):
        """Convert the XML-RPC dict to the RSSFeed class.
        :param feed: The XML-RPC dict
        :type feed: dict
        """
        self.url = str(feed['url'])
        self.title = str(feed['title'])
        return self


class SearchResult(object):
    """
    :param title: the feed's title
    :type title: str
    :param url: the remote URL needed to view the search result online
    :type url: str
    :param excerpt: a short excerpt of the result if it makes sense
    :type excerpt: str
    :param content_type: the type of this result - page, comment, spacedesc,
        attachment, userinfo, blogpost
    :type content_type: str
    :param id: the long ID of the result (if the type has one)
    :type id: str
    """

    def __init__(self):
        self.title = ''
        self.url = ''
        self.excerpt = ''
        self.type = ''
        self.id = ''

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.title)

    def __str__(self):
        return "%s" % (self.title)

    def __unicode__(self):
        return unicode(__str__)

    def display(self, result):
        """Convert the XML-RPC dict to the SearchResult class.
        :param result: The XML-RPC dict
        :type result: dict
        """
        self.title = str(result['title'])
        self.url = str(result['url'])
        self.excerpt = str(result['excerpt'])
        self.type = str(result['type'])
        self.id = str(result['id'])
        return self


class Attachment(object):
    """
    :param id: numeric id of the attachment
    :type id: int
    :param page_id: page ID of the attachment
    :type page_id: str
    :param title: title of the attachment
    :type title: str
    :param file_name: file name of the attachment
    :type file_name: str
    :param file_size: numeric file size of the attachment in bytes
    :type file_size: str
    :param content_type: mime content type of the attachment
    :param created: creation date of the attachment
    :type created: datetime
    :param creator: creator of the attachment
    :type creator: str
    :param url: url to download the attachment online
    :type url: str
    :param comment: comment for the attachment
    :type comment: str
    """


class Comment(object):
    """
    :param id: numeric id of the comment
    :type id: str
    :param page_id: page ID of the comment
    :type page_id: str
    :param title: title of the comment
    :param content: notated content of the comment (use render_content to
        render)
    :type content: str
    :param url: url to view the comment online
    :type url: str
    :param created: creation date of the comment
    :type created: datetime
    :param creator: creator of the attachment
    :type creator: str
    """


class User(object):
    """
    :param name: the username of this user
    :type name: str
    :param fullname: the full name of this user
    :type fullname: str
    :param email: the email address of this user
    :type email: str
    :param url: the url to view this user online
    :type url: str
    """


class ContentPermission(object):
    """
    :param content_type: the type of permission. One of 'View' or 'Edit'
    :type content_type: str
    :param user_name: the username of the user who is permitted to see or edit
        the content. 'None' if this is a group permission.
    :type user_name: str
    :param group_name: The name of the group who is permitted to see or edit
        the content. 'None' if this is a user permission.
    :type group_name: str
    """


class ContentPermissionSet(object):
    """
    :param content_type: the type of permission. One of 'View' or 'Edit'
    :type content_type: str
    :param user_name: the username of the user who is permitted to see or edit
        the content. 'None' if this is a group permission.
    :type user_name: str
    :param group_name: The name of the group who is permitted to see or edit
        the content. 'None' if this is a user permission.
    :type group_name: str
    """


class Label(object):
    
    """
    :param name: the name of the label
    :type name: str
    :param owner: the username of the owner
    :type owner: str
    :param namespace: the namespace of the label
    :type namespace: str
    :param id: the ID of the label
    :type id: int
    """
    def __init__(self):
        self.name = ''
        #self.owner = ''
        self.lnamespace = ''
        self.id = ''

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.name)

    def __str__(self):
        return "%s" % (self.name)

    def __unicode__(self):
        return unicode(__str__)

    def display(self, label):
        """Convert the XML-RPC dict to the RSSFeed class.
        :param feed: The XML-RPC dict
        :type feed: dict
        """
        self.name = str(label['name'])
        #self.owner = str(label['owner'])
        self.namespace = str(label['namespace'])
        self.id = str(label['id'])
        return self


class UserInformation(object):
    """
    :param username: the username of this user
    :type username: str
    :param content: the user description
    :type content: str
    :param creator_name: the creator of the user
    :type creator_name: str
    :param last_modifier_name: the user who last modified
    :type last_modifier_name: str
    :param url: the url to view this user online
    :type url: type
    :param version: the version
    :type version: int
    :param id: the ID of the user
    :type id: int
    :param creation_date: the date the user was created
    :type creation_date: datetime
    :param last_modification_date: the date the user was last modified
    :type last_modification_date: datetime
    """


class ClusterInformation(object):
    """
    :param is_running: true if this node is part of a cluster
    :type is_running: bool
    :param name: the name of the cluster
    :type name: str
    :param member_count: the number of nodes in hte cluster, including this
        node (this will be zero if this node is not clustered)
    :type member_count: int
    :param description: a description of the cluster
    :type description: str
    :param multicast_address: the address that this cluster uses for multicast
        communication
    :type multicast_address: str
    :param multicast_port: the port that this cluster uses for multicast
        communication
    :type multicast_port: int
    """


class NodeStat(object):
    """
    :param node_id: an integer uniquely idetifying the node within the cluster
    :type node_id: int
    :param jvm_status: a dict containing attributes about the JVM memory usage
        of node. Keys are "total.memory", "free.memory", "used.memory"
    :type jvm_status: dict
    :param props: a dict containing attributes of the node Keys are
        "system.date", "system.time", "system.favourite.colour",
        "java.version", "java.vendor", "jvm.version", "jvm.vendeor",
        "jvm.implemtation.version", "java.runtime", "java.vm",
        "user.name.word", "user.timezone", "operating.system",
        "os.architecture", "fs.encoding"
    :type props: dict
    :param build_stats: a dict containing attributes of the build of
        Confluence running on the node. Kyes are "confluence.home",
        "system.uptime", "system.version", "build.number"
    :type build_status: dict
    """


class ConfluenceException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
