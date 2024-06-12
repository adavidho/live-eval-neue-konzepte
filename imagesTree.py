# a tree filled with images

import imageCrawler
import webNode


class ImagesTree:

    # start here to crawl images
    def __init__(self, url, aExcludeList=[]):
        self.root = webNode.WebNode(url)
        self.unexpandedNodes = []
        self.visitedUrlsHash = []
        self.excludeList = aExcludeList

        self.unexpandedNodes.append(self.root)

    def expand(self) -> None:
        "Expand the tree of discovered Websites by one level."

        if len(self.unexpandedNodes) > 0:

            next = self.unexpandedNodes.pop(0)
            url = next.getUrl()
            urlHash = hash(url)  # Attention: unstable hash-value!!!
            if urlHash not in self.visitedUrlsHash:
                self.visitedUrlsHash.append(urlHash)
                print("crawl", url)
                images, links = imageCrawler.parse(next.getUrl(), verbose=False)
                next.setImages(images)
                next.setLinks(links)
                # add children, add to expand list
                for link in links:
                    if link not in self.excludeList:
                        child = webNode.WebNode(link)
                        next.addChild(child)
                        self.unexpandedNodes.append(child)
                print(
                    "found images/links",
                    len(images),
                    len(links),
                    "remaining nodes",
                    len(self.unexpandedNodes),
                )
            else:
                print("already expanded", url)

    def create_dummy_tree(self):
        # Manually create dummy nodes
        nodes = [webNode.WebNode(f"Node {i}") for i in range(1, 7)]

        # Setting up a tree structure with dummy nodes
        self.root = nodes[0]
        nodes[0].addChild(nodes[1])
        nodes[0].addChild(nodes[2])
        nodes[1].addChild(nodes[3])
        nodes[1].addChild(nodes[4])
        nodes[2].addChild(nodes[5])

        image_urls = [
            ["image1.jpg", "image2.jpg"],
            ["image3.jpg"],
            ["image4.jpg", "image5.jpg", "image6.jpg"],
            ["image7.jpg"],
            ["image8.jpg", "image9.jpg"],
            ["image10.jpg"],
        ]

        for i, node in enumerate(nodes):
            node.setImages(image_urls[i])

        # No need to expand further, this is a static structure
        self.unexpandedNodes = (
            []
        )  # Clear unexpanded nodes list since we're not crawling

    def getRoot(self) -> webNode.WebNode:
        "Get the root of a Website discovery tree."

        return self.root
