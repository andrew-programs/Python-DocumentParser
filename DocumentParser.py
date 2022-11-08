class DocumentParser:
    # Will take in filePath to readable file and parse all lines and return an unfiltered word list.
    def parseFile(self, filePath: str) -> list[str]:
        """A method that parses a document's lines and returns a list of lines."""
        wordList = []
        
        with open(filePath, "r") as file:
            lineList = [line for line in file]

        for line in lineList:
            wordList.extend(line.rsplit(" "))
        
        for index in range(len(wordList)):
            wordList[index] = wordList[index].lower()
        return wordList

    # Take a list of words and count the number of times the word was used
    def wordCount(self, wordList: list[str]) -> list[list[str, int]]:
        """
        A method that counts how many times each word has occured and returns a list of lists of strs and ints in descending order.
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
            
            self.__statSort(wordCount)
        
        return wordCount

    # Private method to remove punct from single word.
    def __removePunct(self, word: str) -> str:
        """Private method to remove punctuations from a word, feel free to use it for a singular word."""
        PUNCT_TO_REMOVE = "!@#$%^&*()_+=[]\{}|;':,./<>?\n\\\t"

        chars, newWord = [char for char in word if char not in PUNCT_TO_REMOVE], ""

        for char in chars:
            newWord += char
        
        return newWord

    # Method to remove punct from multiple words in a list.
    def removePuncts(self, words: list[str]) -> list[str]:
        """A method to remove punctuation from a list of words."""
        return [self.__removePunct(word) for word in words]
    
    # Private method to sort word statistics.
    def __statSort(self, list: list) -> list:
        """A private method that sorts out a list using selection sorting algorithm, O(n^2)"""
        for index in range(len(list)):
            minimumIntegerIndex = index

            for secondIndex in range(len(list)):
                if index < secondIndex:
                    if list[secondIndex][1] > list[minimumIntegerIndex][1]:
                        minimumIntegerIndex = secondIndex
            
            list.insert(index, list.pop(minimumIntegerIndex))
        return list
    
    def totalWordCount(self, wordList: list[str]) -> int:
        return len(wordList)