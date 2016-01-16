class Error(Exception):
    pass

class DataError(Error):
    def __init__(self,data):
        self.data = data
    def __str__(self):
        return repr(self.data)

class ImageError(Error):
    def __init__(self,data):
        self.data = data
    def __str__(self):
        return repr(self.data)
