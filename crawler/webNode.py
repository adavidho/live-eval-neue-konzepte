# represents a node in a tree
# children are other WebNodes
class WebNode:
    def __init__(self, aUrl: str) -> None:
        self.url = aUrl
        self.images = []
        self.altTexts = []
        self.links = []
        self.children = []
        self.childIndex = 0

    def setImages(self, aImages: list):
        self.images = aImages

    def setLinks(self, aLinks: list):
        self.links = aLinks

    def addImage(self, aUrl: str):
        "Add the URL of an image."

        self.images.append(aUrl)

    def setAltTexts(self, altTexts: list) -> None:
        self.altTexts = altTexts

    def addAltText(self, altText: str) -> None:
        self.altTexts.append(altText)

    def addLink(self, aUrl: str):
        self.links.append(aUrl)

    def addChild(self, aWebNode):
        self.children.append(aWebNode)

    def getLinks(self):
        return self.links

    def getImages(self):
        return self.images

    def childs(self):
        return self.children

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
