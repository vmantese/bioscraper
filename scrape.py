import shutil #high-level operations on files and collections of files

class Scrape:
    """A class holding a single scrape"""
    def __init__(self,dictionary,address="0",baseURI="",fl="output.txt"):
        self.dictionary = dictionary
        self.address = address
        self.baseURI = baseURI
        self.fileLocation = fl
        if(address=="0"):
            self.baseRoot = True
        else:
            self.baseRoot = False
        

    def getDictionary(self):
        return self.dictionary


    def getAddress(self):
        return self.address


    def longURL(self,absURL):
        return urljoin(self.baseURI,absURL)


    def writeScrape(self,output):
        output.seek(0)
        with open(self.fileLocation, "a") as myfile:
            #myfile.write(output)
            shutil.copyfileobj(output,myfile)


    def loadScrape(self,):
        return 0

    def getSelfPath(self,URL,path=""):
        return 0


