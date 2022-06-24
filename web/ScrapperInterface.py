class ScrapperInterface:

    def __init__(self):
        self.url = ""
        self.source = "",
        self.output_path = "./output/",
        self.output_data = []

    def getCatalog(soup):
        """Get catalog object"""
        pass

    def getProducts(catalog):
        """Get products object"""
        pass

    def getProductTitle(product):
        """Get product title object"""
        pass

    def getProductImage(product):
        """Get product image object"""
        pass

    def getProductPrice(product):
        """Get product price object"""
        pass

    def getProductLink(product):
        """Get product price object"""
        pass

    def fetchData():
        """Fetch data from source"""
        pass

    def parseScrappedData():
        """Parse scrapped data items"""
        pass

    def saveToFile():
        """Parse scrapped data items"""
        pass
