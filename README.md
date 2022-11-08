## About DocumentParser.py ##
This is a simple word count class that will store lines from a document and remove the punctuation from each individual word. The class also comes with a method to count words.

## Getting Started ##
`parser = DocumentParser()`<br />
To get started, you do not need to initialize anything when creating an object from the class.


### Retrieving lines from a text document ###
`parser.parseFile("textPath")`<br />
The parseFile method requires a text file path and will grab all of the words in a plain text document. This method will return a list of uncleaned words.

### Remove punctuations from a list of words ###
`words = parser.removePunct(wordList)`<br />
The removePunct method requires a list of words to be passed in as an argument. Once this requirement is satisfied, the method will return a clean list of words that do not have **most** punctuations. (i.e. words with apostrophes to show ownership)

### Count occurences of individual words ###
`wordsCounted = parser.wordCount(words)`<br />
The wordCount method requires a list of words to be passed in as an argument. Once this requirement is satisfied, the method will return a list of lists of words and their count. For example: [[aWord, itsCount], [anotherWord, itsCount], ...]

### Count occurences of all words ###
`allWordCount = parser.totalWordCount`<br />
the totalWordCount method requires a list of words to be passed in as an argument. Once this requirement is satisfied, the method will return an integer that represents the total number of words used in the document.

### EXAMPLE ###
The main.py file is an example of how the document parser can be used.