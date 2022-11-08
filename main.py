from DocumentParser import *
# ^^ Please don't do this on a regular basis

# Main example function
def main() -> None:
    parser = DocumentParser()

    words = parser.parseFile("./documents/document2.txt")
    words = parser.removePuncts(words)
    words = parser.wordCount(words)

    print(f"[Word Count is {parser.totalWordCount(words)}]")
    for word, count in words:
        print(f"{word:>14} : {count:3d}")


if __name__ == "__main__":
    main()