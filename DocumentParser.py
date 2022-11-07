class DocumentParser:
    # Will take in filePath to readable file and parse all lines and return an unfiltered word list.
    def parseFile(self, filePath: str) -> list[str]:
        """A method that parses a document's lines and returns a list of lines."""
        wordList = []
        
        with open(filePath, "r") as file:
            lineList = [line for line in file]

        for line in lineList:
            wordList.extend(line.rsplit(" "))
            
        return wordList

    # Take a list of words and count the number of times the word was used
    def wordCount(self, wordList: list[str]) -> list[list[str, int]]:
        """
        A method that counts how many times each word has occured and returns a list of lists of strs and ints.
        [[word, count], [word, count]].
        """
        wordSet = set(wordList)
        wordCount = []

        for word in wordSet:
            count = 0

            for werd in wordList:
                if word == werd:
                    count += 1
            
            if word != "":
                wordCount.append([word, count])
        
        return wordCount

    
    def __removePunct(self, word: str) -> str:
        """Private method to remove punctuations from a word, feel free to use it for a singular word."""
        PUNCT_TO_REMOVE = "!@#$%^&*()_+=[]\{}|;':,./<>?\n\\"

        chars, newWord = [char for char in word if char not in PUNCT_TO_REMOVE], ""

        for char in chars:
            newWord += char
        
        return newWord

    def removePuncts(self, words: list[str]) -> list[str]:
        """A method to remove punctuation from a list of words."""
        return [self.__removePunct(word) for word in words]