class DocumentParser:
    def __init__(self):
        pass

    # take in a file and return list of lines
    def parseFile(self, filePath: str) -> list[list[str]]:
        words = []
        with open(filePath, "r") as file:
            for line in file:
                line.rsplit(" ")

                
                        

    # take a list of words a count sum of each
    def wordCount(self, lineList: list[list[str]]):
        raise NotImplementedError()
    
    def removePunctuations(self, word: str) -> str:
        punctuations = [
                        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
                        '_', '+', '-', '=', '`', '~', '{', '}', '[', ']', 
                        '|', '\\', ';', ':', "'", '"', ',', '<', '.', '>', 
                        '/', '?'
                        ]

        for char in word:
            for punc in punctuations:
                if char == punc:
                    word.replace(char, "")
        
        return word
                    

            

def main() -> None:
    parser = DocumentParser()

    print(parser.removePunctuations("mens."))
if __name__ == "__main__":
    main()