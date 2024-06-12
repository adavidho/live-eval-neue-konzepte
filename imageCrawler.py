import urllib.request
import nltk
from bs4 import BeautifulSoup


# returns the collected texts in paragraphs
# just for testing, for standard use, use method crawl
def parse(url, verbose=False):
    imagesFound = []
    altTextsFound = []
    urlsFound = []
    
    try:
        webUrl = urllib.request.urlopen(url)
        data = webUrl.read()
        parser = BeautifulSoup(data, "html.parser")

        links = parser.find_all("a")
        if verbose:
            print("anzahl links", len(links))
        for link in links:
            if "href" in link.attrs:
                href = link["href"]
                if verbose:
                    print("link", href)
                if href.startswith("/"): # relative link detected
                    href = url + href  # add prefix
                urlsFound.append(href)

        images = parser.find_all("img")
        if verbose:
            print("number images", len(images))

        for image in images:

            if "src" in image.attrs:
                src = image["src"]

                if verbose:
                    print("image src", src)
                imagesFound.append(src)

            if "alt" in image.attrs:
                alt = image["alt"]
                if verbose:
                    print("image alt", alt)
                altTextsFound.append(alt)

    except Exception as e:
        print("error during parsing", e)
    return imagesFound, urlsFound, altTextsFound
