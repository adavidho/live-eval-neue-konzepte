# a tree filled with images

import imageCrawler
import webNode

class ImagesTree:

    #start here to crawl images
    def __init__(self,url,aExcludeList=[]):
        self.root=webNode.WebNode(url)
        self.unexpandedNodes=[]
        self.visitedUrlsHash=[]
        self.excludeList=aExcludeList
            
        self.unexpandedNodes.append(self.root)
        
    def expand(self):
        if len(self.unexpandedNodes)>0:
            
            
            next=self.unexpandedNodes.pop(0)
            url=next.getUrl()
            urlHash=hash(url)#Attention: unstable hash-value!!!
            if urlHash not in self.visitedUrlsHash:                
                self.visitedUrlsHash.append(urlHash)
                print("crawl",url)
                images,links=imageCrawler.parse(next.getUrl(),verbose=False)                
                next.setImages(images)
                next.setLinks(links)
                #add children, add to expand list
                for link in links:
                    if link not in self.excludeList:
                        child=webNode.WebNode(link)
                        next.addChild(child)
                        self.unexpandedNodes.append(child)
                print("found images/links",len(images),len(links),"remaining nodes",len(self.unexpandedNodes))
            else:
                print("already expanded",url)
    
    def getRoot(self):
        return self.root