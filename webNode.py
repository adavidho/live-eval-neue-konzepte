# represents a node in a tree
# children are other WebNodes
class WebNode:
    def __init__(self, aUrl):
        self.url = aUrl
        self.images = []
        self.links = []
        self.children = []
        self.childIndex = 0

    def setImages(self, aImages):
        self.images = aImages

    def setLinks(self, aLinks):
        self.links = aLinks

    def addImage(self, aUrl):
        self.images.append(aUrl)

    def addLink(self, aUrl):
        self.links.append(aUrl)

    def addChild(self, aWebNode):
        self.children.append(aWebNode)

    def getLinks(self):
        return self.links

    def getImages(self):
        return self.images

    def childs(self):
        return self.children

    def hasChildren(self):
        return len(self.children) != 0

    def next(self):
        if self.childIndex < len(self.children):
            child = self.children[self.childIndex]
            self.childIndex += 1
            return child
        else:
            return None

    def getUrl(self):
        return self.url

    def __str__(self):
        return self.url + " with " + str(len(self.children)) + " kids"
