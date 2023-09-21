class Parser:
    def __init__(self):
        self.app = "unknown"
        self.data = {}

    def getApp(self, str):
        result = ""
        for el in str:
            if el != " ":
                result += el
            elif el == " ":
                return result
            
    def getArrForm(self, str):
        arr = []

        for el in str:
            arr.append(el)

        firstParameterIndex = arr.index("-")
        
        i = 0
        while i < firstParameterIndex:
            arr.pop(0)
            i += 1

        return arr
    
    def makeJSON(self, arr):
        result = {}

        i = 0
        while i < len(arr):

        return result