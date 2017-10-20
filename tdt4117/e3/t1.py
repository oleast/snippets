import codecs
import functions
import copy

def main(textfile):
    
    # Task 1.1
    f = codecs.open(textfile, "r", "utf-8")

    # Task 1.2
    stemmed_paragraphs = functions.get_paragraphs(f)

    # Task 1.3
    stemmed_paragraphs = functions.remove_containing_word("Gutenberg", stemmed_paragraphs)
    paragraphs = copy.copy(stemmed_paragraphs)

    # Task 1.4
    stemmed_paragraphs = functions.tokenize(stemmed_paragraphs)

    # Task 1.5
    stemmed_paragraphs = functions.remove_punctuations(stemmed_paragraphs)

    # Task 1.6
    stemmed_paragraphs = functions.stem(stemmed_paragraphs)

    return paragraphs, stemmed_paragraphs
